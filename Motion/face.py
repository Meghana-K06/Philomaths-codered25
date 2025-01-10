import cv2
import mediapipe as mp

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Initialize the FaceMesh object
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# OpenCV video capture (camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for better selfie-view
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB (MediaPipe works with RGB images)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to find face landmarks
    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks:
        for landmarks in result.multi_face_landmarks:
            # Draw landmarks on the face
            mp_drawing.draw_landmarks(frame, landmarks, mp_face_mesh.FACEMESH_TESSELATION)

            # Here you can process specific landmarks and gestures (e.g., nodding, eye movement)
            # Example: if the face nods, trigger a click event or scroll action.

    # Display the frame with landmarks
    cv2.imshow("Face Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()