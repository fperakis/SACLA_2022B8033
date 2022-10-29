import numpy as np
import h5py
import glob
import os
import sys
import time
import argparse

# - parsers
parser = argparse.ArgumentParser(description='Combine h5 files from the analysis into one')
parser.add_argument('-r', '--run', type=str, required=True, help='run number to combine')

args = parser.parse_args()

# parameters for loading
path_combined = '/UserData/maddalena/sacla2022/06-Iq_combined/'
path = '/UserData/maddalena/sacla2022/03-h5analysis/'

def combine_files(run):
    os.chdir(path)
    files = glob.glob(f"IqPhi_{run}*.h5")

    f = h5py.File(files[0],'r')
    q = f['q'][:]
    Phi = f['phi'][:]
    
    I = []
    PulseEnergy = []
    PhotonEnergy = []
    tags = []
    shutter = []
    
    for file in files[1:]:
        f = h5py.File(path+file,'r')
        I            += f['I']  
        PulseEnergy  += f['PulseEnergy'][:]
        PhotonEnergy += f['PhotonEnergy']
        tags         += f['tag']
        shutter      += f['shutter']

    timestamp = time.strftime("%d%H%M%S", time.gmtime(time.time()))
    hf = h5py.File(path_combined + f'IqPhi_{run}_{timestamp}.h5', 'w')
    hf.create_dataset('q', data=q)
    hf.create_dataset('I', data=I)
    hf.create_dataset('phi', data=phi)
    hf.create_dataset('PulseEnergy', data=PulseEnergy)
    hf.create_dataset('PhotonEnergy', data=PhotonEnergy)
    hf.create_dataset('tags', data=tags)
    hf.create_dataset('shutter', data=shutter)
    hf.close()
    
combine_files(args.run)
    