
#
# pi.py - Tom's v2 memory add-on and Matthew's v3 pmon extension
#          combined into a Franken-extension by Vince
#
#    vinceskahan@gmail.com - 2014-1128 - original
#
#
# note: Copyright from the originals removed so any blame below
#        goes to me, but of course 99.99% of the credit goes to them.
#
#---------------------------


"""weewx module that records remote Pi temperatures

 This reads a JSON-formatted record from a remote_url
 and loads a 'pi.sdb' sqlite3 database.

 The schema can of course be altered to taste, but
 remember to change the 'meat' of the program

Installation
============

Put this file in the bin/user directory.

Configuration
============

Add the following to weewx.conf:

[PiMonitor]
    data_binding = pi_binding
    remote_url = http://my.example.com/test.json

[DataBindings]
    [[pi_binding]]
        database = pi_sqlite
        manager = weewx.manager.DaySummaryManager
        table_name = archive
        schema = user.pi.schema

[Databases]
    [[pi_sqlite]]
        root = %(WEEWX_ROOT)s
        database_name = archive/mem.sdb
        driver = weedb.sqlite

[Engine]
    [[Services]]
        archive_services = ..., user.mem.PiMonitor
"""

import os
import platform
import re
import sys
import syslog
import time
from subprocess import Popen, PIPE
import resource

import weewx
import weeutil.weeutil
from weewx.engine import StdService

import logging
import json
import urllib2

VERSION = "0.2"

def logmsg(level, msg):
    syslog.syslog(level, 'pi: %s' % msg)

def logdbg(msg):
    logmsg(syslog.LOG_DEBUG, msg)

def loginf(msg):
    logmsg(syslog.LOG_INFO, msg)

def logerr(msg):
    logmsg(syslog.LOG_ERR, msg)

schema = [
    ('dateTime', 'INTEGER NOT NULL PRIMARY KEY'),
    ('usUnits', 'INTEGER NOT NULL'),
    ('interval', 'INTEGER NOT NULL'),
    ('pi','INTEGER'),
    ('extraTemp1','INTEGER'),
    ('extraTemp2','INTEGER'),
    ]

class PiMonitor(StdService):

    def __init__(self, engine, config_dict):
        super(PiMonitor, self).__init__(engine, config_dict)

        d = config_dict.get('PiMonitor', {})
        self.process = d.get('process', 'weewxd')
        self.max_age = weeutil.weeutil.to_int(d.get('max_age', 2592000))
        self.page_size = resource.getpagesize()
        self.remote_url = d.get('remote_url', 'http://localhost/test.json')

        # get the database parameters we need to function
        binding = d.get('data_binding', 'pi_binding')
        self.dbm = self.engine.db_binder.get_manager(data_binding=binding,
                                                     initialize=True)

        # be sure database matches the schema we have
        dbcol = self.dbm.connection.columnsOf(self.dbm.table_name)
        dbm_dict = weewx.manager.get_manager_dict(
            config_dict['DataBindings'], config_dict['Databases'], binding)
        picol = [x[0] for x in dbm_dict['schema']]
        if dbcol != picol:
            raise Exception('pi schema mismatch: %s != %s' % (dbcol, picol))

        self.last_ts = None
        self.bind(weewx.NEW_ARCHIVE_RECORD, self.new_archive_record)

    def shutDown(self):
        try:
            self.dbm.close()
        except:
            pass

    def new_archive_record(self, event):
        """save data to database then prune old records as needed"""
        now = int(time.time() + 0.5)
        delta = now - event.record['dateTime']
        if delta > event.record['interval'] * 60:
            logdbg("Skipping record: time difference %s too big" % delta)
            return
        if self.last_ts is not None:
            self.save_data(self.get_data(now, self.last_ts))
        self.last_ts = now
        #-- TBD: make this tunable on/off via variable
        #-- if self.max_age is not None:
        #--     self.prune_data(now - self.max_age)

    def save_data(self, record):
        """save data to database"""
        self.dbm.addRecord(record)

    def prune_data(self, ts):
        """delete records with dateTime older than ts"""
        sql = "delete from %s where dateTime < %d" % (self.dbm.table_name, ts)
        self.dbm.getSql(sql)
        try:
            # sqlite databases need some help to stay small
            self.dbm.getSql('vacuum')
        except Exception, e:
            pass

    def get_data(self, now_ts, last_ts):
        record = {}
        record['usUnits'] = weewx.METRIC
        record['interval'] = int((now_ts - last_ts) / 60)

        try:
            request = urllib2.Request(self.remote_url)
            response = urllib2.urlopen(request)
            the_page = response.read()
        except (Error), e:
            logerr('pi_info url read failed: %s' % e)
            return

        logging.info(the_page) # ugh
        mydata = json.loads(the_page)
        record['dateTime']     = int(mydata["dateTime"])
        record['pi']           = float(mydata["pi"])
        record['extraTemp1']   = float(mydata["extraTemp1"])
        record['extraTemp2']   = float(mydata["extraTemp2"])

        return record

# what follows is a basic unit test of this module.  to run the test:
#
# cd /home/weewx
# PYTHONPATH=bin python bin/user/pi.py
#
if __name__=="__main__":
    from weewx.engine import StdEngine 
    import time
    config = {
        'Station': {
            'station_type': 'Simulator',
            'altitude': [0, 'foot'],
            'latitude': 0,
            'longitude': 0},
        'Simulator': {
            'driver': 'weewx.drivers.simulator',
            'mode': 'simulator'},
        'PiMonitor': {
            'binding': 'pi_binding',
            'remote_url': 'http://localhost/t.json'},
        'DataBindings': {
            'pi_binding': {
                'database': 'pi_sqlite',
                'manager': 'weewx.manager.DaySummaryManager',
                'table_name': 'archive',
                'schema': 'user.pi.schema'}},
        'Databases': {
            'pi_sqlite': {
                'root': '%(WEEWX_ROOT)s',
                'database_name': '/tmp/pi.sdb',
                'driver': 'weedb.sqlite'}},
        'Engine': {
            'Services': {
                'archive_services': 'user.pi.PiMonitor'}}}
    engine = StdEngine(config)
    svc = PiMonitor(engine, config)

    last_ts=time.time()
    time.sleep(5)
    now_ts=time.time()

    record = svc.get_data(now_ts,last_ts)
    print record

    time.sleep(5)
    last_ts=now_ts
    now_ts=time.time()

    record = svc.get_data(now_ts,last_ts)
    print record

    time.sleep(5)
    last_ts=now_ts
    now_ts=time.time()
    record = svc.get_data(now_ts,last_ts)
    print record

    os.remove('/tmp/pi.sdb')
