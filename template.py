import cv2
import pyautogui
import keyboard

from time import sleep

pyautogui.PAUSE = 0

# first template
template = cv2.imread('t.png')
template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
template_w, template_h = template_gray.shape[::-1]
# [::-1] because opencv gives you height, width

# second template
template2 = cv2.imread('t2.png')
template2_gray = cv2.cvtColor(template2, cv2.COLOR_RGB2GRAY)
template2_w, template2_h = template2_gray.shape[::-1]


# pyautogui.displayMousePosition()

# 367,290
x, y, w, h = 137, 420, 530, 303

sleep(3)

# finding region
# img = pyautogui.screenshot('game.png', (x, y, w, h))
# img.save(r"C:\Users\Panagiotis\Documents\Job\python\findtheseguys\game.png")


while keyboard.is_pressed('q') == False:
    pyautogui.screenshot('game.png', (x, y, w, h))
    image = cv2.imread('game.png')

    while True:
        # see what computer sees
        image_mini = cv2.resize(
            src=image,
            dsize=(530, 303)
        )
        cv2.imshow('vision', image_mini)
        cv2.waitKey(10)

        # make our image gray
        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # match template
        result = cv2.matchTemplate(
            image=image_gray,
            templ=template_gray,
            method=cv2.TM_CCOEFF_NORMED
        )

        result2 = cv2.matchTemplate(
            image=image_gray,
            templ=template2_gray,
            method=cv2.TM_CCOEFF_NORMED
        )
        min2_val, max2_val, min2_loc, max2_loc = cv2.minMaxLoc(result2)

        # find image x, image y
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= 0.8:
            # pyautogui.click(
            #     x=max_loc[0] + x,
            #     y=max_loc[1] + y
            # )
            # draw rectangle
            image = cv2.rectangle(
                img=image,
                pt1=max_loc,
                pt2=(
                    max_loc[0] + template_w,
                    max_loc[1] + template_h
                ),
                color=(0, 255, 0),
                thickness=-1
            )
        elif max2_val >= 0.8:
            image = cv2.rectangle(
                img=image,
                pt1=max2_loc,
                pt2=(
                    max2_loc[0] + template2_w,
                    max2_loc[1] + template2_h
                ),
                color=(0, 255, 0),
                thickness=-1
            )
        else:
            break
