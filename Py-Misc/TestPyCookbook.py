import sys
import urllib2
for (i, value) in enumerate(sys.argv):
    print("arg: %d %s " % (i, value))



contents = urllib2.urlopen("https://www.google.com/").read()
print(contents)
