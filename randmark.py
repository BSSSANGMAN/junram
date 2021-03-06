import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture("C://Users/user/PycharmProjects/datasets/try1.mp4")
pTime=0

mpDraw=mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMash = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:
    success,img=cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceMash.process(imgRGB)
    if results.detections:  # 가능하면
        for id, detection in enumerate(results.detections):
            # mpDraw.draw_detection(img,detection)
            # print(id,detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            x = int(bboxC.xmin * iw)
            y = int(bboxC.ymin * ih)
            w = int(bboxC.width * iw)
            h = int(bboxC.height * ih)
            cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
    cTime=time.time()
    try:
        fps=1/(cTime-pTime)
    except:
        fps=1
    pTime=cTime
    cv2.putText(img,f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,
                3,(0,255,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)