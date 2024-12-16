import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cam = cv2.VideoCapture(0)
mycoordinatedata = {}

while True:
    _,image = cam.read()
    image=cv2.flip(image,1)
    results=hands.process(image)
    height,width,_=image.shape   
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks: #for hands
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
        for id,lms in enumerate(hand_landmarks.landmark):
            x_cord=lms.x*width
            y_cord=lms.y*height
            mycoordinatedata[id] = (x_cord,y_cord)
            try:
                if(
                    mycoordinatedata[8][1] < mycoordinatedata[6][1] and  # Index finger extended
                    mycoordinatedata[12][1] < mycoordinatedata[10][1] and  # Middle finger extended
                    mycoordinatedata[16][1] > mycoordinatedata[14][1] and  # Ring finger curled
                    mycoordinatedata[20][1] > mycoordinatedata[18][1]  # Pinky finger curled
                ):
                    print("Scissor")
                elif (
                    mycoordinatedata[8][1] > mycoordinatedata[6][1] and  # Index finger curled
                    mycoordinatedata[12][1] > mycoordinatedata[10][1] and  # Middle finger curled
                    mycoordinatedata[16][1] > mycoordinatedata[14][1] and  # Ring finger curled
                    mycoordinatedata[20][1] > mycoordinatedata[18][1]  # Pinky finger curled
                ):
                    print("Rock")
                elif (
                    mycoordinatedata[8][1] < mycoordinatedata[6][1] and  # Index finger extended
                    mycoordinatedata[12][1] < mycoordinatedata[10][1] and  # Middle finger extended
                    mycoordinatedata[16][1] < mycoordinatedata[14][1] and  # Ring finger extended
                    mycoordinatedata[20][1] < mycoordinatedata[18][1]  # Pinky finger extended
                ):
                    print("Paper")
                else:
                    print("Unknown sign")     
            except KeyError:
                pass



    cv2.imshow("Project",image)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()