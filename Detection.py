import cv2
import numpy as np
import pandas as pd
  
#Welcome screen
print("-"*96)
print("Welcome  To Color Detection Project ".center(90))
print("-"*96)
print("\n\n")
imgread=input("\t\tEnter Image File with extension :")  #image input
if imgread.endswith('.jpg'):
    print("\n\n")
    print("A New Window has been started with your selected image file ".center(90))
    print("Thank you!!!!".center(90))
else:
    print("\n\n")
    print("Error !!Please choose correct file format")



img=cv2.imread(imgread)  #open image  with opencv

clicked = False

r=g=b=xpos=ypos=0  # global variable for x y z set to 0

index=["color","color_name","hex","Red","Green","Blue"]  #Reading csv file with panda for the upper coloumn
csv = pd.read_csv('colorset.csv',names=index,header=None)

def getColorName(R,G,B): #calculate minimum distance from all colors and get the most matching color
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"Red"])) + abs(G- int(csv.loc[i,"Green"]))+ abs(B- int(csv.loc[i,"Blue"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

def get_corr(event, x,y,flags,param):#get x y coordinates of mouse
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        r=int(r)
        g=int(g)
        b=int(b)     

cv2.namedWindow('image')
cv2.setMouseCallback('image',get_corr)
while(1):
    cv2.imshow("image",img)
    if (clicked): 
        cv2.rectangle(img,(10,10),(700,60),(b,g,r),-1)

        text=getColorName(r,g,b)+' | Red='+ str(r) +' Green='+ str(g) +' Blue='+ str(b)
        
        cv2.putText(img, text,(40,40),2,0.8,(255,255,255),2,cv2.LINE_AA)

        if(r+g+b>=600):
            cv2.putText(img,text,(40,40),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False
   
    if cv2.waitKey(20) & 0xFF==27:
        break
    
cv2.destroyAllWindows()



#To pass with cmd with argparse
"""import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
imgread = args['image']"""