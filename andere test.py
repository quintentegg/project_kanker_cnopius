import pygame
import sys
NEW_WIDTH = 800
NEW_HEIGHT = 600
screen = pygame.display.set_mode((NEW_WIDTH, NEW_HEIGHT))
image = pygame.image.load('achtergrond man.jpg')
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
        
        # Resize the sprite and extra image
        sprite_image_resized = pygame.transform.scale(sprite_image, (50, 50))
        extra_image_resized = pygame.transform.scale(extra_image, (300, 500))
        # Draw everything on the screen
        screen.fill((255, 255, 255))
        screen.blit(extra_image_resized, (150, 120))
        screen.blit(sprite_image_resized, sprite_rect)
        pygame.display.flip()

def andere_man():
    import pygame
    pygame.init()
    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Resizable Image and Buttons")
    # Set up the background
    background_color = (255, 255, 255)
    screen.fill(background_color)
    # Load the image and sprite
    new_size = 350, 600
    imager = pygame.image.load("achtergrond man.jpg")
    image = pygame.transform.scale(imager, new_size)
    new_position = 250, 1
    class Button:
        def __init__(self, x, y, width, height, image_path):
            self.rect = pygame.Rect(x, y, width, height)
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))    
        def draw(self, surface):
            surface.blit(self.image, self.rect)
        def is_clicked(self, pos):
            return self.rect.collidepoint(pos)
    button1 = Button(425, 260, 20, 35, '! (1).png')
    button2 = Button(415, 150, 20, 35, '! (2).png')
    button3 = Button(380, 240, 20, 35, '! (3).png')
    button4 = Button(450, 240, 20, 35, '! (4).png')
    button5 = Button(415, 30, 20, 35, '! (5).png')
    button6 = Button(310, 60, 20, 35, '! (6).png')
    button7 = Button(415, 220, 20, 35, '! (7).png')
    button8 = Button(415, 100, 20, 35, '! (8).png')
    button9 = Button(380, 190, 20, 35, '! (9).png')
    button10 = Button(350, 45, 20, 35, '! (10).png')
    button11 = Button(330, 100, 20, 35, '! (11).png')
    button12 = Button(405, 260, 20, 35, '! (12).png')
    button13 = Button(200, 100, 20, 35, '! (13).png')


    # Add buttons to a list
    buttons = [button1, button2, button3, button4,
               button5, button6, button7, button8,
               button9, button10, button11, button12, button13]


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                size = (event.w, event.h)
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        if button == button1:
                            extra_scherm_m_1()
                        elif button == button2:
                            extra_scherm_2_m()
                        elif button == button3:
                            extra_scherm_3_m()
                        elif button == button4:
                            extra_scherm_4_m()
                        elif button == button5:
                            extra_scherm_5_m()
                        elif button == button6:
                            extra_scherm_6_m()
                        elif button == button7:
                            extra_scherm_7_m()
                        elif button == button8:
                            extra_scherm_8_m()
                        elif button == button9:
                            extra_scherm_9_m()
                        elif button == button10:
                            extra_scherm_10_m()
                        elif button == button11:
                            extra_scherm_11_m()
                        elif button == button12:
                            extra_scherm_12_m()
                        elif button == button13:
                            extra_scherm_13_m()
        screen.blit(image, new_position)
        for button in buttons:
            button.draw(screen)
        
        # Update the display
        pygame.display.flip()
    # Quit pygame properly
    pygame.quit()

