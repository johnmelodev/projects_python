# Importing the necessary libraries
import cv2
import pytesseract

# Asking the user to enter the image path
input_path = input("Please, enter the image path: ")

# Loading the image
image = cv2.imread(input_path)

# Checking if the image was loaded correctly
if image is None:
    print(f"Could not open the image {input_path}")
else:
    # Using Tesseract to extract the text from the image
    text = pytesseract.image_to_string(image, lang='eng')

    # Printing the extracted text
    print(text)

''' pip3 install

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/joaohenriquemelodesouza/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

brew install tesseract

brew install tesseract-lang

pip3 install opencv-python

pip3 install pytesseract
'''
