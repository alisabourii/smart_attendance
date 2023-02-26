import time
import pygame
import pygame.camera
  
# initializing  the camera
pygame.camera.init()
  
# make the list of all available cameras
camlist = pygame.camera.list_cameras()

def take_foto():
    # if camera is detected or not
    for i in range(1,3):
        if camlist:
        
            # initializing the cam variable with default camera
            cam = pygame.camera.Camera(camlist[1], (640, 480))
        
            # opening the camera
            cam.start()
            time.sleep(2.0)
            # capturing the single image
            image = cam.get_image()
        
            # saving the image
            pygame.image.save(image, "filename{0}.jpg".format(i))
        
        # if camera is not detected the moving to else part
        else:
            print("No camera on current device")
