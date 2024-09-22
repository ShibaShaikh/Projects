import cv2 
import mediapipe as mp  

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

vc = cv2.VideoCapture(0) 

with mp_hands.Hands(min_detection_confidence= 0.7, min_tracking_confidence= 0.7) as hands: 
    while vc.isOpened():  
        ret, frame = vc.read() 
        frame = cv2.flip(frame, 1)  
        new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        results = hands.process(new_frame)
        
        if results.multi_hand_landmarks:  
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
        cv2.imshow("Hand Tracking", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
        
cap.release()
cv2.destroyAllWindows()
