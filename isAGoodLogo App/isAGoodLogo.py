from allFunctions import *

isAllDone = False # It's a boolean (which return only True or False) and it will be check during all the program
while isAllDone != True: 
    image = ask_user_image() # We call the function that ask to user an image
    check = check_png_file(image) # We use the function that check if the image is a 'png' file

    # In all the program we will check all the conditions and when all are checked, the image will be considered good
    if check == True:
        size = image_size(image) # For check the size of the image
        if size == True:
            circle = didHaveCircle(image) # For check if there's a circle in the image
            if circle == True:
                isHappyFeeling = check_the_happy_feeling(image) # For check if the image give a 'happy' feeling
                if isHappyFeeling == True:
                    good_image = isGoodImage(image) 
                    isAllDone = True
                    # All things are checked, so we can validate and show the image