import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img = cv2.imread('img3.png')
img = cv2.resize(img, (500,500))

Himg , Wimg, _ = img.shape
# to detect every letter
# boxes = pytesseract.image_to_boxes(img , lang = 'eng')

# print(boxes)

# for b in boxes.splitlines() :
#     print(b)
#     b = b.split(" ")
#     print (b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4]) 
#     cv2.rectangle(img , (x,Himg-y), (w , Himg-h), (0,255,0), 3)
#     cv2.putText(img,b[0],(x ,Himg-y+25), cv2.FONT_HERSHEY_COMPLEX,1, (0,0,255), 3 )
    
 ##################################################################################################   
# # to detect every word    
# boxes = pytesseract.image_to_data(img , lang = 'eng')    
# print(boxes)   

# for x, b in enumerate(boxes.splitlines()) :    
#     if x != 0 :
#         b = b.split( )
#         print (b)
#         if len(b) == 12 :
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img , (x,y), (x+w ,y+h), (0,255,0), 3)
#             cv2.putText(img,b[11],(x,y), cv2.FONT_HERSHEY_COMPLEX,1, (0,0,255), 3 )
            
            

##############################################################################################
# to detect numbers 
# config = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img , lang = 'eng', config = config)    
# print(boxes)   

# for x, b in enumerate(boxes.splitlines()) :    
#     if x != 0 :
#         b = b.split( )
#         print (b)
#         if len(b) == 12 :
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img , (x,y), (x+w ,y+h), (0,255,0), 3)
#             cv2.putText(img,b[11],(x,y), cv2.FONT_HERSHEY_COMPLEX,1, (0,0,255), 3 )
           
############################################################################################
# to put every number in one rectangle
config = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img , lang = 'eng', config = config)

print(boxes)

for b in boxes.splitlines() :
    print(b)
    b = b.split(" ")
    print (b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4]) 
    cv2.rectangle(img , (x,Himg-y), (w , Himg-h), (0,255,0), 3)
    cv2.putText(img,b[0],(x ,Himg-y+25), cv2.FONT_HERSHEY_COMPLEX,1, (0,0,255), 3 )
                 
            
    
    
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    