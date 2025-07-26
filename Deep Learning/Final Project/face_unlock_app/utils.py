import os
import cv2
from deepface import DeepFace

# Capture a single frame from the webcam and save it
def capture_face_image(filename="captured.jpg"):
    cap = cv2.VideoCapture(0)
    ret = False
    while not ret:
        ret, frame = cap.read()
    cv2.imwrite(filename, frame)
    cap.release()
    return filename

# Save the captured image under the user's name
def save_face_image(image_path, user_name, save_dir="registered_faces"):
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"{user_name}.jpg")
    os.replace(image_path, save_path)
    return save_path

# Compare captured image with registered faces using FaceNet
def authenticate_face(captured_img, save_dir="registered_faces"):
    if not os.path.exists(save_dir):
        return "No registered users", False

    for file in os.listdir(save_dir):
        ref_img = os.path.join(save_dir, file)
        try:
            result = DeepFace.verify(
                img1_path=ref_img,
                img2_path=captured_img,
                model_name="Facenet",
                enforce_detection=True
            )
            if result["verified"]:
                return file.replace(".jpg", ""), True
        except:
            continue

    return "Unknown", False