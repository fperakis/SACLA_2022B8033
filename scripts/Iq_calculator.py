import numpy as np
import h5py 
import pyFAI, pyFAI.detectors,pyFAI.azimuthalIntegrator
def Iq_calculator(run, pathData,pathSave):
    #define an integrator
    sample_det_distance=0.095
    wavelength=0.887e-10
    posx=Pixel1*1200
    posy=Pixel2*1150
    ai = pyFAI.azimuthalIntegrator.AzimuthalIntegrator(dist=sample_det_distance, detector=det, wavelength=wavelength,poni1=posx,poni2=posy)
    mask=np.load('/UserData/maddalena/sacla2018/04-utilities/mask.npy')
    maxtag=len(f['/run_'+str(run)+'/event_info/tag_number_list'][:])

    with h5py.File(path+str(run)+'.h5', 'r') as f:
        I=np.zeros([maxtag,100])
        i=0
        for tag in f['/run_'+str(run)+'/event_info/tag_number_list'][:maxtag]:
            q,I[i,:]=np.array(ai.integrate1d(f['/run_'+str(run)+'/detector_2d_assembled_1/tag_'+str(tag)+'/detector_data'][:],
                                          100,mask=mask,correctSolidAngle=True,unit='q_nm^-1'))
            i=i+1
    hf = h5py.File(pathSave+f'{run}_Iq.h5', 'w')
    hf.create_dataset('q', data=q)
    hf.create_dataset('I', data=I)
    hf.close()
Iq_calculator(run, pathData,pathSave)