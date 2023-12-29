'''
Test class Utils
'''
from tests.helper import *
from src.biofile.utils.utils import Utils

@ddt
class TestUtils(TestCase):



    @data(
        ['A0A1J0MUK8', ''],
        # ['Q96678', ''],
    )
    @unpack
    def test_parse_ncbi_acc(self, key, expect):
        infile = os.path.join(DIR_DATA, 'gene_refseq_uniprotkb_collab.txt')
        res = Utils.parse_ncbi_acc(infile)
        # assert res.get(key[:2]) == expect