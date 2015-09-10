from itertools import *

def should_drop(x):
    print 'Testing:', x
    return (x<1)

def check_item(x):
    print 'Testing:', x
    return (x<1)

def should_take(x):
    print 'Testing:', x
    return (x<2)

for i in dropwhile(should_drop, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i
print "\n"
for i in takewhile(should_take, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i
print "\n"
for i in ifilter(check_item, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i
print "\n"

vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}

print vowels.values()
print vowels.keys()
