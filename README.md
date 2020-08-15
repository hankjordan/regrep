# regrep.py

Regrep.py is a simple tool that allows you to recursively search a given directory for files with content matching a given expression.


## Usage

**python regrep.py [-h] [-name [NAME]] expression directory**

-h: Prints help

-name: Allows you to only search files matching a given name. * is wildcard.

expression: The regex expression to match

directory: The directory to traverse

## Known bugs
- The name matching works by compiling the wildcards and the other text given to the parameter into a regex expression, but no regex syntax is actually escaped, so if you use any un-escaped regex syntax it will behave unpredictably.