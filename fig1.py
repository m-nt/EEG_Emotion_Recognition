import matplotlib.pyplot as plt
import Proccess as P
import numpy as np
import Channels

# extracting Channel 10, 14, 18 and 32 of the data using channel function from Channels.py for clean code
alpha10,beta10,theta10,gamma10  = Channels.Channel(P,10)

alpha14,beta14,theta14,gamma14  = Channels.Channel(P,14)

alpha18,beta18,theta18,gamma18  = Channels.Channel(P,18)

alpha32,beta32,theta32,gamma32  = Channels.Channel(P,32)

ind = np.arange(4)  # the x locations for the groups
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind + width/2+width, (theta10,theta14,theta18,theta32), width, yerr=(1,1,1,1),
                label='32 Channel')
rects2 = ax.bar(ind + width/2, (alpha10,alpha14,alpha18,alpha32), width, yerr=(1,1,1,1),
                label='18 Channel')
rects3 = ax.bar(ind - width/2, (beta10,beta14,beta18,beta32), width, yerr=(1,1,1,1),
                label='14 Channel')
rects4 = ax.bar(ind - width/2-width, (gamma10,gamma14,gamma18,gamma32), width, yerr=(1,1,1,1),
                label='10 Channel')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage')
ax.set_title('Fig. 2')
ax.set_xticks(ind)
ax.set_xticklabels(('Theta', 'Alpha', 'Beta','Gamma'))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.
    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")
autolabel(rects3, "right")
autolabel(rects4, "right")

fig.tight_layout()

plt.show()