def extra_scherm_7_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 500, 230
    imager = pygame.image.load("maagkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 40, 380
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Symptomen van maagkanker"
    text_2 = "In het begin heb je van maagkanker meestal weinig of geen klachten."
    text_3 = "Als de tumor in of door de maagwand groeit, kunnen wel klachten ontstaan, "
    text_4 = "zoals (stekende) pijn boven in de buik of rond het borstbeen,"
    text_5 = "afvallen, misselijkheid en/of braken"
    
    text_6 = "Oorzaken en risicofactoren van maagkanker"
    text_7 = "De precieze oorzaak van maagkanker is niet bekend"
    text_8 = "Een langdurige infectie met de Helicobacter pylori bacterie maakt de kans op maagkanker groter"
    text_9 = "Verder speelt leefstijl een belangrijke rol:"   
    text_10 = "roken, lange tijd dagelijks alcohol drinken"
    text_11 = " en veel rood of bewerkt vlees eten vergroten de kans op maagkanker."
    text_12 = "Ongeveer 4 op de 100 mensen met maagkanker krijgt de ziekte door een erfelijke aanleg."

    text_13 = "Soorten maagkanker"
    text_14 = "Bijna alle mensen met maagkanker hebben een adenocarcinoom."
    text_15 = "Deze tumor ontstaat uit de kliercellen van het slijmvlies aan de binnenkant van de maag."

    text_16 = "Uitzaaiingen van maagkanker"
    text_17 = "De kankercellen kunnen zich verspreiden via de lymfe."
    text_18 = "Ze komen dan eerst terecht in de lymfeklieren rond de maag."
    text_19 = "Via de lymfebanen kunnen de kankercellen later ook andere lymfekliergebieden in het lichaam bereiken."
    text_20 = "Kankercellen kunnen ook losraken van de tumor en zich in de buikholte verspreiden"
    text_21 = "Daar kunnen ze uitgroeien tot uitzaaiingen op het buikvlies."
    text_22 = "Ook via het bloed kunnen kankercellen zich verspreiden"
    text_23 = "Ze kunnen dan uitzaaien naar bijvoorbeeld de lever of de longen."

    text_24 = "Gevolgen van maagkanker"
    text_25 = "Na de behandeling kun je nog korte of lange tijd last hebben van vermoeidheid."
    text_26 = "En ook van problemen met eten en drinken,"
    text_27 = "problemen met je ontlasting of neuropathie. Ook psychisch kun je het zwaar hebben."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 72))

    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 92))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 112))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 122))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 132))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 142))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 152))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 172))

    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 192))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 202))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 212))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 222))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 232))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 242))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 252))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 262))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 272))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 282))
    text_surface_23 = font.render(text_23, True, (150, 230, 255))
    screen.blit(text_surface_23, (0, 302))

    text_surface_24 = font_T.render(text_24, True, (150, 230, 255))
    screen.blit(text_surface_24, (0, 322))
    text_surface_25 = font.render(text_25, True, (150, 230, 255))
    screen.blit(text_surface_25, (0, 342))
    text_surface_26 = font.render(text_26, True, (150, 230, 255))
    screen.blit(text_surface_26, (0, 352))
    text_surface_27 = font.render(text_27, True, (150, 230, 255))
    screen.blit(text_surface_27, (0, 362))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_13_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 500, 350
    imager = pygame.image.load("kanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 40, 200
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "andere weetjes"
    text_2 = "1. kanker is niet besmettelijk"
    text_3 = "2. mannen hebben ongeveer 20% meer kans op kanker"
    text_4 = "3. 1/3 volwassenen krijgen kanker"
    text_5 = "4. 7/10 kankerpatiënten is boven de 60 jaar"
 
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 72))

    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_13_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 500, 230
    imager = pygame.image.load("kanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 40, 380
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "andere weetjes"
    text_2 = "1. kanker is niet besmettelijk"
    text_3 = "2. mannen hebben ongeveer 20% meer kans op kanker"
    text_4 = "3. 1/3 volwassenen krijgen kanker"
    text_5 = "4. 7/10 kankerpatiënten is boven de 60 jaar"
 
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 72))

    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_8_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 500, 280
    imager = pygame.image.load("neuskanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 40, 305
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Symptomen bij keelkanker"
    text_2 = "Keelkanker geeft in het begin vage klachten."
    text_3 = "Zoals keelpijn, moeite met slikken en een opgezwollen klier in de hals."
    text_4 = "Pas later ontstaan er andere symptomen."
    text_5 = "Hierdoor wordt de ziekte vaak pas laat ontdekt."
    
    text_6 = "Oorzaken en risicofactoren van keelkanker"
    text_7 = "De belangrijkste risicofactoren voor keelkanker zijn roken,"
    text_8 = " veel alcohol drinken en een besmetting met het humaan papillomavirus (HPV)."
    text_9 = "Er zijn ook nog andere risicofactoren bekend."   

    text_10 = "Groeiwijze van keelkanker"
    text_11 = "Keelkanker ontstaat meestal in het slijmvlies van de keel."
    text_12 = "Als de tumor groter wordt, groeit deze door in de omliggende weefsels."
    text_13 = "Bijvoorbeeld naar de mondbodem, tong of het strottenhoofd."
    
    text_14 = "Cijfers over keelkanker"
    text_15 = "In Nederland kregen in 2021 kregen 892 mensen de diagnose  keelkanker."
    text_16 = "De meeste patiënten zijn mannen tussen de 55 en 75 jaar."
    text_17 = "Omdat keelkanker vaak pas laat ontdekt wordt, is de kans op genezing beperkt."
    text_18 = "Bij uitzaaiingen in de lymfeklieren in de hals is genezing vaak nog mogelijk."
    text_19 = "De kans op genezing is ook beter als de oorzaak van de keelkanker HPV is."
    text_20 = "Als er uitzaaiingen in andere organen zitten, dan is de kans op genezing erg klein."
    text_21 = "Na 5 jaar is ongeveer de helft van de patiënten in leven."

    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 72))

    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 92))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 112))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 122))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 132))

    text_surface_10 = font_T.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 152))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 182))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 192))

    text_surface_14 = font_T.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 212))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 232))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 242))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 252))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 262))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 272))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 282))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 292))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_9_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 380, 220
    imager = pygame.image.load("neuskanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 100, 370
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Symptomen van nierkanker"
    text_2 = "Vaak ontdekt de arts nierkanker toevallig."
    text_3 = "Bijvoorbeeld als je een echografie krijgt van je buik." 
    text_4 = "De meeste mensen met nierkanker hebben in het begin geen klachten."
    text_5 = "Als de tumor groeit, kun je last krijgen van bloed in je plas,"
    text_6 = "pijn in je zij of een voelbare zwelling van je buik."

    text_7 = "Oorzaken en risicofactoren van nierkanker"
    text_8 = "De precieze oorzaak van nierkanker is niet bekend."
    text_9 = "Wel zijn er risicofactoren die de kans groter maken dat je nierkanker krijgt."   

    text_10 = "Uitzaaiingen bij nierkanker"
    text_11 = "Kanker kan uitzaaien. "
    text_12 = "Dat betekent dat kankercellen losraken van de tumor en in een ander deel van het lichaam verder groeien"
    text_13 = "Bij ongeveer 1 op de 7 mensen is nierkanker uitgezaaid op het moment dat ze de diagnose krijgen"
    
    text_14 = "Behandeling van nierkanker"
    text_15 = "De meeste mensen met nierkanker krijgen een operatie."
    text_16 = "De arts haalt de tumor dan weg"
    text_17 = "Je kunt ook een andere behandeling krijgen, "
    text_18 = "zoals bestraling, warmte-ablatie met MWA (microwave ablatie) of cryo-ablatie."
    text_19 = "Bij kleine tumoren in de nier die langzaam groeien kan ook gewacht worden met de behandeling."
    text_20 = "Je krijgt dan regelmatig een echo of scan om de groei van de tumor te volgen."
    text_21 = "Als je uitzaaiingen hebt, krijg je meestal bestraling,"
    text_22 = "doelgerichte therapie of immunotherapie."
    
    text_23 = "Gevolgen van nierkanker"
    text_24 = "Na de behandeling kun je last hebben van pijn of vermoeidheid."
    text_25 = "En van klachten als somberheid en angst"
    text_26 = "Nierkanker kan ook invloed hebben op je seksleven en op intimiteit."

    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 72))

    text_surface_7 = font_T.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 92))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 122))

    text_surface_10 = font_T.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 142))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 162))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 172))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 182))

    text_surface_14 = font_T.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 202))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 222))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 232))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 242))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 252))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 262))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 272))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 282))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 292))

    text_surface_23 = font_T.render(text_23, True, (150, 230, 255))
    screen.blit(text_surface_23, (0, 312))
    text_surface_24 = font.render(text_24, True, (150, 230, 255))
    screen.blit(text_surface_24, (0, 332))
    text_surface_25 = font.render(text_25, True, (150, 230, 255))
    screen.blit(text_surface_25, (0, 342))
    text_surface_26 = font.render(text_26, True, (150, 230, 255))
    screen.blit(text_surface_26, (0, 352))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_9_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 380, 220
    imager = pygame.image.load("nierkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 100, 370
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Symptomen van nierkanker"
    text_2 = "Vaak ontdekt de arts nierkanker toevallig."
    text_3 = "Bijvoorbeeld als je een echografie krijgt van je buik." 
    text_4 = "De meeste mensen met nierkanker hebben in het begin geen klachten."
    text_5 = "Als de tumor groeit, kun je last krijgen van bloed in je plas,"
    text_6 = "pijn in je zij of een voelbare zwelling van je buik."

    text_7 = "Oorzaken en risicofactoren van nierkanker"
    text_8 = "De precieze oorzaak van nierkanker is niet bekend."
    text_9 = "Wel zijn er risicofactoren die de kans groter maken dat je nierkanker krijgt."   

    text_10 = "Uitzaaiingen bij nierkanker"
    text_11 = "Kanker kan uitzaaien. "
    text_12 = "Dat betekent dat kankercellen losraken van de tumor en in een ander deel van het lichaam verder groeien"
    text_13 = "Bij ongeveer 1 op de 7 mensen is nierkanker uitgezaaid op het moment dat ze de diagnose krijgen"
    
    text_14 = "Behandeling van nierkanker"
    text_15 = "De meeste mensen met nierkanker krijgen een operatie."
    text_16 = "De arts haalt de tumor dan weg"
    text_17 = "Je kunt ook een andere behandeling krijgen, "
    text_18 = "zoals bestraling, warmte-ablatie met MWA (microwave ablatie) of cryo-ablatie."
    text_19 = "Bij kleine tumoren in de nier die langzaam groeien kan ook gewacht worden met de behandeling."
    text_20 = "Je krijgt dan regelmatig een echo of scan om de groei van de tumor te volgen."
    text_21 = "Als je uitzaaiingen hebt, krijg je meestal bestraling,"
    text_22 = "doelgerichte therapie of immunotherapie."
    
    text_23 = "Gevolgen van nierkanker"
    text_24 = "Na de behandeling kun je last hebben van pijn of vermoeidheid."
    text_25 = "En van klachten als somberheid en angst"
    text_26 = "Nierkanker kan ook invloed hebben op je seksleven en op intimiteit."

    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 72))

    text_surface_7 = font_T.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 92))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 122))

    text_surface_10 = font_T.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 142))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 162))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 172))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 182))

    text_surface_14 = font_T.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 202))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 222))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 232))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 242))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 252))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 262))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 272))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 282))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 292))

    text_surface_23 = font_T.render(text_23, True, (150, 230, 255))
    screen.blit(text_surface_23, (0, 312))
    text_surface_24 = font.render(text_24, True, (150, 230, 255))
    screen.blit(text_surface_24, (0, 332))
    text_surface_25 = font.render(text_25, True, (150, 230, 255))
    screen.blit(text_surface_25, (0, 342))
    text_surface_26 = font.render(text_26, True, (150, 230, 255))
    screen.blit(text_surface_26, (0, 352))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_12_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 300, 220
    imager = pygame.image.load("vulvakanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 100, 380
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Symptomen van schaamlipkanker"
    text_2 = "De eerste symptomen van schaamlipkanker zijn meestal jeuk, "
    text_3 = "pijn of een branderig gevoel aan de schaamlippen." 
    text_4 = "Je kunt ook bloedverlies hebben, of andere afscheiding"
    text_5 = "Een verdikking of een wondje op "
    text_6 = "de schaamlippen kan ook een symptoom van schaamlipkanker zijn."

    text_7 = "Oorzaken en risicofactoren van schaamlipkanker"
    text_8 = "De precieze oorzaak van schaamlipkanker is niet bekend"
    text_9 = "Sommige vrouwen hebben een grotere kans om schaamlipkanker te krijgen, "   
    text_10 = "of een voorstadium van schaamlipkanker."
    text_11 = "Het gaat om vrouwen met:"
    text_12 = "1. Lichen Sclerosus (LS) van de vulva"
    text_13 = "2. een langdurige infectie met het Humaan Papillomavirus (HPV)"
    
    text_14 = "Soorten schaamlipkanker"
    text_15 = "Er zijn verschillende soorten schaamlipkanker."
    text_16 = "Meestal ontstaat schaamlipkanker in de huidcellen van de schaamlippen."
    text_17 = "Dit heet plaveiselcelcarcinoom."

    text_18 = "Behandeling van schaamlipkanker"
    text_19 = "Er zijn verschillende behandelingen mogelijk bij schaamlipkanker, "
    text_20 = "zoals een operatie, bestraling, chemoradiatie, chemotherapie, "
    text_21 = "of een combinatie van deze behandelingen."
    text_22 = "De behandeling gebeurt meestal in een gespecialiseerd ziekenhuis."
    
    text_23 = "Gevolgen van schaamlipkanker"
    text_24 = "Na de behandeling kun je nog korte of lange tijd last hebben van vermoeidheid."
    text_25 = "En ook van andere klachten zoals lymfoedeem of problemen met seksualiteit."
    text_26 = "Ook psychisch kun je het zwaar hebben."
    text_27 = "Ook kun je door de behandeling minder vruchtbaar of onvruchtbaar worden."


    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 72))

    text_surface_7 = font_T.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 92))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 122))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 132))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 142))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 152))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 162))

    text_surface_14 = font_T.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 182))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 202))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 212))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 222))

    text_surface_18 = font_T.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 242))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 262))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 272))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 282))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 292))

    text_surface_23 = font_T.render(text_23, True, (150, 230, 255))
    screen.blit(text_surface_23, (0, 312))
    text_surface_24 = font.render(text_24, True, (150, 230, 255))
    screen.blit(text_surface_24, (0, 332))
    text_surface_25 = font.render(text_25, True, (150, 230, 255))
    screen.blit(text_surface_25, (0, 342))
    text_surface_26 = font.render(text_26, True, (150, 230, 255))
    screen.blit(text_surface_26, (0, 352))
    text_surface_27 = font.render(text_27, True, (150, 230, 255))
    screen.blit(text_surface_27, (0, 362))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_8_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 500, 280
    imager = pygame.image.load("neuskanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 40, 305
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Symptomen bij keelkanker"
    text_2 = "Keelkanker geeft in het begin vage klachten."
    text_3 = "Zoals keelpijn, moeite met slikken en een opgezwollen klier in de hals."
    text_4 = "Pas later ontstaan er andere symptomen."
    text_5 = "Hierdoor wordt de ziekte vaak pas laat ontdekt."
    
    text_6 = "Oorzaken en risicofactoren van keelkanker"
    text_7 = "De belangrijkste risicofactoren voor keelkanker zijn roken,"
    text_8 = " veel alcohol drinken en een besmetting met het humaan papillomavirus (HPV)."
    text_9 = "Er zijn ook nog andere risicofactoren bekend."   

    text_10 = "Groeiwijze van keelkanker"
    text_11 = "Keelkanker ontstaat meestal in het slijmvlies van de keel."
    text_12 = "Als de tumor groter wordt, groeit deze door in de omliggende weefsels."
    text_13 = "Bijvoorbeeld naar de mondbodem, tong of het strottenhoofd."
    
    text_14 = "Cijfers over keelkanker"
    text_15 = "In Nederland kregen in 2021 kregen 892 mensen de diagnose  keelkanker."
    text_16 = "De meeste patiënten zijn mannen tussen de 55 en 75 jaar."
    text_17 = "Omdat keelkanker vaak pas laat ontdekt wordt, is de kans op genezing beperkt."
    text_18 = "Bij uitzaaiingen in de lymfeklieren in de hals is genezing vaak nog mogelijk."
    text_19 = "De kans op genezing is ook beter als de oorzaak van de keelkanker HPV is."
    text_20 = "Als er uitzaaiingen in andere organen zitten, dan is de kans op genezing erg klein."
    text_21 = "Na 5 jaar is ongeveer de helft van de patiënten in leven."

    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 72))

    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 92))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 112))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 122))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 132))

    text_surface_10 = font_T.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 152))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 182))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 192))

    text_surface_14 = font_T.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 212))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 232))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 242))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 252))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 262))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 272))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 282))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 292))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_12_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 500, 300
    imager = pygame.image.load("teelbalkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 40, 200
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "symptomen van teelbalkanker"
    text_2 = "Dit kunnen soms symptomen van zaadbalkanker zijn:"
    text_3 = "1. een dof, zwaar gevoel in je onderbuik, achter je balzak of in de balzak zelf"
    text_4 = "2. rugpijn"
    text_5 = "3. vermoeidheid of gewichtsverlies zonder aantoonbare reden"
    text_6 = "4. minder zin in seks"
    text_7 = "5. zwelling van de borstklier(en) of rond een van de tepels"
    
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 40 
    button_y = 100
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 72))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 82))

    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_7_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 500, 230
    imager = pygame.image.load("maagkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 40, 380
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Symptomen van maagkanker"
    text_2 = "In het begin heb je van maagkanker meestal weinig of geen klachten."
    text_3 = "Als de tumor in of door de maagwand groeit, kunnen wel klachten ontstaan, "
    text_4 = "zoals (stekende) pijn boven in de buik of rond het borstbeen,"
    text_5 = "afvallen, misselijkheid en/of braken"
    
    text_6 = "Oorzaken en risicofactoren van maagkanker"
    text_7 = "De precieze oorzaak van maagkanker is niet bekend"
    text_8 = "Een langdurige infectie met de Helicobacter pylori bacterie maakt de kans op maagkanker groter"
    text_9 = "Verder speelt leefstijl een belangrijke rol:"   
    text_10 = "roken, lange tijd dagelijks alcohol drinken"
    text_11 = " en veel rood of bewerkt vlees eten vergroten de kans op maagkanker."
    text_12 = "Ongeveer 4 op de 100 mensen met maagkanker krijgt de ziekte door een erfelijke aanleg."

    text_13 = "Soorten maagkanker"
    text_14 = "Bijna alle mensen met maagkanker hebben een adenocarcinoom."
    text_15 = "Deze tumor ontstaat uit de kliercellen van het slijmvlies aan de binnenkant van de maag."

    text_16 = "Uitzaaiingen van maagkanker"
    text_17 = "De kankercellen kunnen zich verspreiden via de lymfe."
    text_18 = "Ze komen dan eerst terecht in de lymfeklieren rond de maag."
    text_19 = "Via de lymfebanen kunnen de kankercellen later ook andere lymfekliergebieden in het lichaam bereiken."
    text_20 = "Kankercellen kunnen ook losraken van de tumor en zich in de buikholte verspreiden"
    text_21 = "Daar kunnen ze uitgroeien tot uitzaaiingen op het buikvlies."
    text_22 = "Ook via het bloed kunnen kankercellen zich verspreiden"
    text_23 = "Ze kunnen dan uitzaaien naar bijvoorbeeld de lever of de longen."

    text_24 = "Gevolgen van maagkanker"
    text_25 = "Na de behandeling kun je nog korte of lange tijd last hebben van vermoeidheid."
    text_26 = "En ook van problemen met eten en drinken,"
    text_27 = "problemen met je ontlasting of neuropathie. Ook psychisch kun je het zwaar hebben."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 72))

    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 92))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 112))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 122))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 132))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 142))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 152))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 172))

    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 192))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 202))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 212))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 222))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 232))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 242))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 252))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 262))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 272))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 282))
    text_surface_23 = font.render(text_23, True, (150, 230, 255))
    screen.blit(text_surface_23, (0, 302))

    text_surface_24 = font_T.render(text_24, True, (150, 230, 255))
    screen.blit(text_surface_24, (0, 322))
    text_surface_25 = font.render(text_25, True, (150, 230, 255))
    screen.blit(text_surface_25, (0, 342))
    text_surface_26 = font.render(text_26, True, (150, 230, 255))
    screen.blit(text_surface_26, (0, 352))
    text_surface_27 = font.render(text_27, True, (150, 230, 255))
    screen.blit(text_surface_27, (0, 362))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_11_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 290, 210
    imager = pygame.image.load("acute leukemie.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 50, 380
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Hoe ontstaat acute leukemie"
    text_2 = "Bij acute leukemie is er een aantal veranderingen (mutaties) ontstaan in het DNA van de stamcellen in het beenmerg."
    text_3 = "Hierdoor rijpen bepaalde jonge witte bloedcellen in het beenmerg niet uit, maar blijven kopieën van zichzelf maken: zogenaamde blasten."
    text_4 = " maar blijven kopieën van zichzelf maken: zogenaamde blasten."
    text_5 = "Gezonde cellen reageren op signalen vanuit de omgeving."
    text_6 = "Bijvoorbeeld het signaal om te stoppen met delen als er voldoende cellen zijn."
    text_7 = "De blasten reageren niet meer op deze signalen: ze delen ongecontroleerd."
    text_8 = "Hierdoor ontstaan heel veel abnormale witte bloedcellen in het beenmerg en meestal ook het bloed."
    text_9 = "De grote hoeveelheden abnormale witte bloedcellen hopen zich op in het beenmerg en verstoren de aanmaak van normale bloedcellen (rode bloedcellen,"   
    text_10 = "witte bloedcellen en bloedplaatjes). "
    text_11 = "Dit kan in korte tijd gebeuren: meestal in enkele weken."
    text_12 = "Later komen de abnormale witte bloedcellen in de bloedbaan en soms ook in de organen terecht."
    text_13 = "Die kunnen dan overvol raken met abnormale cellen."
    text_14 = "Dat is bijvoorbeeld te merken aan:"
    text_15 = "1. sterk verhoogd aantal witte bloedcellen in het bloed"
    text_16 = "3. vergrote lymfeklieren"
    text_17 = "2. vergrote milt"
    text_18 = "4. vergrote lever"

    text_19 = "B-cel of T-cel ALL"
    text_20 = "Acute lymfatische leukemie is onder te verdelen in 2 soorten: "
    text_21 = "1. B-cel-ALL"
    text_22 = "2. T-cel-ALL"
    text_23 = "B-cellen en T-cellen zijn een bepaald type witte bloedcel."
    text_24 = "B-cellen ontwikkelen zich in het beenmerg."
    text_25 = "Als ze volwassen zijn, komen ze in de bloedstroom terecht. "
    text_26 = "T-cellen ontwikkelen zich ook in het beenmerg,"
    text_27 = " maar verhuizen tijdens hun ontwikkeling naar de thymus ('zwezerik')."
    text_28 = "Met het bloed- en beenmergonderzoek bepaalt de arts of u B-cel-ALL hebt of T-cel-ALL."
    text_29 = "Dat is belangrijk om te weten omdat bij T-cel-ALL de lymfeklieren vaak vergroot zijn."
    text_30 = "Vooral de lymfeklieren tussen hart en longen."
    text_31 = " Dat kan benauwdheid veroorzaken."
    text_32 = "Soms is bestraling van deze lymfeklieren nodig om de benauwdheid te verhelpen."
    text_33 = "Verder is de behandeling van beide groepen hetzelfde."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 230
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 72))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 82))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 92))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 102))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 112))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 122))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 132))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 142))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 152))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 162))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 172))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 182))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 192))

    text_surface_19 = font_T.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 212))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 232))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 242))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 252))
    text_surface_23 = font.render(text_23, True, (150, 230, 255))
    screen.blit(text_surface_23, (0, 262))
    text_surface_24 = font.render(text_24, True, (150, 230, 255))
    screen.blit(text_surface_24, (0, 272))
    text_surface_25 = font.render(text_25, True, (150, 230, 255))
    screen.blit(text_surface_25, (0, 282))
    text_surface_26 = font.render(text_26, True, (150, 230, 255))
    screen.blit(text_surface_26, (0, 292))
    text_surface_27 = font.render(text_27, True, (150, 230, 255))
    screen.blit(text_surface_27, (0, 302))
    text_surface_28 = font.render(text_28, True, (150, 230, 255))
    screen.blit(text_surface_28, (0, 312))
    text_surface_29 = font.render(text_29, True, (150, 230, 255))
    screen.blit(text_surface_29, (0, 322))
    text_surface_30 = font.render(text_30, True, (150, 230, 255))
    screen.blit(text_surface_30, (0, 332))
    text_surface_31 = font.render(text_31, True, (150, 230, 255))
    screen.blit(text_surface_31, (0, 342))
    text_surface_32 = font.render(text_32, True, (150, 230, 255))
    screen.blit(text_surface_32, (0, 352))
    text_surface_33 = font.render(text_33, True, (150, 230, 255))
    screen.blit(text_surface_33, (0, 362))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_11_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 290, 210
    imager = pygame.image.load("acute leukemie.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 50, 380
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Hoe ontstaat acute leukemie"
    text_2 = "Bij acute leukemie is er een aantal veranderingen (mutaties) ontstaan in het DNA van de stamcellen in het beenmerg."
    text_3 = "Hierdoor rijpen bepaalde jonge witte bloedcellen in het beenmerg niet uit, maar blijven kopieën van zichzelf maken: zogenaamde blasten."
    text_4 = " maar blijven kopieën van zichzelf maken: zogenaamde blasten."
    text_5 = "Gezonde cellen reageren op signalen vanuit de omgeving."
    text_6 = "Bijvoorbeeld het signaal om te stoppen met delen als er voldoende cellen zijn."
    text_7 = "De blasten reageren niet meer op deze signalen: ze delen ongecontroleerd."
    text_8 = "Hierdoor ontstaan heel veel abnormale witte bloedcellen in het beenmerg en meestal ook het bloed."
    text_9 = "De grote hoeveelheden abnormale witte bloedcellen hopen zich op in het beenmerg en verstoren de aanmaak van normale bloedcellen (rode bloedcellen,"   
    text_10 = "witte bloedcellen en bloedplaatjes). "
    text_11 = "Dit kan in korte tijd gebeuren: meestal in enkele weken."
    text_12 = "Later komen de abnormale witte bloedcellen in de bloedbaan en soms ook in de organen terecht."
    text_13 = "Die kunnen dan overvol raken met abnormale cellen."
    text_14 = "Dat is bijvoorbeeld te merken aan:"
    text_15 = "1. sterk verhoogd aantal witte bloedcellen in het bloed"
    text_16 = "3. vergrote lymfeklieren"
    text_17 = "2. vergrote milt"
    text_18 = "4. vergrote lever"

    text_19 = "B-cel of T-cel ALL"
    text_20 = "Acute lymfatische leukemie is onder te verdelen in 2 soorten: "
    text_21 = "1. B-cel-ALL"
    text_22 = "2. T-cel-ALL"
    text_23 = "B-cellen en T-cellen zijn een bepaald type witte bloedcel."
    text_24 = "B-cellen ontwikkelen zich in het beenmerg."
    text_25 = "Als ze volwassen zijn, komen ze in de bloedstroom terecht. "
    text_26 = "T-cellen ontwikkelen zich ook in het beenmerg,"
    text_27 = " maar verhuizen tijdens hun ontwikkeling naar de thymus ('zwezerik')."
    text_28 = "Met het bloed- en beenmergonderzoek bepaalt de arts of u B-cel-ALL hebt of T-cel-ALL."
    text_29 = "Dat is belangrijk om te weten omdat bij T-cel-ALL de lymfeklieren vaak vergroot zijn."
    text_30 = "Vooral de lymfeklieren tussen hart en longen."
    text_31 = " Dat kan benauwdheid veroorzaken."
    text_32 = "Soms is bestraling van deze lymfeklieren nodig om de benauwdheid te verhelpen."
    text_33 = "Verder is de behandeling van beide groepen hetzelfde."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 230
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 72))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 82))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 92))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 102))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 112))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 122))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 132))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 142))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 152))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 162))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 172))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 182))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 192))

    text_surface_19 = font_T.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 212))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 232))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 242))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 252))
    text_surface_23 = font.render(text_23, True, (150, 230, 255))
    screen.blit(text_surface_23, (0, 262))
    text_surface_24 = font.render(text_24, True, (150, 230, 255))
    screen.blit(text_surface_24, (0, 272))
    text_surface_25 = font.render(text_25, True, (150, 230, 255))
    screen.blit(text_surface_25, (0, 282))
    text_surface_26 = font.render(text_26, True, (150, 230, 255))
    screen.blit(text_surface_26, (0, 292))
    text_surface_27 = font.render(text_27, True, (150, 230, 255))
    screen.blit(text_surface_27, (0, 302))
    text_surface_28 = font.render(text_28, True, (150, 230, 255))
    screen.blit(text_surface_28, (0, 312))
    text_surface_29 = font.render(text_29, True, (150, 230, 255))
    screen.blit(text_surface_29, (0, 322))
    text_surface_30 = font.render(text_30, True, (150, 230, 255))
    screen.blit(text_surface_30, (0, 332))
    text_surface_31 = font.render(text_31, True, (150, 230, 255))
    screen.blit(text_surface_31, (0, 342))
    text_surface_32 = font.render(text_32, True, (150, 230, 255))
    screen.blit(text_surface_32, (0, 352))
    text_surface_33 = font.render(text_33, True, (150, 230, 255))
    screen.blit(text_surface_33, (0, 362))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_2_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 600, 300
    imager = pygame.image.load("longkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 40, 300
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Symptomen van longkanker."
    text_2 = "Longkanker kan verschillende klachten geven."
    text_3 = "Klachten die het vaakst voorkomen zijn prikkelhoest,"
    text_4 = "bloed in opgehoest slijm en kortademigheid."
    text_5 = "Ga met dit soort klachten naar je huisarts."
    
    text_6 = "Oorzaken en risicofactoren bij longkanker"
    text_7 = "Roken is de belangrijkste risicofactor voor longkanker. "
    text_8 = "Ongeveer 85% van alle gevallen van longkanker komt door roken."
    text_9 = "Er zijn ook nog andere zaken die de kans op longkanker groter maken."
    
    text_10 = "Soorten longkanker"
    text_11 = "Er zijn verschillende soorten longkanker. "
    text_12 = "De belangrijkste zijn niet-kleincellige longkanker en kleincellige longkanker."
    text_13 = "Je hoort van je arts welke soort je hebt. "
    text_14 = "Meestal is het niet-kleincellige longkanker."
    text_15 = "De behandeling van deze soorten is verschillend."
    text_16 = " Ook de vooruitzichten zijn anders."

    text_17 = "Uitzaaiingen bij longkanker"
    text_18 = "Longkanker kan uitzaaien naar de lymfeklieren rondom de longen."
    text_19 = "Dan is er nog kans op genezing."
    text_20 = "Bij de helft van de mensen is de ziekte bij de diagnose al verder uitgezaaid."
    text_21 = "De kankercellen hebben zich dan verspreid naar andere delen van de long, lever, hersenen of botten."
    text_22 = "De behandeling richt zich op het remmen van de ziekte en het verlichten van klachten."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 82))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 122))
    text_surface_10 = font_T.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 142))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 162))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 172))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 182))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 192))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 202))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 212))
    text_surface_17 = font_T.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 222))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 242))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 252))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 262))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 272))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 282))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_6_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 350, 200
    imager = pygame.image.load("huidkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 430, 400
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Soorten huidkanker"
    text_2 = "Er zijn verschillende soorten huidkanker:"

    text_3 = "Basaalcelcarcinoom"
    text_4 = "Een basaalcelcarcinoom of basaalcelkanker is de meest voorkomende soort huidkanker"
    text_5 = "Dit is de minst gevaarlijke vorm van huidkanker."
    text_6 = "Deze vorm van huidkanker zaait bijna nooit uit."
    text_7 = "Wel moet hij behandeld worden omdat hij anders diep de huid kan groeien."

    text_8 = "Plaveiselcelcarcinoom"
    text_9 = "Ongeveer 15% van alle huidtumoren is een plaveiselcelcarcinoom of plaveiselcelkanker."
    text_10 = "Plaveiselcelcarcinomen kunnen uitzaaien"

    text_11 = "Melanoom"
    text_12 = "Ruim 12% van alle soorten huidkanker is melanoom."
    text_13 = "Een melanoom ontstaat meestal uit een 'gave' huid, maar kan ook ontstaan uit een bestaande moedervlek."
    text_14 = "Een melanoom zaait sneller uit dan andere vormen van huidkanker, omdat het een agressieve vorm van huidkanker is."

    text_15 = "Zeldzame vormen van huidkanker"
    text_16 = "Er zijn ook vormen van huidkanker die heel weinig voorkomen, zoals merkelcelcarcinoom,"
    text_17 = "talgkliercarcinoom en atypisch fibroxanthoom"

    text_18 = "Hoe herken je huidkanker?"
    text_19 = "Huidkanker komt het meest voor op plekken van het lichaam die veel in de zon komen zoals het gezicht, de romp, de handen, de armen en de benen."
    text_20 = "Elk soort huidkanker ziet er anders uit."
    text_21 = "Plaveiselcelcarcinoom en basaalcelcarcinoom zijn vaak bobbeltjes met een lichtere kleur, bijvoorbeeld bleekroze of rozerood."
    text_22 = "Een melanoom heeft vaak meerdere kleuren zoals verschillende tinten bruin of zwart, maar kan ook rood zijn."

    text_23 = "Hoe ontstaat huidkanker?"
    text_24 = "Huidkanker ontstaat meestal door uv-straling uit zonlicht of straling van de zonnebank."
    text_25 = "Maar ook andere dingen kunnen de kans op huidkanker vergroten zoals het huidtype of erfelijke factoren."
    text_26 = "De risicofactoren voor huidkanker verschillen per soort."

    text_27 = "Behandeling van huidkanker"
    text_28 = "Een operatie is de meest gegeven behandeling bij huidkanker."
    text_29 = "Dan snijdt de arts het plekje weg."
    text_30 = "Als dit niet kan of er uitzaaiingen zijn,"
    text_31 = " zijn er vaak andere behandelingen mogelijk."
    text_32 = "Veel basaalcelcarcinomen kunnen met een zalf behandeld worden."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 100
    button_y = 500
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))

    text_surface_3 = font_T.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 52))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 72))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 82))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 92))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))

    text_surface_8 = font_T.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 122))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 142))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 152))

    text_surface_11 = font_T.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 192))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 202))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 212))

    text_surface_15 = font_T.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 232))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 252))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 262))

    text_surface_18 = font_T.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 282))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 302))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 312))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 322))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 332))

    text_surface_23 = font_T.render(text_23, True, (150, 230, 255))
    screen.blit(text_surface_23, (0, 352))
    text_surface_24 = font.render(text_24, True, (150, 230, 255))
    screen.blit(text_surface_24, (0, 372))
    text_surface_25 = font.render(text_25, True, (150, 230, 255))
    screen.blit(text_surface_25, (0, 382))
    text_surface_26 = font.render(text_26, True, (150, 230, 255))
    screen.blit(text_surface_26, (0, 392))
    
    text_surface_27 = font.render(text_27, True, (150, 230, 255))
    screen.blit(text_surface_27, (0, 412))
    text_surface_28 = font.render(text_28, True, (150, 230, 255))
    screen.blit(text_surface_28, (0, 432))
    text_surface_29 = font.render(text_29, True, (150, 230, 255))
    screen.blit(text_surface_29, (0, 442))
    text_surface_30 = font.render(text_30, True, (150, 230, 255))
    screen.blit(text_surface_30, (0, 452))
    text_surface_31 = font.render(text_31, True, (150, 230, 255))
    screen.blit(text_surface_31, (0, 462))
    text_surface_32 = font.render(text_32, True, (150, 230, 255))
    screen.blit(text_surface_32, (0, 472))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_6_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 350, 200
    imager = pygame.image.load("huidkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 430, 400
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Soorten huidkanker"
    text_2 = "Er zijn verschillende soorten huidkanker:"

    text_3 = "Basaalcelcarcinoom"
    text_4 = "Een basaalcelcarcinoom of basaalcelkanker is de meest voorkomende soort huidkanker"
    text_5 = "Dit is de minst gevaarlijke vorm van huidkanker."
    text_6 = "Deze vorm van huidkanker zaait bijna nooit uit."
    text_7 = "Wel moet hij behandeld worden omdat hij anders diep de huid kan groeien."

    text_8 = "Plaveiselcelcarcinoom"
    text_9 = "Ongeveer 15% van alle huidtumoren is een plaveiselcelcarcinoom of plaveiselcelkanker."
    text_10 = "Plaveiselcelcarcinomen kunnen uitzaaien"

    text_11 = "Melanoom"
    text_12 = "Ruim 12% van alle soorten huidkanker is melanoom."
    text_13 = "Een melanoom ontstaat meestal uit een 'gave' huid, maar kan ook ontstaan uit een bestaande moedervlek."
    text_14 = "Een melanoom zaait sneller uit dan andere vormen van huidkanker, omdat het een agressieve vorm van huidkanker is."

    text_15 = "Zeldzame vormen van huidkanker"
    text_16 = "Er zijn ook vormen van huidkanker die heel weinig voorkomen, zoals merkelcelcarcinoom,"
    text_17 = "talgkliercarcinoom en atypisch fibroxanthoom"

    text_18 = "Hoe herken je huidkanker?"
    text_19 = "Huidkanker komt het meest voor op plekken van het lichaam die veel in de zon komen zoals het gezicht, de romp, de handen, de armen en de benen."
    text_20 = "Elk soort huidkanker ziet er anders uit."
    text_21 = "Plaveiselcelcarcinoom en basaalcelcarcinoom zijn vaak bobbeltjes met een lichtere kleur, bijvoorbeeld bleekroze of rozerood."
    text_22 = "Een melanoom heeft vaak meerdere kleuren zoals verschillende tinten bruin of zwart, maar kan ook rood zijn."

    text_23 = "Hoe ontstaat huidkanker?"
    text_24 = "Huidkanker ontstaat meestal door uv-straling uit zonlicht of straling van de zonnebank."
    text_25 = "Maar ook andere dingen kunnen de kans op huidkanker vergroten zoals het huidtype of erfelijke factoren."
    text_26 = "De risicofactoren voor huidkanker verschillen per soort."

    text_27 = "Behandeling van huidkanker"
    text_28 = "Een operatie is de meest gegeven behandeling bij huidkanker."
    text_29 = "Dan snijdt de arts het plekje weg."
    text_30 = "Als dit niet kan of er uitzaaiingen zijn,"
    text_31 = " zijn er vaak andere behandelingen mogelijk."
    text_32 = "Veel basaalcelcarcinomen kunnen met een zalf behandeld worden."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 100
    button_y = 500
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))

    text_surface_3 = font_T.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 52))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 72))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 82))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 92))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))

    text_surface_8 = font_T.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 122))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 142))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 152))

    text_surface_11 = font_T.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 192))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 202))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 212))

    text_surface_15 = font_T.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 232))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 252))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 262))

    text_surface_18 = font_T.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 282))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 302))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 312))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 322))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 332))

    text_surface_23 = font_T.render(text_23, True, (150, 230, 255))
    screen.blit(text_surface_23, (0, 352))
    text_surface_24 = font.render(text_24, True, (150, 230, 255))
    screen.blit(text_surface_24, (0, 372))
    text_surface_25 = font.render(text_25, True, (150, 230, 255))
    screen.blit(text_surface_25, (0, 382))
    text_surface_26 = font.render(text_26, True, (150, 230, 255))
    screen.blit(text_surface_26, (0, 392))
    
    text_surface_27 = font.render(text_27, True, (150, 230, 255))
    screen.blit(text_surface_27, (0, 412))
    text_surface_28 = font.render(text_28, True, (150, 230, 255))
    screen.blit(text_surface_28, (0, 432))
    text_surface_29 = font.render(text_29, True, (150, 230, 255))
    screen.blit(text_surface_29, (0, 442))
    text_surface_30 = font.render(text_30, True, (150, 230, 255))
    screen.blit(text_surface_30, (0, 452))
    text_surface_31 = font.render(text_31, True, (150, 230, 255))
    screen.blit(text_surface_31, (0, 462))
    text_surface_32 = font.render(text_32, True, (150, 230, 255))
    screen.blit(text_surface_32, (0, 472))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_2_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 600, 300
    imager = pygame.image.load("longkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 40, 300
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Symptomen van longkanker."
    text_2 = "Longkanker kan verschillende klachten geven."
    text_3 = "Klachten die het vaakst voorkomen zijn prikkelhoest,"
    text_4 = "bloed in opgehoest slijm en kortademigheid."
    text_5 = "Ga met dit soort klachten naar je huisarts."
    
    text_6 = "Oorzaken en risicofactoren bij longkanker"
    text_7 = "Roken is de belangrijkste risicofactor voor longkanker. "
    text_8 = "Ongeveer 85% van alle gevallen van longkanker komt door roken."
    text_9 = "Er zijn ook nog andere zaken die de kans op longkanker groter maken."
    
    text_10 = "Soorten longkanker"
    text_11 = "Er zijn verschillende soorten longkanker. "
    text_12 = "De belangrijkste zijn niet-kleincellige longkanker en kleincellige longkanker."
    text_13 = "Je hoort van je arts welke soort je hebt. "
    text_14 = "Meestal is het niet-kleincellige longkanker."
    text_15 = "De behandeling van deze soorten is verschillend."
    text_16 = " Ook de vooruitzichten zijn anders."

    text_17 = "Uitzaaiingen bij longkanker"
    text_18 = "Longkanker kan uitzaaien naar de lymfeklieren rondom de longen."
    text_19 = "Dan is er nog kans op genezing."
    text_20 = "Bij de helft van de mensen is de ziekte bij de diagnose al verder uitgezaaid."
    text_21 = "De kankercellen hebben zich dan verspreid naar andere delen van de long, lever, hersenen of botten."
    text_22 = "De behandeling richt zich op het remmen van de ziekte en het verlichten van klachten."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 82))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_9 = font.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 122))
    text_surface_10 = font_T.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 142))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 162))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 172))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 182))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 192))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 202))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 212))
    text_surface_17 = font_T.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 222))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 242))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 252))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 262))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 272))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 282))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_10_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 200, 300
    imager = pygame.image.load("botkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 550, 300
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Soorten botkanker"
    text_2 = "Botkanker is een verzamelnaam van verschillende vormen van botkanker."
    text_3 = "hier zijn een paar soorten botkanker:"
    text_4 = "1. Chondrosarcoom"
    text_5 = "2. Chordoom"
    text_6 = "3. Ewingsarcoom"
    text_7 = "4. Osteosarcoom"
    text_8 = "5. Adamantinoom"

    text_9 = "Goedaardige tumoren in het bot"
    text_10 = "Goedaardige tumoren in het bot komen ook voor."
    text_11 = "Deze tumoren heten geen botkanker."
    text_12 = "Sommige van deze tumoren groeien zo agressief dat er een behandeling nodig is."
    text_13 = "De behandeling lijkt soms op de behandeling van botkanker,"
    text_14 = "net als de gevolgen van de behandeling."
    text_15 = "Je krijgt deze behandeling van artsen uit een expertisecentrum voor botkanker."
    text_16 = "Een goedaardige tumor in het bot die vaak agressief groeit is reusceltumor in het bot."

    text_17 = "Botkanker of uitzaaiingen in de botten: wat is het verschil?"
    text_18 = "Als er kanker in de botten zit, "
    text_19 = "is dat meestal een uitzaaiing van een andere soort kanker."
    text_20 = "Bijvoorbeeld van prostaatkanker"
    text_21 = "De uitzaaiingen worden dan ook als prostaatkanker behandeld."
    text_22 = "Botkanker, waarbij de kanker in het bot zelf begint, komt veel minder vaak voor."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 72))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 82))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 92))

    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 112))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 132))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 142))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 152))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 162))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 172))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 182))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 192))

    text_surface_17 = font_T.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 212))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 232))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 242))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 252))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 262))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 272))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_10_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 200, 300
    imager = pygame.image.load("botkanker.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 550, 300
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Soorten botkanker"
    text_2 = "Botkanker is een verzamelnaam van verschillende vormen van botkanker."
    text_3 = "hier zijn een paar soorten botkanker:"
    text_4 = "1. Chondrosarcoom"
    text_5 = "2. Chordoom"
    text_6 = "3. Ewingsarcoom"
    text_7 = "4. Osteosarcoom"
    text_8 = "5. Adamantinoom"

    text_9 = "Goedaardige tumoren in het bot"
    text_10 = "Goedaardige tumoren in het bot komen ook voor."
    text_11 = "Deze tumoren heten geen botkanker."
    text_12 = "Sommige van deze tumoren groeien zo agressief dat er een behandeling nodig is."
    text_13 = "De behandeling lijkt soms op de behandeling van botkanker,"
    text_14 = "net als de gevolgen van de behandeling."
    text_15 = "Je krijgt deze behandeling van artsen uit een expertisecentrum voor botkanker."
    text_16 = "Een goedaardige tumor in het bot die vaak agressief groeit is reusceltumor in het bot."

    text_17 = "Botkanker of uitzaaiingen in de botten: wat is het verschil?"
    text_18 = "Als er kanker in de botten zit, "
    text_19 = "is dat meestal een uitzaaiing van een andere soort kanker."
    text_20 = "Bijvoorbeeld van prostaatkanker"
    text_21 = "De uitzaaiingen worden dan ook als prostaatkanker behandeld."
    text_22 = "Botkanker, waarbij de kanker in het bot zelf begint, komt veel minder vaak voor."
    # Render the text

    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 500
    button_y = 10
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    screen.blit(button_image, (button_x, button_y))
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 32))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 42))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 52))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 62))
    text_surface_6 = font.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 72))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 82))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 92))

    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 112))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 132))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 142))
    text_surface_12 = font.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 152))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 162))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 172))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 182))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 192))

    text_surface_17 = font_T.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 212))
    text_surface_18 = font.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 232))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 242))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 252))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 262))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 272))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    
    # Quit Pygame
    pygame.quit()

