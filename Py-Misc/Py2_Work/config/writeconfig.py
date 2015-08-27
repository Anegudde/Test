import ConfigParser
import sys
import codecs
import sys
encoding = sys.argv[1]
filename = encoding + '.txt'

parser = ConfigParser.SafeConfigParser()
parser.add_section('bug_tracker')
parser.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
parser.set('bug_tracker', 'username', 'dhellmann')
parser.set('bug_tracker', 'password', 'secret')
#parser.write(sys.stdout)


print 'Writing to', filename
with codecs.open(filename, mode='w', encoding=encoding) as f: 
    f.write(u'pi: \u03c0')

# Determine the byte grouping to use for to_hex()
nbytes = { 'utf-8':1,
           'utf-16':2,
           'utf-32':4,
           }.get(encoding, 1) 

# Show the raw bytes in the file
print 'File contents:'
with open(filename, mode='rt') as f:
    print (sys.stdout,f.read(), nbytes)