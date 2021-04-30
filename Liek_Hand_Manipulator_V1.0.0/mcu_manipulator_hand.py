import cv2
import mediapipe as mp
import serial
import time
arduino = serial.Serial(
port = "COM4",
baudrate = 9600,
bytesize = serial.EIGHTBITS,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
timeout = 1,
xonxoff = False,
rtscts = False,
dsrdtr = False,
writeTimeout = 2
)
arduino.close()
arduino.open()
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
cap.set(3, 960)
cap.set(4, 480)
tempx = 0.1947479248047
tempy = 0.00149059295654
deltax = 10
deltay = 10
statusFlag = 1
while True:

    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)

            #print(tempx - float(f'{hand_landmarks.landmark[mpHands.HandLandmark.WRIST].x * 960}'))
            #print(tempy - float(f'{hand_landmarks.landmark[mpHands.HandLandmark.WRIST].y * 480}'))


            if (tempx - float(f'{hand_landmarks.landmark[mpHands.HandLandmark.WRIST].x * 960}') > deltax):
                print("0")
                if statusFlag == 1:
                    arduino.write(bytes('0', "utf-8"))
                    statusFlag = 0
            elif (tempx - float(f'{hand_landmarks.landmark[mpHands.HandLandmark.WRIST].x * 960}') < -deltax):
                print("1")
                if statusFlag == 0:
                    arduino.write(bytes('1', "utf-8"))
                    statusFlag = 1

          #  if (tempy - float(f'{hand_landmarks.landmark[mpHands.HandLandmark.WRIST].y * 480}') > deltay):
               # print("Up")
          #  elif (tempy - float(f'{hand_landmarks.landmark[mpHands.HandLandmark.WRIST].y * 480}') < -deltay):
               # print("Down")


            tempx = float(f'{hand_landmarks.landmark[mpHands.HandLandmark.WRIST].x * 960}')
            tempy = float(f'{hand_landmarks.landmark[mpHands.HandLandmark.WRIST].y * 480}')



    cv2.imshow("Image" ,cv2.flip( img , 1))
    cv2.waitKey(1)