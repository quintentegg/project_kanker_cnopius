import pygame
import sys
NEW_WIDTH = 800
NEW_HEIGHT = 600
screen = pygame.display.set_mode((NEW_WIDTH, NEW_HEIGHT))
image = pygame.image.load('achtergrond man.jpg')
IMAGE = pygame.image.load('hallo.png')
# Resize image
window_size = (600,800)
new_size = (300, 500)  # New width and height
resized_image_man = pygame.transform.scale(image, new_size)
# Display resized image
# Load image
image = pygame.image.load('achtergrond vrouw.png')
# Resize image
window_size = (600,800)
new_size = (300, 500)  # New width and height
resized_image_vrouw = pygame.transform.scale(image, new_size)
# Display resized image

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
button1_x = 50
button1_y = 350
button2_x = 400
button2_y = 350
New_width = 150
New_height = 250
NEw_width = 150
NEw_height = 250

def main_scherm():
    pygame.init()
    # Load the images
    image1 = pygame.image.load("achtergrond man.jpg")
    image2 = pygame.image.load("achtergrond vrouw.png")
    # Resize the images
    new_width = 150
    new_height = 250
    NEW_width = 150
    NEW_height = 250
    image1 = pygame.transform.scale(image1, (NEW_width, NEW_height))
    image2 = pygame.transform.scale(image2, (new_width, new_height))
    # Set up the display
    pygame.display.set_caption("project cnopius kanker")
    screen.fill((255, 255, 255))
    # Draw the images on the screen
    screen.blit(image1, (150, 100))
    screen.blit(image2, (450, 100))

    # Update the display
    pygame.display.flip()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        button_maken()
    pygame.quit()

def sprite_hoi():
    import pygame
    pygame.init()
    # Set up the screen
    screen_width = 600
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the images
    sprite_image = pygame.image.load("witte bloedcel.png")
    extra_image = pygame.image.load("achtergrond man.jpg")
    # Set up the sprite
    sprite_rect = sprite_image.get_rect()
    sprite_rect.center = (screen_width / 2, screen_height / 2)
    # Set up the font
    font = pygame.font.SysFont("Arial", 30)
    # Main loop
    sprite_speed = 0.4
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Move the sprite
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            sprite_rect.x -= sprite_speed
        if keys[pygame.K_RIGHT]:
            sprite_rect.x += sprite_speed
        if keys[pygame.K_UP]:
            sprite_rect.y -= sprite_speed
        if keys[pygame.K_DOWN]:
            sprite_rect.y += sprite_speed
        # Check if the sprite is in a specific coordinate
        if sprite_rect.x == 0 and sprite_rect.y == 0:
            # Print hello on the screen
            text = font.render("Hello!", True, (255, 255, 255))
            screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))
        # Resize the sprite and extra image
        sprite_image_resized = pygame.transform.scale(sprite_image, (50, 50))
        extra_image_resized = pygame.transform.scale(extra_image, (300, 500))
        # Draw everything on the screen
        screen.fill((255, 255, 255))
        screen.blit(extra_image_resized, (150, 120))
        screen.blit(sprite_image_resized, sprite_rect)
        pygame.display.flip()



def sprite_man():
    screen = pygame.display.set_mode(window_size)
    # Define colors
    WHITE = (255, 255, 255)
    # Load the image for the sprite
    sprite_image = pygame.image.load('witte bloedcel.png').convert_alpha()
    # Set the starting position of the sprite
    sprite_x = NEW_WIDTH // 2
    sprite_y = NEW_HEIGHT // 2
    trigger_x = 150
    trigger_y = 120
    # Define the size of the sprite
    sprite_width = 50
    sprite_height = 50
    # Resize the sprite image to the desired size
    sprite_image_resized = pygame.transform.scale(sprite_image, (sprite_width, sprite_height))
    sprite_rect = sprite_image.get_rect()
    hoi_rect = IMAGE.get_rect()
    # Define the speed of the sprite
    sprite_speed = 0.4
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Handle movement controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            sprite_x -= sprite_speed
        if keys[pygame.K_RIGHT]:
            sprite_x += sprite_speed
        if keys[pygame.K_UP]:
            sprite_y -= sprite_speed
        if keys[pygame.K_DOWN]:
            sprite_y += sprite_speed
        # Fill the screen with white
        screen.fill(WHITE)
        # Draw the sprite on the screen
        screen.blit(resized_image_man, (150, 120))
        screen.blit(IMAGE, (150, 120))
        screen.blit(sprite_image_resized, (sprite_x, sprite_y))
        if sprite_x == 150 and sprite_y == 120:
        # print hello to the console
            print("hello")
        # Update the display
        pygame.display.update()
    # Quit Pygame
    pygame.quit()

def sprite_vrouw():
    screen = pygame.display.set_mode(window_size)
    # Define colors
    WHITE = (255, 255, 255)
    # Load the image for the sprite
    sprite_image = pygame.image.load('witte bloedcel.png').convert_alpha()
    # Set the starting position of the sprite
    sprite_x = NEW_WIDTH // 2
    sprite_y = NEW_HEIGHT // 2
    # Define the size of the sprite
    sprite_width = 50
    sprite_height = 50
    # Resize the sprite image to the desired size
    sprite_image = pygame.transform.scale(sprite_image, (sprite_width, sprite_height))
    # Define the speed of the sprite
    sprite_speed = 0.4
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Handle movement controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            sprite_x -= sprite_speed
        if keys[pygame.K_RIGHT]:
            sprite_x += sprite_speed
        if keys[pygame.K_UP]:
            sprite_y -= sprite_speed
        if keys[pygame.K_DOWN]:
            sprite_y += sprite_speed
        # Fill the screen with white
        screen.fill(WHITE)
        # Draw the sprite on the screen
        screen.blit(resized_image_vrouw, (150, 120))
        screen.blit(sprite_image, (sprite_x, sprite_y))
        # Update the display
        pygame.display.update()
    # Quit Pygame
    pygame.quit()

def button_maken():
    # Load the button images
    button1_image = pygame.image.load("button man.png")
    button2_image = pygame.image.load("button vrouw.png")
    # Define the button locations
    button1_x = 100
    button1_y = 350
    button2_x = 380
    button2_y = 350
    # Define the button functions
    def button1_clicked():
        print("Button 1 clicked!")
    def button2_clicked():
        print("Button 2 clicked!")
    # Define the function for drawing the buttons
    def draw_buttons():
        screen.blit(button1_image, (button1_x, button1_y))
        screen.blit(button2_image, (button2_x, button2_y))
    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button1_x < mouse_x < button1_x + button1_image.get_width() and \
                   button1_y < mouse_y < button1_y + button1_image.get_height():
                    sprite_hoi()
                elif button2_x < mouse_x < button2_x + button2_image.get_width() and \
                     button2_y < mouse_y < button2_y + button2_image.get_height():
                    sprite_vrouw()
        # Draw the screen
        draw_buttons()
        pygame.display.update()


main_scherm()