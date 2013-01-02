#!/bin/bash

: <<'!'
    Script uses Translate.py script to translate all 6 reading frames of reference transcriptomes;
    translated transcripts get piped into HMMER3's hmmscan to search against selected Pfam HMMs.

    Author: Bastian Bentlage
    Email: bastian.bentlage@gmail.com
!

for File in ~/DimensionsData/T6/Assemblies/DC*/Trinity.fasta ## Directory to Assemblies hardcoded
do
    TEMP=${File##?*Assemblies?}
    FileStem=${TEMP%%?Tr*fasta}
    ../python/translate.py $File | \
        ../bin/hmmer-3.0-linux-x86_64/hmmscan \
        --noali \
        --cpu 24 \
        --cut_ga \
        --tblout ../../logs/$FileStem.tbl \
        ../../Pfam/Dimensions.PfamA \
        - ## Take input from stdout
done &> /dev/null
