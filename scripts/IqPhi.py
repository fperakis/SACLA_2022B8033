import numpy as np
import h5py 
import pyFAI, pyFAI.detectors, pyFAI.azimuthalIntegrator
import sys
import time
import argparse

# - parsers
parser = argparse.ArgumentParser(description='Analyse run')
parser.add_argument('-r', '--run', type=str, required=True, help='run number to process')
parser.add_argument('-s', '--start', type=str, required=True, help='start tag')
parser.add_argument('-e', '--end', type=str, required=True, default=10, help='end tag')

args = parser.parse_args()

def Iq_calculator(run,startTag,endTag):
    """
    Calcuale the Iq and Iphi of an entire run and generates an h5 file with the Iqs for each shot
    args:
        run : run number without extensions
    """

    # detector params
    path = '/UserData/maddalena/sacla2022'
    ponifile='/04-utilities/geometry_final.poni'
#    sample_det_distance = 0.095
#    wavelength = 0.887e-10
#    Pixel1, Pixel2 = 50e-6, 50e-6
#    posx, posy = Pixel1*1200, Pixel2*1150
#    det = pyFAI.detectors.Detector(pixel1=Pixel1, pixel2=Pixel2, max_shape=[2399,2399])
#    ai = pyFAI.azimuthalIntegrator.AzimuthalIntegrator(dist=sample_det_distance, detector=det, wavelength=wavelength, poni1=posx, poni2=posy)
    ai=pyFAI.load(f'{path}{ponifile}')
    # integration params
    nbins = 300
    n_phi = 30
    radial_range = [0,27]
    mask = np.load(f'{path}/04-utilities/mask.npy')
    
    print("Opening the compressed h5 file")
    with h5py.File(f'{path}/02-h5compression/{run}_{startTag}_{endTag}.h5', 'r') as f:
        maxtag = len(f[f'/run_{run}/event_info/tag_number_list'][:])
        I = np.zeros([maxtag, n_phi, nbins])
        i = 0

        print("Start calculating the Iq and Iphi")
        for tag in f[f'/run_{run}/event_info/tag_number_list'][:maxtag]:
            I[i,:,:], q, phi = ai.integrate2d_ng(f[f'/run_{run}/detector_2d_assembled_1/tag_{tag}/detector_data'][:], 
                                        nbins, n_phi, mask=mask, correctSolidAngle=True, unit='q_nm^-1', radial_range=radial_range)
            i += 1
        startTag=f[f'/run_{run}/event_info/tag_number_list'][0]
        endTag=f[f'/run_{run}/event_info/tag_number_list'][maxtag-1]
    print("End of Iq and Iphi calculation")

    hf = h5py.File(f'{path}/03-h5analysis/IqPhi_{run}_{startTag}_{endTag}.h5', 'w')
    hf.create_dataset('q', data=q/10) ##! in angstrom
    hf.create_dataset('I', data=I)
    hf.create_dataset('phi', data=phi)
    hf.create_dataset('PulseEnergy', data=f[f'/run_{run}/event_info/bl_3/oh_2/bm_1_pulse_energy_in_joule'])
    hf.create_dataset('PhotonEnergy', data=f[f'/run_{run}/event_info/bl_3/oh_2/photon_energy_in_eV'])
    hf.create_dataset('tags', data=f[f'/run_{run}/event_info/tag_number_list'])
    hf.create_dataset('shutter', data=f[f'/run_{run}/event_info/bl_3/eh_1/xfel_pulse_selector_status'])
    hf.close()

    print("Analysis saved in f'{path}/03-h5analysis/IqPhi_{run}_{startTag}_{endTag}.h5'")

print("run: ", args.run)
print("start tag: ", args.start)
print("end tag", args.end)

Iq_calculator(args.run, args.start, args.end)
