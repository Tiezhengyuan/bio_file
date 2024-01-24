
import json
import os
from .genome.fasta_dna import FastaDNA
from .genome.gff import GFF


class Wrap:

    def __init__(self, local_files:list, outdir:str=None):
        self.local_files = local_files
        self.outdir = outdir
        self.output_json = os.path.join(self.outdir, 'output.json') \
            if self.outdir and os.path.isdir(self.outdir) else ''

    def load_output(self) -> list:
        if os.path.isfile(self.output_json):
            with open(self.output_json, 'r') as f:
                return json.load(f)
        return []

    def save_output(self, meta:list, overwrite:bool=None) -> list:
        output = [] if overwrite else self.load_output()
        output += meta
        # save
        with open(self.output_json, 'w') as f:
            json.dump(output, f, indent=4)
        return output

    def ncbi_fa_gff(self) -> list:
    
        meta = []
        fd = FastaDNA(self.local_files, self.outdir)
        # RNA.fna
        res = fd.ncbi_rna_dna()
        meta.append(res)
        # mRNA.fna
        res = fd.ncbi_rna_dna('mRNA')
        meta.append(res)
        # CDS.fna
        res = fd.ncbi_cds()
        meta.append(res)
        # pseudogene.fna
        res = fd.ncbi_pseudo()
        meta.append(res)

        gff_file = fd.get_infile('_genomic.gff')
        if gff_file:
            gff = GFF(gff_file, self.outdir)
            res = gff.retrieve_RNA()
            meta.append(res)
            res = gff.retrieve_mRNA()
            meta.append(res)
            res = gff.retrieve_CDS()
            meta.append(res)
            res = gff.retrieve_pseudo()
            meta.append(res)
        return meta
