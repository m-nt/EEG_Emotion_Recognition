import scipy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import mne

# importing datasets 
data = mne.io.read_raw_edf("./S001R01.edf")
#print(data.info)
# List of all 32 channel
Channel_list = ['Fp1.','Fp2.','F3..','F4..','F7..','F8..','Fc5.','Fc6.','Fc1.','Fc2.','Af3.','Af4.','C3..','C4..','T7..','T8..','Fz..','Cz..','Fc3.','Fc4.','Fp3.','Fp4.','Af7.','Af8.','Afz.','Po3.','Po4.','Po7.','Po8.','Poz','T9..','T10.']
# Data selection with diferent channels
data_channel10 = data.pick_channels(Channel_list[0:10])
data_channel14 = data.pick_channels(Channel_list[0:14])
data_channel18 = data.pick_channels(Channel_list[0:18])
data_channel32 = data.pick_channels(Channel_list)

scaler = MinMaxScaler()
scaler.partial_fit(data_channel10.get_data())
raw = scaler.transform(data_channel10.get_data())
#raw = mne.io.RawArray(raw,data.info)
#print(type(raw))
#data_channel10.plot(duration=5, n_channels=10)
plt.plot(np.arange(0,len(raw[0])),raw[0])
plt.show()