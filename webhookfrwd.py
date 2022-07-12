#!/usr/bin/python3
import os
import string

fwd_uri = os.getenv('PROTOCOL')+"://"+os.getenv('JENKINS_USERNAME')+":"+os.getenv('JENKINS_PASSWORD')+"@"+os.getenv('SVC_IP_ADDRESS')+os.getenv('WEBHOOK_ENDPOINT')
os.environ['TARGET_URI'] = fwd_uri

os.system("smee --url "+os.getenv('SMEE_URL')+" --target "+os.getenv('TARGET_URI'))