def parse_options():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option('-t', '--type', action='append',
                      dest='logtypes', type='choice',
                      choices=['in', 'out', 'pre', 'post', 'fs', 'ivrin', 'ivrout', 'all'],
                      help='type of log to search (in, out, pre, post, fs or\
                      all). this option can be given multiple times.\
                      default - all')
    parser.add_option("-f", "--file", dest="file",
                      help="search in given FILE", metavar="FILE")
    parser.add_option('-d', '--time', action='append',type="int",
                      dest='time',help='time should in number')
    (options, args) = parser.parse_args()
    print options
    return options


def main():
    a = parse_options()
    print a

if __name__ == "__main__":
    main()
