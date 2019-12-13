#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vardens.py: Tools for manipulating variable density spectra wave files

File spec gathered from:
    https://xbeach.readthedocs.io/en/latest/xbeach_manual.html#variance-density-spectra

Quoting that website, the specification of a 'vardens.txt' file is:
    <number of frequencies (n)>
    <frequency 1>
    <frequency 2>
    <frequency 3>

    ...
    
    <frequency n-1>
    <frequency n>
    <number of directions (m)>
    <directions 1>
    <directions 2>
    <directions 3>
    
    ...
    
    <directions m-1>
    <directions m>
    <variance density 1,1> <variance density 2,1> ... <variance density m,1>
    <variance density 1,2> <variance density 2,2> ... <variance density m,2>
    
    ...
    
    <variance density 1,n> <variance density 2,n> ... <variance density m,n>

Created by Scott Feister on Thu Dec 12 19:36:04 2019
"""

import os
import numpy as np

def write(freqs, dirs, vardens, outdir = '.'):
    """ Write 'vardens.txt' from vardens array, into the specified folder.
    Inputs:
        dirs     1D float NumPy array (length m), Directions
        freqs    1D float NumPy array (length n)
        vardens  2D float NumPy array (n x m)
        outdir   [Optional] Output directory into which to save 'vardens.txt'
    """
    # Check validity of inputs
    if len(dirs.shape) > 1 or len(freqs.shape) > 1:
        raise Exception("dirs and freqs must be 1D arrays")
    if vardens.shape != (freqs.shape[0], dirs.shape[0]):
        raise Exception("Based on lengths of dirs and freqs, expected vardens shape of " + str((freqs.shape[0], dirs.shape[0])) + " but got shape of " + str(vardens.shape))

    # Write the file
    with open(os.path.join(outdir, 'vardens.txt'), 'w') as f:
        f.write(str(freqs.shape[0])+"\n")
        np.savetxt(f, freqs)
        f.write(str(dirs.shape[0])+"\n")
        np.savetxt(f, dirs)
        np.savetxt(f, vardens, delimiter=' ')
        
if __name__ == "__main__":
    ## Test function
    dirs = np.array([1,2,3])
    freqs = np.array([0.1,0.2])
    vardens = np.array([[10,20,30],[40,50,60]])
    write(freqs, dirs, vardens, outdir=r"C:\Users\scott\Documents\temp\dec2019")
    pass
