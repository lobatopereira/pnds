import os
import hashlib

def getlastid(table_name):
	result = table_name.objects.last()
	if result:
		lastid = result.id
		newid = lastid + 1
	else:
		lastid = 0
		newid = 1
	return lastid, newid
def getnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
		hashid = hashlib.md5(str(newid).encode())
	else:
		newid = 1
		hashid = hashlib.md5(str(newid).encode())
	return newid, hashid.hexdigest()

def getjustnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
	else:
		newid = 1
	return newid

def hash_md5(strhash):
	hashed = hashlib.md5(strhash.encode())
	return hashed.hexdigest()

def split_string(string):
	string2 = string.split()
	return string2[0].lower()

from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):

      R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

      dLat = radians(lat2 - lat1)
      dLon = radians(lon2 - lon1)
      lat1 = radians(lat1)
      lat2 = radians(lat2)

      a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
      c = 2*asin(sqrt(a))

      return R * c
