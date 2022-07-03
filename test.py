import cv2



def latent():
  src = cv2.imread( "/content/ImageInpaintingDeepfill/input/input_img.png")
  grayScale = cv2.cvtColor( src, cv2.COLOR_RGB2GRAY )
  cv2.imwrite('grayScale_sample1.jpg', grayScale, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
  kernel = cv2.getStructuringElement(1,(17,17))
  blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
  cv2.imwrite('blackhat_sample1.jpg', blackhat, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
  ret,thresh2 = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
  cv2.imwrite('thresholded_sample1.jpg', thresh2, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
  dst = cv2.inpaint(src,thresh2,1,cv2.INPAINT_TELEA)
  cv2.imwrite('/content/ImageInpaintingDeepfill/output/inapinted_op.jpg', dst, [int(cv2.IMWRITE_JPEG_QUALITY), 90])