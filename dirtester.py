import urllib2
import argparse
import sys

def testing_host(filename, host):
    file = "results.log"
    bufsize = 0
    e = open(file, 'a', bufsize)
    print("[*] Reading file %s") % (file)
    with open(filename) as f:
        locations = f.readlines()
    for item in locations:
        target = host + "/" + item
        try:
            request = urllib2.Request(target)
            request.get_method = lambda : 'GET'
            response = urllib2.urlopen(request)
        except:
            print("[-] %s is invalid") % (str(target.rstrip('\n')))
            response = None
        if response != None:
            print("[+] %s is valid") % (str(target.rstrip('\n')))
            details = response.info()
            e.write(str(details))
    e.close()

def main():

    usage = '''usage: %(prog)s [-t http://127.0.0.1] [-f wordlist] -q -v -vv -vvv'''
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-t", action="store", dest="target", default=None, help="Target to host to test")
    parser.add_argument("-f", action="store", dest="filename", default=None, help="Filename of directories or pages to test combinations")
    parser.add_argument("-v", action="count", dest="verbose", default=1, help="Verbosity level, regulates detail mode")
    parser.add_argument("-q", action="store_const", dest="verbose", const=0, help="Sets results be quiet")
    parser.add_argument('--version', action='version', version='%(prog)s 1.5')
    args = parser.parse_args()


    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    if (args.target == None) or (args.filename == None):
        parser.print_help()
        sys.exit(1)


    verbose = args.verbose
    filename = args.filename
    target = args.target

    testing_host(filename, target)

if __name__ == '__main__':
    main()
