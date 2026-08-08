#!/bin/bash

echo $1
cd $1
split_fastq_by_bc.py *fastq fastqs_by_bc
