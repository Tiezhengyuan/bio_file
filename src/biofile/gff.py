"""
process GFF file
https://www.ncbi.nlm.nih.gov/genbank/genomes_gff/

"""
from typing import Iterable
import re



class GFF:
    def __init__(self, gff_file:str):
        self.infile = gff_file

    def iter(self) -> Iterable:
        with open(self.infile, 'r') as f:
            for line in f:
                yield line.rstrip()


    def read_gff(self):
        gff_dict={}
        in_obj=open(self.infile, 'r')
        for line in in_obj:
            line=line.rstrip()
            contig_name, geneID, start,end=line.split('\t')
            if contig_name not in gff_dict.keys():
                gff_dict[contig_name]={}
            gff_dict[contig_name][geneID]=(int(start),int(end))
        in_obj.close()
        return gff_dict
    
    # TODO: confirm testing in the future
    def read_gff_files(self, genome_names, gff_tag_name, outfile, fa_dict):
        '''
        outfile is combine them into one gff file
        elicit from fasta and gff
        used for mcscanx
        '''
        out_obj=open(outfile, 'w')  
        for name in genome_names:
            #read gene position
            in_obj=open(self.infile, 'r')
            for line in in_obj:
                line = line.rstrip()
                items=line.split('\t')
                if len(items)==9:#remove comments line
                    annot=re.split(';| ; ', items[8]) #column #9
                    for one in annot:
                        #tage could be geneID or Accession
                        start=re.search('=| ', one).start()
                        tag_name,tag=one[:start], one[(start+1):]
                        ID=name+'_'+tag
                        #print('##{}##{}##{}##'.format(one, tag_name, tag))
                        if tag_name == gff_tag_name and ID in fa_dict.keys():
                            if fa_dict[ID]['gff'] is None:#unique line
                                out=[name+'_'+items[0], ID, items[3],items[4]]
                                fa_dict[ID]['gff']=out
                                out_obj.write("{}\n".format('\t'.join(out)))
                                break
            in_obj.close()
        out_obj.close()
        return fa_dict        

