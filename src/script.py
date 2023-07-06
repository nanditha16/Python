import sys
import cowsay

# takes argument via CLI - sys.arg
if len(sys.argv) < 2:
    sys.exit("Too few arguments. Usage:python script.py arg1 ")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments. Usage:python script.py arg1 ")

# package examples | pip install cowsay
if len(sys.argv) == 2:
    cowsay.dragon("hello, " + sys.argv[1])
else:
    # take a slice of list to start the arv start from 1 instead of beginning from 0
    for arg in sys.argv[1:]:
        print("hello, my name is: ", arg)
        cowsay.meow("hello, " + arg)
