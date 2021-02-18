# add parent dir to path
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import unittest
from src.raspberry import Raspberry

class TestRaspberry(unittest.TestCase):
    def test_temp(self):
        r = Raspberry()
        temp = r.getTemp()
        self.assertEqual(temp, 42)

    def test_temp(self):
        pass



import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

suite = unittest.TestLoader().loadTestsFromTestCase(TestRaspberry)
unittest.TextTestRunner(verbosity=2).run(suite)