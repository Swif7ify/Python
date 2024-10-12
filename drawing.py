# import pyauto
# import time
#
# # Add a small delay to ensure the script starts after switching to the desired window
# time.sleep(2)
#
# # Define initial position
# start_x, start_y = 500, 500
#
# # Move to the starting position
# pyautogui.moveTo(start_x, start_y)
#
# # Draw the head (circle)
# pyautogui.mouseDown()
# pyautogui.moveRel(0, 50, duration=0.5)
# pyautogui.moveRel(50, 0, duration=0.5)
# pyautogui.moveRel(0, -50, duration=0.5)
# pyautogui.moveRel(-50, 0, duration=0.5)
# pyautogui.mouseUp()
#
# # Move to the position for the body
# pyautogui.moveTo(start_x + 25, start_y + 50)
#
# # Draw the body (rectangle)
# pyautogui.mouseDown()
# pyautogui.moveRel(0, 100, duration=1)
# pyautogui.moveRel(50, 0, duration=1)
# pyautogui.moveRel(0, -100, duration=1)
# pyautogui.moveRel(-50, 0, duration=1)
# pyautogui.mouseUp()
#
# # Move to the position for the left arm
# pyautogui.moveTo(start_x + 25, start_y + 70)
#
# # Draw the left arm
# pyautogui.mouseDown()
# pyautogui.moveRel(-30, 0, duration=1)
# pyautogui.moveRel(0, 20, duration=1)
# pyautogui.moveRel(30, 0, duration=1)
# pyautogui.mouseUp()
#
# # Move to the position for the right arm
# pyautogui.moveTo(start_x + 75, start_y + 70)
#
# # Draw the right arm
# pyautogui.mouseDown()
# pyautogui.moveRel(30, 0, duration=1)
# pyautogui.moveRel(0, 20, duration=1)
# pyautogui.moveRel(-30, 0, duration=1)
# pyautogui.mouseUp()
#
# # Move to the position for the left leg
# pyautogui.moveTo(start_x + 25, start_y + 150)
#
# # Draw the left leg
# pyautogui.mouseDown()
# pyautogui.moveRel(-10, 40, duration=1)
# pyautogui.moveRel(20, 0, duration=1)
# pyautogui.moveRel(-10, -40, duration=1)
# pyautogui.mouseUp()
#
# # Move to the position for the right leg
# pyautogui.moveTo(start_x + 75, start_y + 150)
#
# # Draw the right leg
# pyautogui.mouseDown()
# pyautogui.moveRel(-10, 40, duration=1)
# pyautogui.moveRel(20, 0, duration=1)
# pyautogui.moveRel(-10, -40, duration=1)
# pyautogui.mouseUp()
#
# print("Drawing complete!")
