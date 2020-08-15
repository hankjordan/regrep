# regrep.py

Regrep.py is a simple tool that allows you to recursively search a given directory for files with content matching a given expression.


## Usage

**python regrep.py [-h] [-name [NAME]] expression directory**

-h: Prints help

-name: Allows you to only search files matching a given name. * is wildcard.

expression: The regex expression to match

directory: The directory to traverse

## TODO
- Add concurrency
- Add timing printout "Done. Searched 4500 files in 4.3s"