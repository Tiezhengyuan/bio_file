"""
define annotation record

"""
from typing import Iterable
import re

class AnnotRecord:
    names = ['seqid', 'source', 'feature', 'start', 'end',  'score', 'strand', 'phase', 'attributes',]
    # column 1-9 in GTF/GFF
    seqid = None
    source = None
    feature = None
    start = None
    end = None
    score = None
    strand = None
    phase = None
    attributes = None

    def parse(self, record_line:str):
        items = record_line.split('\t')
        for k,v in zip(self.names, items):
            setattr(self, k, v)
        if self.start:
            self.start = int(self.start)
        if self.end:
            self.end = int(self.end)

    def parse_gtf_attributes(self):
        '''
        GTF attributes
        '''
        names = re.findall('([a-zA-Z0-9_]+)\\s\"', self.attributes)
        values = re.findall('\"([a-zA-Z0-9_\\.\\%\\:\\(\\)\\-\\,\\/\\s]*?)\"', self.attributes)
        attr = [{'name': k, 'value': v} for k, v in zip(names, values)]
        return attr

    def parse_gff_attributes(self):
        '''
        GFF attributes
        '''
        names = re.findall('([a-zA-Z0-9_]+)=', self.attributes)
        values = re.findall('=([a-zA-Z0-9_\\.\\s\\:\\/\\-\\%\\(\\)\\,\'\\[\\]\\{\\}]+)', self.attributes)
        attr = []
        for k, v in zip(names, values):
            if k == 'Dbxref' and ',' in v:
                for v2 in v.split(','):
                    attr.append({'name': k, 'value': v2})
            else:
                attr.append({'name': k, 'value': v})
        return attr

    def to_dict(self) -> dict:
        rec = dict([(k, getattr(self, k)) for k in self.names])
        return rec
