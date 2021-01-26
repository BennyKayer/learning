# python classify.py -h

# Import packages
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import os
import pickle

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True, help="path to trained model")
ap.add_argument("-t", "--testset", required=True, help="path to test images")
args = vars(ap.parse_args())

# Resize parmeters (RESIZE should be the same as used in training)
DO_RESIZE = True
RESIZE = 28
# Read labels for classes to recognize
f = open(args["model"] + ".lbl", "rb")
CLASS_LABELS = pickle.load(f)
f.close()
# Load the trained network
model = load_model(args["model"] + ".h5")
# Loop over images
for image_name in os.listdir(args["testset"]):
    # Load the image
    image = cv2.imread(args["testset"] + os.path.sep + image_name)
    orig = image.copy()
    # Preprocess the image
    if DO_RESIZE:
        image = cv2.resize(image, (RESIZE, RESIZE))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    # Classify the input image
    prediction = list(model.predict(image)[0])
    # Find the winner class and the probability
    winner_class = prediction.index(max(prediction))
    winner_prob = round(max(prediction) * 100, 2)
    # Build the label
    label = f"{CLASS_LABELS[winner_class]} : {winner_prob}"
    # Draw the label on the image
    output = imutils.resize(orig, height=600)
    cv2.putText(output, label, (10,  10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,255,0))
    # Show the output image
    cv2.imshow("output", output)
    cv2.waitKey(0)
