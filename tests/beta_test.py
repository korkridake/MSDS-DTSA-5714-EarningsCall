from mlib import *

def test_one():
   assert fmt_name('peter', 'parker')=='Peter PARKER'
   assert fmt_name('tony  ', 'stark')=='Tony STARK'
   