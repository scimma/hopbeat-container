###
### Author: rdt12@psu.edu
### Date:   Jun 26, 2020
### Desc:   Utility functions for runGcn2Hop.py
###
import json
import subprocess
import re
from hop import models
from hop import publish
from hop import io

def getCreds (region, secret):
  cmd   = "/usr/local/bin/aws --region %s secretsmanager get-secret-value --secret-id %s" % (region, secret)
  s = json.loads(subprocess.Popen([cmd], shell=True,
                             stdout=subprocess.PIPE).stdout.read().decode())
  cjson = s["SecretString"]
  c = json.loads(cjson)
  cm = re.match(r'^([^:]+):(.*)$', c["creds"])
  if cm != None:
      creds = {"user": cm.group(1), "pass": cm.group(2)}
  else:
      creds = None
  return creds

def writeConfig (loc, creds):
    cfh = open(loc, "w")
    cfh.write("[auth]\n")
    cfh.write("username = \"%s\"\n" % creds["user"])
    cfh.write("password = \"%s\"\n" % creds["pass"])
    cfh.close()

class ScimmaConnection:

    def __init__ (self, scimmaUrl):
        self.scimmaUrl      = scimmaUrl
        self.msgCount       = 0

    def open (self):
        self.stream       = io.Stream()
        self.streamHandle = self.stream.open(self.scimmaUrl, mode="w")

    def write (self, msg):
        self.streamHandle.write(msg)
        self.msgCount = self.msgCount + 1
        print("Sent message %d" % self.msgCount)

    def close (self):
        self.streamHandle.close()
