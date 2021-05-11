#! /bin/bash
for ((i=0; i<15; i++));
    do
        python /content/SPACES/extract_model.py $i
    done