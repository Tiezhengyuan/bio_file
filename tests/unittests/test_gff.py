from tests.helper import *

from src.biofile.gff import GFF

@ddt
class TestGFF(TestCase):

    @data(
        ['human_genomic.gff', 9991],
    )
    @unpack
    def test_iterator(self, file_name, expect):
        gff_file = os.path.join(DIR_DATA, file_name)
        iter = GFF(gff_file).iterator()
        res = [i for i in iter]
        assert len(res) == expect

    def test_split(self):
        gff_file = os.path.join(DIR_DATA, 'human_genomic.gff')
        # statistics
        res = GFF(gff_file).split_by_feature()
        assert res['transcript'] == 21
        
        # export to json
        res = GFF(gff_file, DIR_TMP).split_by_feature()
        assert res['transcript'] == os.path.join(DIR_TMP, "transcript.json")

        # attributes
        res = GFF(gff_file, DIR_TMP).split_by_feature(True)
    
    @data(
        ['ID', None, 6467],
        ['ID', '_all_', 6467],
        ['ID', 'CDS', 333],
        ['ID', 'mRNA', 334],
        ['gene', 'mRNA', 55],
        ['transcript_id', 'mRNA', 334],
        ['ID', 'wrong', 0],
        ['wrong', None, 0],
    )
    @unpack
    def test_parse_attributes(self, attr, feature, expect):
        gff_file = os.path.join(DIR_DATA, 'human_genomic.gff')
        res = GFF(gff_file, DIR_TMP).parse_attributes(attr, feature)
        assert len(res) == expect

