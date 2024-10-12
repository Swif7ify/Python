# from selenium import webdriver
# from bs4 import BeautifulSoup
# import pyautogui
# import keyboard
# import time
#
# def get_text_to_type(driver):
#     time.sleep(1)
#     src = driver.page_source
#     soup = BeautifulSoup(src, "html.parser")
#     span = soup.find_all("span", class_=["u-pl-0", "u-px-2xs"])
#     # span = soup.find_all("span")
#     text = ""
#
#     for i in span:
#         text += i.text + " "
#
#         if not text:
#             print("No Text Found")
#         else:
#             print("Text Found", text)
#
#     return text
#
#
# def type_text(text):
#     pyautogui.typewrite(text, interval=0.1)
#
#
# def main():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get("https://www.livechat.com/typing-speed-test/#/")
#
#     keyboard.wait("ctrl+alt+t")
#
#     text_to_type = get_text_to_type(driver)
#     if text_to_type:
#         type_text(text_to_type)
#
#
# main()

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import pyautogui
# import keyboard
# import time

# typed_texts = []
# first_run = True
# stop_program = False


# def get_text_to_type(driver):
#     global stop_program
#     time.sleep(0.5)
#     src = driver.page_source
#     soup = BeautifulSoup(src, "html.parser")
#
#     # Check the value of the span with class u-text-p3 u-mb-0
#     value_span = soup.find("span", class_="u-text-p3 u-mb-0")
#     if value_span:
#         try:
#             value = int(value_span.text.strip())  # Convert the text to an integer
#             if value == 0:
#                 print("Value is 0. Stopping the program.")
#                 stop_program = True
#                 return ""
#         except ValueError:
#             print("Could not convert span value to integer.")
#
#     span = soup.find_all("span", class_=["u-pl-0", "u-px-2xs"])
#     text = ""
#
#     for i in span:
#         if i.text.strip() not in typed_texts:
#             text += i.text + " "
#             typed_texts.append(i.text.strip())
#
#     if not text:
#         print("No New Text Found")
#     else:
#         print("New Text Found:", text)
#
#     return text
#
#
# def type_text(text):
#     pyautogui.typewrite(text, interval=0.01)
#
#
# def main():
#     global first_run, stop_program
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get("https://www.livechat.com/typing-speed-test/#/")
#
#     while not stop_program:
#         if first_run:
#             print("Waiting for first keypress (Ctrl+Alt+T)...")
#             keyboard.wait("ctrl+alt+t")
#             first_run = False
#         else:
#             print("Automatically simulating keypress (Ctrl+Alt+T)...")
#             keyboard.press_and_release('ctrl+alt+t')
#
#         text_to_type = get_text_to_type(driver)
#         if text_to_type:
#             type_text(text_to_type)
#
#
#     print("Program has stopped.")
#
#
# main()


from bs4 import BeautifulSoup
import pyautogui
import keyboard
import time
from selenium import webdriver


def get_text_to_type(driver):
    time.sleep(0.5)
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    # Find all divs with class "word active" or "word", but exclude "word type"
    div = soup.find_all("div", class_=["word"])
    text = ""

    for i in div:
        if "typed" not in i.get("class", []):
            text += i.text + " "
        else:
            continue
    return text.strip()


def type_text(text):
    print(text)
    pyautogui.typewrite(text, interval=0.05)
    pyautogui.press("space")


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://monkeytype.com/")

    first_run = True

    while True:
        if first_run:
            print("Waiting for first keypress (Ctrl+Alt+T)...")
            keyboard.wait("ctrl+alt+t")
            first_run = False
        else:
            print("Automatically simulating keypress (Ctrl+Alt+T)...")
            keyboard.press_and_release('ctrl+alt+t')

        # Attempt to get and type the text
        text_to_type = get_text_to_type(driver)

        if text_to_type:
            type_text(text_to_type)
        else:
            print("No new text found, retrying...")



if __name__ == "__main__":
    main()