def extra_scherm_3_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 300, 200
    imager = pygame.image.load("stadia-dikke-darmkanker.jpg")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 460, 400
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    
    # Set the text
    text_1 = "Endeldarmkanker en dunnedarmkanker"
    text_2 = "Kanker in de darmen kan ook in andere delen van onze darmen ontstaan dan in de dikke darm."
    text_3 = "Bijvoorbeeld in de endeldarm of in de dunne darm."
    text_4 = "Als er een tumor ontstaat in de endeldarm, het eind van de dikke darm, dan heet de kanker endeldarmkanker."
    text_5 = "Ontstaat de tumor in de dunne darm, dan heet de kanker dunnedarmkanker."
    
    text_6 = "Vooruitzichten bij darmkanker"
    text_7 = "De prognose van darmkanker verschilt per persoon."
    text_8 = "Het maakt ook uit hoe ernstig de ziekte is: hoe groot de tumor is en of er uitzaaiingen zijn."
    text_8a = "Gemiddeld leven tien jaar na de diagnose dikkedarmkanker nog ongeveer 60 van de 100 mensen."
    
    text_9 = "Symptomen van darmkanker"
    text_10 = "Als je een tumor in je darmen hebt, kan dat allerlei klachten geven."
    text_11 = "Een van de symptomen van darmkanker is bloed of slijm bij je ontlasting."
    text_11a = "Soms heb je helemaal geen klachten, maar wordt darmkanker ontdekt door het bevolkingsonderzoek of een ander onderzoek."
    text_11b = "De meest voorkomende klachten bij darmkanker:"
    text_11c = "1. bloed en/of slijm in je ontlasting"
    text_11d = "2. een verandering in je ontlasting die niet overgaat"
    text_11e = "3. het gevoel dat je moet poepen, ook al moet je niet, of het gevoel dat de darm niet helemaal leeg is na het poepen"
    text_11f = "4. afvallen zonder reden"
    text_11g = "5. vermoeidheid die niet overgaat (vaak door bloedarmoede)"
    text_11h = "6. minder zin in eten"
    text_11i = "7. buikpijn of buikkramp"

    text_12 = "Oorzaken en risicofactoren van darmkanker"
    text_13 = "Er is niet één oorzaak van darmkanker."
    text_14 = "Vaak ontstaat darmkanker uit een poliep in de darmwand."
    text_15 = "Wel zijn er factoren die de kans op darmkanker kunnen vergroten,"
    text_16 = "zoals erfelijke aanleg voor darmkanker,"
    text_17 = " chronische darmontsteking, veel darmpoliepen en/of een ongezonde leefstijl."

    text_18 = "Behandelingen bij darmkanker"
    text_19 = "Personen tussen de 55 en 75 jaar krijgen een oproep voor het bevolkingsonderzoek darmkanker."
    text_20 = "Je kunt dan ontlasting opsturen om te laten onderzoeken of hier bloed in zit."
    text_21 = "Als prostaatkanker uitzaait, is dit meestal naar de botten en lymfeklieren."
    # Render the text
    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 10
    button_y = 400
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    screen.blit(button_image, (button_x, button_y))
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 26))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 36))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 46))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 56))
    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 82))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_8a = font.render(text_8a, True, (150, 230, 255))
    screen.blit(text_surface_8a, (0, 122))
    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 142))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 162))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_11a = font.render(text_11a, True, (150, 230, 255))
    screen.blit(text_surface_11a, (0, 182))
    text_surface_11b = font.render(text_11b, True, (150, 230, 255))
    screen.blit(text_surface_11b, (0, 192))
    text_surface_11c = font.render(text_11c, True, (150, 230, 255))
    screen.blit(text_surface_11c, (0, 202))
    text_surface_11d = font.render(text_11d, True, (150, 230, 255))
    screen.blit(text_surface_11d, (0, 212))
    text_surface_11e = font.render(text_11e, True, (150, 230, 255))
    screen.blit(text_surface_11e, (0, 222))
    text_surface_11f = font.render(text_11f, True, (150, 230, 255))
    screen.blit(text_surface_11f, (0, 232))
    text_surface_11g = font.render(text_11g, True, (150, 230, 255))
    screen.blit(text_surface_11g, (0, 242))
    text_surface_11h = font.render(text_11h, True, (150, 230, 255))
    screen.blit(text_surface_11h, (0, 252))
    text_surface_11i = font.render(text_11i, True, (150, 230, 255))
    screen.blit(text_surface_11i, (0, 262))
    text_surface_12 = font_T.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 272))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 292))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 302))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 312))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 322))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 332))
    text_surface_18 = font_T.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 342))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 362))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 372))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 382))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    # Quit Pygame
    pygame.quit()

