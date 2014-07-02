import json
import datetime
import hashlib
import os
from mega import Mega
mega = Mega()

# Login to MEGA
print "Logging in to mega" + "\r\n\r\n"
m = mega.login()

# Create a blank object we'll return at the end
newjson = {}

now = datetime.datetime.now()
newjson["date"] = now.strftime("%Y-%m-%d")

# Load package.json, convert to object
data = open("Atom/resources/app/package.json")
pkgdata = json.load(data)
print "Loaded package.json" + "\r\n\r\n"

newjson["title"] = "Atom Build " + pkgdata["version"]

# Rar up the file with the version name
outputfile = "Atom " + pkgdata["version"] + ".rar"
print "Rarring up " + outputfile
os.system('rar a -r "' + outputfile + '" Atom')
print "Done rarring up " + outputfile + "\r\n\r\n"

# hash the file
md5 = hashlib.md5()
print "Calculating MD5 hash for " + outputfile
with open(outputfile,'rb') as f: 
    for chunk in iter(lambda: f.read(8192), b''): 
         md5.update(chunk)
newjson["md5"] = md5.hexdigest()
print "DONE calculating MD5 hash for " + outputfile + "\r\n\r\n"

# Upload the file to MEGA
print "Uploading to MEGA: " + outputfile
file = m.upload(outputfile)
newjson["url"] = m.get_upload_link(file)
print "DONE uploading to MEGA: " + outputfile + "\r\n\r\n"

print newjson
print "\r\n\r\n"
print json.JSONEncoder(indent=2).encode(newjson)
