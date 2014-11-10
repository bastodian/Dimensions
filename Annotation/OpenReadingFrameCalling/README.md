

```bash
for Species in DC10 DC20 DC30 DC40 DC50 DC60 DC70 DC80
do
    mkdir $Species &&
    cd $Species &&
    TRANSCRIPTS="PathToAssemblies/$Species/Trinity.fasta"
    /usr/local/src/trinityrnaseq_r2013-02-25/trinity-plugins/transdecoder/transcripts_to_best_scoring_ORFs.pl
    -t $TRANSCRIPTS
    --search_pfam PathTo/Pfam-A.hmm --CPU 24 
    cd ..
done
```


```bash
for ORFs in DC*/best_candidates.eclipsed_orfs_removed.pep
do
    NewFasta=`echo $ORFs | awk -F '/' '{print $1}'`
    echo $ProteinFasta
    ./FastaConvert.py $ORFs $NewFasta > $NewFasta.fst
done
```
