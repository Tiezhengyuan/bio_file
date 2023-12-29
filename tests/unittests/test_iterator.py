'''
Test class Utils
'''
from tests.helper import *
from src.biofile.utils.iterator import Iterator as c

@ddt
class TestIterator(TestCase):
    @skip
    @data(
        [
            ['chrY', 'chr8', 'chrX', 'chr2', 'chr1', 'chr10'],
            ['chr1', 'chr2', 'chr8', 'chr10', 'chrX', 'chrY'],
        ],
    )
    @unpack
    def test_sort_array(self, input, expect):
        res = c.sort_array(input)
        assert res == expect

    @data(
        ['a', [10,]],
        # ['b', ['ab']],
        # ['c', [{'a':1}]],
        # ['wrong', []],
    )
    @unpack
    def test_search_series(self, key, expect):
        s = pd.Series([10, 'ab', {'a':1}, [2,3,4],20,],
            index=['a','b','c','d','e'])
        res = c.search_series(s, key)
        assert res == expect

    @data(
        [[[1,2],[1,2,4]], 0, [[1,2,0],[1,2,4]]],
        [[[1,2],[1,2]], 0, [[1,2],[1,2]]],
        [[], 0, []],
    )
    @unpack
    def test_shape_length(self, input, fill, expect):
        c.shape_length(input, fill)
        assert input == expect