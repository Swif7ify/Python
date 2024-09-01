import pygame
import math
from math import pi, log, log2, factorial, sqrt
from sympy import Sum, Product, symbols

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Scientific Calculator')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
BLUE = (100, 100, 255)

# Fonts
font = pygame.font.SysFont(None, 35)
large_font = pygame.font.SysFont(None, 55)

# Button settings
button_width, button_height = 70, 50
button_margin = 10

# Calculator state
input_str = ''
result_str = ''

# Button labels and positions
buttons = [
    ('7', 10, 130), ('8', 90, 130), ('9', 170, 130), ('/', 250, 130),
    ('4', 10, 190), ('5', 90, 190), ('6', 170, 190), ('*', 250, 190),
    ('1', 10, 250), ('2', 90, 250), ('3', 170, 250), ('-', 250, 250),
    ('0', 10, 310), ('.', 90, 310), ('+', 170, 310), ('=', 250, 310),
    ('C', 10, 370), ('sqrt', 90, 370), ('^', 170, 370), ('log', 250, 370),
    ('floor', 10, 430), ('ceil', 90, 430), ('N!', 170, 430), ('%', 250, 430),
    ('x^n^n', 10, 490), ('log2', 90, 490), ('pi', 170, 490), ('//', 250, 490),
    ('root', 10, 550), ('summ', 90, 550), ('prod', 170, 550), ('a!+b!', 250, 550),
]


# Mathematical functions
def floor_func(x):
    return math.floor(x)


def ceil_func(x):
    return math.ceil(x)


def factorial_func(x):
    return math.factorial(x)


def root_func(x):
    return math.sqrt(x)


def cube_root_func(x):
    return x ** (1 / 3)


def power_func(x, n):
    return x ** n


def power_of_power_func(x, n):
    return x ** (n ** n)


def log_func(x, base=10):
    return math.log(x, base)


def log2_func(x):
    return math.log2(x)


def summation_func(expr, start, end):
    x = symbols('x')
    return Sum(expr, (x, start, end)).doit()


def product_func(expr, start, end):
    x = symbols('x')
    return Product(expr, (x, start, end)).doit()


def evaluate_expression(expr):
    try:
        result = eval(expr)
        return str(result)
    except Exception as e:
        return 'Error'


# Draw buttons on screen
def draw_buttons():
    for label, x, y in buttons:
        rect = pygame.Rect(x, y, button_width, button_height)
        pygame.draw.rect(screen, DARK_GRAY, rect)
        text_surface = font.render(label, True, WHITE)
        screen.blit(text_surface, (x + 20, y + 15))


def draw_screen():
    screen.fill(WHITE)

    # Display input and result
    pygame.draw.rect(screen, GRAY, (10, 10, 380, 100))
    input_text_surface = large_font.render(input_str, True, BLACK)
    screen.blit(input_text_surface, (20, 20))

    result_text_surface = font.render(result_str, True, BLUE)
    screen.blit(result_text_surface, (20, 70))

    draw_buttons()
    pygame.display.flip()


# Check if a button is clicked
def handle_click(pos):
    global input_str, result_str

    for label, x, y in buttons:
        rect = pygame.Rect(x, y, button_width, button_height)
        if rect.collidepoint(pos):
            if label == '=':
                result_str = evaluate_expression(input_str)
            elif label == 'C':
                input_str = ''
                result_str = ''
            else:
                input_str += label
            break


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(event.pos)

    draw_screen()

pygame.quit()
