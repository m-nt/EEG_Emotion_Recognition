

# Extracting Alpha, Beta, Theta and Gamma from Process.py freq_channels function 
def Channel(P,R):
    alpha,beta,theta,gamma = 0,0,0,0
    for i in range(0,R):
        alpha += P.freq_channels(i)['Alpha'][0]*100
        beta += P.freq_channels(i)['Beta'][0]*100
        theta += P.freq_channels(i)['Theta'][0]*100
        gamma += P.freq_channels(i)['Gamma'][0]*100
    alpha = int(alpha / R)
    beta = int(beta / R)
    theta = int(theta / R)
    gamma = int(gamma / R)
    return (alpha,beta,theta,gamma)
