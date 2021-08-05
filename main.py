import sys
import cv2
import numpy as np
from _datetime import datetime
from pprint import pprint as pp


def main(argv):
    filename = argv[0] if argv else 'sample1.png'

    # Create window
    window_name = 'MicroCV'
    cv2.namedWindow(window_name)

    default_min_dist = 10
    default_edge_threshold = 120
    default_centre_threshold = 20
    default_min_radius = 5
    default_max_radius = 40

    cv2.createTrackbar("min_dist", window_name, default_min_dist, 50, lambda x: x)
    cv2.createTrackbar("edge_threshold", window_name, default_edge_threshold, 150, lambda x: x)
    cv2.createTrackbar("centre_threshold", window_name, default_centre_threshold, 150, lambda x: x)
    cv2.createTrackbar("min_radius", window_name, default_min_radius, 40, lambda x: x)
    cv2.createTrackbar("max_radius", window_name, default_max_radius, 100, lambda x: x)

    while True:
        min_dist = cv2.getTrackbarPos("min_dist", window_name)
        edge_threshold = cv2.getTrackbarPos("edge_threshold", window_name)
        centre_threshold = cv2.getTrackbarPos("centre_threshold", window_name)
        min_radius = cv2.getTrackbarPos("min_radius", window_name)
        max_radius = cv2.getTrackbarPos("max_radius", window_name)

        src = generate_image(filename, min_dist, edge_threshold, centre_threshold, min_radius, max_radius)

        cv2.imshow(window_name, src)
        key = cv2.waitKey(1) & 0xFF

        # press 'q' to quit the window
        if key == ord('q'):
            break

        if key == ord('s'):
            cv2.imwrite("image saved {}.png".format(datetime.now()), src)

    cv2.destroyAllWindows()
    return 0


def generate_image(filename, min_dist, edge_threshold, centre_threshold, min_radius, max_radius):
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)  # TODO: make interactive
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, min_dist,
                              param1=edge_threshold, param2=centre_threshold,
                              minRadius=min_radius, maxRadius=max_radius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])  # circle center
            cv2.circle(src, center, 1, (0, 100, 100), 3)
            radius = i[2]  # circle outline
            cv2.circle(src, center, radius, (255, 0, 255), 3)

    text_loc = (100, 100)
    inverted_color = (int(255 - src[text_loc][0]), int(255 - src[text_loc][1]), int(255 - src[text_loc][2]))
    cv2.putText(src, "{} circles".format(circles.shape[1]), text_loc, cv2.FONT_HERSHEY_SIMPLEX, 1.5, inverted_color)

    return src


if __name__ == "__main__":
    main(sys.argv[1:])