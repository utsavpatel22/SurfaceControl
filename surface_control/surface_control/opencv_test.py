import cv2
import time

img =  cv2.imread('golden.jpg')
# cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# cv2.namedWindow("test", cv2.WINDOW_NORMAL)
# cv2.setWindowProperty("test")
cv2.imshow("test",img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
# cv2.DestroyWindow("test")
img =  cv2.imread('golden_2.jpeg')
cv2.namedWindow("test2", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("test2", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("test2",img)
cv2.imshow("test2",img)
cv2.waitKey(3000)
#key=cv2.waitKey(0)


# left_arrow = "golden.jpg"
# right_arrow = "golden_2.jpeg"
# t_screen_time = 1000

# img = cv2.imread(left_arrow)
# cv2.imshow('image',img)
# cv2.waitKey(t_screen_time)
# cv2.destroyAllWindows()

# img = cv2.imread(right_arrow)
# cv2.imshow('image',img)
# cv2.waitKey(t_screen_time)
# cv2.destroyAllWindows()