def extra_scherm_3_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 300, 200
    imager = pygame.image.load("stadia-dikke-darmkanker.jpg")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 460, 400
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    
    # Set the text
    text_1 = "Endeldarmkanker en dunnedarmkanker"
    text_2 = "Kanker in de darmen kan ook in andere delen van onze darmen ontstaan dan in de dikke darm."
    text_3 = "Bijvoorbeeld in de endeldarm of in de dunne darm."
    text_4 = "Als er een tumor ontstaat in de endeldarm, het eind van de dikke darm, dan heet de kanker endeldarmkanker."
    text_5 = "Ontstaat de tumor in de dunne darm, dan heet de kanker dunnedarmkanker."
    
    text_6 = "Vooruitzichten bij darmkanker"
    text_7 = "De prognose van darmkanker verschilt per persoon."
    text_8 = "Het maakt ook uit hoe ernstig de ziekte is: hoe groot de tumor is en of er uitzaaiingen zijn."
    text_8a = "Gemiddeld leven tien jaar na de diagnose dikkedarmkanker nog ongeveer 60 van de 100 mensen."
    
    text_9 = "Symptomen van darmkanker"
    text_10 = "Als je een tumor in je darmen hebt, kan dat allerlei klachten geven."
    text_11 = "Een van de symptomen van darmkanker is bloed of slijm bij je ontlasting."
    text_11a = "Soms heb je helemaal geen klachten, maar wordt darmkanker ontdekt door het bevolkingsonderzoek of een ander onderzoek."
    text_11b = "De meest voorkomende klachten bij darmkanker:"
    text_11c = "1. bloed en/of slijm in je ontlasting"
    text_11d = "2. een verandering in je ontlasting die niet overgaat"
    text_11e = "3. het gevoel dat je moet poepen, ook al moet je niet, of het gevoel dat de darm niet helemaal leeg is na het poepen"
    text_11f = "4. afvallen zonder reden"
    text_11g = "5. vermoeidheid die niet overgaat (vaak door bloedarmoede)"
    text_11h = "6. minder zin in eten"
    text_11i = "7. buikpijn of buikkramp"

    text_12 = "Oorzaken en risicofactoren van darmkanker"
    text_13 = "Er is niet één oorzaak van darmkanker."
    text_14 = "Vaak ontstaat darmkanker uit een poliep in de darmwand."
    text_15 = "Wel zijn er factoren die de kans op darmkanker kunnen vergroten,"
    text_16 = "zoals erfelijke aanleg voor darmkanker,"
    text_17 = " chronische darmontsteking, veel darmpoliepen en/of een ongezonde leefstijl."

    text_18 = "Behandelingen bij darmkanker"
    text_19 = "Personen tussen de 55 en 75 jaar krijgen een oproep voor het bevolkingsonderzoek darmkanker."
    text_20 = "Je kunt dan ontlasting opsturen om te laten onderzoeken of hier bloed in zit."
    text_21 = "Als prostaatkanker uitzaait, is dit meestal naar de botten en lymfeklieren."
    # Render the text
    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 10
    button_y = 400
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    screen.blit(button_image, (button_x, button_y))
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 26))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 36))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 46))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 56))
    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 82))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_8a = font.render(text_8a, True, (150, 230, 255))
    screen.blit(text_surface_8a, (0, 122))
    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 142))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 162))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_11a = font.render(text_11a, True, (150, 230, 255))
    screen.blit(text_surface_11a, (0, 182))
    text_surface_11b = font.render(text_11b, True, (150, 230, 255))
    screen.blit(text_surface_11b, (0, 192))
    text_surface_11c = font.render(text_11c, True, (150, 230, 255))
    screen.blit(text_surface_11c, (0, 202))
    text_surface_11d = font.render(text_11d, True, (150, 230, 255))
    screen.blit(text_surface_11d, (0, 212))
    text_surface_11e = font.render(text_11e, True, (150, 230, 255))
    screen.blit(text_surface_11e, (0, 222))
    text_surface_11f = font.render(text_11f, True, (150, 230, 255))
    screen.blit(text_surface_11f, (0, 232))
    text_surface_11g = font.render(text_11g, True, (150, 230, 255))
    screen.blit(text_surface_11g, (0, 242))
    text_surface_11h = font.render(text_11h, True, (150, 230, 255))
    screen.blit(text_surface_11h, (0, 252))
    text_surface_11i = font.render(text_11i, True, (150, 230, 255))
    screen.blit(text_surface_11i, (0, 262))
    text_surface_12 = font_T.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 272))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 292))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 302))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 312))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 322))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 332))
    text_surface_18 = font_T.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 342))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 362))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 372))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 382))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    # Quit Pygame
    pygame.quit()

