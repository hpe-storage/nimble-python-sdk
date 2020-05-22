# 
# This Makefile is used to regenerate the .md files from pydoc using pydocmd
#
# Script enumerates the .py files in the current branch and pydocmd uses what 
# is installed on the host!
#
# Append the URI references to ../../mkdocs.yml
#

apis = $(shell (ls ../../nimbleclient/v1/api/*[a-z].py | \
	   xargs basename | sed "s/\.py$$//" | tr \\n " "))
class = nimbleclient.v1.api

all:
	for api in $(apis); do pydocmd simple $(class).$${api}+ > $${api}.md;done
	for api in $(apis); do echo "    - '$${api}': 'api/$${api}.md'";done
