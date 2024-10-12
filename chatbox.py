import pygame
import sys
from openai import OpenAI

# Your OpenAI API key (make sure it's correct and valid)
api_key = "AizaSyBSdQ0-Qdc7RbGp"  # Redacted key

# Initialize OpenAI API client
client = OpenAI(api_key=api_key)

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ChatGPT Chatbox")

# Fonts and colors
font = pygame.font.Font(None, 32)
input_box_color = pygame.Color('lightskyblue3')
background_color = pygame.Color('black')
text_color = pygame.Color('white')

# Input box setup
input_box = pygame.Rect(50, HEIGHT - 60, 500, 32)
text = ''
response_text = ''

# Chatbox loop
running = True
while running:
    screen.fill(background_color)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Send text to OpenAI and get a response
                if text:
                    try:
                        response = client.chat.completions.create(
                            messages=[
                                {
                                    "role": "user",
                                    "content": text,
                                }
                            ],
                            model="gpt-4-turbo",
                        )
                        response_text = response['choices'][0]['message']['content'].strip()
                    except Exception as e:
                        print(f"An error occurred: {e}")
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    # Draw the input box
    txt_surface = font.render(text, True, text_color)
    width = max(500, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, input_box_color, input_box, 2)

    # Display response
    if response_text:
        response_surface = font.render(response_text, True, text_color)
        screen.blit(response_surface, (50, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()
