import sys
import cv2
import numpy as np
from pprint import pprint as pp


def main(argv):
    filename = argv[0] if argv else 'sample1.png'

    # Create window
    window_name = 'MicroCV'
    cv2.namedWindow(window_name)

    default_min_centre_distance = 10
    default_edge_threshold = 100
    default_centre_threshold = 25
    default_min_radius = 5
    default_max_radius = 40

    cv2.createTrackbar("min_centre_distance", window_name, default_min_centre_distance, 50, lambda x: x)
    cv2.createTrackbar("edge_threshold", window_name, default_edge_threshold, 150, lambda x: x)
    cv2.createTrackbar("centre_threshold", window_name, default_centre_threshold, 150, lambda x: x)
    cv2.createTrackbar("min_radius", window_name, default_min_radius, 40, lambda x: x)
    cv2.createTrackbar("max_radius", window_name, default_max_radius, 100, lambda x: x)

    while True:
        min_centre_distance = cv2.getTrackbarPos("min_centre_distance", window_name)
        edge_threshold = cv2.getTrackbarPos("edge_threshold", window_name)
        centre_threshold = cv2.getTrackbarPos("centre_threshold", window_name)
        min_radius = cv2.getTrackbarPos("min_radius", window_name)
        max_radius = cv2.getTrackbarPos("max_radius", window_name)

        src = generate_image(filename, min_centre_distance, edge_threshold, centre_threshold, min_radius, max_radius)

        cv2.imshow(window_name, src)
        key = cv2.waitKey(1) & 0xFF

        # press 'q' to quit the window
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    return 0


def generate_image(filename, min_centre_distance, edge_threshold, centre_threshold, min_radius, max_radius):
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, min_centre_distance,
                              param1=edge_threshold, param2=centre_threshold,
                              minRadius=min_radius, maxRadius=max_radius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])  # circle center
            cv2.circle(src, center, 1, (0, 100, 100), 3)
            radius = i[2]  # circle outline
            cv2.circle(src, center, radius, (255, 0, 255), 3)

    cv2.putText(src, "{} circles".format(circles.shape[1]), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255) )

    return src


if __name__ == "__main__":
    main(sys.argv[1:])