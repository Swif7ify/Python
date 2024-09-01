import time
import pyautogui
import math
#
time.sleep(2)
# while True:
#     with open('C:\\Users\\earlo\\OneDrive\\Desktop\\python\\test\\bot\\bot.txt') as file:
#         for i in file:
#             pyautogui.typewrite(i)
#             pyautogui.press('enter')

# def auto():
#     while True:
#         pyautogui.press('a')
#         time.sleep(0.1)  # Add a small delay to avoid overwhelming the system
#         pyautogui.press('w')
#         time.sleep(0.1)
#         pyautogui.press('d')
#         time.sleep(0.1)
#         pyautogui.press('s')
#         time.sleep(0.1)
#
# # Call the function
# auto()


# knowing screen size
# screen_width, screen_height = pyautogui.size()
# print(f"Screen width: {screen_width}, Screen height: {screen_height}")
#
# # Move the mouse to the center of the screen
# pyautogui.moveTo(screen_width // 2, screen_height // 2)

# pyautogui.moveTo(100, 100)


# pyautogui.moveTo(100, 100, duration=2)
# # Move the mouse 50 pixels to the right and 50 pixels down from its current position
# pyautogui.moveRel(50, 50)

#
# Set the initial side length
# side_length = 1
#
# # Number of spiral iterations
# iterations = 20
#
# # Increment value to make the gaps smaller
# increment = 5
# for i in range(iterations):
#     pyautogui.dragRel(side_length, 0, duration=0.25)  # Move right
#     side_length += increment
#     pyautogui.dragRel(0, side_length, duration=0.25)  # Move down
#     side_length += increment
#     pyautogui.dragRel(-side_length, 0, duration=0.25) # Move left
#     side_length += increment
#     pyautogui.dragRel(0, -side_length, duration=0.25) # Move up
#     side_length += increment

# pyautogui.click()
# pyautogui.click(200, 200)
# pyautogui.click(button='right')

# # Hold down the left mouse button at the current position
# pyautogui.mouseDown()
#
# # Perform other actions while the button is held down...
#
# # Release the left mouse button
# pyautogui.mouseUp()

# # Hold down the right mouse button at the current position
# pyautogui.mouseDown(button='right')
#
# # Perform other actions while the button is held down...
#
# # Release the right mouse button
# pyautogui.mouseUp(button='right')




# Add a small delay to ensure the script starts after switching to the desired window
# Add a small delay to ensure the script starts after switching to the desired window

# Set the initial position
# start_x, start_y = pyautogui.position()
# pyautogui.moveTo(start_x, start_y)
# # Set the radius of the circle
# radius = 100
#
# # Number of steps for smoother circle
# steps = 100
#
# pyautogui.dragTo()
# # Draw the circle
# for i in range(steps):
#     # Calculate the next point on the circle
#     angle = 2 * math.pi * i / steps
#     x = start_x + radius * math.cos(angle)
#     y = start_y + radius * math.sin(angle)
#     pyautogui.moveTo(x, y)
