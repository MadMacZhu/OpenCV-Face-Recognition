import cv2
import face_recognition
import numpy as np
import os

path = 'Data'
print(os.listdir(path))

images = []
class_names = []
my_list = os.listdir(path)[1:]

for cls in my_list:
    cur_img = cv2.imread(os.path.join(path, cls))
    images.append(cur_img)
    class_names.append(cls.split('.')[0])
    
print(class_names)

def FindEncodings(images):
    encode_list = []
    for img in images:
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

encode_list = FindEncodings(images)
print("Encoding Complete!")
print(len(encode_list))

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    success, frame = cap.read()
    frame_sm = cv2.resize(frame, (0,0), None, 0.25, 0.25)
    frame_sm = cv2.cvtColor(frame_sm, cv2.COLOR_BGR2RGB)
    
    faces_locs = face_recognition.face_locations(frame_sm)
    encodings = face_recognition.face_encodings(frame_sm, faces_locs)
    
    for encoding, face in zip(encodings, faces_locs):
        matches = face_recognition.compare_faces(encode_list,
        										 encoding,
        										 tolerance = 0.5)
        distance = face_recognition.face_distance(encode_list, encoding)
        match_index = np.argmin(distance)
        
        if matches[match_index]:
            name = class_names[match_index].upper()
            y1, x2, y2, x1 = face
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1), (x2, y2),
                          (0,255,0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2),
            	          (0,255,0), cv2.FILLED)
            cv2.putText(frame, name, (x1+6, y2-6),
            			cv2.FONT_HERSHEY_COMPLEX,
            			1, (255,255,255), 2)
            
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == ord('q'):
    	break

cap.release()
cv2.destroyAllWindows()

def MarkTimeofAppearance(name):
	with open('timestamps.csv') as file:
		data = file.readlines()
		names = []
		for line in data:
			entry = line.split(',')
			names.append(entry[0])
		if name not in names:
			now = datetime.now()
			time = now.strftime('%H:%M:%S')
			f.writelines(f'\n{name},{time}')