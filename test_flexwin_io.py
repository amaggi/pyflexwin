import os, unittest, logging

def suite():
  suite = unittest.TestSuite()
  suite.addTest(FlexwinIOTests('test_readParameterFile'))
  return suite

#@unittest.skip('Not bothering with this test')
class FlexwinIOTests(unittest.TestCase):

  def setUp(self):
    pass

  def test_readParameterFile(self):
    from flexwin_io import readParameterFile
  
    filename=os.path.join('test_data','PAR_FILE')
    p=readParameterFile(filename)
    
    self.assertTrue(p['DEBUG'])
    self.assertFalse(p['BODY_WAVE_ONLY'])
    self.assertAlmostEqual(p['WIN_MAX_PERIOD'],150.0)
    self.assertAlmostEqual(p['C_0'],0.7)

if __name__ == '__main__':

  import logging
  logging.basicConfig(level=logging.INFO, format='%(levelname)s : %(asctime)s : %(message)s')
 
  unittest.TextTestRunner(verbosity=2).run(suite())
 
