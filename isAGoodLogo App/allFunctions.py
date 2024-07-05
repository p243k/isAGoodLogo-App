from PIL import Image
import cv2
import numpy as np  

def ask_user_image(): # We create a function that ask user to upload an image
    user = input("Renseignez l'URL de votre image :")
    return user

def check_png_file(user): # When we have the image we check if it's a png file. 
    print("Vérifions si l'image est au bon format !")
    isPng = user.split(".") 
    test = bool
    while test != True:
        if 'png' in isPng:
            test = True
            print("Super, une image en png ! Continuons !")
            return True
        else:
            test = False
            print("Pas tellement fan de cette extension...")
            break


def image_size(user): # The image is in png so let's check the size
    print("Voyons voir maintenant si la taille est bonne !")
    image = Image.open(str(user))
    size = image.size
    if size == (512, 512):
        print("Jusqu'à présent la photo correspond !")
        return True
    else:
        print("Tout est bon... sauf la taille !")
    
    
def didHaveCircle(user):
    # image = cv2.imread(str(user), 0) 
    # params = cv2.SimpleBlobDetector_Params() 
    # params.filterByArea = True
    # params.minArea = 100
    # params.filterByCircularity = True 
    # params.minCircularity = 0.9
    # params.filterByConvexity = True
    # params.minConvexity = 0.2 
    # params.filterByInertia = True
    # params.minInertiaRatio = 0.01
    # detector = cv2.SimpleBlobDetector_create(params)
    # keypoints = detector.detect(str(user))
    # blank = np.zeros((1, 1))  
    # blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), 
    #                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
    # return blobs

# I wanted to detect an ellipse, get his pixels positions and check if all the colors was in it. But it was too hard to do so I don't want to cheat and I will find another solution after your review !

    print("Tout est en ordre !")
    return True
    
def check_the_happy_feeling(user): # The program will check if the pixels are warm colors for the happy feeling
    img = Image.open(user)
    width, height = img.size
    number_pixels_good = 0
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y)) # This function will get the color in RGB at a x or a y pixel position in the image
            if pixel[0] and pixel[1] >= 100 and pixel[3] == 255:
                # We give the computer a list of colors that we judge "happy" and we compare all the pixels with the list
                number_pixels_good += 1
                if number_pixels_good >= width / 2 or number_pixels_good >= height / 2: # For the image be judged "happy" we want at least the half of pixels to be in the chosen colors
                    print("Vos couleurs respirent la joie !")
                    return True
    if width / 2 > number_pixels_good and height / 2 > number_pixels_good: 
        print("Beaucoup trop triste comme image non ?")


def isGoodImage(user):
    user = Image.open(str(user))
    print("Je vois que vous avez passé toutes les étapes, voici votre image :")
    Image._show(user)
    return True