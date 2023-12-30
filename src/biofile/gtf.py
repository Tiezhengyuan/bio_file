"""
process GFF file
https://www.ncbi.nlm.nih.gov/genbank/genomes_gff/

"""

from .annot_record import AnnotRecord
from .annot_file import AnnotFile

class GTF(AnnotFile):
    def __init__(self, gtf_file:str, outdir:str=None):
        super().__init__(gtf_file, outdir)

    def split_by_feature(self, parse_attributes:bool=None):
        '''
        split annotations by feature (in 3rd column)
        convert annotations to json by feature
        '''
        if not parse_attributes:
            parse_attributes = False
        annot = {}
        for line in self.iterator():
            c = AnnotRecord().parse(line)
            if parse_attributes:
                c.attributes = c.parse_gtf_attributes()
            rec = c.to_dict()
            feature = rec['feature']
            if feature not in annot:
                annot[feature] = []
            annot[feature].append(rec)

        res = self.to_json(annot)
        return res
