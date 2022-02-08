# -*- coding: utf-8 -*-

"""get and save raspi temperatures.

RUN THIS ON THE PI WITH THE TEMPERATURE SENSORS !!!!

This module queries the motherboard temperature sensor
and any defined DS18B20 temperature sensors and converts
their values to deg-F.

The idea is to query the Pi periodically and save the values
and make the output file available for other software ala
a web browser (symlink) or for pickup by scp or the like.

Generally, run this periodically from cron and save the output
to a location that will be served by the Pi's webserver.

Example:
    # go to a ramdisk location to not burn out the Pi SD card
    $ python thisprogram.py > /run/thisprogram.out

    # and of course symlink that location into your web
    $ ln -s /usr/share/nginx/www/html/thisprogram.out /run/thisprogram.out


Attributes:
    tempSensors (list): 1-wire sensor id(s) for any such sensor(s)
    moboSensor  (bool): set True to report on motherboard temperature

"""

import sys
import time
import json

#--- start editing here ---

# set True to report on Pi motherboard temperature
moboSensor = True

# 1-wire sensor id numbers and matching database fields
# note: you need 'both' defined here and the field names
# must match your custom extension on the weewx system
oneWireTempSensors = {
   "28-000005ab3d0c": "extraTemp1" , 
   "28-000005bbe53e": "extraTemp2" ,
}

#--- stop editing here ---

# seconds since epoch
dateTime = int(time.time())

# this will store the hash of results
temperatures = {}

#--------------------

def convertCtoF(t,divisor=1):
    """convert deg-C to deg-F.

    Parameters:
      t       (int): temperature in deg-C
      divisor (int): optional divisor to handle input data
                   that is not in integer degrees. If specified,
               temperature will be divided by the divisor
               during the calculation

    Returns:
      temperature in deg-F if successful, None otherwise

    Raises:
      ValueError: if any input parameter is not a number

    Examples:
      convertCtoF(26)          will return 78.8
      convertCtoF(26000,1000)  will return 78.8
      convertCtoF("foo",1000)  will raise an exception
      convertCtoF(26000,"foo") will raise an exception

    """
    try:
        tempF = float(t)/int(divisor) * 9/5 + 32.0
        return float("%.2f" % tempF)    # plenty precise enough
    except ValueError:
        raise ValueError('input value(s) must be a number')
        return None


#--------------------

def getMoboTemp():
    """get motherboard temperature from the pi.

        motherboard temp is in /sys/class/thermal/thermal-zone0/temp
        as thousandths of a degree C (ie. 26000 = 26.000 C)
    Parameters:
      none

    Returns:
      motherboard temp in deg-F if successful, None otherwise

    """
    # on the pi, this is always the filename
    mobo_filename="/sys/class/thermal/thermal_zone0/temp"
    try:
        tfile=open(mobo_filename,'r')
        moboTemp=tfile.read()
        tfile.close()
        return convertCtoF(moboTemp,1000)
    except:
        return None

#--------------------


def getOneWireTemp(device):
    """get a 1-wire temperature sensor value.

        1wire sensors are in /sys/bus/w1/devices/ID/w1_slave
        ala the following:
            a1 00 4b 46 7f ff 0f 10 e4 : crc=e4 YES
            a1 00 4b 46 7f ff 0f 10 e4 t=10062

    Parameters:
      device: 1-wire device identifier

    Returns:
      sensor temperature in deg-F if successful, None otherwise

    """
    try:
        filename="/sys/bus/w1/devices/" + device + "/w1_slave"
        tfile=open(filename,'r')
        code=tfile.read()
        tfile.close()
        # verify checksum was ok
        lineOne=code.split("\n")[0]       # first line in the file
        crcStat=lineOne.split(" ")[11]    # YES
        if crcStat == "YES":
            linetwo=code.split("\n")[1]       # second line in the file
            tempdata=linetwo.split(" ")[9]    # t=10062
            temp=float(tempdata[2:])
            return convertCtoF(temp,1000)
    except:
        return None

#-----------------------
# main below here
#

# hardcoded for now, might someday have other kinds of sensors
# that have different ways of calculating their values and units

# motherboard
#   we hardcode the name 'pi' for the database field
if moboSensor:
    temperatures["pi"]=getMoboTemp()

# 1-wire sensors
#   this is ugly because we save the temp of the sensor 'id'
#   with a 'name' of the field we'll use in the database eventually
for sensor in oneWireTempSensors.keys():
    temperatures[oneWireTempSensors[sensor]]=getOneWireTemp(sensor)
    
# this is a hash of key/value pairs
temperatures["dateTime"] = dateTime

print json.dumps(temperatures,sort_keys=True)

sys.exit(0)


