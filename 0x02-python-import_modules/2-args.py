#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) is 1:
        print('0 arguments.')
    else:
        print ('{} arguments'.format(len(sys.argv) - 1))
        print ('{}'.format(str(sys.argv)))
