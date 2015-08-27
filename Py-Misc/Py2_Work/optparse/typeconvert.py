import optparse
'''
https://pymotw.com/2/optparse/index.html
'''
parser = optparse.OptionParser()
parser.add_option('-i', action="store", type="int")
parser.add_option('-f', action="store", type="float")
parser.add_option('-l', action="store", type="long")
parser.add_option('-c', action="store", type="complex")

options, args = parser.parse_args()
print 'int    : %-16r %s' % (type(options.i), options.i)
print 'float  : %-16r %s' % (type(options.f), options.f)
print 'long   : %-16r %s' % (type(options.l), options.l)
print 'complex: %-16r %s' % (type(options.c), options.c)
'''
python optparse_types.py -i 1 -f 3.14 -l 1000000 -c 1+2j
'''