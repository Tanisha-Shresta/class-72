import cvzone
import cv2
import os
import math
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceMeshModule import FaceMeshDetector

try:
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    filterImages =[]
    path = "images"
    pathList = os.listdir(path)

    for pathImg in pathList:
        img = (cv2.imread(path+"/"+pathImg, cv2.IMREAD_UNCHANGED))
        filterImages.append(img)

    detector = HandDetector(detectionCon=0.8)

    # Creating object to detect the face
    detector = HandDetector(detectionCon=0.8)
    faceDetector = FaceMeshDetector(maxFaces=2)
except Exception as e:
    print(e)
    
   
while True:
    try:
        success, cameraFeedImg = cap.read()
        
        cameraFeedImg= cv2.resize(cameraFeedImg, (640, 480))
        cameraFeedImg = cv2.flip(cameraFeedImg, 1)

        wHeight, wWidth, wChannel = cameraFeedImg.shape
        
        # Detecting face in the cameraFeedImg
        faceImages = []
        path = "Images/"
        pathList = os.listdir(path)
        pathList.sort()
        # Loop over each face in the faces
        for x, pathImg in enumerate(pathList):
            # Get x and y coordinates of face[21] landmark and save them in xLoc and yLoc variables
            img = (cv2.imread(path+"/"+pathImg, cv2.IMREAD_UNCHANGED))
            img = cv2.resize(img, (100, 100))
            faceImages.append(img)
            # Calculate and store distance between face[21] and face[251] landmakr i.e width of the face    
            def showObjectOnface(backImg, frontImg, xLoc, yLoc, dist, rf, rx, ry):
            
            # Set initial scale to 55, dx to 25 and dy to 35
            
 
            # Distance between 13, 14 is mouth open distance, store it in lipEndDistance variable
            # Distanvce between 76, 106 lip ends, store it in lipOpenDistance variable
             lipOpenDistance = math.dist(face[13], face[14])
             lipEndDistance = math.dist(face[76], face[306])
            # Create variable filterImage and assign filterImages[0] to act as initial filter image
            

            # Check if lipOpenDistance < 10 and set filterImage to filterImages[0]  

            # Else set filterImage to filterImages[1]    

            # Check if dist/lipEndDistance < 2.5 and set filterImage to filterImages[2]  
            
            # Calculate resizefactor as dist/scale
             resizefactor = dist/rf
            # Resize filterImage to standard size of 100,100 
            
            # Resize filterImage to face size using resizefactor
            frontImg = cv2.resize(frontImg, (0, 0), fx=resizefactor, fy=resizefactor)
            # Show filterimage on cameraFeedImg at int(xLoc - (resizefactor*dx)) for x and int(yLoc - (resizefactor*dy)) for y axis
            backImg = cvzone.overlayPNG(backImg, frontImg, [int(
        xLoc - (resizefactor*rx)), int(yLoc - (resizefactor * ry))])
                                   
    except Exception as e:
        print("Exception", e) 

    cv2.imshow("Image", cameraFeedImg)
    cv2.waitKey(1)