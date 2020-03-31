import pickle
favourite = ['sims4','nfs','food','films']
f = open('favorites.dat','wb')
pickle.dump(favourite , f)
f.close()

import pickle
f = open('favorites.dat','rb')
favourite = pickle.load(f)
print(favourite