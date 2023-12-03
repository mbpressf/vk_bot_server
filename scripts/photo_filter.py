import cv2
import numpy as np
import random
from select_text import func_select_text

def red_filter(image):
    red_filter = np.copy(image)
    red_filter[:, :, 0] = 10  
    red_filter[:, :, 1] = 0 
    return red_filter


def blue_filter(image):
    blue_filter = np.copy(image)
    blue_filter[:, :, 2] = 0 
    blue_filter[:, :, 1] = 0 

    return blue_filter

def green_pink_filter(image):
    green_channel = image[:, :, 1]
    negative_green = 255 - green_channel

    image[:, :, 1] = negative_green

    return image

def yellow_green_filter(image):

    red_channel = image[:, :, 2]
    green_channel = image[:, :, 1]

    negative_red = 255 - red_channel
    negative_green = 255 - green_channel

    image[:, :, 2] = negative_red
    image[:, :, 1] = negative_green

    return image


def pink_green_filter(image):
    red_channel = image[:, :, 2]
    blue_channel = image[:, :, 0]

    negative_red = 255 - red_channel
    negative_blue = 255 - blue_channel

    image[:, :, 2] = negative_red  
    image[:, :, 0] = negative_blue  
    
    return image


def blue_red_filter(image):
    image = np.copy(image)

    blue_channel = image[:, :, 0]
    green_channel = image[:, :, 1]

    negative_blue = 255 - blue_channel
    negative_green = 255 - green_channel

    image[:, :, 0] = negative_blue 
    image[:, :, 1] = negative_green  


    return image

def green_pink_filter(image):
    blue_channel = image[:, :, 0]

    negative_blue = 255 - blue_channel

    image[:, :, 0] = negative_blue  

    return image

def negative_filter(image):

    image = 255 - image

    return image

def green_filter(image):
    image[:, :, 1] = cv2.add(image[:, :, 1], 50)

    return image

def black_filter(image):    
    
    image[:, :, 2] = cv2.add(image[:, :, 2], 150)

    brightness_factor = 0.1
    image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)

    return image

def white_blue_filter(image):
    brightness_factor = 4
    image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)

    image[:, :, 0] = cv2.add(image[:, :, 0], 20)

    return image

def pink_filter(image):
    image = 255 - image

    image[:, :, 2] = 255 
    image[:, :, 0] = 255

    return image


# red_filter(image=image)
# blue_filter(image=image)
# yellow_green_filter(image=image)
# pink_filter(image=image)
# pink_green_filter(image=image)
# blue_red_filter(image=image)
# green_filter(image=image)
# green_pink_filter(image=image)
# negative_filter(image=image)
# black_filter(image=image)
# white_blue_filter(image=image)
# pink_filter(image=image)


def main_func(img):


    image = cv2.imread(img)
    filterest = [red_filter, blue_filter, yellow_green_filter, pink_filter, white_blue_filter, black_filter, green_filter, negative_filter, green_pink_filter, blue_red_filter, pink_green_filter]
    filteres1t = [blue_filter]
    random.shuffle(filterest)

    random_func = random.choice(filterest)

    # print()
    # print()
    # print()
    # print()

    # print(random_func)
    filter_img = random_func(image)


    cv2.imwrite('filter_img.jpg', filter_img)
    print()
    print()
    print()
    print()

    txt = func_select_text(random_func)



    return txt


# def texting(filter):

#     if filter == red_filter:
#         f = open("red_filter.txt", 'r')
#         txt = f.read()
#         return "Вот тут он хочет страпонить мои яйца" 
        
#     else:
#         return "Страпоньте мои яйца"


    

    

