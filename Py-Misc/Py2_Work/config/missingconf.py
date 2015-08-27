import ConfigParser

parser = ConfigParser.SafeConfigParser()
parser.read('simple.ini')
#parser.add_section('bug_tracker')
parser.set('bug_tracker', 'url', 'http://%(server)s:%(port)s/bugs')

try:
    print parser.get('bug_tracker', 'url')
    print parser.get('bug_tracker', 'password')
except ConfigParser.InterpolationMissingOptionError, err:
    print 'ERROR:', err
    print "Error here"