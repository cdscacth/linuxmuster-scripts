#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import json

# CONFIG
linbocmdPath = "/var/linbo/linbocmd"
workstations = "/etc/linuxmuster/workstations"
# Optional config for Mattermost
mattermostUrl = ""
channel = "#monitoring"
botName = "Linbo"
icon_url = ""

# Read workstations for hostname lookup
workstationsFile = open(workstations, "r")
devices = workstationsFile.readlines()

#IP to hostname
def lookupIP(ip):
    for host in devices:
        if host.find(";"+ip+";") != -1:
            return host.split(";")[1]
            break;

# Post message to Mattermost channel
def postMessage(message):
    attachment = {"color": "danger", "text":  message}
    data = {"channel": channel, "username": botName, "attachments": [attachment], "icon_url": icon_url}
    conn = requests.post(mattermostUrl, data = json.dumps(data))

# Check if there are files left from Linbo (linbo-remote -r room -p command -w 0)
offlineHosts = sorted(os.listdir(linbocmdPath))
numberOfHosts = len(offlineHosts)
if numberOfHosts > 0:
    message = ":warning: " + str(numberOfHosts) + " host(s) were offline:\n"
    for host in offlineHosts:
        message += "* " + lookupIP(host.replace(".cmd", "")) + "\n"

        # Remove Linbo command files
        commandFile = os.path.join(linbocmdPath, host)
        try:
            if os.path.isfile(commandFile):
                os.unlink(commandFile)
        except Exception as e:
            print(e)

    print(message)

    # Post to Mattermost if a URL is configured
    if mattermostUrl != "":
        postMessage(message)
else:
    print("Everything is OK!")
