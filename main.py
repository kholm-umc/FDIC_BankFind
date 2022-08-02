'''
    I pulled the bankfind library: https://pypi.org/project/bankfind/

    I then copied/pasted their sample code (same URL)

    It ran like a champ.  I changed from 'Colorado' to 'Mississippi' and a bunch
      of data came back.

    We can certainly look at the issues you're working through.  This code here
      (bankfind library) may be an option, too.
'''
from pprint import pprint
import bankfind as bf

# Get Institutions
data = bf.get_institutions()

# Get Institutions from Colorado with high ROE
data = bf.get_institutions(filters="STNAME:Mississippi AND ROE:[25 TO *]")

# Get Commercial Banks from Colorado that aren't S-Corps
data = bf.get_institutions(filters="STNAME:Mississippi AND SUBCHAPS:0 AND CB:1")

pprint(data)