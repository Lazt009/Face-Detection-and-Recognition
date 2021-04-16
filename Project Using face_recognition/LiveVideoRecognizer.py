import face_recognition
import argparse
import pickle
import cv2

#loading our encodings 
#it will be a dictionary containing knownEncodings and knownNames
data = pickle.loads(open("encodings.pickle", "rb").read())


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    #Real logic here ************************************************************************************
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB )
    #get all aface loacations
    boxes = face_recognition.face_locations(rgb_image)
    #encoded data of unknown face(s) in the video
    encodings = face_recognition.face_encodings(rgb_image, boxes)

    # initialize the list of names for each face detected
    names = []

    #for all the encoded faces in video
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "unknown"     #set name is unknown for a while
        
    if True in matches:
        matchedIdxs = [i for (i, b) in enumerate(matches) if b ]
        counts = {}

        for i in matchedIdxs:
            name = data["names"][i]
            counts[name] = counts.get(name, 0) + 1

        # determine the recognized face with the largest number of
		# votes (note: in the event of an unlikely tie Python will
		# select first entry in the dictionary)
        name = max(counts, key=counts.get)

    # update the list of names
    names.append(name)

    for ((top, right, bottom, left), name) in zip(boxes, names):
	# draw the predicted face name on the image
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
    #Ends here*******************************************************************************************


    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()