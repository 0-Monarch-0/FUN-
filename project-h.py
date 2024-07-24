#open cv library is for video capturing and processing 
#mediapipe is for hand tracking and landmark detection 
import cv2 
import mediapipe as mp 

#intitalizing mediapipe hands 
mp_hands  = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

#mp_hands  = access the hand solutions in the mediapipe 
#hands: intitalize the hand module for hand detection 
#mp_draw:utility to draw hand landmark on the frames 

#intializing the video capture 
cap = cv2.VideoCapture(0)
#captures the video from the default camera. in our case its webcam 


#capturing and processing each frame 
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame,1)
    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            #extracting hand landmarks 
            landmark_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                #get the coordinates 
                h , w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([cx,cy])
            
            #code block for gesture recognition 
            if len(landmark_list)!= 0:
                # open hand gesture 
                if landmark_list[4][1] < landmark_list[3][1] and landmark_list[8][1] < landmark_list[6][1]:
                    gesture = "hello there"
                #pointing up gesture 
                elif landmark_list[4][1] < landmark_list[3][1] and landmark_list[8][1] < landmark_list[6][1]:
                    gesture = "lessss goooooo"
                else:
                    gesture = None
                
                #displaying the correspoing text 
                if gesture:
                    cv2.putText(frame, gesture, (landmark_list[0][0] - 50, landmark_list[0][1] - 50),cv2.FONT_HERSHEY_COMPLEX, 2, (0,250,0), 3, cv2.LINE_AA)
                    #increased font scale and thickness 
                    #                 
    cv2.imshow('Hand Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() #release the webcam
cv2.destroyAllWindows() #closes all open cv windows 
#explantion 
"""
ret, frame : reads a frame from the video capture 
cv2.flip(frame, 1):flips the frame horizontally for a mirror view
cv2.cvtColor() converts the frame from BGR to RGB 
hands.process() processes the frame to detect hand landmarks
mp.draw.draw_landmarks() draw the detected hand landmarks on the frame
"""
#display the frame 

     


