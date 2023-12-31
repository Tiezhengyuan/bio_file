from tests.helper import *

from src.biofile.gtf import GTF

@ddt
class TestGTF(TestCase):

    @data(
        ['human_genomic.gtf', 9995],
    )
    @unpack
    def test_iterator(self, file_name, expect):
        gtf_file = os.path.join(DIR_DATA, file_name)
        iter = GTF(gtf_file).iterator()
        res = [i for i in iter]
        assert len(res) == expect

    def test_split(self):
        gtf_file = os.path.join(DIR_DATA, 'human_genomic.gtf')
        # statistics
        res = GTF(gtf_file).split_by_feature()
        assert res['transcript'] == 465
        
        # export to json
        res = GTF(gtf_file, DIR_TMP).split_by_feature()
        assert res['transcript'] == os.path.join(DIR_TMP, "transcript.json")

        # decompose attributes
        res = GTF(gtf_file, DIR_TMP).split_by_feature(True)


    @data(
        ['gene_id', None, 143],
        ['gene_id', '_all_', 143],
        ['gene_id', 'CDS', 55],
        ['gene_id', 'transcript', 115],
        ['gene', 'transcript', 179],
        ['ID', 'wrong', 0],
        ['wrong', None, 0],
    )
    @unpack
    def test_parse_attributes(self, attr, feature, expect):
        gff_file = os.path.join(DIR_DATA, 'human_genomic.gtf')
        res = GTF(gff_file, DIR_TMP).parse_attributes(attr, feature)
        assert len(res) == expect

