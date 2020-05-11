#!/bin/python3

import sys
import lttng
import argparse



#https://docs.python.org/2/library/argparse.html#module-argparse
#https://realpython.com/async-io-python/

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="Makes lttng easy...")
#     parser.add_argument('create', help="creates a new lttng session")
#     parser.add_argument('start', help="creates a new lttng session")
#     #parser.add_argument('-v', dest='verbose', action='store_true')
#     args = parser.parse_args()
#     print(args)
#     # ... do something with args.output ...
#     # ... do something with args.verbose ..


print("Probando lttng")
lttng_session=lttng.lttng()

lttng_session.loadConfiguration()



    


