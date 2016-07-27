#import urllib2
#urllib2.urlopen("apilinkhere")
#import json
#print json.load(urllib2.urlopen("apilinkhere"))

"""
TEMPLATE

================================================

import urllib2
import json

apiKey = ""

url = "apilinkhere"
json_obj = urllib2.urlopen("apilinkhere")

data = json.load(json_obj)

for item in data['objects']:
    print item

================================================

import urllib2
import json

apiKey = ""

url = "https://api.locu.com/v1_0/venue/search/?name=coffee&locality=chicago&api_key="
json_obj = urllib2.urlopen("https://api.locu.com/v1_0/venue/search/?name=coffee&locality=chicago&api_key=")

data = json.load(json_obj)

for item in data['objects']:
    print "item is : " +str(item)
    
================================================
    

import urllib2
import json

apiKey = ""

url = "https://api.locu.com/v1_0/venue/search/?name=coffee&locality=chicago&api_key="
json_obj = urllib2.urlopen("https://api.locu.com/v1_0/venue/search/?name=coffee&locality=chicago&api_key=")

data = json.load(json_obj)

for item in data['objects']:
    print item['name']
    print item['street_address']
    print ""
 
================================================

import urllib2
import json


url = "https://api.locu.com/v1_0/venue/search/?name=Burger&locality=Florida&api_key="
json_obj = urllib2.urlopen("https://api.locu.com/v1_0/venue/search/?name=Burger&locality=Florida&api_key=")

data = json.load(json_obj)

for item in data['objects']:
    print item['name']
    print item['street_address']
    print ""
"""
"""
import urllib2
import json

url = "https://api.locu.com/v1_0/venue/search/?api_key="
json_obj = urllib2.urlopen(url)

locality = name=coffee%20Beach&category=restaurant&

def locu_seacrch(query):
    api_key = locu_api
    url = "https://api.locu.com/v1_0/venue/search/?api_key="
    locality = query.replace('','%20')
    final_url = url +"&locality="+locality+"&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)


for item in data['objects']:
    print item['name'],item['street_address']
"""
import urllib2
import json
import locuApiKey

searchFor = "name=Coffee&locality=Chicago"

def locu_search(query):
    searcFor = query.replace('', '%20')
    url = "https://api.locu.com/v1_0/venue/search/?api_key=" + locuApiKey.apiKey + "&" +searchFor
    json_obj = urllib2.urlopen(url)
    
    data = json.load(json_obj)
    
    returnData = data['objects']
    
    return returnData

for item in locu_search(searchFor):
    print item['name']
    print item['street_address']
    print ""