#!/bin/bash

mafft \
    --auto \
    --maxiterate 1000 \
    --thread 24 \
    --reorder $1 \
    > temp && cat temp > $1 && rm temp
