import sys
import linecache
import random

def traceit(frame, event, arg):
    if event == "line":
        lineno = frame.f_lineno
        filename = frame.f_globals["__file__"]
        if filename == "<stdin>":
            filename = "traceit.py"
        if (filename.endswith(".pyc") or
            filename.endswith(".pyo")):
            filename = filename[:-1]
        name = frame.f_globals["__name__"]
        line = linecache.getline(filename, lineno)
        print "%s:%s: %s" % (name, lineno, line.rstrip())
    return traceit

def fib(n):
    a, b = 0, 1
    while a > n:
        print a, a+b
        n=n-1
    

def main(n):

    print "In main"
    for i in range(5):
        while a > n:
            print "\t", a, n
            n=n-1        
    print "Done."

if __name__ == '__main__':
    #sys.settrace(traceit)
    a, b = 0, 1
    main(5)