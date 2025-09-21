import cv2
import os
video_path='roboticarm.avi'
video=cv2.videoCapture(video_path)
ret=True
while ret:
  ret,frame=video.read()
  if ret:
    cv2.imshow('frame',frame)
    #video is 60fps, which means every frame takes 1/60 i.e. 16ms
    cv2.waitkey(16)


video.release()
cv2.destroyAllWindows()
