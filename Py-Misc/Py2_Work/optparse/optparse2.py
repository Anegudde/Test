import optparse
import sys
'''
https://pymotw.com/2/optparse/index.html
'''
print 'ARGV      :', sys.argv[1:]
parser = optparse.OptionParser()
parser.add_option('-o', '--output',dest="output_filename",default="default.out",)
parser.add_option('-v', '--verbose',dest="verbose",default=False,action="store_true",)
parser.add_option('--version',dest="version",default=1.0,type="float",)
options, remainder = parser.parse_args()
print 'VERSION   :', options.version
print 'VERBOSE   :', options.verbose
print 'OUTPUT    :', options.output_filename
print 'REMAINING :', remainder
'''
python optparse_getoptcomparison.py -o output.txt
python optparse_getoptcomparison.py --output output.txt
python optparse_getoptcomparison.py --out output.txt
'''