# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import os.path

# parameters of augmentation
scale_range = 0.2
shift_range = 0.2
brightness_range = 50

# Impulse noise
def SaltAndPepper(image, noise_density):
    '''
    SP_NoiseImg=src.copy()
    SP_NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for _ in range(SP_NoiseNum):
        randR=np.random.randint(0,src.shape[0]-1)
        randG=np.random.randint(0,src.shape[1]-1)
        randB=np.random.randint(0,3)
        if np.random.randint(0,1)==0:
            SP_NoiseImg[randR,randG,randB]=0
        else:
            SP_NoiseImg[randR,randG,randB]=255
    return SP_NoiseImg
    '''
    rows, cols = image.shape[:2]
    noise = np.random.choice((0, 1, 2), size=(rows, cols), p=[1 - noise_density, noise_density/2., noise_density/2.])
    noise = np.uint8(noise)
    salt = cv2.bitwise_and(np.uint8(noise == 1), np.uint8(noise_density == 1))
    pepper = cv2.bitwise_and(np.uint8(noise == 2), np.uint8(noise_density == 1))
    noise_image = cv2.addWeighted(image, 1, 0.1 * salt, 0.1, 0)
    noise_image = cv2.addWeighted(noise_image, 1, 0.1 * pepper, 0.1, 0)
    return noise_image

# Gaussian noise
def GaussianNoise(image):
    '''
    G_Noiseimg = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    G_NoiseNum=int(percetage*image.shape[0]*image.shape[1])
    for _ in range(G_NoiseNum):
        temp_x = np.random.randint(0,h)
        temp_y = np.random.randint(0,w)
        G_Noiseimg[temp_x][temp_y][np.random.randint(3)] = np.random.randn(1)[0]
    return G_Noiseimg
    '''
    sigma_range = (0, 20)
    sigma = np.random.uniform(sigma_range[0], sigma_range[1])
    gaussian_noise = np.random.normal(0, sigma, image.shape)
    noise_image = cv2.add(image, gaussian_noise.astype(np.uint8))
    return noise_image

# Brightness
def Brightness(image):
    '''
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    #get brighter
    for xi in range(0,w):
        for xj in range(0,h):
            image_copy[xj,xi,0] = np.clip(int(image[xj,xi,0]*percetage),a_max=255,a_min=0)
            image_copy[xj,xi,1] = np.clip(int(image[xj,xi,1]*percetage),a_max=255,a_min=0)
            image_copy[xj,xi,2] = np.clip(int(image[xj,xi,2]*percetage),a_max=255,a_min=0)
    return image_copy
    '''
    brightness = np.random.randint(-brightness_range, brightness_range)
    brightness_image = cv2.add(image, brightness)
    return brightness_image

# rotate
def Rotate(image, angle_range = 0):
    '''
    (h, w) = image.shape[:2]
    # If no rotation center is specified, the center of the image is set as the rotation center
    if center is None:
        center = (w / 2, h / 2)
    m = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, m, (w, h))
    return rotated
    '''
    angle = np.random.uniform(-angle_range, angle_range)
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotate_image = cv2.warpAffine(image, M, (cols, rows))
    return rotate_image

# turn over
def Flip(image):
    flip_image = cv2.flip(image, 1)
    return flip_image

# crop
def Crop(image):
    crop_range = (0.8, 1.0)
    rows, cols = image.shape[:2]
    crop_size = int(min(rows, cols) * crop_range[0])
    top = np.random.randint(0, rows - crop_size)
    left = np.random.randint(0, cols - crop_size)
    crop_image = image[top:top+crop_size, left:left+crop_size, :]
    return crop_image
    
def Shift(image):
    rows, cols = image.shape[:2]
    x_shift = np.random.uniform(-shift_range, shift_range) * cols
    y_shift = np.random.uniform(-shift_range, shift_range) * rows
    M = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
    shift_image = cv2.warpAffine(image, M, (cols, rows))
    return shift_image

def FigAug(root_path):
    # root_path = "../data/train"
    for dirpath, dirnames, filenames in os.walk(root_path):
        save_path = dirpath
        print('********')
        print(save_path)
        print('********')
        for file_i in filenames:
            file_i_path = os.path.join(dirpath, file_i)
            print(file_i_path)
            if '.DS_Store' in file_i_path:
                continue

            img_i = cv2.imread(file_i_path)
            filename = os.path.basename(file_i_path)

            img_crop = Crop(img_i)
            cv2.imwrite(os.path.join(save_path, 'crop_' + filename), img_crop)

            img_flip = Flip(img_i)
            cv2.imwrite(os.path.join(save_path, 'flip_' + filename), img_flip)

            img_rotate1 = Rotate(img_i, 90)
            cv2.imwrite(os.path.join(save_path, 'rotate90_' + filename), img_rotate1)
            img_rotate2 = Rotate(img_i, 180)
            cv2.imwrite(os.path.join(save_path, 'rotate180_' + filename), img_rotate2)
            img_rotate3 = Rotate(img_i, 270)
            cv2.imwrite(os.path.join(save_path, 'rotate270_' + filename), img_rotate3)

            img_shift = Shift(img_i)
            cv2.imwrite(os.path.join(save_path, 'shift_' + filename), img_shift)

            img_brighter = Brightness(img_i)
            cv2.imwrite(os.path.join(save_path, 'brighter_' + filename), img_brighter)

            img_salt = SaltAndPepper(img_i, 0.01)
            cv2.imwrite(os.path.join(save_path, 'salt_' + filename), img_salt)

            img_gaussian = GaussianNoise(img_i)
            cv2.imwrite(os.path.join(save_path, 'gaussian_' + filename), img_gaussian)

if __name__ == '__main__':
    path = '../Data/train/'
    FigAug(path)