def extra_scherm_4_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 280, 220
    imager = pygame.image.load("alvleesklierkanker.jpg")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 440, 380
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    
    # Set the text
    text_1 = "Pancreascarcinoom of pancreaskanker"
    text_2 = "De medische term voor alvleesklierkanker is pancreascarcinoom."
    text_3 = "in 2021 kregen 2.931 mensen de diagnose alvleesklierkanker."
    text_4 = "De meeste mensen met alvleesklierkanker zijn ouder dan 60 jaar. "
    
    text_6 = "Soorten kanker in de alvleesklier"
    text_7 = "Bij alvleesklierkanker gaat het bijna altijd om een adenocarcinoom."
    text_8 = "Dat betekent dat de tumor in de afvoerbuisjes is ontstaan."
    text_8a = "Een adenocarcinoom kan overal in de alvleesklier ontstaan, maar zit meestal in de kop van de alvleesklier."
    text_8b = "Er zijn ook andere soorten kanker mogelijk in de alvleesklier."
    
    text_9 = "Klachten of symptomen van alvleesklierkanker"
    text_10 = "Alvleesklierkanker wordt meestal laat ontdekt"
    text_11 = "Dat komt doordat er vaak pas klachten ontstaan als de tumor in andere organen is gegroeid"
    text_11a = "De kanker is in veel gevallen dan ook al uitgezaaid."
    text_11b = "De klachten van alvleesklierkanker kunnen erg verschillen."
    text_11c = "Geelzucht is een van de klachten bij alvleesklierkanker."
    text_11d = "De oorzaak van geelzucht kan zijn dat de tumor de afvoerbuis dichtdrukt."
    text_11e = "De gal kan niet weg en komt uiteindelijk in het bloed."
    text_11f = "Bij geelzucht wordt het oogwit geel en is de huid grauwig of geel."
    text_11g = "Andere klachten bij alvleesklierkanker zijn bijvoorbeeld vettige ontlasting (vetdiarree), afvallen, een opgeblazen gevoel of pijn."

    text_12 = "Oorzaken en risicofactoren van alvleesklierkanker"
    text_13 = "Een precieze oorzaak van alvleesklierkanker is niet bekend. "
    text_14 = "Er zijn wel een aantal dingen die de kans op alvleesklierkanker vergroten."
    text_15 = "Door roken, veel alcoholgebruik, chronische ontsteking van de alvleesklier (chronische pancreatitis) en erfelijke aanleg is de kans groter op alvleesklierkanker."

    text_18 = "Uitzaaiingen van alvleesklierkanker"
    text_19 = "Meestal zaait alvleesklierkanker het eerst uit naar de lever, de lymfeklieren, de longen, de botten of de buikholte."
    # Render the text
    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 10
    button_y = 400
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    screen.blit(button_image, (button_x, button_y))
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 26))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 36))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 46))
    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 82))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_8a = font.render(text_8a, True, (150, 230, 255))
    screen.blit(text_surface_8a, (0, 122))
    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 142))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 162))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_11a = font.render(text_11a, True, (150, 230, 255))
    screen.blit(text_surface_11a, (0, 182))
    text_surface_11b = font.render(text_11b, True, (150, 230, 255))
    screen.blit(text_surface_11b, (0, 192))
    text_surface_11c = font.render(text_11c, True, (150, 230, 255))
    screen.blit(text_surface_11c, (0, 202))
    text_surface_11d = font.render(text_11d, True, (150, 230, 255))
    screen.blit(text_surface_11d, (0, 212))
    text_surface_11e = font.render(text_11e, True, (150, 230, 255))
    screen.blit(text_surface_11e, (0, 222))
    text_surface_11f = font.render(text_11f, True, (150, 230, 255))
    screen.blit(text_surface_11f, (0, 232))
    text_surface_11g = font.render(text_11g, True, (150, 230, 255))
    screen.blit(text_surface_11g, (0, 242))
    text_surface_12 = font_T.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 272))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 292))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 302))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 312))
    text_surface_18 = font_T.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 342))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 362))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    # Quit Pygame
    pygame.quit()

