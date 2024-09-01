import pyautogui
import time

# Add a small delay to ensure the script starts after switching to the desired window
time.sleep(2)

# Define initial position
start_x, start_y = 500, 500

# Move to the starting position
pyautogui.moveTo(start_x, start_y)

# Draw the head (circle)
pyautogui.mouseDown()
pyautogui.dragRel(0, 50)
pyautogui.dragRel(50, 0)
pyautogui.dragRel(0, -50)
pyautogui.dragRel(-50, 0)
pyautogui.mouseUp()

# Move to the position for the body
pyautogui.dragTo(start_x + 25, start_y + 50)

# Draw the body (rectangle)
pyautogui.mouseDown()
pyautogui.dragRel(0, 100)
pyautogui.dragRel(50, 0)
pyautogui.dragRel(0, -100)
pyautogui.dragRel(-50, 0)
pyautogui.mouseUp()

# Move to the position for the left arm
pyautogui.dragTo(start_x + 25, start_y + 70)

# Draw the left arm
pyautogui.mouseDown()
pyautogui.dragRel(-30, 0)
pyautogui.dragRel(0, 20)
pyautogui.dragRel(30, 0)
pyautogui.mouseUp()

# Move to the position for the right arm
pyautogui.dragTo(start_x + 75, start_y + 70)

# Draw the right arm
pyautogui.mouseDown()
pyautogui.dragRel(30, 0)
pyautogui.dragRel(0, 20)
pyautogui.dragRel(-30, 0)
pyautogui.mouseUp()

# Move to the position for the left leg
pyautogui.dragTo(start_x + 25, start_y + 150)

# Draw the left leg
pyautogui.mouseDown()
pyautogui.dragRel(-10, 40)
pyautogui.dragRel(20, 0)
pyautogui.dragRel(-10, -40)
pyautogui.mouseUp()

# Move to the position for the right leg
pyautogui.dragTo(start_x + 75, start_y + 150)

# Draw the right leg
pyautogui.mouseDown()
pyautogui.dragRel(-10, 40)
pyautogui.dragRel(20, 0)
pyautogui.dragRel(-10, -40)
pyautogui.mouseUp()

print("Drawing complete!")
