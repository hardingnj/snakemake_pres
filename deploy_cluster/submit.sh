#! /bin/bash
mkdir -p _log

snakemake -T $@ \
    --cluster 'qsub -v PATH="/home/njh/miniconda3/bin:$PATH" -j y -o $(pwd)/_log/ -b n -l {params.req} -S /bin/bash' \
    --jobs 10 \
    --latency-wait 60 \
    --restart-times 0 \
    --jn "{rulename}.{jobid}.sh" \
    --use-conda
