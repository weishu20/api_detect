import argparse
import sys,os
import cv2

from common.detect import Detect

if __name__=="__main__":
  a = argparse.ArgumentParser()
  a.add_argument("--fn")
  a.add_argument("--save_path")

  args = a.parse_args()
  if args.fn is None or args.save_path is None:
    a.print_help()
    sys.exit(1)

  if (not os.path.exists(args.fn)):
    print("directories do not exist")
    sys.exit(1)

  detect = Detect()
  boundingboxes, points = detect.API_3R_detect(args.fn)
  img = cv2.imread(args.fn)
  img1 = detect.drawBoxes(img, boundingboxes)
  cv2.imwrite(args.save_path, img1)