import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')
parser.add_argument("-v",dest='counters' , default=0,
                    action="count", help="increase output verbosity.")
parser.add_argument('-S', action='store', dest='simple_value_int',
                    default=0,help='Store a simple int value',type=int)

parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
                    dest='boolean_switch',
                    help='Set a switch to false')

parser.add_argument('-a', action='store', dest='collection',
                    help='saving inputs to lists',nargs='+'
                    )

parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-A-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection',
                    const='value-B-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()
print 'simple_value     =', results.simple_value
print 'simple_value_int =', results.simple_value_int
print 'constant_value   =', results.constant_value
print 'boolean_switch   =', results.boolean_switch
print 'collection       =', results.collection
print 'const_collection =', results.const_collection

if(results.counters>=1):
    print "hey,hey,I'm here "+str(results.counters)+" times."
