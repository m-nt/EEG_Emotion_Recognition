import scipy
from scipy.signal import welch
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier as knn
import mne
from mne.minimum_norm import read_inverse_operator, compute_source_psd
import pywt
import yasa
# importing datasets 
data = mne.io.read_raw_edf("./S001R01.edf")

# List of all 32 channel
Channel_list = ['Fp1.','Fp2.','F3..','F4..','F7..','F8..','Fc5.','Fc6.','Fc1.','Fc2.','Af3.','Af4.','C3..','C4..','T7..','T8..','Fz..','Cz..','Fc3.','Fc4.','Fp3.','Fp4.','Af7.','Af8.','Afz.','Po3.','Po4.','Po7.','Po8.','Poz','T9..','T10.']

# Data selection with diferent channels

data_channel10 = data.pick_channels(Channel_list[0:10])
data_channel14 = data.pick_channels(Channel_list[0:14])
data_channel18 = data.pick_channels(Channel_list[0:18])
data_channel32 = data.pick_channels(Channel_list)

# **** WARNING ****
# PreProcessing | WARNING because data is pre processed already this normalization will break the data
# Add MinMax Normalization 
# scaler = MinMaxScaler()
# scaler.fit(data_channel10.get_data())
# raw = scaler.transform(data_channel1.get_data())

# PSD compution
freqs, psd = welch(data_channel10.get_data()[0], 256, nperseg=1024)


# Alpha Bata Theta Gamma
print(yasa.bandpower_from_psd(psd, freqs))

# Convert back to mne array for ploting
#raw = mne.io.RawArray(raw,data.info)
#print(type(raw))
#raw.plot(duration=5, n_channels=10)
#plt.show()
