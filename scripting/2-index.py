#!/usr/bin/env python
import os

# get path system
print os.getcwd()

# print os.listdir("/Users/joelengt")
dir = os.popen("ls").readlines()
print dir
