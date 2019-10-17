import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer();
path='dataSet'

def getImagesWithID(path):
   
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
   
    faces=[]
   
    IDs=[]
  
    for imagePath in imagePaths:
        
        faceImage=Image.open(imagePath).convert('L')
        
        faceNp=np.array(faceImage,'uint8')
       
        ID=int(os.path.split(imagePath)[-1].split(".")[1])
      
        faces.append(ID)
        cv2.imshow("training", faceNp)
        cv2.waitKey(10)
        return IDs,faces
    Ids,faces=getImagesWithID(path)
       

recognizer.train(faces , np.array(Ids))
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()
