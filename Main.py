import os

from numpy import trim_zeros
from decrypt import HybridDeCryptKeys
from encrypt import HybridCryptKeys
from split import *
from Threads import *

def EncryptInput():
	Segment()
	gatherInfo()
	HybridDeCryptKeys()

def DecryptMessage():
    HybridCryptKeys()
    trim_zeros()
    Merge()
        
def main():
    EncryptInput()
    #DecryptMessage()
    
if __name__=="__main__":
    main()

