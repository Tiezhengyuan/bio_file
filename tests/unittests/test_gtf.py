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

