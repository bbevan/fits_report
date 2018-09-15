'''
Created on May 1, 2018

@author: Brandon Bevan
'''
from pathlib2 import Path
from astropy.io import fits


class MyClass(object):
    '''
    classdocs
    '''
    # Return a list of fits files in all subdirectories

    def fitslist(self):
        p = Path('.')  # work in current directory

        # [x for x in p.iterdir() if x.is_dir()]

        return list(p.glob('**/*.fits'))
    # end

    # Print the fits list
    def fitsprint(self,mylist):
    
        for x in mylist:
            print(x)

            # end

# Return a list containing a fits filename and certain header info
    def limheaderinfo(self,fitsfile):
        hdul = fits.open(fitsfile)

        a = [hdul[0].header['DATE'], hdul[0].header['FILTER2'], hdul[0].header['OBJECT'], hdul[1].header['CCDSUM']]

        hdul.close()

        return a

    # end

    # Print out header info for all fits files in a tree
    def printlimheaderinfo(self):
    
        for x in fitslist():
            print(x)
            for y in limheaderinfo(x):
                print(y)
                print("\n")

                # end

    def __init__(self, params):
        '''
        Constructor
        '''
# end class       
