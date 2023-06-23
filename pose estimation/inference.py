from ultralytics import YOLO
import cv2


model_path = 'E:/University/Semester 6/Grad/CHICK_t/CHICK_t/April/pose/pose-detection-keypoints-estimation-yolov8-main/pose-detection-keypoints-estimation-yolov8-main/runs/pose/train16\weights/last.pt'

image_path = '/samples/1 (1).png'
img = cv2.imread(image_path)

model = YOLO(model_path)

results = model(image_path)[0]

for result in results:
    for keypoint_indx, keypoint in enumerate(result.keypoints.tolist()):
        cv2.putText(img, str(keypoint_indx), (int(keypoint[0]), int(keypoint[1])),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
