import numpy as np
import cv2
import glob

images  = []
for file in glob.glob("*.png"):
    if "reference" in file or "output" in file or "gain" in file or "toprocess" in file:
        continue
    print(file)
    images.append(cv2.imread(file))

images = np.array(images)
print(images.shape)

reference_image = np.average(images[:,:,:,:], axis=0)

white_r = reference_image[:, :, 2]
white_g = reference_image[:, :, 1]
white_b = reference_image[:, :, 0]

dark_r = np.ones_like(reference_image[:, :, 2]) * 16
dark_g = np.ones_like(reference_image[:, :, 1]) * 16
dark_b = np.ones_like(reference_image[:, :, 0]) * 16

target_white = 220
target_black = 8


gain_white_b = (target_white - target_black) / (white_b - dark_b).astype(float)
gain_white_g =  (target_white - target_black) / (white_g - dark_g).astype(float)
gain_white_r = (target_white - target_black) / (white_r - dark_r).astype(float)
cv2.imwrite("gain_r.png", gain_white_r*10)
cv2.imwrite("gain_b.png", gain_white_b*10)
cv2.imwrite("gain_g.png", gain_white_g*10)

offset_r = target_black - (dark_r * gain_white_r)
offset_g = target_black - (dark_g * gain_white_g)
offset_b = target_black - (dark_b * gain_white_b)

img_process = cv2.imread("toprocess3.png")
img_process[:,:,2] = np.clip(img_process[:,:,2]  * gain_white_r + offset_r, 0, 255)
img_process[:,:,1] = np.clip(img_process[:,:,1]  * gain_white_g + offset_g, 0, 255)
img_process[:,:,0] = np.clip(img_process[:,:,0]  * gain_white_b + offset_b, 0, 255)



cv2.imwrite("reference.png", reference_image)
cv2.imwrite("output.png", img_process)
