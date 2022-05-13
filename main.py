import cv2

CIRCLE_RADIUS = 50
CIRCLE_DISTANCE = 130
CIRCLE_TOUCH_COLOR = (0, 0, 255)
FINGERTIP_RADIUS = 0
ANIMATION_LENGTH = 120

current_menu = 'EYES'
menus = {'EYES': {'menu_count': 4}}


def DrawMenu(fingerpos, img, frame):
    init_pos_y = 75
    image = img.copy()

    if current_menu == 'EYES':
        if(frame < 30):
            for i in range(3):
                image = cv2.circle(
                    image, [1150, init_pos_y+i*CIRCLE_DISTANCE-90*i+frame*3*i], CIRCLE_RADIUS, (255, 255, 255), -1)
            return image
        else:
            for i in range(3):
                if FingerTouch([1150, init_pos_y+i*CIRCLE_DISTANCE], fingerpos):
                    image = cv2.circle(
                        image, [1150, init_pos_y+i*CIRCLE_DISTANCE], CIRCLE_RADIUS, (255, 255, 255), -1)
                else:
                    image = cv2.circle(
                        image, [1150, init_pos_y+i*CIRCLE_DISTANCE], CIRCLE_RADIUS, CIRCLE_TOUCH_COLOR, -1)
            return image

    else:
        return image


def FingerTouch(circleMid, fingerpos):
    if CIRCLE_RADIUS+FINGERTIP_RADIUS < ((circleMid[0] - fingerpos[0])**2 + (circleMid[1] - fingerpos[1])**2)**0.5:
        return True
    else:
        return False


cap = cv2.VideoCapture(1)
fy = 0
while True:
    # Getting out image by webcam
    _, image = cap.read()
    # Converting the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Get faces into webcam's image
    # For each detected face, find the landmark.

    # Show the image
    image = cv2.flip(image, 1)
    image = DrawMenu([1150, fy], image, fy)
    if(fy < 30):
        fy += 2
    cv2.imshow("Output", image)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    # Q
    if k == 113:
        fy = 0
        #current_menu = 'NOSE'


cv2.destroyAllWindows()
cap.release()