def extra_scherm_4_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 280, 220
    imager = pygame.image.load("alvleesklierkanker.jpg")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 440, 380
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    
    # Set the text
    text_1 = "Pancreascarcinoom of pancreaskanker"
    text_2 = "De medische term voor alvleesklierkanker is pancreascarcinoom."
    text_3 = "in 2021 kregen 2.931 mensen de diagnose alvleesklierkanker."
    text_4 = "De meeste mensen met alvleesklierkanker zijn ouder dan 60 jaar. "
    
    text_6 = "Soorten kanker in de alvleesklier"
    text_7 = "Bij alvleesklierkanker gaat het bijna altijd om een adenocarcinoom."
    text_8 = "Dat betekent dat de tumor in de afvoerbuisjes is ontstaan."
    text_8a = "Een adenocarcinoom kan overal in de alvleesklier ontstaan, maar zit meestal in de kop van de alvleesklier."
    text_8b = "Er zijn ook andere soorten kanker mogelijk in de alvleesklier."
    
    text_9 = "Klachten of symptomen van alvleesklierkanker"
    text_10 = "Alvleesklierkanker wordt meestal laat ontdekt"
    text_11 = "Dat komt doordat er vaak pas klachten ontstaan als de tumor in andere organen is gegroeid"
    text_11a = "De kanker is in veel gevallen dan ook al uitgezaaid."
    text_11b = "De klachten van alvleesklierkanker kunnen erg verschillen."
    text_11c = "Geelzucht is een van de klachten bij alvleesklierkanker."
    text_11d = "De oorzaak van geelzucht kan zijn dat de tumor de afvoerbuis dichtdrukt."
    text_11e = "De gal kan niet weg en komt uiteindelijk in het bloed."
    text_11f = "Bij geelzucht wordt het oogwit geel en is de huid grauwig of geel."
    text_11g = "Andere klachten bij alvleesklierkanker zijn bijvoorbeeld vettige ontlasting (vetdiarree), afvallen, een opgeblazen gevoel of pijn."

    text_12 = "Oorzaken en risicofactoren van alvleesklierkanker"
    text_13 = "Een precieze oorzaak van alvleesklierkanker is niet bekend. "
    text_14 = "Er zijn wel een aantal dingen die de kans op alvleesklierkanker vergroten."
    text_15 = "Door roken, veel alcoholgebruik, chronische ontsteking van de alvleesklier (chronische pancreatitis) en erfelijke aanleg is de kans groter op alvleesklierkanker."

    text_18 = "Uitzaaiingen van alvleesklierkanker"
    text_19 = "Meestal zaait alvleesklierkanker het eerst uit naar de lever, de lymfeklieren, de longen, de botten of de buikholte."
    # Render the text
    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 10
    button_y = 400
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    screen.blit(button_image, (button_x, button_y))
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 26))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 36))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 46))
    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 82))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_8a = font.render(text_8a, True, (150, 230, 255))
    screen.blit(text_surface_8a, (0, 122))
    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 142))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 162))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_11a = font.render(text_11a, True, (150, 230, 255))
    screen.blit(text_surface_11a, (0, 182))
    text_surface_11b = font.render(text_11b, True, (150, 230, 255))
    screen.blit(text_surface_11b, (0, 192))
    text_surface_11c = font.render(text_11c, True, (150, 230, 255))
    screen.blit(text_surface_11c, (0, 202))
    text_surface_11d = font.render(text_11d, True, (150, 230, 255))
    screen.blit(text_surface_11d, (0, 212))
    text_surface_11e = font.render(text_11e, True, (150, 230, 255))
    screen.blit(text_surface_11e, (0, 222))
    text_surface_11f = font.render(text_11f, True, (150, 230, 255))
    screen.blit(text_surface_11f, (0, 232))
    text_surface_11g = font.render(text_11g, True, (150, 230, 255))
    screen.blit(text_surface_11g, (0, 242))
    text_surface_12 = font_T.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 272))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 292))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 302))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 312))
    text_surface_18 = font_T.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 342))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 362))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    # Quit Pygame
    pygame.quit()

