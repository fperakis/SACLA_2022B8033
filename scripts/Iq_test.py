# Script to calculate the Iq of all the shots of a run
# Argument: run number
# run the script with: $ python Iq_test.sh 690007

import numpy as np
import h5py 
import pyFAI, pyFAI.detectors, pyFAI.azimuthalIntegrator
import sys

def Iq_calculator(run):
    """
    Calcuale the Iq of an entire run and generates an h5 file with the Iqs for each shot
    args:
        run : run number without extensions
    """
    # define an integrator
    sample_det_distance = 0.095
    wavelength = 0.887e-10
    Pixel1, Pixel2 = 50e-6, 50e-6
    det = pyFAI.detectors.Detector(pixel1=Pixel1, pixel2=Pixel2, max_shape=[2399,2399])

    posx = Pixel1*1200
    posy = Pixel2*1150
    ai = pyFAI.azimuthalIntegrator.AzimuthalIntegrator(dist=sample_det_distance, detector=det, wavelength=wavelength, poni1=posx, poni2=posy)
    mask = np.load('/UserData/maddalena/sacla2018/04-utilities/mask.npy')

    with h5py.File(f'/UserData/maddalena/sacla2018/02-h5compression/{run}.h5', 'r') as f:
        maxtag = len(f['/run_'+str(run)+'/event_info/tag_number_list'][:])
        I = np.zeros([maxtag,100])
        i = 0
        for tag in f['/run_'+str(run)+'/event_info/tag_number_list'][:maxtag]:
            q,I[i,:] = np.array(ai.integrate1d(f['/run_'+str(run)+'/detector_2d_assembled_1/tag_'+str(tag)+'/detector_data'][:],
                                          100,mask=mask, correctSolidAngle=True, unit='q_nm^-1')) # add radial range
            i += 1
    hf = h5py.File(f'/UserData/maddalena/sacla2018/03-h5analysis/{run}_Iq_test.h5', 'w')
    hf.create_dataset('q', data=q)
    hf.create_dataset('I', data=I)
    hf.create_dataset('Energy', data=f[f'/run_'{run}'/event_info/bl_3/eh_1/xfel_pulse_selector_status']
    hf.create_dataset('I_0', data=f[f'/run_'{run}'/event_info/bl_3/eh_2/bm_1_signal_in_coulomb'])
    hf.create_dataset('tags', data=f[f'/run_'{run}'/event_info/tag_number_list'])
    hf.create_dataset('shutter', data=f[f'/run_'{run}'/event_info/bl_3/eh_1/xfel_pulse_selector_status'])
    hf.close()

Iq_calculator(sys.argv[1])