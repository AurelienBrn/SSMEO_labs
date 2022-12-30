#%%
import numpy as np
import cv2



#%% Read image and define parameters
image_path = '/home/aurelien/Pictures/18704.jpg'

img = cv2.imread(image_path)
param= {'x':[], 'y':[]}

#%% Define callback function  
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.line(img, (x,y-25), (x, y+25), (51,87,255), 1)
        cv2.line(img, (x-25,y), (x+25, y), (51,87,255), 1)
        cv2.imshow('image', img)
        param['x'].append(x)
        param['y'].append(y)

#%% Image display loop
cv2.namedWindow('image', cv2.WINDOW_GUI_NORMAL)
for i in range(0, max(img.shape), 500):
    cv2.line(img, (0,i), (img.shape[1], i), (0,0,0), 3)
    cv2.line(img, (i,0), (i, img.shape[0]), (0,0,0), 3)

cv2.setMouseCallback('image', click_event, param)
cv2.imshow('image', img)
cv2.resizeWindow('image', 600,600)

while True:
    k = cv2.waitKey(100) # change the value from the original 0 (wait forever) to something appropriate
    if k == 27: # wait for ESC key to exit
        cv2.destroyAllWindows()
        break        
    if cv2.getWindowProperty('image',cv2.WND_PROP_VISIBLE) < 1:# wait for window to be closed        
        break        
cv2.destroyAllWindows()

# TODO : save the coordinates in a file
# TODO : define a function to read the coordinates from a file
# TODO : define a function to draw the coordinates on an image
# TODO : define camera distortion correction function from coef
# TODO : estimate x' y' from x y and camera distortion correction function$
# TODO : draw camera distortion correction vector on image
# TODO : convert to jupyter notebook
