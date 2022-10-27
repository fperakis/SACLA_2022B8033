import numpy as np
import h5py 
import pyFAI, pyFAI.detectors, pyFAI.azimuthalIntegrator
import sys
import time

def Iq_calculator(run):
    """
    Calcuale the Iq and Iphi of an entire run and generates an h5 file with the Iqs for each shot
    args:
        run : run number without extensions
    """

    # detector params
    path = '/UserData/maddalena/sacla2018'
    sample_det_distance = 0.095
    wavelength = 0.887e-10
    Pixel1, Pixel2 = 50e-6, 50e-6
    posx, posy = Pixel1*1200, Pixel2*1150
    det = pyFAI.detectors.Detector(pixel1=Pixel1, pixel2=Pixel2, max_shape=[2399,2399])
    ai = pyFAI.azimuthalIntegrator.AzimuthalIntegrator(dist=sample_det_distance, detector=det, wavelength=wavelength, poni1=posx, poni2=posy)
    
    # integration params
    nbins = 300
    n_phi = 30
    radial_range = [0,27]
    mask = np.load(f'{path}/04-utilities/mask.npy')
    
    with h5py.File(f'{path}/02-h5compression/{run}.h5', 'r') as f:
        maxtag = len(f[f'/run_{run}/event_info/tag_number_list'][:])
        I = np.zeros([maxtag, n_phi, nbins])
        i = 0
        
        for tag in f[f'/run_{run}/event_info/tag_number_list'][:maxtag]:
            I[i,:,:], q, phi = ai.integrate2d_ng(f[f'/run_{run}/detector_2d_assembled_1/tag_{tag}/detector_data'][:], 
                                        nbins, n_phi, mask=mask, correctSolidAngle=True, unit='q_nm^-1', radial_range=radial_range)
            i += 1

    timestamp = time.strftime("%d%H%M%S", time.gmtime(time.time()))
    hf = h5py.File(f'{path}/03-h5analysis/{run}_IqPhi_{timestamp}.h5', 'w')
    hf.create_dataset('q', data=q)
    hf.create_dataset('I', data=I)
    hf.create_dataset('phi', data=phi)
    # hf.create_dataset('Energy', data=f[f'/run_{run}/event_info/bl_3/eh_1/xfel_pulse_selector_status'])
    # hf.create_dataset('I_0', data=f[f'/run_{run}/event_info/bl_3/eh_2/bm_1_signal_in_coulomb'])
    # f.create_dataset('tags', data=f[f'/run_{run}/event_info/tag_number_list'])
    # hf.create_dataset('shutter', data=f[f'/run_{run}/event_info/bl_3/eh_1/xfel_pulse_selector_status'])
    hf.close()
    
Iq_calculator(sys.argv[1])