import sys

print(sys.argv)
if(len(sys.argv) > 1):
    a = sys.argv[-1]
    print(a.upper())