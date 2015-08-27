import optparse
'''
https://pymotw.com/2/optparse/index.html
'''
parser = optparse.OptionParser()
parser.add_option('-o', action="store", default="default value")
options, args = parser.parse_args()
print options.o

parser = optparse.OptionParser()
parser.add_option('-o', action="store")
parser.set_defaults(o='new value')
options, args = parser.parse_args()
print options.o

'''
python optparse_default.py
python optparse_default.py -o "different value"

'''