#!/bin/bash
#SBATCH -t 7-00:00:00
#SBATCH -N 1
#SBATCH -n 20
#SBATCH -J mmp_bcs
#SBATCH --mem=32G

module load minimap2/2.22-GCCcore-11.2.0
module load SAMtools/1.21-GCC-13.3.0


refgenome=/g/stegle/hawkins/decode/annotation/dm6/ensembl/Drosophila_melanogaster.BDGP6.28.dna.toplevel.fa

threads=$SLURM_CPUS_ON_NODE
    
outdir=spliced_bams
mkdir $outdir
for fastqfile in *.fq ;
do
    runname=`basename $fastqfile .fq`
    outsam=${outdir}/${runname}.sam
    outbam=${outdir}/${runname}.sorted.bam
    minimap2 -w 4 -k 13 -ax splice–eqx -t $threads $refgenome $fastqfile > $outsam      # Oxford Nanopore genomic reads
    samtools view -b $outsam | samtools sort - > $outbam
    samtools index $outbam
done


