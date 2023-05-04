import cv2
from tracker import *
from csv import DictWriter
import csv
import keyboard

# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture(r"E:\University\Semester 6\Grad\CHICK_t\CHICK_t\object_tracking\object_tracking\New folder\14 12 vids\walk10.mp4")
# cap=cv2.VideoCapture("highway.mp4")
# Object detection from Stable camera

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=75)
row= list()  
ys , ye , xs , xe =370 , 750 , 140 , 690
trajct = 0
row.append('walking')
traj = []
while True:
    ret, frame = cap.read()
    x=i=0
    if ret ==True:


        trajct +=1
        height, width, _ = frame.shape
        flag=0
        f2=frame
        # Extract Region of interest
        roi = frame[ys:ye,xs:xe]
        if i ==0:
             b_frame =roi
        if i %10==0:
        # 1. Object Detection
            mask = object_detector.apply(b_frame)
            b_frame = roi 
            _, mask = cv2.threshold(mask,0, 255, cv2.THRESH_TRIANGLE)
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            detections = []
            max=-99999

        #mask = cv2.GaussianBlur(mask, (5, 5), cv2.BORDER_DEFAULT)
        
        
            for cnt in contours:
            # Calculate area and remove small elements
                area = cv2.contourArea(cnt)
                if area>max and area>50 :
                    max = area
                    x, y, w, h = cv2.boundingRect(cnt)
               
            
            
                #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            if x!=0:    
                detections.append([x, y, w, h])
        # 2. Object Tracking
                boxes_ids,xx,cy= tracker.update(detections)
                row.append(xx)
                row.append(cy)
                flag=0
        
                for box_id in boxes_ids:
                    x, y, w, h, id = box_id
                # row.append(x)
                # row.append(y)
                #cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    if trajct%2 ==0:
                        traj.append(x+460)
                        traj.append(y+70)
                    #for j in range(0,len(traj),2):
                        
                        #cv2.circle(f2,(traj[j],traj[j+1]),3,(0,0,255),5)
                    #cv2.rectangle(f2, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        if keyboard.is_pressed('left'):  # if key 'q' is pressed 
            if xs>10:

                xs = xs - 10
            if xe>10:
                xe = xe - 10
        if keyboard.is_pressed('right'):  # if key 'q' is pressed 
            xe = xe + 10
            xs = xs + 10
        if keyboard.is_pressed('up'):  # if key 'q' is pressed 
            if ys>10:
                ys = ys - 10
            if ye >10:
                ye = ye - 10
        if keyboard.is_pressed('down'):  # if key 'q' is pressed 
            ye = ye + 10
            ys = ys + 10


        if keyboard.is_pressed('r'):  # if key 'q' is pressed 
            if xs>10:
                xs = xs - 10

        if keyboard.is_pressed('e'):  # if key 'q' is pressed 
            xe = xe + 10
  
        if keyboard.is_pressed('t'):  # if key 'q' is pressed 
            if ys>10:
                ys = ys - 10

        if keyboard.is_pressed('s'):  # if key 'q' is pressed 
            ye = ye + 10


        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            
            xs = xs + 10

        if keyboard.is_pressed('y'):  # if key 'q' is pressed 
            if xe > 10:
                xe = xe - 10
  
        if keyboard.is_pressed('w'):  # if key 'q' is pressed 
           
            ys = ys + 10

        if keyboard.is_pressed('h'):  # if key 'q' is pressed 
            if ye > 10:
                ye = ye - 10
                    

       
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("roi", roi)
        #cv2.imshow("f2", f2)
        i+=1
        key = cv2.waitKey(30)
    else:
        break
    if key == 27:
        break
# with open(r'E:\University\Semester 6\Grad\CHICK_t\CHICK_t\object_tracking\object_tracking\New folder\14 12.csv', 'a+') as f:
#     writer = csv.writer(f)

#     writer.writerow(row)
# f.close()
cap.release()
cv2.destroyAllWindows()
print(ys,',',ye,',',xs,',',xe)