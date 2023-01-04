import os
import cv2
import numpy as np
 

#Mappák összeszedése



#bele kell tenni az Alabama... mappák mellé
Direc = os.getcwd()
print('Ebben a directory-ban vannak a mappák:',Direc)
 
folders = os.listdir()
folders = [f for f in folders if not os.path.isfile('/'+f) and f != 'Picture_merger.py'] #Filtering only the folders.

print('\nEzek a mappák vannak benne:',folders,sep = '\n')



#Create new super folder
#If it already exists, comment this line
print("Új mappa létrehozáse: /50States10K_Panorama")
os.mkdir('../' + '50States10K_Panorama')

for folder in folders:
    print(f'{folder} in progress...')
    pictures = os.listdir(Direc + '/' + folder)

    #Create new folder
    os.mkdir('../50States10K_Panorama/' + folder)
    
    #Get every location
    names = []
    for picture in pictures:
        if picture[-5] == '0' and picture[-6] == '_':
            names.append(picture[:-5])

    #concatenating and writing the new images
    for name in names:
        img1 = cv2.imread(folder + '/' + name + '0.jpg')
        img2 = cv2.imread(folder + '/' + name + '90.jpg')
        img3 = cv2.imread(folder + '/' + name + '180.jpg')
        img4 = cv2.imread(folder + '/' + name + '270.jpg')

        #Kell egy kitétel, ha esetleg lenne olyan location, ahol nincs meg mind a 4 kép
        #Pl.: Alaskában van, pont bele is futottam...
        if img1 is not None and img2 is not None and img3 is not None and img4 is not None:
            vis = np.concatenate((img1, img2, img3, img4), axis=1)
            #cv2.imshow('Osszekapcsolt',vis)

            cv2.imwrite('../50States10K_Panorama/' + folder + '/' + name + '.jpg', vis)
        
        

        
        
    
