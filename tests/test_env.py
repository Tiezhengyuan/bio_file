'''
Test ENV
'''
from tests.helper import *


@ddt
class TestENV(TestCase):

    def setUp(self):
        pass

    @mock.patch.dict(os.environ, {'DIR_DOWNLOAD': DIR_TMP})
    def test_env(self):
        print(os.getenv('DIR_DOWNLOAD'))