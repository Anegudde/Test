import optparse
'''
https://pymotw.com/2/optparse/index.html
'''
parser = optparse.OptionParser()
parser.add_option('-a', action="store_true", default=False)
parser.add_option('-b', action="store", dest="b")
parser.add_option('-c', action="store", dest="c", type="int")
print parser.parse_args(['-a', '-bval', '-c', '3'])

parser = optparse.OptionParser()
parser.add_option('--noarg', action="store_true", default=False)
parser.add_option('--witharg', action="store", dest="witharg")
parser.add_option('--witharg2', action="store", dest="witharg2", type="int")
print parser.parse_args([ '--noarg', '--witharg', 'val', '--witharg2=3' ])