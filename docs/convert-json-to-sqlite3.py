import json
"""

EXAMPLE PROGRAM - this is an example for how to
  convert JSON format into sqlite3 INSERT commands

This generates 'insert into' statements for weewx sqlite3
based a JSON file containing records to be added.

This assumes of course a valid json file as input, meaning
something like:
          [
            {line1},
            {line2},
            {line3}
          ]

(see jsonlint.con for a nice web checker)

This is a quickie, so it does 'not' do much if any error checking.
Sample sqlite dump/restore data and input JSON data is below.

"""

with open("t2.json") as myfile:
    data = json.load(myfile)

for d in data:
    usUnits = 16
    interval = 5
    dateTime = d["dateString"]
    pi       = d["pi"]
    t1       = d["extraTemp1"]
    t2       = d["extraTemp2"]
    print 'INSERT INTO "archive" VALUES(' , dateTime , "," , usUnits , "," , interval , "," , pi , "," , t1 , "," , t2 , ");"

#PRAGMA foreign_keys=OFF;
#BEGIN TRANSACTION;
#CREATE TABLE archive (`dateTime` INTEGER NOT NULL PRIMARY KEY, `usUnits` INTEGER NOT NULL, `interval` INTEGER NOT NULL, `pi` INTEGER, `extraTemp1` INTEGER, `extraTemp2` INTEGER);
#INSERT INTO "archive" VALUES(1425593701,16,5,102.21,64.85,65.41);
#INSERT INTO "archive" VALUES(1425594001,16,5,102.21,64.96,65.41);
#INSERT INTO "archive" VALUES(1425594302,16,5,102.21,64.96,65.41);
#INSERT INTO "archive" VALUES(1425594602,16,5,102.21,65.08,65.53);
#INSERT INTO "archive" VALUES(1425594902,16,5,102.21,65.19,65.64);
#INSERT INTO "archive" VALUES(1425595202,16,5,102.21,65.19,65.75);
#CREATE TABLE archive_day_pi (dateTime INTEGER NOT NULL UNIQUE PRIMARY KEY, min REAL, mintime INTEGER, max REAL, maxtime INTEGER, sum REAL, count INTEGER, wsum REAL, sumtime INTEGER);
#INSERT INTO "archive_day_pi" VALUES(1425542400,102.21,1425593701,102.21,1425593701,613.26,6,613.26,6);
#CREATE TABLE archive_day_extraTemp1 (dateTime INTEGER NOT NULL UNIQUE PRIMARY KEY, min REAL, mintime INTEGER, max REAL, maxtime INTEGER, sum REAL, count INTEGER, wsum REAL, sumtime INTEGER);
#INSERT INTO "archive_day_extraTemp1" VALUES(1425542400,64.85,1425593701,65.19,1425594902,390.23,6,390.23,6);
#CREATE TABLE archive_day_extraTemp2 (dateTime INTEGER NOT NULL UNIQUE PRIMARY KEY, min REAL, mintime INTEGER, max REAL, maxtime INTEGER, sum REAL, count INTEGER, wsum REAL, sumtime INTEGER);
#INSERT INTO "archive_day_extraTemp2" VALUES(1425542400,65.41,1425593701,65.75,1425595202,393.15,6,393.15,6);
#CREATE TABLE archive_day__metadata (name CHAR(20) NOT NULL UNIQUE PRIMARY KEY, value TEXT);
#INSERT INTO "archive_day__metadata" VALUES('Version','1.0');
#INSERT INTO "archive_day__metadata" VALUES('lastUpdate','1425595202');
#COMMIT;

# 
# [
# {"dateString": 1425424501, "extraTemp1": 63.61, "extraTemp2": 63.05, "pi": 104.15},
# {"dateString": 1425424802, "extraTemp1": 63.61, "extraTemp2": 63.05, "pi": 102.21},
# {"dateString": 1425425101, "extraTemp1": 63.61, "extraTemp2": 63.16, "pi": 101.25},
# {"dateString": 1425425401, "extraTemp1": 63.73, "extraTemp2": 63.27, "pi": 102.21},
# {"dateString": 1425425701, "extraTemp1": 63.95, "extraTemp2": 63.27, "pi": 100.28},
# {"dateString": 1425593101, "extraTemp1": 64.85, "extraTemp2": 65.08, "pi": 102.21}
# ]
