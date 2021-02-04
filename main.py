#importing the libraries
import cv2
import numpy as np
import requests
import io
import json

#importing the image
img = cv2.imread("img2.jpg")
height, width, _ = img.shape

#cutting the image
roi = img[0: height, 400: width]


#calling ocr_api
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode("img2.jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {"img2.jpg": file_bytes},
              data = {"apikey": "aa309cb84f88957",
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)

text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)

cv2.imshow("roi", roi)
cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

