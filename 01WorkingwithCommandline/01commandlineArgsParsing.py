
# How to run 
# python3 commandline_args.py -n Alireza
# or using --name

# tutorial from: https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/



import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser() #we instantiate the ArgumentParser  object as ap
ap.add_argument("-n", "--name", required=True, help="name of the user")
args = vars(ap.parse_args())

print(args) # prints the arguments names and values

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))

