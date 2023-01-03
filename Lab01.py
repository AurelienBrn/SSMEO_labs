#%%
import numpy as np
import cv2



#%% Read image and define parameters
image_path = '/media/topo/Data/ALS/Vallet/Images/18704.jpg'
output_path = '/media/topo/Data/ALS/Vallet/Images/'

img = cv2.imread(image_path)
param= {'x':[], 'y':[]}

#%% Define callback function  
def click_event(event, x, y, flags, param):
    buf = 25
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.line(img, (x,y-buf), (x, y+buf), (51,87,255), 1)
        cv2.line(img, (x-buf,y), (x+buf, y), (51,87,255), 1)
        cv2.imshow('image', img)
        param['x'].append(x)
        param['y'].append(y)

    if event == cv2.EVENT_RBUTTONDOWN:
        
        for i in range(len(param['x'])):
            cv2.line(img, (param['x'][i],param['y'][i]-buf), (param['x'][i], param['y'][i]+buf), (255,0,0), 1)
            cv2.line(img, (param['x'][i]-buf,param['y'][i]), (param['x'][i]+buf, param['y'][i]), (255,0,0), 1)
            #write coordinates on image
            cv2.putText(img, f"{param['x'][i]}, {param['y'][i]}",(param['x'][i]+5, param['y'][i]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1, cv2.LINE_AA,)
            cv2.imshow('image', img)
        np.savetxt(output_path + 'coordinates.txt', np.array([param['x'], param['y']]).T, fmt='%f')

    


#%% Image display loop
cv2.namedWindow('image', cv2.WINDOW_GUI_NORMAL)


cv2.setMouseCallback('image', click_event, param)
cv2.imshow('image', img)
cv2.resizeWindow('image', 600,600)

while True:
    k = cv2.waitKey(100)
    if k == 27: # wait for ESC key to exit
        cv2.destroyAllWindows()
        break        
    if cv2.getWindowProperty('image',cv2.WND_PROP_VISIBLE) < 1:# wait for window to be closed        
        break        
cv2.destroyAllWindows()


# TODO : define a function to read the coordinates from a file

# %%
# define function to read coordinates from a file
def read_coordinates(file_path):
    coordinates = np.loadtxt(file_path)
    return coordinates

# TODO : define a function to draw the coordinates on an image
# TODO : define camera distortion correction function from coef
# TODO : estimate x' y' from x y and camera distortion correction function$
# TODO : draw camera distortion correction vector on image
# TODO : convert to jupyter notebook

# %%
