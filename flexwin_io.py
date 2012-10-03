import logging
import numpy as np

"""
IO routines for flexwin
"""
def readParameterFile(filename):
  """
  Read flexwin PAR_FILE

  :param filename: Full path to PAR_FILE filename 
  :rtype: Python dictionary 
  :return: Flexwin parameters
  """
  p={}

  # read the parameter file
  f=open(filename,'r')
  lines=f.readlines()
  f.close()

  # extract information into the dictionary
  for line in lines:
    words=line.split()
    if len(words)>=3 and words[-2] == '=' :
      name=words[0]
      val=words[-1]
      p[name]=val

  _verifyParameters(p)

  return p

def _verifyParameters(p):
  """
  Private function to verify the validity of a parameter dictionary
  """
  # names of logical parameters
  logical_names=['DEBUG','MAKE_SEISMO_PLOTS','MAKE_WINDOW_FILES','BODY_WAVE_ONLY','RUN_BANDPASS','DATA_QUALITY']

  # names of floating point parameters
  float_names=['WIN_MIN_PERIOD','WIN_MAX_PERIOD','STALTA_BASE','TSHIFT_BASE','TSHIFT_REFERENCE','DLNA_BASE',
               'DLNA_REFERENCE','CC_BASE','SNR_INTEGRATE_BASE','SNR_MAX_BASE','WINDOW_S2N_BASE',
               'C_0','C_1','C_2','C_3a','C_3b','C_4a','C_4b',
               'WEIGHT_SPACE_COVERAGE','WEIGHT_AVERAGE_CC','WEIGHT_N_WINDOWS']

  # cleanup types in dictionary
  try:
    # deal with the logical names
    for name in logical_names:
      val=p[name]
      if val=='.true.': 
        p[name]=True
      elif val=='.false.': 
        p[name]=False
      else : 
        raise UserWarning('Parameter %s should be either .true. or .false., not %s'%(name,val))
    # deal with the float names
    for name in float_names:
      val=p[name]
      p[name]=np.float(val)
  except KeyError:
    logging.error('Missing parameter %s in PAR_FILE'%name)
