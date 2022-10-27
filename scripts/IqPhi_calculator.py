import numpy as np
import h5py 
import pyFAI, pyFAI.detectors,pyFAI.azimuthalIntegrator

def Iq_calculator(run, pathData,pathSave):
    #define an integrator
    path = '/UserData/maddalena/sacla2018'
    sample_det_distance = 0.095
    wavelength = 0.887e-10
    posx = Pixel1*1200
    posy = Pixel2*1150
    ai = pyFAI.azimuthalIntegrator.AzimuthalIntegrator(dist=sample_det_distance, detector=det, wavelength=wavelength,poni1=posx,poni2=posy)
    mask = np.load(f'{path}/04-utilities/mask.npy')
    
    with h5py.File(f'{path}/02-h5compression/{run}.h5', 'r') as f:
        maxtag = len(f[f'/run_{run}/event_info/tag_number_list'][:])
        n_phi = 10
        I = np.zeros([maxtag,n_phi,100])
        i = 0
        
        for tag in f['/run_{run}/event_info/tag_number_list'][:maxtag]:
            I[i,:,:], q, phi = ai.integrate2d_ng(f['/run_{run}/detector_2d_assembled_1/tag_{tag}/detector_data'][:], 
                                        100, n_phi,mask=mask,correctSolidAngle=True,unit='q_nm^-1')
            i += 1

    hf = h5py.File(f'{path}/03-h5analysis/{run}_IqPhi.h5', 'w')
    hf.create_dataset('q', data=q)
    hf.create_dataset('I', data=I)
    hf.create_dataset('phi', data=I)
    hf.close()
    
Iq_calculator(run, pathData,pathSave)