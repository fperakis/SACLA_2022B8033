import numpy as np
import h5py
import os
import sys

# parameters for loading
path_combined='/UserData/maddalena/sacla2018/06-Iq_combined/'
path='/UserData/maddalena/sacla2018/03-h5analysis/'



def combine_files(run):
    a=os.popen(f'cd '+path+';ls IqPhi_{run}_*')
    string=a.read()

    string=string.partition('\n')[2]
    I=[]
    while string!='':
            file=string.partition('\n')[0]
            f=h5py.File(pathSave+string.partition('\n')[0],'r')
            I+=f['I']
            print(np.shape(I2d))
            string=string.partition('\n')[2]



    q=f['q'][:]
    Phi=f['phi'][:]


    hf = h5py.File(pathSave+f'{run}_IqPhi.h5', 'w')
    hf.create_dataset('q', data=q)
    hf.create_dataset('I', data=I)
    hf.create_dataset('phi', data=I)
    hf.close()
combine_files(sys.argv[1])