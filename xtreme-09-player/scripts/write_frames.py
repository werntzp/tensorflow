# ==========================
#
# Purpose: read mp4 file, generate a frame for each one, and add prefix
#
# ==========================
import cv2

fn = sys.argv[0]
pf = sys.argv[1]

vidcap = cv2.VideoCapture(fn)
success, image = vidcap.read()
count = 0 
success = True
print("starting ... ")
while success:
    cv2.imwrite(pf + "-frame%d.jpg" % count, image)
    success, image = vidcap.read()
    count += 1
print("completed - created " + str(count) + " frames")
  
 
