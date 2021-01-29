import argparse
import re
import os

# ReGrep - REcursive Global Regular Expression Print

parser = argparse.ArgumentParser(description="Recursively search a directory for files matching a regex.")

parser.add_argument("expression", type=str)

parser.add_argument("directory", type=str)

parser.add_argument("-name", type=str, nargs="?", default="*")

args = parser.parse_args()

name_regex = re.escape(args.name).replace("\*", ".*")

name_prog = re.compile(name_regex)
expression_prog = re.compile(args.expression.encode("utf8"))

count = 0

for root, dirs, files in os.walk(args.directory):
	for file in files:
		if re.match(name_prog, file):
			filename = os.path.join(root, file)
			
			try:
				data = open(filename, "rb").read()
			except FileNotFoundError as e:
				continue
			
			result = re.search(expression_prog, data)
			if result:
				print(filename, result)
		
		print("Files searched: "+str(count)+"\r", end="")
		count+=1