import numpy as np
import matplotlib.pyplot as plt
import json

with open('/Users/paul.le/Desktop/data.json', 'r') as json_file:
		s = json.load(json_file)

x = []
y = []

valence = []
danceability = []
energy = []
acousticness = []
instrumentalness = []
speechiness = []
liveness = []

xValue = 'Valence'
yValue = 'Danceability'

for distro in s:
    x.append(distro[xValue])
    y.append(distro[yValue])
'''
    valence.append(distro['Valence'])
    danceability.append(distro['Danceability'])
    energy.append(distro['Energy'])
    acousticness.append(distro['Acousticness'])
    instrumentalness.append(distro['Instrumentalness'])
    speechiness.append(distro['Speechiness'])
    liveness.append(distro['Liveness'])
'''
'''
valenceAvg = sum(valence) / float(len(valence))
danceabilityAvg = sum(danceability) / float(len(danceability))
energyAvg = sum(energy) / float(len(energy))
acousticnessAvg = sum(acousticness) / float(len(acousticness))
instrumentalnessAvg = sum(instrumentalness) / float(len(instrumentalness))
speechinessAvg = sum(speechiness) / float(len(speechiness))
livenessAvg = sum(liveness) / float(len(liveness))
'''

#array = [valenceAvg, danceabilityAvg, energyAvg, acousticnessAvg, instrumentalnessAvg, speechinessAvg, livenessAvg]
#array.sort()

# Scatter Plot
plt.scatter(x, y, s=np.pi*3, c='#006EB6', cmap='#006EB6', alpha=0.5)
plt.title('Spotify Data')
plt.xlabel(xValue)
plt.ylabel(yValue)
plt.show()

# Bar Chart
#objects = ('Valence', 'Danceability', 'Energy', 'Acousticness', 'Instrumentalness', 'Speechiness', 'Liveness')
#y_pos = np.arange(len(objects))

#plt.bar(y_pos, array, align='center', color=(0,0,0), alpha=0.5)
#plt.xticks(y_pos, objects)
#plt.title('Spotify Artist Analysis')

#plt.show()
