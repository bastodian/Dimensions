#!/bin/bash
#
## Generate a background distribution of GO terms
#./ExtractAllGOs.py PTHR8.1_arabidopsis GlobalGOs > GlobalGOs.annot
#
## Extract GO terms for over-/under-yielders
#while read line
#do
#    ./ParseGO.py ./PTHR8.1_arabidopsis GeneFamilyDE-Results/$line.counts.matrix.condA_vs_condB.edgeR.DE_results
#done < RelYield/Overyielders 1> RelYield/Overyielders.Upregulated.annot 2> RelYield/Overyielders.Downregulated.annot
#
#while read line
#do
#    ./ParseGO.py ./PTHR8.1_arabidopsis GeneFamilyDE-Results/$line.counts.matrix.condA_vs_condB.edgeR.DE_results
#done < RelYield/Underyielders 1> RelYield/Underyielders.Upregulated.annot 2> RelYield/Underyielders.Downregulated.annot

# Extract GO terms for facilitators/competitors
while read line
do
    ./ParseGO.py ./PTHR8.1_arabidopsis GeneFamilyDE-Results/$line.counts.matrix.condA_vs_condB.edgeR.DE_results
done < FacilitateVSCompete/Facilitators 1> FacilitateVSCompete/Facilitators.Upregulated.annot 2> FacilitateVSCompete/Facilitators.Downregulated.annot

while read line
do
    ./ParseGO.py ./PTHR8.1_arabidopsis GeneFamilyDE-Results/$line.counts.matrix.condA_vs_condB.edgeR.DE_results
done < FacilitateVSCompete/Competitors 1> FacilitateVSCompete/Competitors.Upregulated.annot 2> FacilitateVSCompete/Competitors.Downregulated.annot
