# import cv2
# import pickle
# import cvzone
# import numpy as np

# # Video feed
# cap = cv2.VideoCapture('carPark.mp4')

# with open('CarParkPos', 'rb') as f:
#     posList = pickle.load(f)

# width, height = 107, 48
# entry_point = (50, 50)  # Define the entry point for your parking lot


# def draw_directions(img, pos, label):
#     """Draw directions from the entry point to the parking spot."""
#     x, y = pos
#     parking_center = (x + width // 2, y + height // 2)

#     # Draw an arrow from entry point to the parking spot
#     cv2.arrowedLine(img, entry_point, parking_center, (255, 0, 0), 2, tipLength=0.05)
#     cv2.putText(img, f'Spot {label}', (x + 10, y - 10),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)


# def checkParkingSpace(imgProcess):
#     spaceCounter = 0

#     for i, pos in enumerate(posList):
#         x, y = pos

#         # Crop the image to check for cars in the parking spot
#         imgCrop = imgProcess[y:y+height, x:x+width]
#         count = cv2.countNonZero(imgCrop)

#         label = chr(65 + i)  # Assign labels A, B, C, ... to spots

#         # Determine if the spot is free
#         if count < 900:
#             color = (0, 255, 0)
#             thickness = 5
#             spaceCounter += 1
#             draw_directions(img, pos, label)  # Add direction for free spots
#         else:
#             color = (0, 0, 255)
#             thickness = 2

#         cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, thickness)
#         cvzone.putTextRect(img, str(count), (x, y+height-10),
#                            scale=1.5, thickness=2, offset=0)

#     cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50),
#                        scale=3, thickness=5, offset=20, colorR=(0, 200, 0))


# while True:
#     if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
#         cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#     success, img = cap.read()

#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
#     imgThreshold = cv2.adaptiveThreshold(
#         imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
#     imgMedian = cv2.medianBlur(imgThreshold, 5)
#     kernel = np.ones((3, 3), np.uint8)
#     imgDil = cv2.dilate(imgMedian, kernel, iterations=1)

#     checkParkingSpace(imgDil)

#     cv2.imshow('Image', img)
#     cv2.waitKey(10)


import cv2
import pickle
import cvzone
import numpy as np

# Video feed
cap = cv2.VideoCapture('carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48
entry_point = (50, 50)  # Define the entry point for your parking lot

# Define a list of unique colors for each parking spot
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
    (255, 0, 255), (255, 165, 0), (0, 128, 0), (128, 0, 128), (255, 105, 180)
]

def draw_directions(img, pos, label, is_free):
    """Draw directions from the entry point to the parking spot with different colors."""
    if not is_free:
        return  # Do not draw direction for occupied spots

    x, y = pos
    parking_center = (x + width // 2, y + height // 2)

    # Direction color changes based on whether the spot is free
    direction_color = (0, 255, 0)  # Green arrow for free spots

    # Draw an arrow from entry point to the parking spot
    cv2.arrowedLine(img, entry_point, parking_center, direction_color, 2, tipLength=0.05)
    
    # Display the spot label with black color and bold text
    cv2.putText(img, f'Spot {label}', (x + 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3, cv2.LINE_AA)


def checkParkingSpace(imgProcess):
    spaceCounter = 0

    for i, pos in enumerate(posList):
        x, y = pos

        # Crop the image to check for cars in the parking spot
        imgCrop = imgProcess[y:y+height, x:x+width]
        count = cv2.countNonZero(imgCrop)

        label = chr(65 + i)  # Assign labels A, B, C, ... to spots

        # Determine if the spot is free
        is_free = count < 900

        # Set color based on whether the spot is free or occupied
        color = (0, 255, 0) if is_free else (0, 0, 255)
        thickness = 5 if is_free else 2

        # Draw the parking spot
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, thickness)

        # Add the count of pixels detected in the parking spot
        cvzone.putTextRect(img, str(count), (x, y + height - 10),
                           scale=1.5, thickness=2, offset=0)

        # Draw directions for free spots only
        draw_directions(img, pos, label, is_free)

    # Display total number of free spaces
    spaceCounter = sum([1 for i in posList if cv2.countNonZero(imgProcess[i[1]:i[1]+height, i[0]:i[0]+width]) < 900])
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50),
                       scale=3, thickness=5, offset=20, colorR=(0, 200, 0))


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDil = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDil)

    cv2.imshow('Image', img)
    cv2.waitKey(10)
