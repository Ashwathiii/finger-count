import mediapipe as mp
import cv2
medhands=mp.solutions.hands     #hands module is used here....hands nte or module aan Hands...Hands nta objet nta name aan hand
draw=mp.solutions.drawing_utils
hand=medhands.Hands(max_num_hands=1)  #otta hand na matro read akan

video =cv2.VideoCapture(0)
while True:
    success,img=video.read()
    img=cv2.flip(img,1)
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hand.process(imgrgb)
    #thirch convert aaknda coz imgrgb variablila ullee..img ippazm same aan bgr la ulle
    tipids=[4,8,12,16,20]   #oro fingersnta tipid aan ith
    lmlist=[]       #landmarklist
    cv2.rectangle(img,(20,350),(90,440),(123,46,67),cv2.FILLED)    
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):#ethaan landmark aan aryan  lm==x,y,z values
                # print(id,lm)
                cx=lm.x
                cy=lm.y   #x,y martree vndu
                lmlist.append([id,cx,cy])
                # print(lmlist)   #id,x,y values print akum
                #identify finger is open or closed
                if len(lmlist)!=0 and len(lmlist)==21:  # lmlist!=0 aanenke chyn pattu..ie. empty akn padilla
                    fingerlist=[]    #ethoke fing open aan ,close aan nokn or list...0-closed,,1-open


                    #thumb
                    if lmlist[20][1]>lmlist[12][1]:     #left hand ano identify
                        if lmlist[4][1]>lmlist[3][1]:    #left hand finger closed ano nokn
                            fingerlist.append(0)
                        else:
                            fingerlist.append(1)
                    else:
                        if lmlist[4][1]<lmlist[3][1]:   #right hand finger closed ano nokan
                            fingerlist.append(0)
                        else:
                            fingerlist.append(1)




                    for i in range(1,5):   #thumbna consider aknda..vera code ind#for i in range(0,5):   #calculate the count  (5 verlindallo)
                        if lmlist[tipids[i]][2]>lmlist[tipids[i]-2][2]:  #tipid de thayata value compare akyal mnslaku open or closed... lmlistle i th elementle corresponding y value aan kitua  ex..[[0,x,y],[1,x,y]..[20,x,y]]
                            fingerlist.append(0)
                        else:
                            fingerlist.append(1)
                    #print(fingerlist)
                    if len(fingerlist)!=0:
                        fingercount=fingerlist.count(1)
                        #print(fingercount)
                    cv2.putText(img,str(fingercount),(35,436),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,0),4)

                draw.draw_landmarks(img,handlms,medhands.HAND_CONNECTIONS,draw.DrawingSpec(color=(255,0,0),thickness=2,circle_radius=4),draw.DrawingSpec(color=(255,255,0),thickness=2))  #drawing spec naml color radis okke specify aaka..athyatha drwaing spec


    cv2.imshow('HAND',img)
    if cv2.waitKey(1)&0XFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
