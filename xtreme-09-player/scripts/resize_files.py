# ==========================
#
# Purpose: read mp4 file, generate a frame for each one, and add prefix
#
# ==========================

from PIL import Image 
import glob, os 
size = 600, 600
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + "_resize.jpg", "JPEG")


