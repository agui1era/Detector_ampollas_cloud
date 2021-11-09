
import cv2  


def main():

  img_input='input.jpg'


  cap = cv2.VideoCapture(1) # video capture source camera (Here webcam of laptop) 

  while cv2.waitKey(1) & 0xFF != ord('q'):
    # Open the url image, set stream to True, this will return the stream content.

    ret,frame = cap.read() # return a single frame in variable `frame`
    cv2.imwrite(img_input,frame)   
   
    image = cv2.imread(img_input) 
    
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window",image)
    
      #closing all open windows  
  cv2.destroyAllWindows()   
  cap.release()   

if __name__ == '__main__':
  main()
  
