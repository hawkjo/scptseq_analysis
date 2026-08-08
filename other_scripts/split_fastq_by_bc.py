#!/usr/bin/env python

import sys
import os
import gzip
from Bio import SeqIO


class FileHandler(dict):
    def __init__(self):
        pass

    def __getitem__(self, out_fpath):
        if out_fpath not in self.__dict__:
            self.__dict__[out_fpath] = open(out_fpath, 'w')
        return self.__dict__[out_fpath]

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        for fh in self.__dict__.values():
            fh.close()

def gzip_friendly_open(fpath, mode='rt'):
    if fpath.endswith('.gz'):
        return gzip.open(fpath, mode)
    return open(fpath, mode)

def split_fastq_by_bc(fastq_fpath, out_dir):
    if os.path.exists(out_dir):
        sys.exit('Output directory already exists')
    os.mkdir(out_dir)

    with FileHandler() as fh:
        for rec in SeqIO.parse(gzip_friendly_open(fastq_fpath), 'fastq'):
            bc = str(rec.id).split('_')[0]
            out_fpath = os.path.join(out_dir, f'{bc}.fq')
            SeqIO.write(rec, fh[out_fpath], 'fastq')

if __name__ == '__main__':
    fmt = f'{sys.argv[0]} <fastq_file> <out_dir>'
    if len(fmt.split()) != len(sys.argv):
        sys.exit(f'Usage: {fmt}')

    fastq_fpath, out_dir = sys.argv[1:]
    split_fastq_by_bc(fastq_fpath, out_dir)
