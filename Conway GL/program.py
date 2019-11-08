import cv2
import numpy as np

#sets color for both variables
deadColor=(0,0,0)
liveColor=(255,255,255)


deadCell=0
liveCell=1

#getting image info
def show(img, title="image", wait=30):
    d=np.max(img.shape)
    h,w=img.shape[:2]
    unitSize=1200//d #d is dimensions
    resized = cv2.resize(np.uint8(img), (unitSize*w,unitSize*h), interpolation = cv2.INTER_AREA)
    cv2.imshow(title, resized)
    cv2.waitKey(wait) # 0 means wait for key input. postive value waits for that many milliseconds

#sets dementions of what will be displayed 
def showCA(ca, wait=0):
    h,w = ca.shape[:2]
    out = np.zeros((h,w,3))

    out[ca==liveCell]=liveColor
    out[ca==deadCell]=deadColor
    show(out, wait=wait)
    
def load(filename):
    img=cv2.imread(filename)
    h,w = img.shape[:2]
    out = np.zeros((h,w))
    out[img[:,:,1]<100]=deadCell
    out[img[:,:,1]>150]=liveCell
    return out
    
    

def iterate(world):
    newWorld=world*1
    kernel=np.int16([[1,1,1],
                     [1,0,1],
                     [1,1,1]])
    whereTheLiveCellsAre=np.int16(world==liveCell)
    neighborCount=cv2.filter2D(whereTheLiveCellsAre,-1,kernel,borderType=cv2.BORDER_CONSTANT)
    newWorld[np.logical_and(neighborCount > 3, world==liveCell)]=deadCell
    newWorld[np.logical_and(neighborCount == 3, world==deadCell)]=liveCell
    newWorld[np.logical_and(neighborCount < 2, world==liveCell)]=deadCell
    newWorld[np.logical_and(np.logical_and(world==liveCell,2<=neighborCount),neighborCount<=3)]= liveCell
    return newWorld




world=load("canvas.png")
fps=30
while True:
    showCA(world,1000//fps)
    world=iterate(world)
    #print(i)
