import cv2
import sys

def main():
    # Initialize the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        sys.exit()
    
    # Load the face cascade classifier
    # This uses Haar cascades for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Check if the cascade loaded successfully
    if face_cascade.empty():
        print("Error: Could not load face cascade classifier")
        cap.release()
        sys.exit()
    
    print("Face detection started. Press 'q' to quit.")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If frame reading was not successful, break the loop
        if not ret:
            print("Error: Can't receive frame. Exiting...")
            break
        
        # Convert frame to grayscale (face detection works better on grayscale)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,      # How much the image size is reduced at each scale
            minNeighbors=5,       # How many neighbors each rectangle should retain
            minSize=(30, 30),     # Minimum possible face size
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            # Draw a green rectangle around each face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Optional: Add a label
            cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.9, (0, 255, 0), 2)
        
        # Display the number of faces detected
        face_count = len(faces)
        cv2.putText(frame, f'Faces detected: {face_count}', (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Display the resulting frame
        cv2.imshow('Face Detection', frame)
        
        # Break the loop when 'q' key is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        # Alternative: press ESC to quit
        elif key == 27:  # ESC key
            break
    
    # Release everything when done
    cap.release()
    cv2.destroyAllWindows()
    print("Camera released and windows closed.")

if __name__ == "__main__":
    main()