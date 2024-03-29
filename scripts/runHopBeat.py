#!/usr/bin/python3
###
### Author: rdt12@psu.edu
### Date:   Apr 24, 2020
### Desc:   Run gcn2hop in a loop with credentials taken from an AWS secret.
###
from datetime import datetime, timezone
import Utils as u
import time
import pytz
import sys
import os

region       = "us-west-2"
secret       = "dev-gcn2hop-hopcreds"
configDir    = "/root/shared"
Location     = "%s/config.toml" % configDir
hopUrl       = "kafka://dev.hop.scimma.org:9092/heartbeat"
hopInterval  = "30"

if (os.environ.get('HOP_SECRET') is not None):
    secret = os.environ.get('HOP_SECRET')

if (os.environ.get('HOP_REGION') is not None):
    region = os.environ.get('HOP_REGION')

if (os.environ.get('HOP_URL') is not None):
    hopUrl = os.environ.get('HOP_URL')

if (os.environ.get('HOP_INTERVAL') is not None):
    hopInterval = os.environ.get('HOP_INTERVAL')

## Look for creds in the environment, then in AWS secrets manager.
if (os.environ.get('HOP_CREDS') is not None):
    creds = u.getCredsFromString(os.environ.get('HOP_CREDS'))
else:
    creds = u.getCreds(region, secret)

## Line buffer stdout and stderr
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buffering=1)

os.system("mkdir -p %s" % configDir)
u.writeConfig(Location, creds)

while True:
    print("======================================")
    print("== Starting hopBeat")
    print("Date: %s" % datetime.now(pytz.timezone('America/New_York')))
    print("======================================")
    exitVal = os.system("/root/hopBeat -F %s --scimma=%s --interval=%s" % (Location, hopUrl, hopInterval))
    print("hopBeat exited with os.system returning: %d" % exitVal)
    time.sleep(30)
