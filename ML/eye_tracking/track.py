import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# # First detect face
# img = cv2.imread("face.jpeg")

# gray_picture = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray_picture, 1.3, 5)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

# # Show
# # cv2.imshow("detected", img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# gray_face = gray_picture[y : y + h, x : x + w]
# face = img[y : y + h, x : x + w]
# eyes = eye_cascade.detectMultiScale(gray_face)

# for (ex, ey, ew, eh) in eyes:
#     cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

# # Show
# cv2.imshow("detected", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# def detect_eyes_1(img, img_gray, classifier):
#     """Eyes are always in the upper half"""
#     coords = cascade.detectMultiScale(img_gray, 1.3, 5)  # detect eyes
#     height = np.size(image, 0)  # get face frame height
#     for (x, y, w, h) in coords:
#         if y + h > height / 2:  # pass if the eye is at the bottom
#             pass


def detect_eyes(img, classifier):
    """Left eye and right eye"""
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5)  # detect eyes
    width = np.size(image, 1)  # get face frame width
    height = np.size(image, 0)  # get face frame height
    left_eye = None
    right_eye = None
    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2  # get the eye center
        if eyecenter < width * 0.5:
            left_eye = img[y : y + h, x : x + w]
        else:
            right_eye = img[y : y + h, x : x + w]
    return left_eye, right_eye


def detect_faces(img, classifier):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords = cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None
    for (x, y, w, h) in biggest:
        frame = img[y : y + h, x : x + w]
    return frame


detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv2.SimpleBlobDetector_create(detector_params)

# _, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)


def cut_eyebrows(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]  # cut eyebrows out (15 px)
    return img


def blob_process(img, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(gray_frame, 42, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, None, iterations=2)  # 1
    img = cv2.dilate(img, None, iterations=4)  # 2
    img = cv2.medianBlur(img, 5)  # 3
    keypoints = detector.detect(img)
    return keypoints


def main():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        face_frame = detect_faces(frame, face_cascade)
        if face_frame is not None:
            eyes = detect_eyes(face_frame, eye_cascade)
            for eye in eyes:
                if eye is not None:
                    eye = cut_eyebrows(eye)
                    keypoints = blob_process(eye, detector)
                    eye = cv2.drawKeypoints(
                        eye,
                        keypoints,
                        eye,
                        (0, 0, 255),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                    )
        cv2.imshow("my image", face_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


main()