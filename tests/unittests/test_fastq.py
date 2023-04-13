'''
Test class 
'''
from tests.helper import *
# from Bio import SeqIO, Seq, SeqRecord
from bio_file.biofiles.fastq import FASTQ


@ddt
class Test_(TestCase):
    def setUp(self):
        self.c = FASTQ()


    @data(
        ['1_control_18S_2019_minq7.fastq'],
        ['left.fastq']
    )
    @unpack
    def test_read_fq(self, input):
        infile = os.path.join(DIR_DATA, input)
        iter = self.c.read_fq(infile)
        res = next(iter)
        assert len(res.seq) > 50


    @data(
        ['left.fastq', 'right.fastq'],
    )
    @unpack
    def test_read_pair(self, fq1_file, fq2_file):
        f1 = os.path.join(DIR_DATA, fq1_file)
        f2 = os.path.join(DIR_DATA, fq2_file)
        iter = self.c.read_pair(f1, f2)
        res = next(iter)
        assert len(res[0].seq) > 50


    @data(
        ['left.fastq'],
    )
    @unpack
    @mock.patch.dict(os.environ, env)
    def test_quality_scores(self, input):
        infile = os.path.join(DIR_DATA, input)
        iter = self.c.read_fq(infile)
        self.c.quality_scores(iter)

    @data(
        ['left.fastq', True],
        ['left.fq', True],
        ['wrong', False],
        ['dna.fa', False],
    )
    @unpack
    @mock.patch.dict(os.environ, env)
    def test_is_fastq(self, input, expect):
        infile = os.path.join(DIR_DATA, input)
        res = self.c.is_fastq(infile)
        assert res == expect