def extra_scherm_m_1():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 300, 200
    imager = pygame.image.load("prostaatkanker.jpg")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 390, 350
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    def create_button(x, y, width, height, inactive_color, active_color, text, text_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            pygame.draw.rect(window, active_color, (x, y, width, height))
            if click[0] == 1:
                print("Button clicked!")
                # Add your button click action here
        else:
            pygame.draw.rect(window, inactive_color, (x, y, width, height))

        # Draw button text
        font_B = pygame.font.Font(None, 36)
        text_surface_B = font.render(text, True, text_color)
        text_rect_B = text_surface_B.get_rect(center=(x + width / 2, y + height / 2))
        window.blit(text_surface_B, text_rect_B)


    text_1 = "Vooruitzichten bij prostaatkanker."
    text_2 = "Prostaatkanker is de meest voorkomende vorm van kanker bij mannen."
    text_3 = "lk jaar krijgen ongeveer 13.000 mannen de diagnose prostaatkanker."
    text_4 = "De ziekte komt vooral voor bij mannen boven de 65 jaar."
    text_5 = "Maar ook jongere mannen kunnen prostaatkanker krijgen."
    
    text_6 = "Symptomen van prostaatkanker"
    text_7 = "Prostaatkanker geeft in het begin vaak geen duidelijke klachten."
    text_8 = "De meeste mannen merken daardoor niet dat ze prostaatkanker hebben."
    
    text_9 = "Oorzaken en risicofactoren van prostaatkanker"
    text_10 = "Er is meestal geen duidelijke oorzaak van prostaatkanker aan te wijzen."
    text_11 = "Er zijn wel risicofactoren die de kans op prostaatkanker vergroten."

    text_12 = "Erfelijkheid en prostaatkanker"
    text_13 = "Prostaatkanker komt vaak voor."
    text_14 = "Als meer mannen in dezelfde familie prostaatkanker hebben, is dit meestal toeval"
    text_15 = "Bij de helft van de mensen is de ziekte bij de diagnose al verder uitgezaaid."
    text_16 = "Soms is een erfelijke aanleg de oorzaak van prostaatkanker"
    text_17 = "Dat is bij ongeveer 5-10% van de mannen met prostaatkanker zo"

    text_18 = "Uitzaaiingen bij prostaatkanker"
    text_19 = "Prostaatkanker groeit meestal langzaam."
    text_20 = "Vaak zaait het niet uit, of pas na jaren."
    text_21 = "Als prostaatkanker uitzaait, is dit meestal naar de botten en lymfeklieren."
    # Render the text
    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 10
    button_y = 400
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    screen.blit(button_image, (button_x, button_y))
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 26))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 36))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 46))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 56))
    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 82))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 132))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 152))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 162))
    text_surface_12 = font_T.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 182))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 202))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 212))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 222))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 232))
    text_surface_17 = font.render(text_17, True, (150, 230, 255))
    screen.blit(text_surface_17, (0, 242))
    text_surface_18 = font_T.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 252))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 282))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 292))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 302))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    # Quit Pygame
    pygame.quit()

def extra_scherm_5_m():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 300, 200
    imager = pygame.image.load("hersentumor.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 390, 350
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    def create_button(x, y, width, height, inactive_color, active_color, text, text_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            pygame.draw.rect(window, active_color, (x, y, width, height))
            if click[0] == 1:
                print("Button clicked!")
                # Add your button click action here
        else:
            pygame.draw.rect(window, inactive_color, (x, y, width, height))

        # Draw button text
        font_B = pygame.font.Font(None, 36)
        text_surface_B = font.render(text, True, text_color)
        text_rect_B = text_surface_B.get_rect(center=(x + width / 2, y + height / 2))
        window.blit(text_surface_B, text_rect_B)


    text_1 = "Goedaardige hersentumor"
    text_2 = "Een goedaardige hersentumor is meestal goed afgegrensd,"
    text_3 = "groeit langzaam en dringt niet door in het omliggende weefsel."
    text_4 = "De tumor zaait niet uit. "
    text_5 = "Een goedaardige tumor kan wel gevaarlijk zijn als deze in een belangrijk hersendeel zit."
    
    text_6 = "Kwaadaardige hersentumor (hersenkanker)"
    text_7 = "Een kwaadaardige hersentumor groeit snel en dringt wel door in het omliggende hersenweefsel."
    text_8 = "De tumor kan uitzaaien naar andere delen van de hersenen of het ruggenmerg."
    text_8a = "Een kwaadaardige hersentumor zaait heel zelden uit naar andere delen van het lichaam."
    
    text_9 = "Symptomen van een hersentumor"
    text_10 = "Een tumor in de hersenen kan invloed hebben op de werking van de hersenen en daardoor klachten geven."
    text_11 = "Dat geldt zowel voor kwaadaardige als goedaardige tumoren in de hersenen."
    text_11a = "Symptomen die veel voorkomen bij een tumor in het hoofd zijn:"
    text_11b = "1. aanhoudende hoofdpijn"
    text_11c = "2. verandering in verstandelijk vermogen en gedrag"
    text_11d = "3. uitvalsverschijnselen "
    text_11e = "4. epileptische aanvallen"
    text_11f = "Niet iedereen met een hersentumor heeft dezelfde symptomen."
    text_11g = "Welke klachten iemand heeft, hangt sterk af van:"
    text_11h = "de grootte van de tumor, de groeisnelheid en de plaats van de tumor in de hersenen."
    
    text_12 = "Primaire hersentumor of uitzaaiing in de hersenen. Wat is het verschil?"
    text_13 = "Wanneer de tumor ontstaat vanuit de hersenen of hersenvliezen heet het een primaire hersentumor."
    text_14 = "Vaak is het dan een glioom of een meningeoom, maar het kan ook een andere soort hersentumor zijn."
    text_15 = "Een tumor in de hersenen kan ook een uitzaaiing zijn van kanker ergens anders in het lichaam (bijvoorbeeld borst- of longkanker)."

    # Render the text
    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 10
    button_y = 400
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    screen.blit(button_image, (button_x, button_y))
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 26))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 36))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 46))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 56))
    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 82))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_8a = font.render(text_8a, True, (150, 230, 255))
    screen.blit(text_surface_8a, (0, 122))
    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 142))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 162))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_11a = font.render(text_11a, True, (150, 230, 255))
    screen.blit(text_surface_11a, (0, 182))
    text_surface_11b = font.render(text_11b, True, (150, 230, 255))
    screen.blit(text_surface_11b, (0, 192))
    text_surface_11c = font.render(text_11c, True, (150, 230, 255))
    screen.blit(text_surface_11c, (0, 202))
    text_surface_11d = font.render(text_11d, True, (150, 230, 255))
    screen.blit(text_surface_11d, (0, 212))
    text_surface_11e = font.render(text_11e, True, (150, 230, 255))
    screen.blit(text_surface_11e, (0, 222))
    text_surface_11f = font.render(text_11f, True, (150, 230, 255))
    screen.blit(text_surface_11f, (0, 232))
    text_surface_11g = font.render(text_11g, True, (150, 230, 255))
    screen.blit(text_surface_11g, (0, 242))
    text_surface_11h = font.render(text_11h, True, (150, 230, 255))
    screen.blit(text_surface_11h, (0, 252))
    text_surface_12 = font_T.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 272))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 292))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 302))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 312))

    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_man()
    # Quit Pygame
    pygame.quit()

def extra_scherm_5_v():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 300, 200
    imager = pygame.image.load("hersentumor.png")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 390, 350
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    def create_button(x, y, width, height, inactive_color, active_color, text, text_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            pygame.draw.rect(window, active_color, (x, y, width, height))
            if click[0] == 1:
                print("Button clicked!")
                # Add your button click action here
        else:
            pygame.draw.rect(window, inactive_color, (x, y, width, height))

        # Draw button text
        font_B = pygame.font.Font(None, 36)
        text_surface_B = font.render(text, True, text_color)
        text_rect_B = text_surface_B.get_rect(center=(x + width / 2, y + height / 2))
        window.blit(text_surface_B, text_rect_B)


    text_1 = "Goedaardige hersentumor"
    text_2 = "Een goedaardige hersentumor is meestal goed afgegrensd,"
    text_3 = "groeit langzaam en dringt niet door in het omliggende weefsel."
    text_4 = "De tumor zaait niet uit. "
    text_5 = "Een goedaardige tumor kan wel gevaarlijk zijn als deze in een belangrijk hersendeel zit."
    
    text_6 = "Kwaadaardige hersentumor (hersenkanker)"
    text_7 = "Een kwaadaardige hersentumor groeit snel en dringt wel door in het omliggende hersenweefsel."
    text_8 = "De tumor kan uitzaaien naar andere delen van de hersenen of het ruggenmerg."
    text_8a = "Een kwaadaardige hersentumor zaait heel zelden uit naar andere delen van het lichaam."
    
    text_9 = "Symptomen van een hersentumor"
    text_10 = "Een tumor in de hersenen kan invloed hebben op de werking van de hersenen en daardoor klachten geven."
    text_11 = "Dat geldt zowel voor kwaadaardige als goedaardige tumoren in de hersenen."
    text_11a = "Symptomen die veel voorkomen bij een tumor in het hoofd zijn:"
    text_11b = "1. aanhoudende hoofdpijn"
    text_11c = "2. verandering in verstandelijk vermogen en gedrag"
    text_11d = "3. uitvalsverschijnselen "
    text_11e = "4. epileptische aanvallen"
    text_11f = "Niet iedereen met een hersentumor heeft dezelfde symptomen."
    text_11g = "Welke klachten iemand heeft, hangt sterk af van:"
    text_11h = "de grootte van de tumor, de groeisnelheid en de plaats van de tumor in de hersenen."
    
    text_12 = "Primaire hersentumor of uitzaaiing in de hersenen. Wat is het verschil?"
    text_13 = "Wanneer de tumor ontstaat vanuit de hersenen of hersenvliezen heet het een primaire hersentumor."
    text_14 = "Vaak is het dan een glioom of een meningeoom, maar het kan ook een andere soort hersentumor zijn."
    text_15 = "Een tumor in de hersenen kan ook een uitzaaiing zijn van kanker ergens anders in het lichaam (bijvoorbeeld borst- of longkanker)."

    # Render the text
    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 10
    button_y = 400
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    screen.blit(button_image, (button_x, button_y))
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 26))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 36))
    text_surface_4 = font.render(text_4, True, (150, 230, 255))
    screen.blit(text_surface_4, (0, 46))
    text_surface_5 = font.render(text_5, True, (150, 230, 255))
    screen.blit(text_surface_5, (0, 56))
    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 82))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 102))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 112))
    text_surface_8a = font.render(text_8a, True, (150, 230, 255))
    screen.blit(text_surface_8a, (0, 122))
    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 142))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 162))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 172))
    text_surface_11a = font.render(text_11a, True, (150, 230, 255))
    screen.blit(text_surface_11a, (0, 182))
    text_surface_11b = font.render(text_11b, True, (150, 230, 255))
    screen.blit(text_surface_11b, (0, 192))
    text_surface_11c = font.render(text_11c, True, (150, 230, 255))
    screen.blit(text_surface_11c, (0, 202))
    text_surface_11d = font.render(text_11d, True, (150, 230, 255))
    screen.blit(text_surface_11d, (0, 212))
    text_surface_11e = font.render(text_11e, True, (150, 230, 255))
    screen.blit(text_surface_11e, (0, 222))
    text_surface_11f = font.render(text_11f, True, (150, 230, 255))
    screen.blit(text_surface_11f, (0, 232))
    text_surface_11g = font.render(text_11g, True, (150, 230, 255))
    screen.blit(text_surface_11g, (0, 242))
    text_surface_11h = font.render(text_11h, True, (150, 230, 255))
    screen.blit(text_surface_11h, (0, 252))
    text_surface_12 = font_T.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 272))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 292))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 302))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 312))

    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    # Quit Pygame
    pygame.quit()

