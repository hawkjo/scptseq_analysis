#!/bin/bash

module load SAMtools
echo $1
samtools fastq $1 > ${1::-4}.fq
