#!/usr/bin/env python
# Send download notifications from Sabnzbd to iPhone
import sys
import pyrowl

# Prowl API settings
API_KEY = "yourapikeyhere"


# Get NZB info
job = dict(name=sys.argv[3], status=int(sys.argv[7]))

if job['status'] == 0:
	job['long_status'] = "OK"
elif job['status'] == 1:
	job['long_status'] = "failed verification"
elif job['status'] == 2:
	job['long_status'] = "failed unpacking"
elif job['status'] == 3:
	job['long_status'] = "failed verification & unpacking"

p = pyrowl.Pyrowl(API_KEY)


if job['status'] == 0:
    result = p.push("Sabnzbd", "Download Complete",
                    "{name} downloaded successfully".format(**job))
    if result[API_KEY].get('code') == "200":
        print "Sent Sucessfully"
    else:
        print "Sending failed with error: {} {}".format(result[API_KEY].get('code'), 
                                                        result[API_KEY].get('message'))
else:
    result = p.push("Sabnzbd", "Download Failed",
                    "{name} failed with error: {long_status}".format(**job))
    if result[API_KEY].get('code') == "200":
        print "Sent Sucessfully"
    else:
        print "Sending failed with error: {} {}".format(result[API_KEY].get('code'), 
                                                        result[API_KEY].get('message'))