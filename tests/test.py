import unittest

import sys
sys.path.append("..")

from src.outils.outils import Outils

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.parser = Outils() 
        
    def checkIfPrimaryInstanceIsWellDefine(self):
        self.assertIsInstance(self.parser , Outils)

    
if __name__=="__main__":
    unittest.main()