------------------------------------------------------------------------------
help infomation
$ python argExample.py -h

usage: argExample2.py [-h] [-s SIMPLE_VALUE] [-S SIMPLE_VALUE_INT] [-c] [-t]
                      [-f] [-a COLLECTION] [-A] [-B] [--version]

optional arguments:
  -h, --help           show this help message and exit
  -s SIMPLE_VALUE      Store a simple value
  -S SIMPLE_VALUE_INT  Store a simple int value
  -c                   Store a constant value
  -t                   Set a switch to true
  -f                   Set a switch to false
  -a COLLECTION        Add repeated values to a list
  -A                   Add different values to list
  -B                   Add different values to list
  --version            show program's version number and exit

------------------------------------------------------------------------------
showing default values:
$python argExample.py 

jjjj@jjjj-virtual-machine:~/Argparse/example2$ python argExample2.py
simple_value     = None
simple_value_int = 0
constant_value   = None
boolean_switch   = False
collection       = []
const_collection = []

------------------------------------------------------------------------------

set values :
$python argExample2.py -s kerker -S 1 -a 1 3 -A -A -B -A

simple_value     = kerker
simple_value_int = 1
constant_value   = None
boolean_switch   = False
collection       = ['1', '3']
const_collection = ['value-A-to-append', 'value-A-to-append', 'value-B-to-append', 'value-A-to-append']

------------------------------------------------------------------------------
try this
$python argExample2.py -v
$python argExample2.py -vv
$python argExample2.py -vvv
$python argExample2.py -vvvv


