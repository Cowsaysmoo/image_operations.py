####Jared Homer, Alex Stephens, Tracey Gibson
import cv2
import matplotlib.pyplot as plt
import numpy as np

capture = cv2.VideoCapture(cv2.CAP_DSHOW)             #Used this because it looks better ¯\_(ツ)_/¯
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame width:', frame_width)
print('Frame height:', frame_height)
video = cv2.VideoWriter('C:/tmp/live_camera.avi', cv2.VideoWriter_fourcc('M','J','P','G'),25,(frame_width, frame_height))
escape = False
frameCount = 0
while not escape and frameCount < 4500:  #Part 1
    has_frame, frame = capture.read()
    if not has_frame:
        print('Can\'t get frame')
        break
    video.write(frame)         #Part 2
    cv2.imshow('frame', frame)
    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed esc')
        escape = True
    frameCount += 1
capture.release()
video.release()
cv2.destroyAllWindows()

capture = cv2.VideoCapture('C:/tmp/live_camera.avi')       #Part 3
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame width:', frame_width)
print('Frame height:', frame_height)
frameRate = capture.get(cv2.CAP_PROP_FPS)
video = cv2.VideoWriter('C:/tmp/modified_video.avi', cv2.VideoWriter_fourcc('M','J','P','G'),frameRate, (frame_width, frame_height))  #Part 5k
escape = False
plotted = False
while not escape:        #Part 4
    has_frame, frame = capture.read()
    if not has_frame:
        print('Can\'t get frame')
        break

    print('Frame width:', frame_width)          #Part 5b
    print('Frame height:', frame_height)

    blueFrame = np.copy(frame)                  #Part 5c
    greenFrame = np.copy(frame)
    redFrame = np.copy(frame)
    blueFrame[:,:,1] = 0
    blueFrame[:,:,2] = 0
    greenFrame[:,:,0] = 0
    greenFrame[:,:,2] = 0
    redFrame[:,:,0] = 0
    redFrame[:,:,1] = 0

    (width, height) = (capture.get(cv2.CAP_PROP_FRAME_WIDTH), capture.get(cv2.CAP_PROP_FRAME_HEIGHT))    #Part 5d
    resizedFrame = cv2.resize(frame, (int(width * 0.7), int(height * 0.7)))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                #Part 5e
    saturation = hsv[:, :, 1]
    hsv[:, :, 2] = 255 * 0.5                                    #Part 5f
    from_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)             #Part 5i

    gauss_blur = cv2.GaussianBlur(frame, (7, 7), 0)
    video.write(gauss_blur)

    cv2.imshow('frame', frame)                   #Part 5a
    cv2.moveWindow("frame", 800, 0)
    cv2.imshow('blueFrame', blueFrame)           #Part 5c
    cv2.moveWindow("blueFrame", 50, 0)
    cv2.imshow('greenFrame', greenFrame)
    cv2.moveWindow("greenFrame", 100, 0)
    cv2.imshow('redFrame', redFrame)
    cv2.moveWindow("redFrame", 150, 0)
    cv2.imshow("resizedFrame", resizedFrame)     #Part 5d
    cv2.moveWindow("resizedFrame", 1450, 0)
    cv2.imshow("hsv", from_hsv)
    cv2.moveWindow("hsv", 0, 480)
    cv2.imshow("gauss_blur", gauss_blur)         #Part 5j
    cv2.moveWindow("gauss_blur", 1300, 480)

    key = cv2.waitKey(int((1/frameRate)*1000))
    if not plotted:                              #Part 5g
        fig = plt.figure(figsize=(8, 3))
        fig.canvas.set_window_title('Saturation Histograms')

        hist1, bins1 = np.histogram(saturation, 256, [0, 255])
        plt.fill_between(range(256), hist1, 0)
        plt.xlabel('Saturation')

        eq_hist = cv2.equalizeHist(saturation)                 #Part 5h
        hist2, bins2 = np.histogram(eq_hist, 256, [0, 255])
        plt.subplot(122)
        plt.fill_between(range(256), hist2, 0)
        plt.xlabel('EQ Saturation')

        plt.tight_layout()
        plt.ion()
        plt.show()
        plotted = True
    else:
        fig.clear()

        plt.subplot(121)                                      #Part 5g
        hist1, bins1 = np.histogram(saturation, 256, [0, 255])
        plt.fill_between(range(256), hist1, 0, color='C0')
        plt.xlabel('Saturation')

        plt.subplot(122)                                      #Part 5h
        eq_hist = cv2.equalizeHist(saturation)
        hist2, bins2 = np.histogram(eq_hist, 256, [0, 255])
        plt.fill_between(range(256), hist2, 0, color='R0')
        plt.xlabel('EQ Saturation')

        fig.canvas.draw()

    if key == 27:
        print('Pressed esc')
        escape = True
capture.release()
video.release()
cv2.destroyAllWindows()

escape = False
capture = cv2.VideoCapture('C:/tmp/modified_video.avi')          #Part 6
while not escape:
    has_frame, frame = capture.read()
    if not has_frame:
        print('Can\'t get frame')
        break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(int((1/frameRate)*1000))
    if key == 27:
        print('Pressed esc')
        escape = True
capture.release()
cv2.destroyAllWindows()
