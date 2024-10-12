import pygame
import sys
import requests

# Your Gemini API key
api_key = "AizaSyBSdQ0-Qdc7RbGp"  # Replace with your actual Gemini API key

# Define the API endpoint
api_endpoint = "https://api.gemini.com/v1/completions"

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gemini Chatbox")

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
                # Send text to Gemini and get a response
                if text:
                    try:
                        response = requests.post(
                            api_endpoint,
                            headers={
                                "Authorization": f"Bearer {api_key}",
                                "Content-Type": "application/json"
                            },
                            json={
                                "model": "gpt-4-turbo",
                                "messages": [
                                    {
                                        "role": "user",
                                        "content": text
                                    }
                                ]
                            }
                        )
                        response.raise_for_status()  # Check for HTTP errors
                        response_data = response.json()
                        response_text = response_data['choices'][0]['message']['content'].strip()
                    except requests.RequestException as e:
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
