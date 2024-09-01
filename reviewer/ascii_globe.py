import numpy as np
import time
import os

# ASCII characters to represent the intensity
ascii_chars = " .:-=+*#%@"

# Function to map intensity to ASCII characters
def get_char(val):
    return ascii_chars[int(val * (len(ascii_chars) - 1))]

# Generate the globe
def generate_globe(radius=20, step=0.3):
    theta = np.arange(0, np.pi * 2, step)
    phi = np.arange(0, np.pi, step)
    theta, phi = np.meshgrid(theta, phi)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return x, y, z

# Rotate the globe
def rotate_globe(x, y, z, angle_x, angle_y):
    cos_x, sin_x = np.cos(angle_x), np.sin(angle_x)
    cos_y, sin_y = np.cos(angle_y), np.sin(angle_y)

    # Rotation around the x-axis
    y_new = y * cos_x - z * sin_x
    z_new = y * sin_x + z * cos_x

    # Rotation around the y-axis
    x_new = x * cos_y + z_new * sin_y
    z_final = -x * sin_y + z_new * cos_y

    return x_new, y_new, z_final

# Render the globe to ASCII
def render_globe(x, y, z, radius):
    output = []
    for i in range(len(x)):
        row = []
        for j in range(len(x[i])):
            intensity = (z[i][j] + radius) / (2 * radius)
            char = get_char(intensity)
            row.append(char)
        output.append("".join(row))
    return "\n".join(output)

# Main loop to animate the globe
def animate_globe():
    radius = 20
    x, y, z = generate_globe(radius=radius)

    angle_x, angle_y = 0, 0
    while True:
        x_rot, y_rot, z_rot = rotate_globe(x, y, z, angle_x, angle_y)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(render_globe(x_rot, y_rot, z_rot, radius))
        time.sleep(0.1)
        angle_x += 0.05
        angle_y += 0.03

# Run the animation
animate_globe()
