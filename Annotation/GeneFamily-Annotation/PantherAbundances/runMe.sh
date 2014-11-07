#!/bin/bash

# In order to create gene family counts (based on gene to PANTHER family ID
# mappings) I first create gene family counts from the RSEM gene count files 
# stored in ../RSEM using the following script
#
# This results in 187 gene family count files (DC*); log files for the
# transformation are written to the logs directory

./PantherAbundanceConvert.py

# The following combines gene family counts from the 187 separate fies into 
# two single spreadsheets:
#
# TPM-Counts.csv <- TPM (transcripts per million)
# Expected-Counts.csv <- expected (raw) read counts

./CombinedPantherCounts.py Counts-CSV/TPM-Counts.csv TPM

./CombinedPantherCounts.py Counts-CSV/Expected-Counts.csv ExpectedCount