def extra_scherm_v_1():
    # Initialize Pygame
    pygame.init()
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Load the image
    new_size = 400, 250
    imager = pygame.image.load("baarmoederhalskanker.jpg")
    image = pygame.transform.scale(imager, new_size)
    
    new_image_pos = 390, 330
    # Set the font and font size
    font = pygame.font.Font(None, 20)
    font_T = pygame.font.Font(None, 30)
    # Set the text
    text_1 = "Vooruitzichten bij baarmoederhalskanker"
    text_2 = "De vooruitzichten bij baarmoederhalskanker hangen af van hoe uitgebreid de tumor is, en of er uitzaaiingen zijn."
    text_3 = "Aan je arts kun je vragen wat je vooruitzichten zijn."
    
    text_6 = "Symptomen van baarmoederhalskanker"
    text_7 = "Baarmoederhalskanker ontstaat heel langzaam."
    text_8 = "In het begin zijn er vaak geen klachten. De eerste symptomen zijn meestal:"
    text_8a = "1. bloedverlies na het vrijen"
    text_8b = "2. bloedverlies tussen de menstruaties door"
    text_8c = "3. afscheiding die er anders uitziet dan je gewend bent"
    
    text_9 = "Oorzaken en risicofactoren van baarmoederhalskanker"
    text_10 = "Baarmoederhalskanker ontstaat meestal door een jarenlange infectie met het humaan papillomavirus (HPV)."
    text_11 = "Dit virus komt vaak voor. Bij sommige vrouwen kan het virus een voorstadium van baarmoederhalskanker veroorzaken. "
    #geen titel
    text_12 = "Het voorstadium van baarmoederhalskanker heet CIN."
    text_13 = "Bij CIN wijken de cellen in het slijmvlies van de baarmoederhals af van normale cellen."
    text_14 = "De afwijkende cellen kunnen uiteindelijk in kankercellen veranderen."
    text_15 = "Meestal gebeurt dit niet en ruimt het lichaam de afwijkende cellen zelf op. "
    text_16 = "Baarmoederhalskanker is niet erfelijk. Het is ook niet besmettelijk."

    text_18 = "Baarmoederhalskanker en baarmoederkanker: wat is het verschil?"
    text_19 = "Baarmoederhalskanker is een andere ziekte dan baarmoederkanker."
    text_20 = "Het ontstaat namelijk in een ander deel van de baarmoeder."
    text_21 = "Baarmoederhalskanker ontstaat in het onderste, smalle deel van de baarmoeder."
    text_22 = "Baarmoederkanker ontstaat in het brede deel van de baarmoeder: het baarmoederlichaam."
    # Render the text
    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 10
    button_y = 400
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    screen.blit(button_image, (button_x, button_y))
    button_image = pygame.image.load("button_ga-terug.png")  # Replace with the path to your button image
    button_x = 10
    button_y = 400
    def is_button_clicked(mouse_pos):
        button_rect = button_image.get_rect()
        button_rect.x = button_x
        button_rect.y = button_y
        return button_rect.collidepoint(mouse_pos)
    screen.blit(button_image, (button_x, button_y))
    # Blit the image and text to the screen
    screen.blit(image, new_image_pos)
    #blit the text
    text_surface_1 = font_T.render(text_1, True, (150, 230, 255))
    screen.blit(text_surface_1, (0, 10))
    text_surface_2 = font.render(text_2, True, (150, 230, 255))
    screen.blit(text_surface_2, (0, 26))
    text_surface_3 = font.render(text_3, True, (150, 230, 255))
    screen.blit(text_surface_3, (0, 36))

    text_surface_6 = font_T.render(text_6, True, (150, 230, 255))
    screen.blit(text_surface_6, (0, 52))
    text_surface_7 = font.render(text_7, True, (150, 230, 255))
    screen.blit(text_surface_7, (0, 72))
    text_surface_8 = font.render(text_8, True, (150, 230, 255))
    screen.blit(text_surface_8, (0, 82))
    text_surface_8a = font.render(text_8a, True, (150, 230, 255))
    screen.blit(text_surface_8a, (0, 92))
    text_surface_8b = font.render(text_8b, True, (150, 230, 255))
    screen.blit(text_surface_8b, (0, 102))
    text_surface_8c = font.render(text_8c, True, (150, 230, 255))
    screen.blit(text_surface_8c, (0, 112))
    text_surface_9 = font_T.render(text_9, True, (150, 230, 255))
    screen.blit(text_surface_9, (0, 132))
    text_surface_10 = font.render(text_10, True, (150, 230, 255))
    screen.blit(text_surface_10, (0, 152))
    text_surface_11 = font.render(text_11, True, (150, 230, 255))
    screen.blit(text_surface_11, (0, 162))
    text_surface_12 = font_T.render(text_12, True, (150, 230, 255))
    screen.blit(text_surface_12, (0, 182))
    text_surface_13 = font.render(text_13, True, (150, 230, 255))
    screen.blit(text_surface_13, (0, 202))
    text_surface_14 = font.render(text_14, True, (150, 230, 255))
    screen.blit(text_surface_14, (0, 212))
    text_surface_15 = font.render(text_15, True, (150, 230, 255))
    screen.blit(text_surface_15, (0, 222))
    text_surface_16 = font.render(text_16, True, (150, 230, 255))
    screen.blit(text_surface_16, (0, 232))

    text_surface_18 = font_T.render(text_18, True, (150, 230, 255))
    screen.blit(text_surface_18, (0, 262))
    text_surface_19 = font.render(text_19, True, (150, 230, 255))
    screen.blit(text_surface_19, (0, 282))
    text_surface_20 = font.render(text_20, True, (150, 230, 255))
    screen.blit(text_surface_20, (0, 292))
    text_surface_21 = font.render(text_21, True, (150, 230, 255))
    screen.blit(text_surface_21, (0, 302))
    text_surface_22 = font.render(text_22, True, (150, 230, 255))
    screen.blit(text_surface_22, (0, 312))
    # Update the display
    pygame.display.update()
    # Run the game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if is_button_clicked(mouse_pos):
                        andere_vrouw()
    # Quit Pygame
    pygame.quit()

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
        screen.blit(sprite_image_resized, (sprite_x, sprite_y))
        knoppen_man()
        # Update the display
        pygame.display.update()
    # Quit Pygame
    pygame.quit()

def andere_vrouw():
    import pygame
    pygame.init()
    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Resizable Image and Buttons")
    # Set up the background
    background_color = (255, 255, 255)
    screen.fill(background_color)
    # Load the image and sprite
    new_size = 350, 600
    imager = pygame.image.load("achtergrond vrouw.png")
    image = pygame.transform.scale(imager, new_size)
    new_position = 250, 1
    class Button:
        def __init__(self, x, y, width, height, image_path):
            self.rect = pygame.Rect(x, y, width, height)
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))    
        def draw(self, surface):
            surface.blit(self.image, self.rect)
        def is_clicked(self, pos):
            return self.rect.collidepoint(pos)
    button1 = Button(415, 270, 20, 35, '! (1).png')
    button2 = Button(425, 150, 20, 35, '! (2).png')
    button3 = Button(385, 240, 20, 35, '! (3).png')
    button4 = Button(465, 240, 20, 35, '! (4).png')
    button5 = Button(425, 30, 20, 35, '! (5).png')
    button6 = Button(330, 180, 20, 35, '! (6).png')
    button7 = Button(425, 220, 20, 35, '! (7).png')
    button8 = Button(425, 100, 20, 35, '! (8).png')
    button9 = Button(390, 190, 20, 35, '! (9).png')
    button10 = Button(360, 130, 20, 35, '! (10).png')
    button11 = Button(360, 200, 20, 35, '! (11).png')
    button12 = Button(435, 270, 20, 35, '! (12).png') 
    button13 = Button(200, 100, 20, 35, '! (13).png') 
    # Add buttons to a list
    buttons = [button1, button2, button3, button4,
               button5, button6, button7, button8,
               button9, button10, button11, button12, button13]  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                size = (event.w, event.h)
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(pygame.mouse.get_pos()):
                        if button == button1:
                            extra_scherm_v_1()
                        elif button == button2:
                            extra_scherm_2_v()
                        elif button == button3:
                            extra_scherm_3_v()
                        elif button == button4:
                            extra_scherm_4_v()
                        elif button == button5:
                            extra_scherm_5_v()
                        elif button == button6:
                            extra_scherm_6_v()
                        elif button == button7:
                            extra_scherm_7_v()
                        elif button == button8:
                            extra_scherm_8_v()
                        elif button == button9:
                            extra_scherm_9_v()
                        elif button == button10:
                            extra_scherm_10_v()
                        elif button == button11:
                            extra_scherm_11_v()
                        elif button == button12:
                            extra_scherm_12_v()
                        elif button == button13:
                            extra_scherm_13_v()
        screen.blit(image, new_position)
        for button in buttons:
            button.draw(screen)

        # Update the display
        pygame.display.flip()
    # Quit pygame properly
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
                    andere_man()
                elif button2_x < mouse_x < button2_x + button2_image.get_width() and \
                     button2_y < mouse_y < button2_y + button2_image.get_height():
                    andere_vrouw()
        # Draw the screen
        draw_buttons()
        pygame.display.update()
import pygame

# Define button class
class Button:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, self.rect)
def knoppen_man():
    import pygame
    # Define button class
    class Button:
        def __init__(self, image, x, y, function):
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.function = function
        def draw(self, surface):
            surface.blit(self.image, self.rect)
        def click(self):
            self.function()
    # Initialize Pygame
    pygame.init()
    # Set screen dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Create buttons
    button_images = ["! (1).png", "! (2).png", "! (3).png", "! (4).png", "! (5).png", "! (6).png", "! (7).png", "! (8).png", "! (9).png", "! (10).png", "! (11).png", "! (12).png", "! (13).png"]
    button_functions = [button1_function, button2_function, button3_function, button4_function, button5_function, button6_functon, button7_function, button8_function, button9_function, button10_function, button11_function, button12_function, button13_function]
    buttons = []
    for i in range(len(button_images)):
        button = Button(button_images[i], 50 + (i % 7) * 100, 50 + (i // 7) * 100, button_functions[i])
        buttons.append(button)
    # Define button functions
    def button1_function():
        print("Button 1 clicked.")
    def button2_function():
        print("Button 2 clicked.")
    def button3_function():
        print("Button 3 clicked.")
    def button4_function():
        print("Button 4 clicked.")
    def button5_function():
        print("Button 5 clicked.")
    def button6_functon():
        print("Button 6 clicked.")
    def button7_function():
        print("Button 7 clicked.")
    def button8_function():
        print("Button 8 clicked.")
    def button9_function():
        print("Button 9 clicked.")
    def button10_function():
        print("Button 10 clicked.")
    def button11_function():
        print("Button 11 clicked.")
    def button12_function():
        print("Button 12 clicked.")
    def button13_function():
        print("Button 13 clicked.")
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        button.click()
        # Draw buttons on screen
        for button in buttons:
            button.draw(screen)
        # Update display
        pygame.display.update()
    # Quit Pygame
    pygame.quit()



main_scherm()