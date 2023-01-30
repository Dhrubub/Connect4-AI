import cv2
import numpy as np
import time


# Create a video capture object
cap = cv2.VideoCapture(0)

# Check if the camera is opened
if not cap.isOpened():
    print("Unable to open camera")
    exit()

# Continuously capture frames until the user presses 'q'

capture = None


# def imgshow(name,img):
#     cv2.imshow(name,img)
#     cv2.moveWindow(name,200,200)
#     cv2.waitKey(0)





def get_circles(img):
    new_width = 500 # Resize
    img_h,img_w,_ = img.shape
    scale = new_width / img_w
    img_w = int(img_w * scale)
    img_h = int(img_h * scale)
    img = cv2.resize(img, (img_w,img_h), interpolation = cv2.INTER_AREA)
    img_orig = img.copy()
    # imgshow('Original Image (Resized)', img_orig)

    # Bilateral Filter
    bilateral_filtered_image = cv2.bilateralFilter(img, 15, 190, 190) 
    # imgshow('Bilateral Filter', bilateral_filtered_image)

    # Outline Edges
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 150) 
    # imgshow('Edge Detection', edge_detected_image)

    # Find Circles
    contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Edges to contours

    contour_list = []
    rect_list = []
    position_list = []


    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True) # Contour Polygons
        area = cv2.contourArea(contour)

        rect = cv2.boundingRect(contour) # Polygon bounding rectangles
        x_rect,y_rect,w_rect,h_rect = rect
        x_rect +=  w_rect/2
        y_rect += h_rect/2
        area_rect = w_rect*h_rect

        if ((len(approx) > 8) & (len(approx) < 23) & (area > 250) & (area_rect < (img_w*img_h)/5)) & (w_rect in range(h_rect-10,h_rect+10)): # Circle conditions
            contour_list.append(contour)
            position_list.append((x_rect,y_rect))
            rect_list.append(rect)

    img_circle_contours = img_orig.copy()
    cv2.drawContours(img_circle_contours, contour_list,  -1, (0,255,0), thickness=1) # Display Circles
    for rect in rect_list:
        x,y,w,h = rect
        cv2.rectangle(img_circle_contours,(x,y),(x+w,y+h),(0,0,255),1)


    if not (len(position_list) and len(rect_list) and len(contour_list)):
        return img


    # imgshow('Circles Detected',img_circle_contours)

    # Interpolate Grid
    rows, cols = (6,7)
    mean_w = sum([rect[2] for r in rect_list]) / len(rect_list)
    mean_h = sum([rect[3] for r in rect_list]) / len(rect_list)
    position_list.sort(key = lambda x:x[0])
    max_x = int(position_list[-1][0])
    min_x = int(position_list[0][0])
    position_list.sort(key = lambda x:x[1])
    max_y = int(position_list[-1][1])
    min_y = int(position_list[0][1])
    grid_width = max_x - min_x
    grid_height = max_y - min_y
    col_spacing = int(grid_width / (cols-1))
    row_spacing = int(grid_height / (rows - 1))

    # Identify Colours
    grid = np.zeros((rows,cols))
    img_grid_overlay = img_orig.copy()
    img_grid = np.zeros([img_h,img_w,3], dtype=np.uint8)

    for x_i in range(0,cols):
        x = int(min_x + x_i * col_spacing)
        for y_i in range(0,rows):
            y = int(min_y + y_i * row_spacing)
            r = int((mean_h + mean_w)/5)
            img_grid_circle = np.zeros((img_h, img_w))
            cv2.circle(img_grid_circle, (x,y), r, (255,255,255),thickness=-1)
            img_grid_circle = np.zeros((img_h, img_w))
            cv2.circle(img_grid_circle, (x,y), r, (255,255,255),thickness=-1)
            cv2.circle(img_grid_overlay, (x,y), r, (0,255,0),thickness=1)


    # print('Grid Detected:\n', grid)
    # imgshow('Img Grid Overlay',img_grid_overlay)



    img_output = img_grid_overlay.copy()
    x = int(min_x + 2 * col_spacing)
    y = int(min_y) + (3) * row_spacing
    cv2.circle(img_output, (x,y), r+4, (0,0,255),thickness=-1)
        # cv2.circle(img_output, (x,y), r+4, (0,255,255),thickness=-1)
    cv2.circle(img_output, (x,y), r+5, (0,255,0),thickness=2)


    return img_output

frame_rate = 30

# Calculate the desired delay between frames in milliseconds
delay = int(1000 / frame_rate)

while True:
    # Start timer
    start_time = cv2.getTickCount()

    # Capture a frame
    ret, frame = cap.read()

    # Show the processed frame
    f = get_circles(frame)
    cv2.imshow("frame", f)

    # End timer
    end_time = cv2.getTickCount()


    # Calculate elapsed time in milliseconds
    elapsed_time = int((end_time - start_time) / cv2.getTickFrequency() * 1000)

    # Delay to match desired frame rate
    time.sleep(max((delay - elapsed_time), 0) / 1000.0)

    # Check if the user pressed 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Save the processed image
        # capture = frame
        # cv2.imwrite("screen_capture.jpg", frame)
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()



# # Read the saved image
# img = capture

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# # Define the range for blue color
# lower_blue = np.array([110,50,50])
# upper_blue = np.array([130,255,255])

# mask = cv2.inRange(hsv, lower_blue, upper_blue)
# # Threshold the image to create a binary image


# # Fill any holes in the binary image
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))



# # Enter code here

# # Use HoughCircles to detect circles in the binary image
# circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# # Check if any circles were detected
# if circles is not None:
#     # Convert the (x, y) coordinates and radius of the circles to integers
#     circles = np.round(circles[0, :]).astype("int")

#     # Create a list to store the circle sizes
#     circle_sizes = []
#     for (x, y, r) in circles:
#         circle_sizes.append(r)

#     # Find the most frequently occurring circle size
#     most_frequent_size = max(set(circle_sizes), key=circle_sizes.count)

#     # Loop over the (x, y) coordinates and radius of the circles
#     for (x, y, r) in circles:
#         # Only show the circles with the most frequently occurring size
#         if r == most_frequent_size:
#             # Draw the circle in the output image
#             cv2.circle(mask, (x, y), r, (0, 255, 0), 4)




# # Show the output image
# cv2.imshow("Circles", mask)

# # Wait for the user to press a key
# cv2.waitKey(0)

# # Destroy all windows
# cv2.destroyAllWindows()





