import pytesseract 
from pytesseract import Output
import PIL.Image
import cv2
import pyttsx3

"""
Page segmentation modes: 

0 Orientation and script detection (OSD) only.

1 Automatic page segmentation with OSD. 

2 Automatic page segmentation, but no OSD, or OCR.

3 Fully automatic page segmentation, but no OSD. (Default)

4 Assume a Single column of text of variable sizes.

5 Assume a single uniform block of vertically aligned text.

6 Assume a Single uniform block of text.

7 Treat the image as a single text Line.

8 Treat the image as a single word.

9 Treat the image as a single word in a circle.

10 Treat the image as a single character.

11 Sparse text. Find as much text as possible in no particular order.

12 Sparse text with OSD.

13 Raw Line. Treat the image as a single text Line,

bypassing hacks that are Tesseract-specific.

"""

myconfig = r"--psm 11 --oem 3"

#-------------------------------------------------------------------
# text = pytesseract.image_to_string(PIL.Image.open("test4.png"),config = myconfig)         # Image to text direct
# print(text)
#-------------------------------------------------------------------

img = cv2.imread("test3.jpg")
height, width, _  = img.shape

#-------------------------------------------------------------------
# boxes = pytesseract.image_to_boxes(img, config=myconfig)      # To box every charecter
# print(boxes)

# for box in boxes.splitlines():
#     box=box.split(" ")
#     img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0,255,0),2)
#--------------------------------------------------------------------


data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

# print(data['text'])
extracted_text = ""
amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i])>80:
        (x,y,width,height)=(data['left'][i],data['top'][i],data['width'][i],data['height'][i])
        img=cv2.rectangle(img,(x,y),(x+width, y+height),(0,255,0))
        img=cv2.putText(img, data['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)

        extracted_text += data['text'][i] + "\n"

with open("extracted_text.txt", "w") as file:
    file.write(extracted_text)



def read_text_file_aloud(file_path):
    try:
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        
        # Open the text file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Speak the content
        engine.say(content)
        engine.runAndWait()
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your text file
file_path = "extracted_text.txt"  # Replace with your file path

read_text_file_aloud(file_path)

cv2.imshow("img",img)
cv2.waitKey(0)