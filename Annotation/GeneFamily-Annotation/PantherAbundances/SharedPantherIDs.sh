#!/bin/bash

# There are a total of 187 mapping files. From these the PTHR IDs are extracted (grep and awk) and subsequently
# sorted and counted. Only those IDs that are present in all 187 files are retained and written to SharedPantherIDs
# that contains all PTHR IDs present in all species/mapping files

grep PTHR D* | awk '{print $1}' | awk -F ':' '{ print $2}' | sort | uniq -c | sort | grep '187 ' | awk '{ print $2}' > SharedPantherIDs
