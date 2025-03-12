import numpy as np
from PIL import Image

img_path = "images/birds.jpg"

def flip_img(img_arr, direction="hor"):
    if direction == "hor":
        return np.flip(img_arr, axis=1)
    elif direction == "ver":
        return np.flip(img_arr, axis=0)
    return img_arr

def add_noise(img_arr, intensity=50):
    noise = np.random.randint(0, intensity, img_arr.shape, dtype=np.uint8)
    return np.clip(img_arr + noise, 0, 255)

def brighten_channels(img_arr, channel=0, value=40):
    brightened_img = img_arr.copy()
    brightened_img[:, :, channel] = np.clip(brightened_img[:, :, channel] + value, 0, 255)
    return brightened_img

def apply_mask(img_arr, mask_size=100):
    masked_img = img_arr.copy()
    h, w, _ = img_arr.shape
    center_x, center_y = w // 2, h // 2
    x1, y1 = center_x - mask_size // 2, center_y - mask_size // 2
    x2, y2 = x1 + mask_size, y1 + mask_size
    masked_img[y1:y2, x1:x2] = [0, 0, 0]
    return masked_img

img = Image.open(img_path)
img_arr = np.array(img)

flip_hor = flip_img(img_arr, "hor")
flip_ver = flip_img(img_arr, "ver")
noisy_img = add_noise(img_arr)
brightened_img = brighten_channels(img_arr, channel=0, value=40)
masked_img = apply_mask(img_arr)

Image.fromarray(flip_hor).save("images/flip_hor.jpg")
Image.fromarray(flip_ver).save("images/flip_ver.jpg")
Image.fromarray(noisy_img).save("images/noisy_img.jpg")
Image.fromarray(brightened_img).save("images/brightened_img.jpg")
Image.fromarray(masked_img).save("images/masked_img.jpg")
