# Noor Ul Huda
# DecodeLabs Internship Project 4
# AI-Based Text Recognition System using OCR

# importing libraries
import cv2
import pytesseract


print("====================================")
print(" DecodeLabs - AI Project 4")
print(" AI Text Recognition System")
print(" Submitted by: Noor Ul Huda")
print("====================================\n")

# setting tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# loading image
image_path = "sample_text_image.png"

image = cv2.imread(image_path)

if image is None:
    print("Image not found")
    exit()

print("Image loaded successfully")

# converting image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Grayscale conversion completed")

# removing noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

print("Noise removal completed")

# thresholding image
threshold = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)[1]

print("Thresholding completed")

# extracting text from image
text = pytesseract.image_to_string(threshold)

print("\n====================================")
print(" Recognized Text")
print("====================================\n")

print(text)

# saving extracted text
with open("recognized_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nText saved successfully")

# showing images
cv2.imshow("Original Image", image)

cv2.imshow("Processed Image", threshold)

cv2.waitKey(0)

cv2.destroyAllWindows()


print("\nProject completed successfully")