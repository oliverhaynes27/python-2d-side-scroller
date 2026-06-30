import pygame
import os
import math
import random
from os import listdir
from os.path import isfile, join
pygame.init()
# Initialising Pygame and initialising elements to be used later within the code
# Importing and initialising Pygame
main_menu = True
screen_width = 1500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
goback = True
Music = True
LevelSelectorMusic = False
global Count
Count = 0
global life_count 
life_count = 3
# Defining Key Variables for buttons, music, counts and the game's overall screen size 

pygame.display.set_caption("Velocity - Main Menu")
main_font = pygame.font.SysFont("Arial black", 50)
sub_font = pygame.font.SysFont("Arial black", 25)
# Setting game name and default fonts that will be used for text (If later required)

main_menu_background = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/MainMenu.png')
# Loading the Main Menu Background Image

level_selector_background = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/LevelSelector.png')
# Loading the Level Selector Image

options_background = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/No Icons.png')
# Loading the Level Selector Background Image

controls = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Controls.png')
# Loading the controls image

Lives = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Official NEA Resources/Levels - Prototypes + Videos/assets/General/Heart/Heart2.png')
# Loading the Heart Image

CoinImage = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Official NEA Resources/Levels - Prototypes + Videos/assets/General/Coins/CoinImage.png')
# Loading the Coin Image

def Pause_Game():
# Defining the Pause_Game() function
    if Music == True:
    # If Music variable is equal to True
        pygame.mixer.music.pause()
        # Current music is paused
    Pause = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Pause Menu.png')
    # Defining the Pause variable to load the paused image (The Pause Menu screen)
    screen.blit((Pause), (200,125))
    # Blitting the Pause Menu to the screen
    pause_status = True
    # While the game is in a paused state (When the pause_status variable equals to True)
    while pause_status:
    # While the program is in the pause state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                pygame.quit()
                # The game will be exited / quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                # If the player has pressed the Enter (Return) Key
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the player has pressed the right mouse key
                if UnPause.checkForInputUnpause(pygame.mouse.get_pos()):
                # If the UnPause button returns True (From being pressed by the player)
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
                level.checkForInputlevel(pygame.mouse.get_pos())
                # Level Button will be checked for inputs
                restart.checkForInputRestart(pygame.mouse.get_pos())
                # Restart Button will be checked for inputs

        UnPause.update()
        level.update()
        restart.update()
        # All 3 buttons will be updated, following any inputs from the player
                    
        pygame.display.update()
pygame.display.update()
# Updating and quitting the game

def Pause_Game2():
# Defining the Pause_Game2() function
    if Music == True:
    # If Music variable is equal to True
        pygame.mixer.music.pause()
        # Current music is paused
    Pause = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Pause Menu.png')
    # Defining the Pause variable to load the paused image (The Pause Menu screen)
    screen.blit((Pause), (200,125))
    # Blitting the Pause Menu to the screen
    pause_status = True
    # While the game is in a paused state (When the pause_status variable equals to True)
    while pause_status:
    # While the program is in the pause state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                pygame.quit()
                # The game will be exited / quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                # If the player has pressed the Enter (Return) Key
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the player has pressed the right mouse key
                if UnPause.checkForInputUnpause(pygame.mouse.get_pos()):
                # If the UnPause button returns True (From being pressed by the player)
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
                level.checkForInputlevel(pygame.mouse.get_pos())
                # Level Button will be checked for inputs
                restart.checkForInputRestart2(pygame.mouse.get_pos())
                # Restart2 Button will be checked for inputs

        UnPause.update()
        level.update()
        restart.update()
        # All 3 buttons will be updated, following any inputs from the player
                    
        pygame.display.update()
pygame.display.update()
# Updating and quitting the game

def Pause_Game3():
# Defining the Pause_Game3() function
    if Music == True:
    # If Music variable is equal to True
        pygame.mixer.music.pause()
        # Current music is paused
    Pause = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Pause Menu.png')
    # Defining the Pause variable to load the paused image (The Pause Menu screen)
    screen.blit((Pause), (200,125))
    # Blitting the Pause Menu to the screen
    pause_status = True
    # While the game is in a paused state (When the pause_status variable equals to True)
    while pause_status:
    # While the program is in the pause state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                pygame.quit()
                # The game will be exited / quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                # If the player has pressed the Enter (Return) Key
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the player has pressed the right mouse key
                if UnPause.checkForInputUnpause(pygame.mouse.get_pos()):
                # If the UnPause button returns True (From being pressed by the player)
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
                level.checkForInputlevel(pygame.mouse.get_pos())
                # Level Button will be checked for inputs
                restart.checkForInputRestart3(pygame.mouse.get_pos())
                # Restart3 Button will be checked for inputs

        UnPause.update()
        level.update()
        restart.update()
        # All 3 buttons will be updated, following any inputs from the player
                    
        pygame.display.update()
pygame.display.update()
# Updating and quitting the game

def Pause_Game4():
# Defining the Pause_Game4() function
    if Music == True:
    # If Music variable is equal to True
        pygame.mixer.music.pause()
        # Current music is paused
    Pause = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Pause Menu.png')
    # Defining the Pause variable to load the paused image (The Pause Menu screen)
    screen.blit((Pause), (200,125))
    # Blitting the Pause Menu to the screen
    pause_status = True
    # While the game is in a paused state (When the pause_status variable equals to True)
    while pause_status:
    # While the program is in the pause state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                pygame.quit()
                # The game will be exited / quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                # If the player has pressed the Enter (Return) Key
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the player has pressed the right mouse key
                if UnPause.checkForInputUnpause(pygame.mouse.get_pos()):
                # If the UnPause button returns True (From being pressed by the player)
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
                level.checkForInputlevel(pygame.mouse.get_pos())
                # Level Button will be checked for inputs
                restart.checkForInputRestart4(pygame.mouse.get_pos())
                # Restart4 Button will be checked for inputs

        UnPause.update()
        level.update()
        restart.update()
        # All 3 buttons will be updated, following any inputs from the player
                    
        pygame.display.update()
pygame.display.update()
# Updating and quitting the game

def Pause_Game5():
# Defining the Pause_Game5() function
    if Music == True:
    # If Music variable is equal to True
        pygame.mixer.music.pause()
        # Current music is paused
    Pause = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Pause Menu.png')
    # Defining the Pause variable to load the paused image (The Pause Menu screen)
    screen.blit((Pause), (200,125))
    # Blitting the Pause Menu to the screen
    pause_status = True
    # While the game is in a paused state (When the pause_status variable equals to True)
    while pause_status:
    # While the program is in the pause state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                pygame.quit()
                # The game will be exited / quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                # If the player has pressed the Enter (Return) Key
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the player has pressed the right mouse key
                if UnPause.checkForInputUnpause(pygame.mouse.get_pos()):
                # If the UnPause button returns True (From being pressed by the player)
                    pause_status = False
                    # The pause_status variable is equal to False; ending the while loop
                    if Music == True:
                    # If the Music variable is equal to True
                        pygame.mixer.music.unpause()
                        # The Music is unpaused, when the player presses the enter key 
                level.checkForInputlevel(pygame.mouse.get_pos())
                # Level Button will be checked for inputs
                restart.checkForInputRestart5(pygame.mouse.get_pos())
                # Restart5 Button will be checked for inputs

        UnPause.update()
        level.update()
        restart.update()
        # All 3 buttons will be updated, following any inputs from the player
                    
        pygame.display.update()
pygame.display.update()
# Updating and quitting the game

def PlayMusic(Music):
# PlayMusic function is defined, to play music when not muted
    if Music == True:
    # If Variable Music is true
        pygame.mixer.music.unpause()
        # Current Music track will play (be unpaused)

def PauseMusic(Music):
# PauseMusic function is defined, to pause music when muted
    if Music == False:
    # If Variable Music is False
        pygame.mixer.music.pause()
        # Current Music track will stop (be paused)

def play(Music):
# Function, for when the play button is selected
        global Count
        Count = 0
        # Setting Count globally to 0, when the Level Selector Screen is loaded
        if Music == True:
        # If the Music variable is equal to True
            PauseMusic(Music)
            # Main Menu music is paused
            pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/LevelSelectorMusic.mp3")
            # Level Selector Music is loaded
            pygame.mixer.music.play(-1)
            # Music track is looped indefinitely
            PlayMusic(Music)
            # PlayMusic function is called
            global LevelSelectorMusic
            # LevelSelectorMusic variable set to a global variable
            LevelSelectorMusic = True
            # LevelSelectorMusic set to True
        else:
        # If the Music Variable is equal to False
            PauseMusic(Music)
            # PlayMusic function is called
            pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/LevelSelectorMusic.mp3")
            pygame.mixer.music.play(-1)
            # Level Selector Music is loaded and looped
            PauseMusic(Music)
            # Music is paused
        play=True
        # play variable set to True
        pygame.display.set_caption("Velocity - Level Selector")
        # Setting the caption of the Pygame Window, to: 'Velocity - Level Selector'
        screen.blit((level_selector_background), (0, 0))
        # Blitting the level selector background over the top of the Main Menu Screen (Illusion of replacing it, for the player)
        pygame.display.update()
        # Updating the display with the new background

        while play:
        # While the program is in the play state
            for event in pygame.event.get():
            # For loop for any event to take place in the game
                if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                    pygame.quit()
                    # The game will quit (end)
                if event.type == pygame.MOUSEBUTTONDOWN:
                # if the player has pressed the right mouse button down
                    level1.checkForInputLevel1(pygame.mouse.get_pos())
                    # The first level of the game will be loaded, if the level 1 button is selected
                    level2.checkForInputLevel2(pygame.mouse.get_pos())
                    # The second level of the game will be loaded, if the level 2 button is selected
                    level3.checkForInputLevel3(pygame.mouse.get_pos())
                    # The third level of the game will be loaded, if the level 3 button is selected
                    level4.checkForInputLevel4(pygame.mouse.get_pos())
                    # The fourth level of the game will be loaded, if the level 4 button is selected
                    level5.checkForInputLevel5(pygame.mouse.get_pos())
                    # The fifth level of the game will be loaded, if the level 5 button is selected
                    backbutton.checkForInputBackSelector(pygame.mouse.get_pos())
                    # Checking if the back button has been pressed
                   
            backbutton.update()
            level1.update()
            level2.update()
            level3.update()
            level4.update()
            level5.update()
            # Allows the player to load the level, over the top of the previous level selector screen
                    
            pygame.display.update()
        pygame.quit()
        # Update and quitting pygame modules

def options():
# Defining the options() function, to load the Options Menu

    options = True
    # options variable set to true

    pygame.display.set_caption("Velocity - Options Menu")
    # Setting the caption of the Pygame Window, to: 'Velocity Options Menu'
    screen.blit((options_background), (0, 0))
    # Blitting the options background over the top of the Main Menu Screen (Illusion of replacing it, for the player)
    screen.blit((controls), (500, 400))
    # Blitting the controls image to the screen, in specific coordinates

    text = main_font.render("Controls", True, "white")
    # Creating a text variable (stores the condition for: 'Controls' to be printed to the screen, in the previously-declared default font)
    text_rect = text.get_rect(center=(740,350))
    # Defining text_rect, which will store the position of the text on the screen
    screen.blit(text, text_rect)
    # Blitting both the text and its respective position, onto the options screen
    pygame.display.update()
    # Updating the display with the new background, image, and text

    while options:
    # while options = True
        for event in pygame.event.get():
        # For loop for any event to take place in the game
            if event.type == pygame.QUIT:
            # If the type of event causes the game to be quitted
                pygame.quit()
                # The game will quit (end)
            if event.type == pygame.MOUSEBUTTONDOWN:
            # if the player has pressed the right mouse button down
                backbutton.checkForInputBack(pygame.mouse.get_pos())
                # Checking if the back button has been pressed
        backbutton.update()
        # Updating the back button, to its pressed state

        pygame.display.update()
    pygame.quit()
    # Update and quitting pygame modules

def volume(Music):
# Defining the volume() function, and passing the Music Variable as a parameter

    volume = True
    # volume variable is set to True
    pygame.display.set_caption("Velocity - Music Menu")
    # Setting the caption of the Pygame Window, to: 'Velocity - Music Menu'
    screen.blit((options_background), (0, 0))
    # Blitting the options background over the top of the Main Menu Screen (Illusion of replacing it, for the player)
    # Blitting the controls image to the screen, in specific coordinates

    text = main_font.render("Music", True, "white")
    # Creating a text variable (stores the condition for: 'Music' to be printed to the screen, in the previously-declared default font)
    text_rect = text.get_rect(center=(740,350))
    # Defining text_rect, which will store the position of the text on the screen
    screen.blit(text, text_rect)
    # Blitting both the text and its respective position, onto the options screen
    pygame.display.update()
    # Updating the display with the new background, image, and text

    while volume:
    # while volume = True
        for event in pygame.event.get():
        # For loop for any event to take place in the volume menu
            if event.type == pygame.QUIT:
            # If the type of event causes the game to be quitted
                pygame.quit()
                # The game will quit (end)
            if event.type == pygame.MOUSEBUTTONDOWN:
            # if the player has pressed the right mouse button down
                if backbutton.checkForInputBack(pygame.mouse.get_pos()):
                # If the player has clicked on the back button
                    global LevelSelectorMusic
                    # LevelSelectorMusic is set as a global variable
                    LevelSelectorMusic = False
                    # LevelSelectorMusic is set to False, across the entire program
                if musicbutton.checkForInputMusic(pygame.mouse.get_pos()):
                # If the player has clicked on the Music button
                    if Music == True:
                    # If Music is equal to True
                        PlayMusic(Music)
                        # Continue playing the current Main Menu music
                        Music = True
                        # Music variable remains as True
                    elif Music == False:
                    # If Music is equal to False
                        Music = True
                        # Music Variable is set to True
                        PlayMusic(Music)
                        # Begin playing the Main Menu music
                        Music = True
                        # Music Variable remains as True
                if nomusicbutton.checkForInputNoMusic(pygame.mouse.get_pos()):
                # If the No Music Button has been pressed
                    if Music == False:
                    # If Music is equal to False
                        PauseMusic(Music)
                        # Music is paused
                        Music = False
                        # Music variable remains as False
                    elif Music == True:
                    # If Music is equal to True
                        Music = False
                        # Music variable is set to False
                        PauseMusic(Music)
                        # Music is paused
                        Music = False
                        # Music variable remains set at False
        nomusicbutton.update()
        backbutton.update()
        button2.update()
        # Updating the required buttons, to its their pressed/ not pressed states 

        pygame.display.update()
    pygame.quit()
    # Updating display and quitting out of the Menu Screen

def FirstLevel():
# Function, when the first level has been selected to be played

    pygame.display.set_caption("Velocity - Level #1")
    # Setting the caption of the Pygame Window, to: 'Velocity - Level #1'

    BG_COLOR = (255, 255, 255)
    WIDTH = 1500
    HEIGHT = 800
    FPS = 60
    PLAYER_VEL = 5
    # Defining key Variables (Caps to not interfere with any later-declared similar variables)

    def game_over():
    # Defining the game_over function
        global life_count
        # Setting the life_count variable to a global variable
        life_count = 3
        # Setting the life_count variable to 3
        GameOver = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Game Over Screen.png')
        # Defining the GameOver variable to load the background image (The Game Over Screen)
        screen.blit((GameOver), (0, 0))
        # Blitting the Game Over Screen onto the screen
        gameover = True
        # setting the gameover variable to true
        if Music == True:
        # If there is music present in the game
            pygame.mixer.music.stop()
            # Current music is paused
            pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/GameOverMusic.mp3")
            pygame.mixer.music.play()
            # Game Over music is loaded and played
        while gameover:
        # While the program is in the gameover state
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                    pygame.quit()
                    # The game will quit (end)
                if event.type == pygame.MOUSEBUTTONDOWN:
                # if the player has pressed the right mouse button down
                    GameOver_MainMenu.checkForInputGameOver(pygame.mouse.get_pos())
                    # Inputs will be checked for the GameOver_MainMenu button
                    Continue.checkForInputContinue(pygame.mouse.get_pos())
                    # Inputs will be checked for the Continue button

            GameOver_MainMenu.update()
            # Updating the GameOver_MainMenu button
            Continue.update()
            # Updating the Continue button
                    
            pygame.display.update()
        pygame.quit()
    pygame.display.update()
    # Updating and quitting the game

    def text(Count):
    # Defining the text function; passing Count as a parameter
     if Count >=1 and Count <= 9:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render("0"+ Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     elif Count > 9:
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render(Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text = sub_font.render("00", True, "white")
         # Creating a text variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text_rect = text.get_rect(center=(170, 20))
         # Defining text_rect, which will store the position of the text on the screen
         screen.blit(text, text_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()
    
    def text2(life_count):
    # Defining the text2 function; passing Count as a parameter
     if life_count >=1:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(life_count)
        # Convert Count integer into a string, storing it under Count1
        text2 = sub_font.render("0"+ Count1, True, "white")
        # Creating a text2 variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text2_rect = text2.get_rect(center=(75,20))
        # Defining text2_rect, which will store the position of the text on the screen
        screen.blit(text2, text2_rect)
        # Blitting both the text and its respective position, onto the screen
        life_count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text2 = sub_font.render("00", True, "white")
         # Creating a text2 variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text2_rect = text2.get_rect(center=(75,20))
         # Defining text_rect2, which will store the position of the text on the screen
         screen.blit(text2, text2_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()

    if Music == True:
    # If the Music variable is equal to True
        PauseMusic(Music)
        # Main Menu music is paused
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        # Level 1 Music is loaded
        pygame.mixer.music.play(-1)
        # Music track is looped indefinitely
        PlayMusic(Music)
        # PlayMusic function is called
        global LevelSelectorMusic
        # LevelSelectorMusic variable set to a global variable
        LevelSelectorMusic = True
        # LevelSelectorMusic set to True
    else:
    # If the Music Variable is equal to False
        PauseMusic(Music)
        # PlayMusic function is called
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        pygame.mixer.music.play(-1)
        # Level Selector Music is loaded and looped
        PauseMusic(Music)
        # Music is paused

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    # Using Width and Height variables to set size of Window

    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
    # Defining flip function, which flips the sprite left/right, depending on what direction the player is facing

    def load_sprite_sheets(dir1, width, height, direction=False):
        path = join("General", dir1)
        # Creating the path variable, to join the assets in the: "Assets" folder to directory 1
        images = [f for f in listdir(path) if isfile(join(path, f))]
        # Dividing each individual image from the main image into seperate divisons
        
        all_sprites = {}
        # Defining the all_sprites dictionary, where all sprites will be stored

        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            # Creating a for loop for each image within the sprite sheet; joining path and image variables and converting into alpha form
            sprites = []
            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0,0), rect)
                sprites.append(pygame.transform.scale2x(surface))
            # Scaling the sprite to the size of the player character

            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
            # Left sprite loaded, when facing left direction
            # Right sprite loaded, when facing right direction
            else:
                all_sprites[image.replace(".png", "")] = sprites
            # Condition for else; replacing ".png" with "" for all sprites (Default Sprite)

        return all_sprites
        # Returning all sprites that are required, depending on player movement

    def get_block(size):
    # Defining the get_block() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(96, 0, size, size)
        # Specifically loading the grass block image in its full size, using (96,0) coordinates / Brick blocks = (272, 64)
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of block is doubled from previously-declared size

    def get_bricks(size):
    # Defining the get_brick() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(272, 64, size, size)
        # Specifically loading the brick image in its full size, using (272, 64) coordinates
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of brick is doubled from previously-declared size

    class Player(pygame.sprite.Sprite):
    # Creating the Player class
        COLOR = (255, 0, 0)
        # The Player will firstly be a square. The COLOR Variable defines what colour the player will be (Currently Red)
        GRAVITY = 1
        # Setting the GRAVITY Variable to 1
        SPRITES = load_sprite_sheets("MaskDude", 32, 32, True)
        # Variable to call function, to load sprite with direction
        ANIMATION_DELAY = 3
        # Variable to account for delay in animation of sprites

        def __init__(self, x, y, width, height):
            super().__init__()
            self.rect = pygame.Rect(x, y, width, height)
            self.x_vel = 0
            self.y_vel = 0
            self.mask = None
            self.direction = "left"
            self.animation_count = 0
            self.fall_count = 0
            self.jump_count = 0
            self.hit = False
            self.hit_count = 0
        # The __init__ method of the Player class is defined to create key variables that define the Player

        def jump(self):
        # Defining jump method
            self.y_vel = -self.GRAVITY * 8
            # Negative gravity multiplied by 8, in order for a constant speed of gravity to be implemented (Downwards Gravity)
            self.animation_count = 0
            self.jump_count += 1
            if self.jump_count == 1:
                self.fall_count = 0
            # As soon as the player jumps, any obtained gravity will be removed (Not a factor), and then gravity is applied after jumping
                
        def move(self, dx, dy):
            self.rect.x += dx
            self.rect.y += dy
        # The move method is defined to register player positions and movement (x and y values - However, no movement in the y-axis)

        def make_hit(self):
            self.hit = True
            self.hit_count = 0
        # The make_hit method is defined to register when the player has been hit

        def move_left(self, vel):
            self.x_vel = -vel
            if self.direction != "left":
                self.direction = "left"
                self.animation_count = 0
        # move_left method defined to register left player movements

        def move_right(self, vel):
            self.x_vel = vel
            if self.direction != "right":
                self.direction = "right"
                self.animation_count = 0
        # move_right method defined to register right player movements

        def loop(self, fps):
            self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
            self.move(self.x_vel, self.y_vel)
        # loop method defined to move player with set x and y velocities; y velocity now takes into account gravity (1)

            if self.hit:
            # Condition for if the player has been hit
                self.hit_count +=1
                # Adding one to the counter of time being hit for 
            if self.hit_count > fps * 2:
            # Condition for after being in the hit state for greater than 2 seconds
                self.hit = False
                global life_count
                life_count = life_count -1
                # Player is no longer in the hit state
                self.hit_count = 0
                # hit Counter being set to 0

            self.fall_count += 1 
            # Adding 1 to the fall count, as the player as still currently falling, if the method has been executed
            self.update_sprite()
            # Update sprite

        def landed(self):
        # Method for the player to land on a block
            self.fall_count = 0
            # Set to 0, to stop adding gravity
            self.y_vel = 0
            # No upwards or downwards velocity
            self.jump_count = 0
            # Not jumping (Uesful for double-jumps)

        def hit_head(self):
        # Method for the player to hit their head on a block
            self.count = 0
            # Set to 0
            self.y_vel *= -1
            # Velocity is reversed (Moving downwards, rather than upwards)

        def update_sprite(self):
        # Method to update sprites, depending on if running or idle
            sprite_sheet = "idle"
            # Default sprite sheet, if player is not moving
            if self.hit:
            # If the player has been hit
                sprite_sheet = "hit"
                # Load the hit sprite sheet
            if self.y_vel < 0:
            # If velocity is less than 0 (Moving upwards)
                if self.jump_count == 1:
                    sprite_sheet = "jump"
                # If this is the player's first jump, normal jump animation will be featured
                elif self.jump_count == 2:
                    sprite_sheet = "double_jump"
                # If this is the player's second jump, the double jump animation will be featured
            elif self.y_vel > self.GRAVITY * 2:
            # If velocity is greater than gravity * 2 (Moving downwards)
                sprite_sheet = "fall"
                # If player is moving down, then fall animation will be loaded
            elif self.x_vel != 0:
                sprite_sheet = "run"
            # If x velocity is not 0, then running animations will be loaded

            sprite_sheet_name = sprite_sheet + "_" + self.direction
            sprites = self.SPRITES[sprite_sheet_name]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.sprite = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.update()
            # Calling update method

        def update(self):
        # Defining update method
            self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.sprite)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

        def draw(self, win, offset_x):
            win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
        # draw method defined to redraw the current figure in a given position

    # End of the Player class

    class Object(pygame.sprite.Sprite):
    # Creating the Object class (Base class for all objects, so that collision is uniform across all)
    # Inherits from the Sprite class
        def __init__(self, x, y, width, height, name=None):
            super().__init__()
            # Initialising Superclass (pygame.sprite.Sprite)
            self.rect = pygame.Rect(x, y, width, height)
            # Defining Rectangle for a valid sprite
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            # Defining Object image (Supports transparrent images)
            self.width = width
            self.height = height
            self.name = name
            # Defining self variables

        def draw(self, win, offset_x):
            win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        # Draw function automatically draws Object instantly on the screen

    class Coin(Object):
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "coins")
            # Calling super-initialiser (Name is being passed; allows for later checks if coin has been collided with)
            self.coins = load_sprite_sheets("Coins", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.coins["Coin"][0]
            # Loading the Coin animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work)

    class Block(Object):
    # Creating Block class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            block = get_block(size)
            # variable that stores a function to retrieve the size of a block
            self.image.blit(block, (0,0))
            # Block is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Brick(Object):
    # Creating Brick class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            brick = get_bricks(size)
            # variable that stores a function to retrieve the size of a brick (same as a block)
            self.image.blit(brick, (0,0))
            # Brick is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Fire(Object):
    # Creating Fire class - Inherits from Object class
        ANIMATION_DELAY = 3
        # Defining local variable, to account for delay in the animations
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "fire")
            # Calling super-initialiser (Name is being passed; allows for later checks if fire has been hit)
            self.fire = load_sprite_sheets("Fire", width, height)
            # Loading sprites for fire
            self.image = self.fire["off"][0]
            # Specifying image (Fire begins as being off)
            self.mask = pygame.mask.from_surface(self.image)
            # Creating the mask for the fire sprite
            self.animation_count = 0
            # Defining animation count (Same as player)
            self.animation_name = "off"
            # Off animation is automatically played

        def on(self):
        # Defining On method
            self.animation_name = "on"
            # On Fire Animation is played

        def off(self):
        # Defining Off method
            self.animation_name = "off"
            # Off Fire Animation is played

        def loop(self):
            sprites = self.fire[self.animation_name]
            # Defining local variable sprites to store all fire sprites
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.image = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

            if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            # Animation count for fire will continue no matter what; if it gets too high, it will cause the game to lag - This condition prevents it from becomming too high
                self.animation_count = 0
                # Animation count is reset

    class Spikes(Object):
    # Creating the Spikes class (Sub-class of the Object superclass)

        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "spikes")
            # Calling super-initialiser (Name is being passed; allows for later checks if spikes have been hit)
            self.spikes = load_sprite_sheets("Spikes", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.spikes["Idle"][0]
            # Loading the idle spike animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included

    def get_background():
    # get_background() function is defined

        image = pygame.image.load("C:/Users/olive/OneDrive/Desktop/A-Level Work/Computer Science/NEA/NEA Work/Design - Resources/8-bit Game Assets/Main Menu/Main Menu Background.jpg")
        _, _, width, height = image.get_rect()
        tiles = []
        # Defining the get_background() method, to directly load a background image into the game

        for i in range(WIDTH // width + 1):
            for j in range(HEIGHT // height + 1):
                pos = (i * width, j * height)
                tiles.append(pos)
        # Dividing the background into individual tiles, before reforming them, based on the size of the Window

        return tiles, image
        # Returning the tiles array and the image variable

    def draw(window, background, bg_image, Player, objects, offset_x):
        for tile in background:
            window.blit(bg_image, tile)
    # Defining the draw method, which will use each tile of the background and place the respective part of the image overtop of it
    
        for obj in objects:
        # For loop created for each object within objects
            obj.draw(window, offset_x)
            # Object is drawn onto the window
        
        Player.draw(window, offset_x)
        # Using the window variable to add the background to the window

    def handle_vertical_collision(player, objects, dy):
    # Seperate handling of vertical collision (Function)
        collided_objects = []
        # List to keep track of what objects have been collided with
        for obj in objects:
        # For loop (Objects that can be collided with)
            if pygame.sprite.collide_mask(player, obj):
            # Determines if 2 objects are colliding (Player and Block sprites)
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    # Bottom of object equals top of object; prevents player clipping inside of the object
                    player.landed()
                    # Method call
                # If player collides with top of object, bottom of player is set on-top of the object
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    # Top of object equals bottom of object; prevents player clipping inside of the object
                    player.hit_head()
                    # Method call
                # If player collides with bottom of object

                collided_objects.append(obj)
                # Add collided object to list

        return collided_objects
        # Returns collided objects, to determine what type of object has been collided with

    def collide(player, objects, dx):
    # Defining collide function (For horizontal collision)
        player.move(dx, 0)
        # Player moved in displacement-x direction; checking that if the player was to move left/right, would they hit a block?
        player.update()
        # Updating rectangle and player mask
        collided_object = None
        # No current collided object
        for obj in objects:
            if pygame.sprite.collide_mask(player,obj):
            # If an object collides with the updated mask
                collided_object = obj
                # obj is colliding with player
                break

        player.move(-dx, 0)
        # Player moved back to original spot
        player.update()
        # Updating rectangle and mask back to original
        return collided_object
        # If object will collide with player. return the object / If not, no item will be returned

    def handle_move(player, objects):
        keys = pygame.key.get_pressed()
    # Defining the handle_move procedure, which will register when the player enters specific keys that will allow them to move their character

        player.x_vel = 0
        vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
        collide_left = collide(player, objects, -PLAYER_VEL * 2)
        # Checking if player will collide with an object to their left
        collide_right = collide(player, objects, PLAYER_VEL * 2)
        # Checking if player will collide with an object to their right

        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)
        if keys[pygame.K_a] and not collide_right:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_d] and not collide_right:
            player.move_right(PLAYER_VEL) 
        # If left arrow click (and no potential block collisions), player moves left
        # If right arrow click (and no potential block collisions), player moves right

        vertical = [*vertical_collide]
        horizontal = [collide_left, collide_right]
        # Conditions to be checked (Left, right, and vertical collisions)

        for obj in vertical:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "fire":
            # If the player has collided with fire
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                global Count
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen

        for obj in horizontal:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen
                
    def main(window):
        clock = pygame.time.Clock()
        background, bg_image = get_background()
    # Defining main window of the game, and creating clock and background / bg_image variables
        block_size = 96
        # Defining the block_size variable, for later use in declaring the sizes of blocks
        player = Player(100, 100, 50, 50)
        # Creating an instance of the Player class
        fire = Fire(2915, HEIGHT - block_size - 350, 16, 32)
        # Defining fire variable and calling the Fire class
        fire.on()
        # Fire is always on
        spikes = Spikes(1410, HEIGHT - block_size - 30, 16, 32)
        spikes2 = Spikes(1375, HEIGHT - block_size - 30, 16, 32)
        spikes3 = Spikes(1340, HEIGHT - block_size - 30, 16, 32)
        spikes4 = Spikes(1305, HEIGHT - block_size - 30, 16, 32)
        spikes5 = Spikes(1270, HEIGHT - block_size - 30, 16, 32)
        spikes6 = Spikes(1254, HEIGHT - block_size - 30, 16, 32)
        spikes7 = Spikes(block_size * 40, HEIGHT - block_size - 30, 16, 32)
        spikes8 = Spikes((block_size * 40) + 35, HEIGHT - block_size - 30, 16, 32)
        spikes9 = Spikes((block_size * 40) + 70, HEIGHT - block_size - 30, 16, 32)
        spikes10 = Spikes((block_size * 41) - 8.2, HEIGHT - block_size - 30, 16, 32)
        spikes11 = Spikes((block_size * 41) + 26.8, HEIGHT - block_size - 30, 16, 32)
        spikes12 = Spikes((block_size * 41) + 61.8, HEIGHT - block_size - 30, 16, 32)
        coin = Coin(300, HEIGHT - block_size - 64, 16, 32)
        coin2 = Coin(400, HEIGHT - block_size - 64, 16, 32)
        coin3= Coin(500, HEIGHT - block_size - 64, 16, 32)
        coin4 = Coin((block_size * 10) + 200, HEIGHT - block_size - 128, 16, 32)
        coin5 = Coin((block_size * 40), HEIGHT - block_size - 128, 16, 32)
        coin6 = Coin((block_size * 40) + 60, HEIGHT - block_size - 192, 16, 32)
        coin7 = Coin((block_size * 40) + 120, HEIGHT - block_size - 192, 16, 32)
        coin8 = Coin((block_size * 40) + 190, HEIGHT - block_size - 128, 16, 32)
        coin9 = Coin(block_size * 63, HEIGHT - block_size * 6.5, 16, 32)
        coin10 = Coin(block_size * 64, HEIGHT - block_size * 6.5, 16, 32)
        coin11 = Coin(block_size * 65, HEIGHT - block_size * 6.5, 16, 32)
        coin12 = Coin(block_size * 66, HEIGHT - block_size * 6.5, 16, 32)
        coin13 = Coin(block_size * 67, HEIGHT - block_size * 6.5, 16, 32)
        coin14 = Coin(block_size * 68, HEIGHT - block_size * 6.5, 16, 32)
        coin15 = Coin(block_size * 69, HEIGHT - block_size * 6.5, 16, 32)
        coin16 = Coin(block_size * 70, HEIGHT - block_size * 6.5, 16, 32)
        coin17 = Coin(block_size * 71, HEIGHT - block_size * 6.5, 16, 32)
        coin18 = Coin(block_size * 72, HEIGHT - block_size * 6.5, 16, 32)
        coin19 = Coin(block_size * 73, HEIGHT - block_size * 6.5, 16, 32)
        coin20 = Coin(block_size * 74, HEIGHT - block_size * 6.5, 16, 32)
        coin21 = Coin(block_size * 75, HEIGHT - block_size * 6.5, 16, 32)
        coin22 = Coin(block_size * 76, HEIGHT - block_size * 6.5, 16, 32)
        coin23 = Coin(block_size * 77, HEIGHT - block_size * 6.5, 16, 32)
        # Creating 12 instances of spikes and 23 instances of coins, each stored under a different variable name
        floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
        # Creating the floor variable; create a number of blocks that will be duplicated to the left and right of the initial block (Working, for a scrolling background)
        objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size), Brick(block_size * 3, HEIGHT - block_size * 4, block_size),  Brick(block_size * 4, HEIGHT - block_size * 4, block_size),  
                    Brick(block_size * 5, HEIGHT - block_size * 4, block_size), Block(block_size * 10, HEIGHT - block_size * 3, block_size), Brick(block_size * 12, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 10, HEIGHT - block_size * 2, block_size), Block(block_size * 9, HEIGHT - block_size * 2, block_size), Block(block_size * 11, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 11, HEIGHT - block_size * 3, block_size), Block(block_size * 11, HEIGHT - block_size * 4, block_size), Block(block_size * 15, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 15, HEIGHT - block_size * 3, block_size), Block(block_size * 15, HEIGHT - block_size * 2, block_size), Block(block_size * 16, HEIGHT - block_size * 2, block_size), 
                    Block(block_size * 16, HEIGHT - block_size * 3, block_size), Block(block_size * 17, HEIGHT - block_size * 2, block_size), Brick(block_size * 24, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 25, HEIGHT - block_size * 3, block_size), Brick(block_size * 26, HEIGHT - block_size * 3, block_size), Brick(block_size * 25, HEIGHT - block_size * 5, block_size),
                    Brick(block_size * 29, HEIGHT - block_size * 4, block_size), Brick(block_size * 30, HEIGHT - block_size * 4, block_size), Brick(block_size * 31, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 36, HEIGHT - block_size * 3, block_size), Block(block_size * 37, HEIGHT - block_size * 3, block_size), Block(block_size * 38, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 37, HEIGHT - block_size * 4, block_size), Block(block_size * 38, HEIGHT - block_size * 4, block_size), Block(block_size * 39, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 38, HEIGHT - block_size * 5, block_size), Block(block_size * 39, HEIGHT - block_size * 5, block_size), Block(block_size * 40, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 41, HEIGHT - block_size * 5, block_size), Block(block_size * 42, HEIGHT - block_size * 5, block_size), Block(block_size * 43, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 42, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Block(block_size * 45, HEIGHT - block_size * 3, block_size), Block(block_size * 44, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Brick(block_size * 49, HEIGHT - block_size * 3, block_size), Brick(block_size * 50, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 49, HEIGHT - block_size * 2, block_size), Brick(block_size * 50, HEIGHT - block_size * 2, block_size), Brick(block_size * 48, HEIGHT - block_size * 2, block_size), 
                    Brick(block_size * 51, HEIGHT - block_size * 2, block_size), Brick(block_size * 53, HEIGHT - block_size * 3, block_size), Brick(block_size * 54, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 58, HEIGHT - block_size * 2, block_size), Block(block_size * 59, HEIGHT - block_size * 2, block_size), Block(block_size * 60, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 59, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 4, block_size),
                    Brick(block_size * 63, HEIGHT - block_size * 6, block_size), Brick(block_size * 64, HEIGHT - block_size * 6, block_size), Brick(block_size * 65, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 66, HEIGHT - block_size * 6, block_size), Brick(block_size * 67, HEIGHT - block_size * 6, block_size), Brick(block_size * 68, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 69, HEIGHT - block_size * 6, block_size), Brick(block_size * 70, HEIGHT - block_size * 6, block_size), Brick(block_size * 71, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 72, HEIGHT - block_size * 6, block_size), Brick(block_size * 73, HEIGHT - block_size * 6, block_size), Brick(block_size * 74, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 75, HEIGHT - block_size * 6, block_size), Brick(block_size * 76, HEIGHT - block_size * 6, block_size), Brick(block_size * 77, HEIGHT - block_size * 6, block_size),
                    fire, spikes, spikes2, spikes3, spikes4, spikes5, spikes6, spikes7, spikes8, spikes9, spikes10, spikes11, spikes12, coin, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                    coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22, coin23]
        # Floor broken into individual elements (that are added to the list)
        # Blocks / Bricks passed through (Coordinates) - y multiplied by a larger number, in order to be positioned higher on the screen
        # Block / Brick size passed through and all is stored in variable: objects
        # Fire variable passed through; fire is a sub-class of the superclass: Objects
        # All spikes are passed through; spikes are a sub-class of the superclass: Objects
        
        offset_x = 0
        # Stores by how much the screen is currently offset (How much it has moved to the left/right)
        scroll_area_width = 300
        # Amount of pixels to the left/ right, for the game to start scrolling

        run = True
        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
        # Allows the player to load the game and quit the game
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
                    # If space bar is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_UP and player.jump_count < 2:
                        player.jump()
                    # If up arrow key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_w and player.jump_count < 2:
                        player.jump()
                    # If the W key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_p:
                        x = Pause_Game()
                        print(x)
                    # If: 'p' is pressed, the pause menu will be loaded

            player.loop(FPS)
            fire.loop()
            handle_move(player, objects)
            draw(window, background, bg_image, player, objects, offset_x)
            texts = text(Count)
            print(texts)
            texts2 = text2(life_count)
            print(texts2)
            screen.blit((Lives), (22, 2))
            screen.blit((CoinImage), (120, 8))
            # Drawing the player, background, objects and the offset into the game

            if life_count <= 0:
                x = game_over()
                print(x)
            # If the player's life count is at 0, the game_over function will be printed

            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and (player.x_vel > 0)) or ((player.rect.left - offset_x <= scroll_area_width) and (player.x_vel < 0)):
            # If player is over the pixel limit to what is being shown on the window (Left and Right sides)
                offset_x += player.x_vel
                # Offset by the velocity of how much the player moved to the right

            if (player.rect.right >= 7500):
                # If the player's right directional movement exceeds 7500 pixels
                if Music == True:
                        x = play(True)
                        print(x)
                # If Music is True, play() function will be loaded with music
                else:
                    x = play(False)
                    print(x)
                # If Music is False, play() function will be loaded without music

            pygame.display.update()

        pygame.quit()
        quit()
        # Quitting the pygame program

    if __name__ == "__main__":
        main(window)
    # Calling main(window), if the player has just loaded the game

def SecondLevel():
# Function, when the first level has been selected to be played

    pygame.display.set_caption("Velocity - Level #2")
    # Setting the caption of the Pygame Window, to: 'Velocity - Level #1'

    BG_COLOR = (255, 255, 255)
    WIDTH = 1500
    HEIGHT = 800
    FPS = 60
    PLAYER_VEL = 5
    # Defining key Variables (Caps to not interfere with any later-declared similar variables)

    def game_over():
    # Defining the game_over function
        global life_count
        # Setting the life_count variable to a global variable
        life_count = 3
        # Setting the life_count variable to 3
        GameOver = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Game Over Screen.png')
        # Defining the GameOver variable to load the background image (The Game Over Screen)
        screen.blit((GameOver), (0, 0))
        # Blitting the Game Over Screen onto the screen
        gameover = True
        # setting the gameover variable to true
        if Music == True:
        # If there is music present in the game
            pygame.mixer.music.stop()
            # Current music is paused
            pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/GameOverMusic.mp3")
            pygame.mixer.music.play()
            # Game Over music is loaded and played
        while gameover:
        # While the program is in the gameover state
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                    pygame.quit()
                    # The game will quit (end)
                if event.type == pygame.MOUSEBUTTONDOWN:
                # if the player has pressed the right mouse button down
                    GameOver_MainMenu.checkForInputGameOver(pygame.mouse.get_pos())
                    # Inputs will be checked for the GameOver_MainMenu button
                    Continue.checkForInputContinue(pygame.mouse.get_pos())
                    # Inputs will be checked for the Continue button

            GameOver_MainMenu.update()
            # Updating the GameOver_MainMenu button
            Continue.update()
            # Updating the Continue button
                    
            pygame.display.update()
        pygame.quit()
    pygame.display.update()
    # Updating and quitting the game

    def text(Count):
    # Defining the text function; passing Count as a parameter
     if Count >=1 and Count <= 9:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render("0"+ Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     elif Count > 9:
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render(Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text = sub_font.render("00", True, "white")
         # Creating a text variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text_rect = text.get_rect(center=(170, 20))
         # Defining text_rect, which will store the position of the text on the screen
         screen.blit(text, text_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()
    
    def text2(life_count):
    # Defining the text2 function; passing Count as a parameter
     if life_count >=1:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(life_count)
        # Convert Count integer into a string, storing it under Count1
        text2 = sub_font.render("0"+ Count1, True, "white")
        # Creating a text2 variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text2_rect = text2.get_rect(center=(75,20))
        # Defining text2_rect, which will store the position of the text on the screen
        screen.blit(text2, text2_rect)
        # Blitting both the text and its respective position, onto the screen
        life_count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text2 = sub_font.render("00", True, "white")
         # Creating a text2 variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text2_rect = text2.get_rect(center=(75,20))
         # Defining text_rect2, which will store the position of the text on the screen
         screen.blit(text2, text2_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()

    if Music == True:
    # If the Music variable is equal to True
        PauseMusic(Music)
        # Main Menu music is paused
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        # Level 1 Music is loaded
        pygame.mixer.music.play(-1)
        # Music track is looped indefinitely
        PlayMusic(Music)
        # PlayMusic function is called
        global LevelSelectorMusic
        # LevelSelectorMusic variable set to a global variable
        LevelSelectorMusic = True
        # LevelSelectorMusic set to True
    else:
    # If the Music Variable is equal to False
        PauseMusic(Music)
        # PlayMusic function is called
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        pygame.mixer.music.play(-1)
        # Level Selector Music is loaded and looped
        PauseMusic(Music)
        # Music is paused

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    # Using Width and Height variables to set size of Window

    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
    # Defining flip function, which flips the sprite left/right, depending on what direction the player is facing

    def load_sprite_sheets(dir1, width, height, direction=False):
        path = join("General", dir1)
        # Creating the path variable, to join the assets in the: "Assets" folder to directory 1
        images = [f for f in listdir(path) if isfile(join(path, f))]
        # Dividing each individual image from the main image into seperate divisons
        
        all_sprites = {}
        # Defining the all_sprites dictionary, where all sprites will be stored

        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            # Creating a for loop for each image within the sprite sheet; joining path and image variables and converting into alpha form
            sprites = []
            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0,0), rect)
                sprites.append(pygame.transform.scale2x(surface))
            # Scaling the sprite to the size of the player character

            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
            # Left sprite loaded, when facing left direction
            # Right sprite loaded, when facing right direction
            else:
                all_sprites[image.replace(".png", "")] = sprites
            # Condition for else; replacing ".png" with "" for all sprites (Default Sprite)

        return all_sprites
        # Returning all sprites that are required, depending on player movement

    def get_block(size):
    # Defining the get_block() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(96, 0, size, size)
        # Specifically loading the grass block image in its full size, using (96,0) coordinates / Brick blocks = (272, 64)
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of block is doubled from previously-declared size

    def get_bricks(size):
    # Defining the get_brick() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(272, 64, size, size)
        # Specifically loading the brick image in its full size, using (272, 64) coordinates
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of brick is doubled from previously-declared size

    class Player(pygame.sprite.Sprite):
    # Creating the Player class
        COLOR = (255, 0, 0)
        # The Player will firstly be a square. The COLOR Variable defines what colour the player will be (Currently Red)
        GRAVITY = 1
        # Setting the GRAVITY Variable to 1
        SPRITES = load_sprite_sheets("MaskDude", 32, 32, True)
        # Variable to call function, to load sprite with direction
        ANIMATION_DELAY = 3
        # Variable to account for delay in animation of sprites

        def __init__(self, x, y, width, height):
            super().__init__()
            self.rect = pygame.Rect(x, y, width, height)
            self.x_vel = 0
            self.y_vel = 0
            self.mask = None
            self.direction = "left"
            self.animation_count = 0
            self.fall_count = 0
            self.jump_count = 0
            self.hit = False
            self.hit_count = 0
        # The __init__ method of the Player class is defined to create key variables that define the Player

        def jump(self):
        # Defining jump method
            self.y_vel = -self.GRAVITY * 8
            # Negative gravity multiplied by 8, in order for a constant speed of gravity to be implemented (Downwards Gravity)
            self.animation_count = 0
            self.jump_count += 1
            if self.jump_count == 1:
                self.fall_count = 0
            # As soon as the player jumps, any obtained gravity will be removed (Not a factor), and then gravity is applied after jumping
                
        def move(self, dx, dy):
            self.rect.x += dx
            self.rect.y += dy
        # The move method is defined to register player positions and movement (x and y values - However, no movement in the y-axis)

        def make_hit(self):
            self.hit = True
            self.hit_count = 0
        # The make_hit method is defined to register when the player has been hit

        def move_left(self, vel):
            self.x_vel = -vel
            if self.direction != "left":
                self.direction = "left"
                self.animation_count = 0
        # move_left method defined to register left player movements

        def move_right(self, vel):
            self.x_vel = vel
            if self.direction != "right":
                self.direction = "right"
                self.animation_count = 0
        # move_right method defined to register right player movements
        

        def loop(self, fps):
            self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
            self.move(self.x_vel, self.y_vel)
        # loop method defined to move player with set x and y velocities; y velocity now takes into account gravity (1)

            if self.hit:
            # Condition for if the player has been hit
                self.hit_count +=1
                # Adding one to the counter of time being hit for 
            if self.hit_count > fps * 2:
            # Condition for after being in the hit state for greater than 2 seconds
                self.hit = False
                global life_count
                life_count = life_count -1
                # Player is no longer in the hit state
                self.hit_count = 0
                # hit Counter being set to 0

            self.fall_count += 1 
            # Adding 1 to the fall count, as the player as still currently falling, if the method has been executed
            self.update_sprite()
            # Update sprite

        def landed(self):
        # Method for the player to land on a block
            self.fall_count = 0
            # Set to 0, to stop adding gravity
            self.y_vel = 0
            # No upwards or downwards velocity
            self.jump_count = 0
            # Not jumping (Uesful for double-jumps)

        def hit_head(self):
        # Method for the player to hit their head on a block
            self.count = 0
            # Set to 0
            self.y_vel *= -1
            # Velocity is reversed (Moving downwards, rather than upwards)

        def update_sprite(self):
        # Method to update sprites, depending on if running or idle
            sprite_sheet = "idle"
            # Default sprite sheet, if player is not moving
            if self.hit:
            # If the player has been hit
                sprite_sheet = "hit"
                # Load the hit sprite sheet
            if self.y_vel < 0:
            # If velocity is less than 0 (Moving upwards)
                if self.jump_count == 1:
                    sprite_sheet = "jump"
                # If this is the player's first jump, normal jump animation will be featured
                elif self.jump_count == 2:
                    sprite_sheet = "double_jump"
                # If this is the player's second jump, the double jump animation will be featured
            elif self.y_vel > self.GRAVITY * 2:
            # If velocity is greater than gravity * 2 (Moving downwards)
                sprite_sheet = "fall"
                # If player is moving down, then fall animation will be loaded
            elif self.x_vel != 0:
                sprite_sheet = "run"
            # If x velocity is not 0, then running animations will be loaded

            sprite_sheet_name = sprite_sheet + "_" + self.direction
            sprites = self.SPRITES[sprite_sheet_name]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.sprite = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.update()
            # Calling update method

        def update(self):
        # Defining update method
            self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.sprite)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

        def draw(self, win, offset_x):
            win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
        # draw method defined to redraw the current figure in a given position

    # End of the Player class

    class Object(pygame.sprite.Sprite):
    # Creating the Object class (Base class for all objects, so that collision is uniform across all)
    # Inherits from the Sprite class
        def __init__(self, x, y, width, height, name=None):
            super().__init__()
            # Initialising Superclass (pygame.sprite.Sprite)
            self.rect = pygame.Rect(x, y, width, height)
            # Defining Rectangle for a valid sprite
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            # Defining Object image (Supports transparrent images)
            self.width = width
            self.height = height
            self.name = name
            # Defining self variables

        def draw(self, win, offset_x):
            win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        # Draw function automatically draws Object instantly on the screen

    class Coin(Object):
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "coins")
            # Calling super-initialiser (Name is being passed; allows for later checks if coin has been collided with)
            self.coins = load_sprite_sheets("Coins", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.coins["Coin"][0]
            # Loading the Coin animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work)

    class Block(Object):
    # Creating Block class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            block = get_block(size)
            # variable that stores a function to retrieve the size of a block
            self.image.blit(block, (0,0))
            # Block is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Brick(Object):
    # Creating Brick class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            brick = get_bricks(size)
            # variable that stores a function to retrieve the size of a brick (same as a block)
            self.image.blit(brick, (0,0))
            # Brick is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Fire(Object):
    # Creating Fire class - Inherits from Object class
        ANIMATION_DELAY = 3
        # Defining local variable, to account for delay in the animations
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "fire")
            # Calling super-initialiser (Name is being passed; allows for later checks if fire has been hit)
            self.fire = load_sprite_sheets("Fire", width, height)
            # Loading sprites for fire
            self.image = self.fire["off"][0]
            # Specifying image (Fire begins as being off)
            self.mask = pygame.mask.from_surface(self.image)
            # Creating the mask for the fire sprite
            self.animation_count = 0
            # Defining animation count (Same as player)
            self.animation_name = "off"
            # Off animation is automatically played

        def on(self):
        # Defining On method
            self.animation_name = "on"
            # On Fire Animation is played

        def off(self):
        # Defining Off method
            self.animation_name = "off"
            # Off Fire Animation is played

        def loop(self):
            sprites = self.fire[self.animation_name]
            # Defining local variable sprites to store all fire sprites
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.image = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

            if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            # Animation count for fire will continue no matter what; if it gets too high, it will cause the game to lag - This condition prevents it from becomming too high
                self.animation_count = 0
                # Animation count is reset

    class Spikes(Object):
    # Creating the Spikes class (Sub-class of the Object superclass)

        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "spikes")
            # Calling super-initialiser (Name is being passed; allows for later checks if spikes have been hit)
            self.spikes = load_sprite_sheets("Spikes", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.spikes["Idle"][0]
            # Loading the idle spike animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included

    def get_background():
    # get_background() function is defined

        image = pygame.image.load("C:/Users/olive/OneDrive/Desktop/A-Level Work/Computer Science/NEA/NEA Work/Design - Resources/8-bit Game Assets/Main Menu/Level2 Background.jpg")
        _, _, width, height = image.get_rect()
        tiles = []
        # Defining the get_background() method, to directly load a background image into the game

        for i in range(WIDTH // width + 1):
            for j in range(HEIGHT // height + 1):
                pos = (i * width, j * height)
                tiles.append(pos)
        # Dividing the background into individual tiles, before reforming them, based on the size of the Window

        return tiles, image
        # Returning the tiles array and the image variable

    def draw(window, background, bg_image, Player, objects, offset_x):
        for tile in background:
            window.blit(bg_image, tile)
    # Defining the draw method, which will use each tile of the background and place the respective part of the image overtop of it
    
        for obj in objects:
        # For loop created for each object within objects
            obj.draw(window, offset_x)
            # Object is drawn onto the window
        
        Player.draw(window, offset_x)
        # Using the window variable to add the background to the window

    def handle_vertical_collision(player, objects, dy):
    # Seperate handling of vertical collision (Function)
        collided_objects = []
        # List to keep track of what objects have been collided with
        for obj in objects:
        # For loop (Objects that can be collided with)
            if pygame.sprite.collide_mask(player, obj):
            # Determines if 2 objects are colliding (Player and Block sprites)
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    # Bottom of object equals top of object; prevents player clipping inside of the object
                    player.landed()
                    # Method call
                # If player collides with top of object, bottom of player is set on-top of the object
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    # Top of object equals bottom of object; prevents player clipping inside of the object
                    player.hit_head()
                    # Method call
                # If player collides with bottom of object

                collided_objects.append(obj)
                # Add collided object to list

        return collided_objects
        # Returns collided objects, to determine what type of object has been collided with

    def collide(player, objects, dx):
    # Defining collide function (For horizontal collision)
        player.move(dx, 0)
        # Player moved in displacement-x direction; checking that if the player was to move left/right, would they hit a block?
        player.update()
        # Updating rectangle and player mask
        collided_object = None
        # No current collided object
        for obj in objects:
            if pygame.sprite.collide_mask(player,obj):
            # If an object collides with the updated mask
                collided_object = obj
                # obj is colliding with player
                break

        player.move(-dx, 0)
        # Player moved back to original spot
        player.update()
        # Updating rectangle and mask back to original
        return collided_object
        # If object will collide with player. return the object / If not, no item will be returned

    def handle_move(player, objects):
        keys = pygame.key.get_pressed()
    # Defining the handle_move procedure, which will register when the player enters specific keys that will allow them to move their character

        player.x_vel = 0
        vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
        collide_left = collide(player, objects, -PLAYER_VEL * 2)
        # Checking if player will collide with an object to their left
        collide_right = collide(player, objects, PLAYER_VEL * 2)
        # Checking if player will collide with an object to their right

        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)
        if keys[pygame.K_a] and not collide_right:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_d] and not collide_right:
            player.move_right(PLAYER_VEL) 
        # If left arrow click (and no potential block collisions), player moves left
        # If right arrow click (and no potential block collisions), player moves right

        vertical = [*vertical_collide]
        horizontal = [collide_left, collide_right]
        # Conditions to be checked (Left, right, and vertical collisions)

        for obj in vertical:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "fire":
            # If the player has collided with fire
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                global Count
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen

        for obj in horizontal:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen
                
    def main(window):
        clock = pygame.time.Clock()
        background, bg_image = get_background()
    # Defining main window of the game, and creating clock and background / bg_image variables
        block_size = 96
        # Defining the block_size variable, for later use in declaring the sizes of blocks
        player = Player(100, 100, 50, 50)
        # Creating an instance of the Player class
        fire = Fire(2915, HEIGHT - block_size - 350, 16, 32)
        # Defining fire variable and calling the Fire class
        fire.on()
        # Fire is always on
        spikes = Spikes(1410, HEIGHT - block_size - 30, 16, 32)
        spikes2 = Spikes(1375, HEIGHT - block_size - 30, 16, 32)
        spikes3 = Spikes(1340, HEIGHT - block_size - 30, 16, 32)
        spikes4 = Spikes(1305, HEIGHT - block_size - 30, 16, 32)
        spikes5 = Spikes(1270, HEIGHT - block_size - 30, 16, 32)
        spikes6 = Spikes(1254, HEIGHT - block_size - 30, 16, 32)
        spikes7 = Spikes(block_size * 40, HEIGHT - block_size - 30, 16, 32)
        spikes8 = Spikes((block_size * 40) + 35, HEIGHT - block_size - 30, 16, 32)
        spikes9 = Spikes((block_size * 40) + 70, HEIGHT - block_size - 30, 16, 32)
        spikes10 = Spikes((block_size * 41) - 8.2, HEIGHT - block_size - 30, 16, 32)
        spikes11 = Spikes((block_size * 41) + 26.8, HEIGHT - block_size - 30, 16, 32)
        spikes12 = Spikes((block_size * 41) + 61.8, HEIGHT - block_size - 30, 16, 32)
        coin = Coin(300, HEIGHT - block_size - 64, 16, 32)
        coin2 = Coin(400, HEIGHT - block_size - 64, 16, 32)
        coin3= Coin(500, HEIGHT - block_size - 64, 16, 32)
        coin4 = Coin((block_size * 10) + 200, HEIGHT - block_size - 128, 16, 32)
        coin5 = Coin((block_size * 40), HEIGHT - block_size - 128, 16, 32)
        coin6 = Coin((block_size * 40) + 60, HEIGHT - block_size - 192, 16, 32)
        coin7 = Coin((block_size * 40) + 120, HEIGHT - block_size - 192, 16, 32)
        coin8 = Coin((block_size * 40) + 190, HEIGHT - block_size - 128, 16, 32)
        coin9 = Coin(block_size * 63, HEIGHT - block_size * 6.5, 16, 32)
        coin10 = Coin(block_size * 64, HEIGHT - block_size * 6.5, 16, 32)
        coin11 = Coin(block_size * 65, HEIGHT - block_size * 6.5, 16, 32)
        coin12 = Coin(block_size * 66, HEIGHT - block_size * 6.5, 16, 32)
        coin13 = Coin(block_size * 67, HEIGHT - block_size * 6.5, 16, 32)
        coin14 = Coin(block_size * 68, HEIGHT - block_size * 6.5, 16, 32)
        coin15 = Coin(block_size * 69, HEIGHT - block_size * 6.5, 16, 32)
        coin16 = Coin(block_size * 70, HEIGHT - block_size * 6.5, 16, 32)
        coin17 = Coin(block_size * 71, HEIGHT - block_size * 6.5, 16, 32)
        coin18 = Coin(block_size * 72, HEIGHT - block_size * 6.5, 16, 32)
        coin19 = Coin(block_size * 73, HEIGHT - block_size * 6.5, 16, 32)
        coin20 = Coin(block_size * 74, HEIGHT - block_size * 6.5, 16, 32)
        coin21 = Coin(block_size * 75, HEIGHT - block_size * 6.5, 16, 32)
        coin22 = Coin(block_size * 76, HEIGHT - block_size * 6.5, 16, 32)
        coin23 = Coin(block_size * 77, HEIGHT - block_size * 6.5, 16, 32)
        # Creating 12 instances of spikes and 23 instances of coins, each stored under a different variable name
        floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
        # Creating the floor variable; create a number of blocks that will be duplicated to the left and right of the initial block (Working, for a scrolling background)
        objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),  
                    Block(block_size * 10, HEIGHT - block_size * 3, block_size), Brick(block_size * 12, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 10, HEIGHT - block_size * 2, block_size), Block(block_size * 9, HEIGHT - block_size * 2, block_size), Block(block_size * 11, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 11, HEIGHT - block_size * 3, block_size), Block(block_size * 11, HEIGHT - block_size * 4, block_size), Block(block_size * 15, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 15, HEIGHT - block_size * 3, block_size), Block(block_size * 15, HEIGHT - block_size * 2, block_size), Block(block_size * 16, HEIGHT - block_size * 2, block_size), 
                    Block(block_size * 16, HEIGHT - block_size * 3, block_size), Block(block_size * 17, HEIGHT - block_size * 2, block_size), Brick(block_size * 24, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 25, HEIGHT - block_size * 3, block_size), Brick(block_size * 26, HEIGHT - block_size * 3, block_size), Brick(block_size * 25, HEIGHT - block_size * 5, block_size),
                    Brick(block_size * 29, HEIGHT - block_size * 4, block_size), Brick(block_size * 30, HEIGHT - block_size * 4, block_size), Brick(block_size * 31, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 36, HEIGHT - block_size * 3, block_size), Block(block_size * 37, HEIGHT - block_size * 3, block_size), Block(block_size * 38, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 37, HEIGHT - block_size * 4, block_size), Block(block_size * 38, HEIGHT - block_size * 4, block_size), Block(block_size * 39, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 38, HEIGHT - block_size * 5, block_size), Block(block_size * 39, HEIGHT - block_size * 5, block_size), Block(block_size * 40, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 41, HEIGHT - block_size * 5, block_size), Block(block_size * 42, HEIGHT - block_size * 5, block_size), Block(block_size * 43, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 42, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Block(block_size * 45, HEIGHT - block_size * 3, block_size), Block(block_size * 44, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Brick(block_size * 49, HEIGHT - block_size * 3, block_size), Brick(block_size * 50, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 49, HEIGHT - block_size * 2, block_size), Brick(block_size * 50, HEIGHT - block_size * 2, block_size), Brick(block_size * 48, HEIGHT - block_size * 2, block_size), 
                    Brick(block_size * 51, HEIGHT - block_size * 2, block_size), Brick(block_size * 53, HEIGHT - block_size * 3, block_size), Brick(block_size * 54, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 58, HEIGHT - block_size * 2, block_size), Block(block_size * 59, HEIGHT - block_size * 2, block_size), Block(block_size * 60, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 59, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 4, block_size),
                    Brick(block_size * 63, HEIGHT - block_size * 6, block_size), Brick(block_size * 64, HEIGHT - block_size * 6, block_size), Brick(block_size * 65, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 66, HEIGHT - block_size * 6, block_size), Brick(block_size * 67, HEIGHT - block_size * 6, block_size), Brick(block_size * 68, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 69, HEIGHT - block_size * 6, block_size), Brick(block_size * 70, HEIGHT - block_size * 6, block_size), Brick(block_size * 71, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 72, HEIGHT - block_size * 6, block_size), Brick(block_size * 73, HEIGHT - block_size * 6, block_size), Brick(block_size * 74, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 75, HEIGHT - block_size * 6, block_size), Brick(block_size * 76, HEIGHT - block_size * 6, block_size), Brick(block_size * 77, HEIGHT - block_size * 6, block_size),
                    fire, spikes, spikes2, spikes3, spikes4, spikes5, spikes6, spikes7, spikes8, spikes9, spikes10, spikes11, spikes12, coin, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                    coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22, coin23]
        # Floor broken into individual elements (that are added to the list)
        # Blocks / Bricks passed through (Coordinates) - y multiplied by a larger number, in order to be positioned higher on the screen
        # Block / Brick size passed through and all is stored in variable: objects
        # Fire variable passed through; fire is a sub-class of the superclass: Objects
        # All spikes are passed through; spikes are a sub-class of the superclass: Objects
        
        offset_x = 0
        # Stores by how much the screen is currently offset (How much it has moved to the left/right)
        scroll_area_width = 300
        # Amount of pixels to the left/ right, for the game to start scrolling

        run = True
        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
        # Allows the player to load the game and quit the game
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
                    # If space bar is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_UP and player.jump_count < 2:
                        player.jump()
                    # If up arrow key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_w and player.jump_count < 2:
                        player.jump()
                    # If the W key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_p:
                        x = Pause_Game2()
                        print(x)
                    # If: 'p' is pressed, the pause menu will be loaded

            player.loop(FPS)
            fire.loop()
            handle_move(player, objects)
            draw(window, background, bg_image, player, objects, offset_x)
            texts = text(Count)
            print(texts)
            texts2 = text2(life_count)
            print(texts2)
            screen.blit((Lives), (22, 2))
            screen.blit((CoinImage), (120, 8))
            # Drawing the player, background, objects and the offset into the game

            if life_count <= 0:
                x = game_over()
                print(x)
            # If the player's life count is at 0, the game_over function will be printed

            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and (player.x_vel > 0)) or ((player.rect.left - offset_x <= scroll_area_width) and (player.x_vel < 0)):
            # If player is over the pixel limit to what is being shown on the window (Left and Right sides)
                offset_x += player.x_vel
                # Offset by the velocity of how much the player moved to the right

            if (player.rect.right >= 7500):
                # If the player's right directional movement exceeds 7500 pixels
                if Music == True:
                        x = play(True)
                        print(x)
                # If Music is True, play() function will be loaded with music
                else:
                    x = play(False)
                    print(x)
                # If Music is False, play() function will be loaded without music

            pygame.display.update()

        pygame.quit()
        quit()
        # Quitting the pygame program

    if __name__ == "__main__":
        main(window)
    # Calling main(window), if the player has just loaded the game

def ThirdLevel():
# Function, when the first level has been selected to be played

    pygame.display.set_caption("Velocity - Level #3")
    # Setting the caption of the Pygame Window, to: 'Velocity - Level #1'

    BG_COLOR = (255, 255, 255)
    WIDTH = 1500
    HEIGHT = 800
    FPS = 60
    PLAYER_VEL = 5
    # Defining key Variables (Caps to not interfere with any later-declared similar variables)

    def game_over():
    # Defining the game_over function
        global life_count
        # Setting the life_count variable to a global variable
        life_count = 3
        # Setting the life_count variable to 3
        GameOver = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Game Over Screen.png')
        # Defining the GameOver variable to load the background image (The Game Over Screen)
        screen.blit((GameOver), (0, 0))
        # Blitting the Game Over Screen onto the screen
        gameover = True
        # setting the gameover variable to true
        if Music == True:
        # If there is music present in the game
            pygame.mixer.music.stop()
            # Current music is paused
            pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/GameOverMusic.mp3")
            pygame.mixer.music.play()
            # Game Over music is loaded and played
        while gameover:
        # While the program is in the gameover state
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                    pygame.quit()
                    # The game will quit (end)
                if event.type == pygame.MOUSEBUTTONDOWN:
                # if the player has pressed the right mouse button down
                    GameOver_MainMenu.checkForInputGameOver(pygame.mouse.get_pos())
                    # Inputs will be checked for the GameOver_MainMenu button
                    Continue.checkForInputContinue(pygame.mouse.get_pos())
                    # Inputs will be checked for the Continue button

            GameOver_MainMenu.update()
            # Updating the GameOver_MainMenu button
            Continue.update()
            # Updating the Continue button
                    
            pygame.display.update()
        pygame.quit()
    pygame.display.update()
    # Updating and quitting the game

    def text(Count):
    # Defining the text function; passing Count as a parameter
     if Count >=1 and Count <= 9:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render("0"+ Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     elif Count > 9:
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render(Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text = sub_font.render("00", True, "white")
         # Creating a text variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text_rect = text.get_rect(center=(170, 20))
         # Defining text_rect, which will store the position of the text on the screen
         screen.blit(text, text_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()
    
    def text2(life_count):
    # Defining the text2 function; passing Count as a parameter
     if life_count >=1:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(life_count)
        # Convert Count integer into a string, storing it under Count1
        text2 = sub_font.render("0"+ Count1, True, "white")
        # Creating a text2 variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text2_rect = text2.get_rect(center=(75,20))
        # Defining text2_rect, which will store the position of the text on the screen
        screen.blit(text2, text2_rect)
        # Blitting both the text and its respective position, onto the screen
        life_count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text2 = sub_font.render("00", True, "white")
         # Creating a text2 variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text2_rect = text2.get_rect(center=(75,20))
         # Defining text_rect2, which will store the position of the text on the screen
         screen.blit(text2, text2_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()

    if Music == True:
    # If the Music variable is equal to True
        PauseMusic(Music)
        # Main Menu music is paused
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        # Level 1 Music is loaded
        pygame.mixer.music.play(-1)
        # Music track is looped indefinitely
        PlayMusic(Music)
        # PlayMusic function is called
        global LevelSelectorMusic
        # LevelSelectorMusic variable set to a global variable
        LevelSelectorMusic = True
        # LevelSelectorMusic set to True
    else:
    # If the Music Variable is equal to False
        PauseMusic(Music)
        # PlayMusic function is called
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        pygame.mixer.music.play(-1)
        # Level Selector Music is loaded and looped
        PauseMusic(Music)
        # Music is paused

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    # Using Width and Height variables to set size of Window

    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
    # Defining flip function, which flips the sprite left/right, depending on what direction the player is facing

    def load_sprite_sheets(dir1, width, height, direction=False):
        path = join("General", dir1)
        # Creating the path variable, to join the assets in the: "Assets" folder to directory 1
        images = [f for f in listdir(path) if isfile(join(path, f))]
        # Dividing each individual image from the main image into seperate divisons
        
        all_sprites = {}
        # Defining the all_sprites dictionary, where all sprites will be stored

        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            # Creating a for loop for each image within the sprite sheet; joining path and image variables and converting into alpha form
            sprites = []
            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0,0), rect)
                sprites.append(pygame.transform.scale2x(surface))
            # Scaling the sprite to the size of the player character

            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
            # Left sprite loaded, when facing left direction
            # Right sprite loaded, when facing right direction
            else:
                all_sprites[image.replace(".png", "")] = sprites
            # Condition for else; replacing ".png" with "" for all sprites (Default Sprite)

        return all_sprites
        # Returning all sprites that are required, depending on player movement

    def get_block(size):
    # Defining the get_block() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(96, 0, size, size)
        # Specifically loading the grass block image in its full size, using (96,0) coordinates / Brick blocks = (272, 64)
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of block is doubled from previously-declared size

    def get_bricks(size):
    # Defining the get_brick() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(272, 64, size, size)
        # Specifically loading the brick image in its full size, using (272, 64) coordinates
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of brick is doubled from previously-declared size

    class Player(pygame.sprite.Sprite):
    # Creating the Player class
        COLOR = (255, 0, 0)
        # The Player will firstly be a square. The COLOR Variable defines what colour the player will be (Currently Red)
        GRAVITY = 1
        # Setting the GRAVITY Variable to 1
        SPRITES = load_sprite_sheets("MaskDude", 32, 32, True)
        # Variable to call function, to load sprite with direction
        ANIMATION_DELAY = 3
        # Variable to account for delay in animation of sprites

        def __init__(self, x, y, width, height):
            super().__init__()
            self.rect = pygame.Rect(x, y, width, height)
            self.x_vel = 0
            self.y_vel = 0
            self.mask = None
            self.direction = "left"
            self.animation_count = 0
            self.fall_count = 0
            self.jump_count = 0
            self.hit = False
            self.hit_count = 0
        # The __init__ method of the Player class is defined to create key variables that define the Player

        def jump(self):
        # Defining jump method
            self.y_vel = -self.GRAVITY * 8
            # Negative gravity multiplied by 8, in order for a constant speed of gravity to be implemented (Downwards Gravity)
            self.animation_count = 0
            self.jump_count += 1
            if self.jump_count == 1:
                self.fall_count = 0
            # As soon as the player jumps, any obtained gravity will be removed (Not a factor), and then gravity is applied after jumping
                
        def move(self, dx, dy):
            self.rect.x += dx
            self.rect.y += dy
        # The move method is defined to register player positions and movement (x and y values - However, no movement in the y-axis)

        def make_hit(self):
            self.hit = True
            self.hit_count = 0
        # The make_hit method is defined to register when the player has been hit

        def move_left(self, vel):
            self.x_vel = -vel
            if self.direction != "left":
                self.direction = "left"
                self.animation_count = 0
        # move_left method defined to register left player movements

        def move_right(self, vel):
            self.x_vel = vel
            if self.direction != "right":
                self.direction = "right"
                self.animation_count = 0
        # move_right method defined to register right player movements
        

        def loop(self, fps):
            self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
            self.move(self.x_vel, self.y_vel)
        # loop method defined to move player with set x and y velocities; y velocity now takes into account gravity (1)

            if self.hit:
            # Condition for if the player has been hit
                self.hit_count +=1
                # Adding one to the counter of time being hit for 
            if self.hit_count > fps * 2:
            # Condition for after being in the hit state for greater than 2 seconds
                self.hit = False
                global life_count
                life_count = life_count -1
                # Player is no longer in the hit state
                self.hit_count = 0
                # hit Counter being set to 0

            self.fall_count += 1 
            # Adding 1 to the fall count, as the player as still currently falling, if the method has been executed
            self.update_sprite()
            # Update sprite

        def landed(self):
        # Method for the player to land on a block
            self.fall_count = 0
            # Set to 0, to stop adding gravity
            self.y_vel = 0
            # No upwards or downwards velocity
            self.jump_count = 0
            # Not jumping (Uesful for double-jumps)

        def hit_head(self):
        # Method for the player to hit their head on a block
            self.count = 0
            # Set to 0
            self.y_vel *= -1
            # Velocity is reversed (Moving downwards, rather than upwards)

        def update_sprite(self):
        # Method to update sprites, depending on if running or idle
            sprite_sheet = "idle"
            # Default sprite sheet, if player is not moving
            if self.hit:
            # If the player has been hit
                sprite_sheet = "hit"
                # Load the hit sprite sheet
            if self.y_vel < 0:
            # If velocity is less than 0 (Moving upwards)
                if self.jump_count == 1:
                    sprite_sheet = "jump"
                # If this is the player's first jump, normal jump animation will be featured
                elif self.jump_count == 2:
                    sprite_sheet = "double_jump"
                # If this is the player's second jump, the double jump animation will be featured
            elif self.y_vel > self.GRAVITY * 2:
            # If velocity is greater than gravity * 2 (Moving downwards)
                sprite_sheet = "fall"
                # If player is moving down, then fall animation will be loaded
            elif self.x_vel != 0:
                sprite_sheet = "run"
            # If x velocity is not 0, then running animations will be loaded

            sprite_sheet_name = sprite_sheet + "_" + self.direction
            sprites = self.SPRITES[sprite_sheet_name]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.sprite = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.update()
            # Calling update method

        def update(self):
        # Defining update method
            self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.sprite)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

        def draw(self, win, offset_x):
            win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
        # draw method defined to redraw the current figure in a given position

    # End of the Player class

    class Object(pygame.sprite.Sprite):
    # Creating the Object class (Base class for all objects, so that collision is uniform across all)
    # Inherits from the Sprite class
        def __init__(self, x, y, width, height, name=None):
            super().__init__()
            # Initialising Superclass (pygame.sprite.Sprite)
            self.rect = pygame.Rect(x, y, width, height)
            # Defining Rectangle for a valid sprite
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            # Defining Object image (Supports transparrent images)
            self.width = width
            self.height = height
            self.name = name
            # Defining self variables

        def draw(self, win, offset_x):
            win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        # Draw function automatically draws Object instantly on the screen

    class Coin(Object):
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "coins")
            # Calling super-initialiser (Name is being passed; allows for later checks if coin has been collided with)
            self.coins = load_sprite_sheets("Coins", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.coins["Coin"][0]
            # Loading the Coin animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work)

    class Block(Object):
    # Creating Block class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            block = get_block(size)
            # variable that stores a function to retrieve the size of a block
            self.image.blit(block, (0,0))
            # Block is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Brick(Object):
    # Creating Brick class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            brick = get_bricks(size)
            # variable that stores a function to retrieve the size of a brick (same as a block)
            self.image.blit(brick, (0,0))
            # Brick is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Fire(Object):
    # Creating Fire class - Inherits from Object class
        ANIMATION_DELAY = 3
        # Defining local variable, to account for delay in the animations
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "fire")
            # Calling super-initialiser (Name is being passed; allows for later checks if fire has been hit)
            self.fire = load_sprite_sheets("Fire", width, height)
            # Loading sprites for fire
            self.image = self.fire["off"][0]
            # Specifying image (Fire begins as being off)
            self.mask = pygame.mask.from_surface(self.image)
            # Creating the mask for the fire sprite
            self.animation_count = 0
            # Defining animation count (Same as player)
            self.animation_name = "off"
            # Off animation is automatically played

        def on(self):
        # Defining On method
            self.animation_name = "on"
            # On Fire Animation is played

        def off(self):
        # Defining Off method
            self.animation_name = "off"
            # Off Fire Animation is played

        def loop(self):
            sprites = self.fire[self.animation_name]
            # Defining local variable sprites to store all fire sprites
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.image = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

            if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            # Animation count for fire will continue no matter what; if it gets too high, it will cause the game to lag - This condition prevents it from becomming too high
                self.animation_count = 0
                # Animation count is reset

    class Spikes(Object):
    # Creating the Spikes class (Sub-class of the Object superclass)

        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "spikes")
            # Calling super-initialiser (Name is being passed; allows for later checks if spikes have been hit)
            self.spikes = load_sprite_sheets("Spikes", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.spikes["Idle"][0]
            # Loading the idle spike animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included

    def get_background():
    # get_background() function is defined

        image = pygame.image.load("C:/Users/olive/OneDrive/Desktop/A-Level Work/Computer Science/NEA/NEA Work/Design - Resources/8-bit Game Assets/Main Menu/Level3 Background.jpg")
        _, _, width, height = image.get_rect()
        tiles = []
        # Defining the get_background() method, to directly load a background image into the game

        for i in range(WIDTH // width + 1):
            for j in range(HEIGHT // height + 1):
                pos = (i * width, j * height)
                tiles.append(pos)
        # Dividing the background into individual tiles, before reforming them, based on the size of the Window

        return tiles, image
        # Returning the tiles array and the image variable

    def draw(window, background, bg_image, Player, objects, offset_x):
        for tile in background:
            window.blit(bg_image, tile)
    # Defining the draw method, which will use each tile of the background and place the respective part of the image overtop of it
    
        for obj in objects:
        # For loop created for each object within objects
            obj.draw(window, offset_x)
            # Object is drawn onto the window
        
        Player.draw(window, offset_x)
        # Using the window variable to add the background to the window

    def handle_vertical_collision(player, objects, dy):
    # Seperate handling of vertical collision (Function)
        collided_objects = []
        # List to keep track of what objects have been collided with
        for obj in objects:
        # For loop (Objects that can be collided with)
            if pygame.sprite.collide_mask(player, obj):
            # Determines if 2 objects are colliding (Player and Block sprites)
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    # Bottom of object equals top of object; prevents player clipping inside of the object
                    player.landed()
                    # Method call
                # If player collides with top of object, bottom of player is set on-top of the object
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    # Top of object equals bottom of object; prevents player clipping inside of the object
                    player.hit_head()
                    # Method call
                # If player collides with bottom of object

                collided_objects.append(obj)
                # Add collided object to list

        return collided_objects
        # Returns collided objects, to determine what type of object has been collided with

    def collide(player, objects, dx):
    # Defining collide function (For horizontal collision)
        player.move(dx, 0)
        # Player moved in displacement-x direction; checking that if the player was to move left/right, would they hit a block?
        player.update()
        # Updating rectangle and player mask
        collided_object = None
        # No current collided object
        for obj in objects:
            if pygame.sprite.collide_mask(player,obj):
            # If an object collides with the updated mask
                collided_object = obj
                # obj is colliding with player
                break

        player.move(-dx, 0)
        # Player moved back to original spot
        player.update()
        # Updating rectangle and mask back to original
        return collided_object
        # If object will collide with player. return the object / If not, no item will be returned

    def handle_move(player, objects):
        keys = pygame.key.get_pressed()
    # Defining the handle_move procedure, which will register when the player enters specific keys that will allow them to move their character

        player.x_vel = 0
        vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
        collide_left = collide(player, objects, -PLAYER_VEL * 2)
        # Checking if player will collide with an object to their left
        collide_right = collide(player, objects, PLAYER_VEL * 2)
        # Checking if player will collide with an object to their right

        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)
        if keys[pygame.K_a] and not collide_right:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_d] and not collide_right:
            player.move_right(PLAYER_VEL) 
        # If left arrow click (and no potential block collisions), player moves left
        # If right arrow click (and no potential block collisions), player moves right

        vertical = [*vertical_collide]
        horizontal = [collide_left, collide_right]
        # Conditions to be checked (Left, right, and vertical collisions)

        for obj in vertical:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "fire":
            # If the player has collided with fire
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                global Count
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen

        for obj in horizontal:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen
                
    def main(window):
        clock = pygame.time.Clock()
        background, bg_image = get_background()
    # Defining main window of the game, and creating clock and background / bg_image variables
        block_size = 96
        # Defining the block_size variable, for later use in declaring the sizes of blocks
        player = Player(100, 100, 50, 50)
        # Creating an instance of the Player class
        fire = Fire(2915, HEIGHT - block_size - 350, 16, 32)
        # Defining fire variable and calling the Fire class
        fire.on()
        # Fire is always on
        spikes = Spikes(1410, HEIGHT - block_size - 30, 16, 32)
        spikes2 = Spikes(1375, HEIGHT - block_size - 30, 16, 32)
        spikes3 = Spikes(1340, HEIGHT - block_size - 30, 16, 32)
        spikes4 = Spikes(1305, HEIGHT - block_size - 30, 16, 32)
        spikes5 = Spikes(1270, HEIGHT - block_size - 30, 16, 32)
        spikes6 = Spikes(1254, HEIGHT - block_size - 30, 16, 32)
        spikes7 = Spikes(block_size * 40, HEIGHT - block_size - 30, 16, 32)
        spikes8 = Spikes((block_size * 40) + 35, HEIGHT - block_size - 30, 16, 32)
        spikes9 = Spikes((block_size * 40) + 70, HEIGHT - block_size - 30, 16, 32)
        spikes10 = Spikes((block_size * 41) - 8.2, HEIGHT - block_size - 30, 16, 32)
        spikes11 = Spikes((block_size * 41) + 26.8, HEIGHT - block_size - 30, 16, 32)
        spikes12 = Spikes((block_size * 41) + 61.8, HEIGHT - block_size - 30, 16, 32)
        coin = Coin(300, HEIGHT - block_size - 64, 16, 32)
        coin2 = Coin(400, HEIGHT - block_size - 64, 16, 32)
        coin3= Coin(500, HEIGHT - block_size - 64, 16, 32)
        coin4 = Coin((block_size * 10) + 200, HEIGHT - block_size - 128, 16, 32)
        coin5 = Coin((block_size * 40), HEIGHT - block_size - 128, 16, 32)
        coin6 = Coin((block_size * 40) + 60, HEIGHT - block_size - 192, 16, 32)
        coin7 = Coin((block_size * 40) + 120, HEIGHT - block_size - 192, 16, 32)
        coin8 = Coin((block_size * 40) + 190, HEIGHT - block_size - 128, 16, 32)
        coin9 = Coin(block_size * 63, HEIGHT - block_size * 6.5, 16, 32)
        coin10 = Coin(block_size * 64, HEIGHT - block_size * 6.5, 16, 32)
        coin11 = Coin(block_size * 65, HEIGHT - block_size * 6.5, 16, 32)
        coin12 = Coin(block_size * 66, HEIGHT - block_size * 6.5, 16, 32)
        coin13 = Coin(block_size * 67, HEIGHT - block_size * 6.5, 16, 32)
        coin14 = Coin(block_size * 68, HEIGHT - block_size * 6.5, 16, 32)
        coin15 = Coin(block_size * 69, HEIGHT - block_size * 6.5, 16, 32)
        coin16 = Coin(block_size * 70, HEIGHT - block_size * 6.5, 16, 32)
        coin17 = Coin(block_size * 71, HEIGHT - block_size * 6.5, 16, 32)
        coin18 = Coin(block_size * 72, HEIGHT - block_size * 6.5, 16, 32)
        coin19 = Coin(block_size * 73, HEIGHT - block_size * 6.5, 16, 32)
        coin20 = Coin(block_size * 74, HEIGHT - block_size * 6.5, 16, 32)
        coin21 = Coin(block_size * 75, HEIGHT - block_size * 6.5, 16, 32)
        coin22 = Coin(block_size * 76, HEIGHT - block_size * 6.5, 16, 32)
        coin23 = Coin(block_size * 77, HEIGHT - block_size * 6.5, 16, 32)
        # Creating 12 instances of spikes and 23 instances of coins, each stored under a different variable name
        floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
        # Creating the floor variable; create a number of blocks that will be duplicated to the left and right of the initial block (Working, for a scrolling background)
        objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),  
                    Block(block_size * 10, HEIGHT - block_size * 3, block_size), Brick(block_size * 12, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 10, HEIGHT - block_size * 2, block_size), Block(block_size * 9, HEIGHT - block_size * 2, block_size), Block(block_size * 11, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 11, HEIGHT - block_size * 3, block_size), Block(block_size * 11, HEIGHT - block_size * 4, block_size), Block(block_size * 15, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 15, HEIGHT - block_size * 3, block_size), Block(block_size * 15, HEIGHT - block_size * 2, block_size), Block(block_size * 16, HEIGHT - block_size * 2, block_size), 
                    Block(block_size * 16, HEIGHT - block_size * 3, block_size), Block(block_size * 17, HEIGHT - block_size * 2, block_size), Brick(block_size * 24, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 25, HEIGHT - block_size * 3, block_size), Brick(block_size * 26, HEIGHT - block_size * 3, block_size), Brick(block_size * 25, HEIGHT - block_size * 5, block_size),
                    Brick(block_size * 29, HEIGHT - block_size * 4, block_size), Brick(block_size * 30, HEIGHT - block_size * 4, block_size), Brick(block_size * 31, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 36, HEIGHT - block_size * 3, block_size), Block(block_size * 37, HEIGHT - block_size * 3, block_size), Block(block_size * 38, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 37, HEIGHT - block_size * 4, block_size), Block(block_size * 38, HEIGHT - block_size * 4, block_size), Block(block_size * 39, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 38, HEIGHT - block_size * 5, block_size), Block(block_size * 39, HEIGHT - block_size * 5, block_size), Block(block_size * 40, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 41, HEIGHT - block_size * 5, block_size), Block(block_size * 42, HEIGHT - block_size * 5, block_size), Block(block_size * 43, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 42, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Block(block_size * 45, HEIGHT - block_size * 3, block_size), Block(block_size * 44, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Brick(block_size * 49, HEIGHT - block_size * 3, block_size), Brick(block_size * 50, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 49, HEIGHT - block_size * 2, block_size), Brick(block_size * 50, HEIGHT - block_size * 2, block_size), Brick(block_size * 48, HEIGHT - block_size * 2, block_size), 
                    Brick(block_size * 51, HEIGHT - block_size * 2, block_size), Brick(block_size * 53, HEIGHT - block_size * 3, block_size), Brick(block_size * 54, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 58, HEIGHT - block_size * 2, block_size), Block(block_size * 59, HEIGHT - block_size * 2, block_size), Block(block_size * 60, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 59, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 4, block_size),
                    Brick(block_size * 63, HEIGHT - block_size * 6, block_size), Brick(block_size * 64, HEIGHT - block_size * 6, block_size), Brick(block_size * 65, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 66, HEIGHT - block_size * 6, block_size), Brick(block_size * 67, HEIGHT - block_size * 6, block_size), Brick(block_size * 68, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 69, HEIGHT - block_size * 6, block_size), Brick(block_size * 70, HEIGHT - block_size * 6, block_size), Brick(block_size * 71, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 72, HEIGHT - block_size * 6, block_size), Brick(block_size * 73, HEIGHT - block_size * 6, block_size), Brick(block_size * 74, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 75, HEIGHT - block_size * 6, block_size), Brick(block_size * 76, HEIGHT - block_size * 6, block_size), Brick(block_size * 77, HEIGHT - block_size * 6, block_size),
                    fire, spikes, spikes2, spikes3, spikes4, spikes5, spikes6, spikes7, spikes8, spikes9, spikes10, spikes11, spikes12, coin, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                    coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22, coin23]
        # Floor broken into individual elements (that are added to the list)
        # Blocks / Bricks passed through (Coordinates) - y multiplied by a larger number, in order to be positioned higher on the screen
        # Block / Brick size passed through and all is stored in variable: objects
        # Fire variable passed through; fire is a sub-class of the superclass: Objects
        # All spikes are passed through; spikes are a sub-class of the superclass: Objects
        
        offset_x = 0
        # Stores by how much the screen is currently offset (How much it has moved to the left/right)
        scroll_area_width = 300
        # Amount of pixels to the left/ right, for the game to start scrolling

        run = True
        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
        # Allows the player to load the game and quit the game
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
                    # If space bar is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_UP and player.jump_count < 2:
                        player.jump()
                    # If up arrow key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_w and player.jump_count < 2:
                        player.jump()
                    # If the W key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_p:
                        x = Pause_Game3()
                        print(x)
                    # If: 'p' is pressed, the pause menu will be loaded

            player.loop(FPS)
            fire.loop()
            handle_move(player, objects)
            draw(window, background, bg_image, player, objects, offset_x)
            texts = text(Count)
            print(texts)
            texts2 = text2(life_count)
            print(texts2)
            screen.blit((Lives), (22, 2))
            screen.blit((CoinImage), (120, 8))
            # Drawing the player, background, objects and the offset into the game

            if life_count <= 0:
                x = game_over()
                print(x)
            # If the player's life count is at 0, the game_over function will be printed

            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and (player.x_vel > 0)) or ((player.rect.left - offset_x <= scroll_area_width) and (player.x_vel < 0)):
            # If player is over the pixel limit to what is being shown on the window (Left and Right sides)
                offset_x += player.x_vel
                # Offset by the velocity of how much the player moved to the right

            if (player.rect.right >= 7500):
                # If the player's right directional movement exceeds 7500 pixels
                if Music == True:
                        x = play(True)
                        print(x)
                # If Music is True, play() function will be loaded with music
                else:
                    x = play(False)
                    print(x)
                # If Music is False, play() function will be loaded without music

            pygame.display.update()

        pygame.quit()
        quit()
        # Quitting the pygame program

    if __name__ == "__main__":
        main(window)
    # Calling main(window), if the player has just loaded the game

def FourthLevel():
# Function, when the first level has been selected to be played

    pygame.display.set_caption("Velocity - Level #4")
    # Setting the caption of the Pygame Window, to: 'Velocity - Level #1'

    BG_COLOR = (255, 255, 255)
    WIDTH = 1500
    HEIGHT = 800
    FPS = 60
    PLAYER_VEL = 5
    # Defining key Variables (Caps to not interfere with any later-declared similar variables)

    def game_over():
    # Defining the game_over function
        global life_count
        # Setting the life_count variable to a global variable
        life_count = 3
        # Setting the life_count variable to 3
        GameOver = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Game Over Screen.png')
        # Defining the GameOver variable to load the background image (The Game Over Screen)
        screen.blit((GameOver), (0, 0))
        # Blitting the Game Over Screen onto the screen
        gameover = True
        # setting the gameover variable to true
        if Music == True:
        # If there is music present in the game
            pygame.mixer.music.stop()
            # Current music is paused
            pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/GameOverMusic.mp3")
            pygame.mixer.music.play()
            # Game Over music is loaded and played
        while gameover:
        # While the program is in the gameover state
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                    pygame.quit()
                    # The game will quit (end)
                if event.type == pygame.MOUSEBUTTONDOWN:
                # if the player has pressed the right mouse button down
                    GameOver_MainMenu.checkForInputGameOver(pygame.mouse.get_pos())
                    # Inputs will be checked for the GameOver_MainMenu button
                    Continue.checkForInputContinue(pygame.mouse.get_pos())
                    # Inputs will be checked for the Continue button

            GameOver_MainMenu.update()
            # Updating the GameOver_MainMenu button
            Continue.update()
            # Updating the Continue button
                    
            pygame.display.update()
        pygame.quit()
    pygame.display.update()
    # Updating and quitting the game

    def text(Count):
    # Defining the text function; passing Count as a parameter
     if Count >=1 and Count <= 9:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render("0"+ Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     elif Count > 9:
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render(Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text = sub_font.render("00", True, "white")
         # Creating a text variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text_rect = text.get_rect(center=(170, 20))
         # Defining text_rect, which will store the position of the text on the screen
         screen.blit(text, text_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()
    
    def text2(life_count):
    # Defining the text2 function; passing Count as a parameter
     if life_count >=1:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(life_count)
        # Convert Count integer into a string, storing it under Count1
        text2 = sub_font.render("0"+ Count1, True, "white")
        # Creating a text2 variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text2_rect = text2.get_rect(center=(75,20))
        # Defining text2_rect, which will store the position of the text on the screen
        screen.blit(text2, text2_rect)
        # Blitting both the text and its respective position, onto the screen
        life_count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text2 = sub_font.render("00", True, "white")
         # Creating a text2 variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text2_rect = text2.get_rect(center=(75,20))
         # Defining text_rect2, which will store the position of the text on the screen
         screen.blit(text2, text2_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()

    if Music == True:
    # If the Music variable is equal to True
        PauseMusic(Music)
        # Main Menu music is paused
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        # Level 1 Music is loaded
        pygame.mixer.music.play(-1)
        # Music track is looped indefinitely
        PlayMusic(Music)
        # PlayMusic function is called
        global LevelSelectorMusic
        # LevelSelectorMusic variable set to a global variable
        LevelSelectorMusic = True
        # LevelSelectorMusic set to True
    else:
    # If the Music Variable is equal to False
        PauseMusic(Music)
        # PlayMusic function is called
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        pygame.mixer.music.play(-1)
        # Level Selector Music is loaded and looped
        PauseMusic(Music)
        # Music is paused

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    # Using Width and Height variables to set size of Window

    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
    # Defining flip function, which flips the sprite left/right, depending on what direction the player is facing

    def load_sprite_sheets(dir1, width, height, direction=False):
        path = join("General", dir1)
        # Creating the path variable, to join the assets in the: "Assets" folder to directory 1
        images = [f for f in listdir(path) if isfile(join(path, f))]
        # Dividing each individual image from the main image into seperate divisons
        
        all_sprites = {}
        # Defining the all_sprites dictionary, where all sprites will be stored

        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            # Creating a for loop for each image within the sprite sheet; joining path and image variables and converting into alpha form
            sprites = []
            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0,0), rect)
                sprites.append(pygame.transform.scale2x(surface))
            # Scaling the sprite to the size of the player character

            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
            # Left sprite loaded, when facing left direction
            # Right sprite loaded, when facing right direction
            else:
                all_sprites[image.replace(".png", "")] = sprites
            # Condition for else; replacing ".png" with "" for all sprites (Default Sprite)

        return all_sprites
        # Returning all sprites that are required, depending on player movement

    def get_block(size):
    # Defining the get_block() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(96, 0, size, size)
        # Specifically loading the grass block image in its full size, using (96,0) coordinates / Brick blocks = (272, 64)
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of block is doubled from previously-declared size

    def get_bricks(size):
    # Defining the get_brick() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(272, 64, size, size)
        # Specifically loading the brick image in its full size, using (272, 64) coordinates
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of brick is doubled from previously-declared size

    class Player(pygame.sprite.Sprite):
    # Creating the Player class
        COLOR = (255, 0, 0)
        # The Player will firstly be a square. The COLOR Variable defines what colour the player will be (Currently Red)
        GRAVITY = 1
        # Setting the GRAVITY Variable to 1
        SPRITES = load_sprite_sheets("MaskDude", 32, 32, True)
        # Variable to call function, to load sprite with direction
        ANIMATION_DELAY = 3
        # Variable to account for delay in animation of sprites

        def __init__(self, x, y, width, height):
            super().__init__()
            self.rect = pygame.Rect(x, y, width, height)
            self.x_vel = 0
            self.y_vel = 0
            self.mask = None
            self.direction = "left"
            self.animation_count = 0
            self.fall_count = 0
            self.jump_count = 0
            self.hit = False
            self.hit_count = 0
        # The __init__ method of the Player class is defined to create key variables that define the Player

        def jump(self):
        # Defining jump method
            self.y_vel = -self.GRAVITY * 8
            # Negative gravity multiplied by 8, in order for a constant speed of gravity to be implemented (Downwards Gravity)
            self.animation_count = 0
            self.jump_count += 1
            if self.jump_count == 1:
                self.fall_count = 0
            # As soon as the player jumps, any obtained gravity will be removed (Not a factor), and then gravity is applied after jumping
                
        def move(self, dx, dy):
            self.rect.x += dx
            self.rect.y += dy
        # The move method is defined to register player positions and movement (x and y values - However, no movement in the y-axis)

        def make_hit(self):
            self.hit = True
            self.hit_count = 0
        # The make_hit method is defined to register when the player has been hit

        def move_left(self, vel):
            self.x_vel = -vel
            if self.direction != "left":
                self.direction = "left"
                self.animation_count = 0
        # move_left method defined to register left player movements

        def move_right(self, vel):
            self.x_vel = vel
            if self.direction != "right":
                self.direction = "right"
                self.animation_count = 0
        # move_right method defined to register right player movements
        

        def loop(self, fps):
            self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
            self.move(self.x_vel, self.y_vel)
        # loop method defined to move player with set x and y velocities; y velocity now takes into account gravity (1)

            if self.hit:
            # Condition for if the player has been hit
                self.hit_count +=1
                # Adding one to the counter of time being hit for 
            if self.hit_count > fps * 2:
            # Condition for after being in the hit state for greater than 2 seconds
                self.hit = False
                global life_count
                life_count = life_count -1
                # Player is no longer in the hit state
                self.hit_count = 0
                # hit Counter being set to 0

            self.fall_count += 1 
            # Adding 1 to the fall count, as the player as still currently falling, if the method has been executed
            self.update_sprite()
            # Update sprite

        def landed(self):
        # Method for the player to land on a block
            self.fall_count = 0
            # Set to 0, to stop adding gravity
            self.y_vel = 0
            # No upwards or downwards velocity
            self.jump_count = 0
            # Not jumping (Uesful for double-jumps)

        def hit_head(self):
        # Method for the player to hit their head on a block
            self.count = 0
            # Set to 0
            self.y_vel *= -1
            # Velocity is reversed (Moving downwards, rather than upwards)

        def update_sprite(self):
        # Method to update sprites, depending on if running or idle
            sprite_sheet = "idle"
            # Default sprite sheet, if player is not moving
            if self.hit:
            # If the player has been hit
                sprite_sheet = "hit"
                # Load the hit sprite sheet
            if self.y_vel < 0:
            # If velocity is less than 0 (Moving upwards)
                if self.jump_count == 1:
                    sprite_sheet = "jump"
                # If this is the player's first jump, normal jump animation will be featured
                elif self.jump_count == 2:
                    sprite_sheet = "double_jump"
                # If this is the player's second jump, the double jump animation will be featured
            elif self.y_vel > self.GRAVITY * 2:
            # If velocity is greater than gravity * 2 (Moving downwards)
                sprite_sheet = "fall"
                # If player is moving down, then fall animation will be loaded
            elif self.x_vel != 0:
                sprite_sheet = "run"
            # If x velocity is not 0, then running animations will be loaded

            sprite_sheet_name = sprite_sheet + "_" + self.direction
            sprites = self.SPRITES[sprite_sheet_name]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.sprite = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.update()
            # Calling update method

        def update(self):
        # Defining update method
            self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.sprite)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

        def draw(self, win, offset_x):
            win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
        # draw method defined to redraw the current figure in a given position

    # End of the Player class

    class Object(pygame.sprite.Sprite):
    # Creating the Object class (Base class for all objects, so that collision is uniform across all)
    # Inherits from the Sprite class
        def __init__(self, x, y, width, height, name=None):
            super().__init__()
            # Initialising Superclass (pygame.sprite.Sprite)
            self.rect = pygame.Rect(x, y, width, height)
            # Defining Rectangle for a valid sprite
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            # Defining Object image (Supports transparrent images)
            self.width = width
            self.height = height
            self.name = name
            # Defining self variables

        def draw(self, win, offset_x):
            win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        # Draw function automatically draws Object instantly on the screen

    class Coin(Object):
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "coins")
            # Calling super-initialiser (Name is being passed; allows for later checks if coin has been collided with)
            self.coins = load_sprite_sheets("Coins", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.coins["Coin"][0]
            # Loading the Coin animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work)

    class Block(Object):
    # Creating Block class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            block = get_block(size)
            # variable that stores a function to retrieve the size of a block
            self.image.blit(block, (0,0))
            # Block is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Brick(Object):
    # Creating Brick class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            brick = get_bricks(size)
            # variable that stores a function to retrieve the size of a brick (same as a block)
            self.image.blit(brick, (0,0))
            # Brick is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Fire(Object):
    # Creating Fire class - Inherits from Object class
        ANIMATION_DELAY = 3
        # Defining local variable, to account for delay in the animations
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "fire")
            # Calling super-initialiser (Name is being passed; allows for later checks if fire has been hit)
            self.fire = load_sprite_sheets("Fire", width, height)
            # Loading sprites for fire
            self.image = self.fire["off"][0]
            # Specifying image (Fire begins as being off)
            self.mask = pygame.mask.from_surface(self.image)
            # Creating the mask for the fire sprite
            self.animation_count = 0
            # Defining animation count (Same as player)
            self.animation_name = "off"
            # Off animation is automatically played

        def on(self):
        # Defining On method
            self.animation_name = "on"
            # On Fire Animation is played

        def off(self):
        # Defining Off method
            self.animation_name = "off"
            # Off Fire Animation is played

        def loop(self):
            sprites = self.fire[self.animation_name]
            # Defining local variable sprites to store all fire sprites
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.image = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

            if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            # Animation count for fire will continue no matter what; if it gets too high, it will cause the game to lag - This condition prevents it from becomming too high
                self.animation_count = 0
                # Animation count is reset

    class Spikes(Object):
    # Creating the Spikes class (Sub-class of the Object superclass)

        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "spikes")
            # Calling super-initialiser (Name is being passed; allows for later checks if spikes have been hit)
            self.spikes = load_sprite_sheets("Spikes", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.spikes["Idle"][0]
            # Loading the idle spike animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included

    def get_background():
    # get_background() function is defined

        image = pygame.image.load("C:/Users/olive/OneDrive/Desktop/A-Level Work/Computer Science/NEA/NEA Work/Design - Resources/8-bit Game Assets/Main Menu/Level4 Background.jpg")
        _, _, width, height = image.get_rect()
        tiles = []
        # Defining the get_background() method, to directly load a background image into the game

        for i in range(WIDTH // width + 1):
            for j in range(HEIGHT // height + 1):
                pos = (i * width, j * height)
                tiles.append(pos)
        # Dividing the background into individual tiles, before reforming them, based on the size of the Window

        return tiles, image
        # Returning the tiles array and the image variable

    def draw(window, background, bg_image, Player, objects, offset_x):
        for tile in background:
            window.blit(bg_image, tile)
    # Defining the draw method, which will use each tile of the background and place the respective part of the image overtop of it
    
        for obj in objects:
        # For loop created for each object within objects
            obj.draw(window, offset_x)
            # Object is drawn onto the window
        
        Player.draw(window, offset_x)
        # Using the window variable to add the background to the window

    def handle_vertical_collision(player, objects, dy):
    # Seperate handling of vertical collision (Function)
        collided_objects = []
        # List to keep track of what objects have been collided with
        for obj in objects:
        # For loop (Objects that can be collided with)
            if pygame.sprite.collide_mask(player, obj):
            # Determines if 2 objects are colliding (Player and Block sprites)
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    # Bottom of object equals top of object; prevents player clipping inside of the object
                    player.landed()
                    # Method call
                # If player collides with top of object, bottom of player is set on-top of the object
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    # Top of object equals bottom of object; prevents player clipping inside of the object
                    player.hit_head()
                    # Method call
                # If player collides with bottom of object

                collided_objects.append(obj)
                # Add collided object to list

        return collided_objects
        # Returns collided objects, to determine what type of object has been collided with

    def collide(player, objects, dx):
    # Defining collide function (For horizontal collision)
        player.move(dx, 0)
        # Player moved in displacement-x direction; checking that if the player was to move left/right, would they hit a block?
        player.update()
        # Updating rectangle and player mask
        collided_object = None
        # No current collided object
        for obj in objects:
            if pygame.sprite.collide_mask(player,obj):
            # If an object collides with the updated mask
                collided_object = obj
                # obj is colliding with player
                break

        player.move(-dx, 0)
        # Player moved back to original spot
        player.update()
        # Updating rectangle and mask back to original
        return collided_object
        # If object will collide with player. return the object / If not, no item will be returned

    def handle_move(player, objects):
        keys = pygame.key.get_pressed()
    # Defining the handle_move procedure, which will register when the player enters specific keys that will allow them to move their character

        player.x_vel = 0
        vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
        collide_left = collide(player, objects, -PLAYER_VEL * 2)
        # Checking if player will collide with an object to their left
        collide_right = collide(player, objects, PLAYER_VEL * 2)
        # Checking if player will collide with an object to their right

        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)
        if keys[pygame.K_a] and not collide_right:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_d] and not collide_right:
            player.move_right(PLAYER_VEL) 
        # If left arrow click (and no potential block collisions), player moves left
        # If right arrow click (and no potential block collisions), player moves right

        vertical = [*vertical_collide]
        horizontal = [collide_left, collide_right]
        # Conditions to be checked (Left, right, and vertical collisions)

        for obj in vertical:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "fire":
            # If the player has collided with fire
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                global Count
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen

        for obj in horizontal:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen
                
    def main(window):
        clock = pygame.time.Clock()
        background, bg_image = get_background()
    # Defining main window of the game, and creating clock and background / bg_image variables
        block_size = 96
        # Defining the block_size variable, for later use in declaring the sizes of blocks
        player = Player(100, 100, 50, 50)
        # Creating an instance of the Player class
        fire = Fire(2915, HEIGHT - block_size - 350, 16, 32)
        # Defining fire variable and calling the Fire class
        fire.on()
        # Fire is always on
        spikes = Spikes(1410, HEIGHT - block_size - 30, 16, 32)
        spikes2 = Spikes(1375, HEIGHT - block_size - 30, 16, 32)
        spikes3 = Spikes(1340, HEIGHT - block_size - 30, 16, 32)
        spikes4 = Spikes(1305, HEIGHT - block_size - 30, 16, 32)
        spikes5 = Spikes(1270, HEIGHT - block_size - 30, 16, 32)
        spikes6 = Spikes(1254, HEIGHT - block_size - 30, 16, 32)
        spikes7 = Spikes(block_size * 40, HEIGHT - block_size - 30, 16, 32)
        spikes8 = Spikes((block_size * 40) + 35, HEIGHT - block_size - 30, 16, 32)
        spikes9 = Spikes((block_size * 40) + 70, HEIGHT - block_size - 30, 16, 32)
        spikes10 = Spikes((block_size * 41) - 8.2, HEIGHT - block_size - 30, 16, 32)
        spikes11 = Spikes((block_size * 41) + 26.8, HEIGHT - block_size - 30, 16, 32)
        spikes12 = Spikes((block_size * 41) + 61.8, HEIGHT - block_size - 30, 16, 32)
        coin = Coin(300, HEIGHT - block_size - 64, 16, 32)
        coin2 = Coin(400, HEIGHT - block_size - 64, 16, 32)
        coin3= Coin(500, HEIGHT - block_size - 64, 16, 32)
        coin4 = Coin((block_size * 10) + 200, HEIGHT - block_size - 128, 16, 32)
        coin5 = Coin((block_size * 40), HEIGHT - block_size - 128, 16, 32)
        coin6 = Coin((block_size * 40) + 60, HEIGHT - block_size - 192, 16, 32)
        coin7 = Coin((block_size * 40) + 120, HEIGHT - block_size - 192, 16, 32)
        coin8 = Coin((block_size * 40) + 190, HEIGHT - block_size - 128, 16, 32)
        coin9 = Coin(block_size * 63, HEIGHT - block_size * 6.5, 16, 32)
        coin10 = Coin(block_size * 64, HEIGHT - block_size * 6.5, 16, 32)
        coin11 = Coin(block_size * 65, HEIGHT - block_size * 6.5, 16, 32)
        coin12 = Coin(block_size * 66, HEIGHT - block_size * 6.5, 16, 32)
        coin13 = Coin(block_size * 67, HEIGHT - block_size * 6.5, 16, 32)
        coin14 = Coin(block_size * 68, HEIGHT - block_size * 6.5, 16, 32)
        coin15 = Coin(block_size * 69, HEIGHT - block_size * 6.5, 16, 32)
        coin16 = Coin(block_size * 70, HEIGHT - block_size * 6.5, 16, 32)
        coin17 = Coin(block_size * 71, HEIGHT - block_size * 6.5, 16, 32)
        coin18 = Coin(block_size * 72, HEIGHT - block_size * 6.5, 16, 32)
        coin19 = Coin(block_size * 73, HEIGHT - block_size * 6.5, 16, 32)
        coin20 = Coin(block_size * 74, HEIGHT - block_size * 6.5, 16, 32)
        coin21 = Coin(block_size * 75, HEIGHT - block_size * 6.5, 16, 32)
        coin22 = Coin(block_size * 76, HEIGHT - block_size * 6.5, 16, 32)
        coin23 = Coin(block_size * 77, HEIGHT - block_size * 6.5, 16, 32)
        # Creating 12 instances of spikes and 23 instances of coins, each stored under a different variable name
        floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
        # Creating the floor variable; create a number of blocks that will be duplicated to the left and right of the initial block (Working, for a scrolling background)
        objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),  
                    Block(block_size * 10, HEIGHT - block_size * 3, block_size), Brick(block_size * 12, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 10, HEIGHT - block_size * 2, block_size), Block(block_size * 9, HEIGHT - block_size * 2, block_size), Block(block_size * 11, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 11, HEIGHT - block_size * 3, block_size), Block(block_size * 11, HEIGHT - block_size * 4, block_size), Block(block_size * 15, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 15, HEIGHT - block_size * 3, block_size), Block(block_size * 15, HEIGHT - block_size * 2, block_size), Block(block_size * 16, HEIGHT - block_size * 2, block_size), 
                    Block(block_size * 16, HEIGHT - block_size * 3, block_size), Block(block_size * 17, HEIGHT - block_size * 2, block_size), Brick(block_size * 24, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 25, HEIGHT - block_size * 3, block_size), Brick(block_size * 26, HEIGHT - block_size * 3, block_size), Brick(block_size * 25, HEIGHT - block_size * 5, block_size),
                    Brick(block_size * 29, HEIGHT - block_size * 4, block_size), Brick(block_size * 30, HEIGHT - block_size * 4, block_size), Brick(block_size * 31, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 36, HEIGHT - block_size * 3, block_size), Block(block_size * 37, HEIGHT - block_size * 3, block_size), Block(block_size * 38, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 37, HEIGHT - block_size * 4, block_size), Block(block_size * 38, HEIGHT - block_size * 4, block_size), Block(block_size * 39, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 38, HEIGHT - block_size * 5, block_size), Block(block_size * 39, HEIGHT - block_size * 5, block_size), Block(block_size * 40, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 41, HEIGHT - block_size * 5, block_size), Block(block_size * 42, HEIGHT - block_size * 5, block_size), Block(block_size * 43, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 42, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Block(block_size * 45, HEIGHT - block_size * 3, block_size), Block(block_size * 44, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Brick(block_size * 49, HEIGHT - block_size * 3, block_size), Brick(block_size * 50, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 49, HEIGHT - block_size * 2, block_size), Brick(block_size * 50, HEIGHT - block_size * 2, block_size), Brick(block_size * 48, HEIGHT - block_size * 2, block_size), 
                    Brick(block_size * 51, HEIGHT - block_size * 2, block_size), Brick(block_size * 53, HEIGHT - block_size * 3, block_size), Brick(block_size * 54, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 58, HEIGHT - block_size * 2, block_size), Block(block_size * 59, HEIGHT - block_size * 2, block_size), Block(block_size * 60, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 59, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 4, block_size),
                    Brick(block_size * 63, HEIGHT - block_size * 6, block_size), Brick(block_size * 64, HEIGHT - block_size * 6, block_size), Brick(block_size * 65, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 66, HEIGHT - block_size * 6, block_size), Brick(block_size * 67, HEIGHT - block_size * 6, block_size), Brick(block_size * 68, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 69, HEIGHT - block_size * 6, block_size), Brick(block_size * 70, HEIGHT - block_size * 6, block_size), Brick(block_size * 71, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 72, HEIGHT - block_size * 6, block_size), Brick(block_size * 73, HEIGHT - block_size * 6, block_size), Brick(block_size * 74, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 75, HEIGHT - block_size * 6, block_size), Brick(block_size * 76, HEIGHT - block_size * 6, block_size), Brick(block_size * 77, HEIGHT - block_size * 6, block_size),
                    fire, spikes, spikes2, spikes3, spikes4, spikes5, spikes6, spikes7, spikes8, spikes9, spikes10, spikes11, spikes12, coin, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                    coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22, coin23]
        # Floor broken into individual elements (that are added to the list)
        # Blocks / Bricks passed through (Coordinates) - y multiplied by a larger number, in order to be positioned higher on the screen
        # Block / Brick size passed through and all is stored in variable: objects
        # Fire variable passed through; fire is a sub-class of the superclass: Objects
        # All spikes are passed through; spikes are a sub-class of the superclass: Objects
        
        offset_x = 0
        # Stores by how much the screen is currently offset (How much it has moved to the left/right)
        scroll_area_width = 300
        # Amount of pixels to the left/ right, for the game to start scrolling

        run = True
        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
        # Allows the player to load the game and quit the game
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
                    # If space bar is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_UP and player.jump_count < 2:
                        player.jump()
                    # If up arrow key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_w and player.jump_count < 2:
                        player.jump()
                    # If the W key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_p:
                        x = Pause_Game4()
                        print(x)
                    # If: 'p' is pressed, the pause menu will be loaded

            player.loop(FPS)
            fire.loop()
            handle_move(player, objects)
            draw(window, background, bg_image, player, objects, offset_x)
            texts = text(Count)
            print(texts)
            texts2 = text2(life_count)
            print(texts2)
            screen.blit((Lives), (22, 2))
            screen.blit((CoinImage), (120, 8))
            # Drawing the player, background, objects and the offset into the game

            if life_count <= 0:
                x = game_over()
                print(x)
            # If the player's life count is at 0, the game_over function will be printed

            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and (player.x_vel > 0)) or ((player.rect.left - offset_x <= scroll_area_width) and (player.x_vel < 0)):
            # If player is over the pixel limit to what is being shown on the window (Left and Right sides)
                offset_x += player.x_vel
                # Offset by the velocity of how much the player moved to the right

            if (player.rect.right >= 7500):
                # If the player's right directional movement exceeds 7500 pixels
                if Music == True:
                        x = play(True)
                        print(x)
                # If Music is True, play() function will be loaded with music
                else:
                    x = play(False)
                    print(x)
                # If Music is False, play() function will be loaded without music

            pygame.display.update()

        pygame.quit()
        quit()
        # Quitting the pygame program

    if __name__ == "__main__":
        main(window)
    # Calling main(window), if the player has just loaded the game

def FifthLevel():
# Function, when the first level has been selected to be played

    pygame.display.set_caption("Velocity - Level #5")
    # Setting the caption of the Pygame Window, to: 'Velocity - Level #1'

    BG_COLOR = (255, 255, 255)
    WIDTH = 1500
    HEIGHT = 800
    FPS = 60
    PLAYER_VEL = 5
    # Defining key Variables (Caps to not interfere with any later-declared similar variables)

    def game_over():
    # Defining the game_over function
        global life_count
        # Setting the life_count variable to a global variable
        life_count = 3
        # Setting the life_count variable to 3
        GameOver = pygame.image.load('C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Game Over Screen.png')
        # Defining the GameOver variable to load the background image (The Game Over Screen)
        screen.blit((GameOver), (0, 0))
        # Blitting the Game Over Screen onto the screen
        gameover = True
        # setting the gameover variable to true
        if Music == True:
        # If there is music present in the game
            pygame.mixer.music.stop()
            # Current music is paused
            pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/GameOverMusic.mp3")
            pygame.mixer.music.play()
            # Game Over music is loaded and played
        while gameover:
        # While the program is in the gameover state
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                # If the type of event causes the game to be quitted
                    pygame.quit()
                    # The game will quit (end)
                if event.type == pygame.MOUSEBUTTONDOWN:
                # if the player has pressed the right mouse button down
                    GameOver_MainMenu.checkForInputGameOver(pygame.mouse.get_pos())
                    # Inputs will be checked for the GameOver_MainMenu button
                    Continue.checkForInputContinue(pygame.mouse.get_pos())
                    # Inputs will be checked for the Continue button

            GameOver_MainMenu.update()
            # Updating the GameOver_MainMenu button
            Continue.update()
            # Updating the Continue button
                    
            pygame.display.update()
        pygame.quit()
    pygame.display.update()
    # Updating and quitting the game

    def text(Count):
    # Defining the text function; passing Count as a parameter
     if Count >=1 and Count <= 9:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render("0"+ Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     elif Count > 9:
        Count1 = str(Count)
        # Convert Count integer into a string, storing it under Count1
        text = sub_font.render(Count1, True, "white")
        # Creating a text variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text_rect = text.get_rect(center=(170,20))
        # Defining text_rect, which will store the position of the text on the screen
        screen.blit(text, text_rect)
        # Blitting both the text and its respective position, onto the screen
        Count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text = sub_font.render("00", True, "white")
         # Creating a text variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text_rect = text.get_rect(center=(170, 20))
         # Defining text_rect, which will store the position of the text on the screen
         screen.blit(text, text_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()
    
    def text2(life_count):
    # Defining the text2 function; passing Count as a parameter
     if life_count >=1:
        # If Count has been incremented to be above, or equal to, 1
        Count1 = str(life_count)
        # Convert Count integer into a string, storing it under Count1
        text2 = sub_font.render("0"+ Count1, True, "white")
        # Creating a text2 variable (stores the condition for: '0+Count1' to be printed to the screen, in the previously-declared default font)
        text2_rect = text2.get_rect(center=(75,20))
        # Defining text2_rect, which will store the position of the text on the screen
        screen.blit(text2, text2_rect)
        # Blitting both the text and its respective position, onto the screen
        life_count = int(Count1)
        # Converting Count from a string, back to an integer value
     else:
         text2 = sub_font.render("00", True, "white")
         # Creating a text2 variable (stores the condition for: '00' to be printed to the screen, in the previously-declared default font)
         text2_rect = text2.get_rect(center=(75,20))
         # Defining text_rect2, which will store the position of the text on the screen
         screen.blit(text2, text2_rect)
         # Blitting both the text and its respective position, onto the screen
    pygame.display.update()

    if Music == True:
    # If the Music variable is equal to True
        PauseMusic(Music)
        # Main Menu music is paused
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        # Level 1 Music is loaded
        pygame.mixer.music.play(-1)
        # Music track is looped indefinitely
        PlayMusic(Music)
        # PlayMusic function is called
        global LevelSelectorMusic
        # LevelSelectorMusic variable set to a global variable
        LevelSelectorMusic = True
        # LevelSelectorMusic set to True
    else:
    # If the Music Variable is equal to False
        PauseMusic(Music)
        # PlayMusic function is called
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1Music.mp3")
        pygame.mixer.music.play(-1)
        # Level Selector Music is loaded and looped
        PauseMusic(Music)
        # Music is paused

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    # Using Width and Height variables to set size of Window

    def flip(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
    # Defining flip function, which flips the sprite left/right, depending on what direction the player is facing

    def load_sprite_sheets(dir1, width, height, direction=False):
        path = join("General", dir1)
        # Creating the path variable, to join the assets in the: "Assets" folder to directory 1
        images = [f for f in listdir(path) if isfile(join(path, f))]
        # Dividing each individual image from the main image into seperate divisons
        
        all_sprites = {}
        # Defining the all_sprites dictionary, where all sprites will be stored

        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            # Creating a for loop for each image within the sprite sheet; joining path and image variables and converting into alpha form
            sprites = []
            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0,0), rect)
                sprites.append(pygame.transform.scale2x(surface))
            # Scaling the sprite to the size of the player character

            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
            # Left sprite loaded, when facing left direction
            # Right sprite loaded, when facing right direction
            else:
                all_sprites[image.replace(".png", "")] = sprites
            # Condition for else; replacing ".png" with "" for all sprites (Default Sprite)

        return all_sprites
        # Returning all sprites that are required, depending on player movement

    def get_block(size):
    # Defining the get_block() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(96, 0, size, size)
        # Specifically loading the grass block image in its full size, using (96,0) coordinates / Brick blocks = (272, 64)
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of block is doubled from previously-declared size

    def get_bricks(size):
    # Defining the get_brick() function
        path = join("Terrain", "Terrain.png")
        # Declaring path variable (Joins the Terrain directory with the Terrain.png image)
        image = pygame.image.load(path).convert_alpha()
        # Loading the image; conversion to alpha allows for a transparrent background
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        # Creating the surface (ground), of a fixed size (Square), and a depth of 32
        rect = pygame.Rect(272, 64, size, size)
        # Specifically loading the brick image in its full size, using (272, 64) coordinates
        # Passing the position and defining it in the variable rect
        surface.blit(image, (0,0), rect)
        # Blitting loaded image to coordinates (0,0), in the pygame window
        return pygame.transform.scale2x(surface)
        # Size of brick is doubled from previously-declared size

    class Player(pygame.sprite.Sprite):
    # Creating the Player class
        COLOR = (255, 0, 0)
        # The Player will firstly be a square. The COLOR Variable defines what colour the player will be (Currently Red)
        GRAVITY = 1
        # Setting the GRAVITY Variable to 1
        SPRITES = load_sprite_sheets("MaskDude", 32, 32, True)
        # Variable to call function, to load sprite with direction
        ANIMATION_DELAY = 3
        # Variable to account for delay in animation of sprites

        def __init__(self, x, y, width, height):
            super().__init__()
            self.rect = pygame.Rect(x, y, width, height)
            self.x_vel = 0
            self.y_vel = 0
            self.mask = None
            self.direction = "left"
            self.animation_count = 0
            self.fall_count = 0
            self.jump_count = 0
            self.hit = False
            self.hit_count = 0
        # The __init__ method of the Player class is defined to create key variables that define the Player

        def jump(self):
        # Defining jump method
            self.y_vel = -self.GRAVITY * 8
            # Negative gravity multiplied by 8, in order for a constant speed of gravity to be implemented (Downwards Gravity)
            self.animation_count = 0
            self.jump_count += 1
            if self.jump_count == 1:
                self.fall_count = 0
            # As soon as the player jumps, any obtained gravity will be removed (Not a factor), and then gravity is applied after jumping
                
        def move(self, dx, dy):
            self.rect.x += dx
            self.rect.y += dy
        # The move method is defined to register player positions and movement (x and y values - However, no movement in the y-axis)

        def make_hit(self):
            self.hit = True
            self.hit_count = 0
        # The make_hit method is defined to register when the player has been hit

        def move_left(self, vel):
            self.x_vel = -vel
            if self.direction != "left":
                self.direction = "left"
                self.animation_count = 0
        # move_left method defined to register left player movements

        def move_right(self, vel):
            self.x_vel = vel
            if self.direction != "right":
                self.direction = "right"
                self.animation_count = 0
        # move_right method defined to register right player movements
        

        def loop(self, fps):
            self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
            self.move(self.x_vel, self.y_vel)
        # loop method defined to move player with set x and y velocities; y velocity now takes into account gravity (1)

            if self.hit:
            # Condition for if the player has been hit
                self.hit_count +=1
                # Adding one to the counter of time being hit for 
            if self.hit_count > fps * 2:
            # Condition for after being in the hit state for greater than 2 seconds
                self.hit = False
                global life_count
                life_count = life_count -1
                # Player is no longer in the hit state
                self.hit_count = 0
                # hit Counter being set to 0

            self.fall_count += 1 
            # Adding 1 to the fall count, as the player as still currently falling, if the method has been executed
            self.update_sprite()
            # Update sprite

        def landed(self):
        # Method for the player to land on a block
            self.fall_count = 0
            # Set to 0, to stop adding gravity
            self.y_vel = 0
            # No upwards or downwards velocity
            self.jump_count = 0
            # Not jumping (Uesful for double-jumps)

        def hit_head(self):
        # Method for the player to hit their head on a block
            self.count = 0
            # Set to 0
            self.y_vel *= -1
            # Velocity is reversed (Moving downwards, rather than upwards)

        def update_sprite(self):
        # Method to update sprites, depending on if running or idle
            sprite_sheet = "idle"
            # Default sprite sheet, if player is not moving
            if self.hit:
            # If the player has been hit
                sprite_sheet = "hit"
                # Load the hit sprite sheet
            if self.y_vel < 0:
            # If velocity is less than 0 (Moving upwards)
                if self.jump_count == 1:
                    sprite_sheet = "jump"
                # If this is the player's first jump, normal jump animation will be featured
                elif self.jump_count == 2:
                    sprite_sheet = "double_jump"
                # If this is the player's second jump, the double jump animation will be featured
            elif self.y_vel > self.GRAVITY * 2:
            # If velocity is greater than gravity * 2 (Moving downwards)
                sprite_sheet = "fall"
                # If player is moving down, then fall animation will be loaded
            elif self.x_vel != 0:
                sprite_sheet = "run"
            # If x velocity is not 0, then running animations will be loaded

            sprite_sheet_name = sprite_sheet + "_" + self.direction
            sprites = self.SPRITES[sprite_sheet_name]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.sprite = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.update()
            # Calling update method

        def update(self):
        # Defining update method
            self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.sprite)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

        def draw(self, win, offset_x):
            win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
        # draw method defined to redraw the current figure in a given position

    # End of the Player class

    class Object(pygame.sprite.Sprite):
    # Creating the Object class (Base class for all objects, so that collision is uniform across all)
    # Inherits from the Sprite class
        def __init__(self, x, y, width, height, name=None):
            super().__init__()
            # Initialising Superclass (pygame.sprite.Sprite)
            self.rect = pygame.Rect(x, y, width, height)
            # Defining Rectangle for a valid sprite
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            # Defining Object image (Supports transparrent images)
            self.width = width
            self.height = height
            self.name = name
            # Defining self variables

        def draw(self, win, offset_x):
            win.blit(self.image, (self.rect.x - offset_x, self.rect.y))
        # Draw function automatically draws Object instantly on the screen

    class Coin(Object):
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "coins")
            # Calling super-initialiser (Name is being passed; allows for later checks if coin has been collided with)
            self.coins = load_sprite_sheets("Coins", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.coins["Coin"][0]
            # Loading the Coin animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work)

    class Block(Object):
    # Creating Block class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            block = get_block(size)
            # variable that stores a function to retrieve the size of a block
            self.image.blit(block, (0,0))
            # Block is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Brick(Object):
    # Creating Brick class - Inherits from Object class
        def __init__(self, x, y, size):
            # 1 dimension needed (Block is a square)
            super().__init__(x, y, size, size)
            brick = get_bricks(size)
            # variable that stores a function to retrieve the size of a brick (same as a block)
            self.image.blit(brick, (0,0))
            # Brick is blitted onto position (0,0) of the screen; starting from the bottom-left corner
            self.mask = pygame.mask.from_surface(self.image)
            # creation of mask for collision

    class Fire(Object):
    # Creating Fire class - Inherits from Object class
        ANIMATION_DELAY = 3
        # Defining local variable, to account for delay in the animations
        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "fire")
            # Calling super-initialiser (Name is being passed; allows for later checks if fire has been hit)
            self.fire = load_sprite_sheets("Fire", width, height)
            # Loading sprites for fire
            self.image = self.fire["off"][0]
            # Specifying image (Fire begins as being off)
            self.mask = pygame.mask.from_surface(self.image)
            # Creating the mask for the fire sprite
            self.animation_count = 0
            # Defining animation count (Same as player)
            self.animation_name = "off"
            # Off animation is automatically played

        def on(self):
        # Defining On method
            self.animation_name = "on"
            # On Fire Animation is played

        def off(self):
        # Defining Off method
            self.animation_name = "off"
            # Off Fire Animation is played

        def loop(self):
            sprites = self.fire[self.animation_name]
            # Defining local variable sprites to store all fire sprites
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            # Dynamic (will work for every sprite); used to increment through which sprite should be loaded at which time
            self.image = sprites[sprite_index]
            self.animation_count += 1
            # Increments animation count by 1, to load next animation for sprites
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite) - Allowing for pixel-perfection collision, as collision only occurs when sprites interact, not when the base rectangle interacts

            if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            # Animation count for fire will continue no matter what; if it gets too high, it will cause the game to lag - This condition prevents it from becomming too high
                self.animation_count = 0
                # Animation count is reset

    class Spikes(Object):
    # Creating the Spikes class (Sub-class of the Object superclass)

        def __init__(self, x, y, width, height):
            super(). __init__(x, y, width, height, "spikes")
            # Calling super-initialiser (Name is being passed; allows for later checks if spikes have been hit)
            self.spikes = load_sprite_sheets("Spikes", width, height)
            # Loading the sprite sheet image, with taken width and height
            self.image = self.spikes["Idle"][0]
            # Loading the idle spike animation (Which is the only one that is needed)
            self.mask = pygame.mask.from_surface(self.image)
            # Creation of the mask (A mapping to all pixels that exist on the sprite)
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            # Rectangle should be the same size as sprite (Making collisions work) - Rectangle width and height is adjusted, depending on the sprite that is included

    def get_background():
    # get_background() function is defined

        image = pygame.image.load("C:/Users/olive/OneDrive/Desktop/A-Level Work/Computer Science/NEA/NEA Work/Design - Resources/8-bit Game Assets/Main Menu/Level5 Background.jpg")
        _, _, width, height = image.get_rect()
        tiles = []
        # Defining the get_background() method, to directly load a background image into the game

        for i in range(WIDTH // width + 1):
            for j in range(HEIGHT // height + 1):
                pos = (i * width, j * height)
                tiles.append(pos)
        # Dividing the background into individual tiles, before reforming them, based on the size of the Window

        return tiles, image
        # Returning the tiles array and the image variable

    def draw(window, background, bg_image, Player, objects, offset_x):
        for tile in background:
            window.blit(bg_image, tile)
    # Defining the draw method, which will use each tile of the background and place the respective part of the image overtop of it
    
        for obj in objects:
        # For loop created for each object within objects
            obj.draw(window, offset_x)
            # Object is drawn onto the window
        
        Player.draw(window, offset_x)
        # Using the window variable to add the background to the window

    def handle_vertical_collision(player, objects, dy):
    # Seperate handling of vertical collision (Function)
        collided_objects = []
        # List to keep track of what objects have been collided with
        for obj in objects:
        # For loop (Objects that can be collided with)
            if pygame.sprite.collide_mask(player, obj):
            # Determines if 2 objects are colliding (Player and Block sprites)
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    # Bottom of object equals top of object; prevents player clipping inside of the object
                    player.landed()
                    # Method call
                # If player collides with top of object, bottom of player is set on-top of the object
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    # Top of object equals bottom of object; prevents player clipping inside of the object
                    player.hit_head()
                    # Method call
                # If player collides with bottom of object

                collided_objects.append(obj)
                # Add collided object to list

        return collided_objects
        # Returns collided objects, to determine what type of object has been collided with

    def collide(player, objects, dx):
    # Defining collide function (For horizontal collision)
        player.move(dx, 0)
        # Player moved in displacement-x direction; checking that if the player was to move left/right, would they hit a block?
        player.update()
        # Updating rectangle and player mask
        collided_object = None
        # No current collided object
        for obj in objects:
            if pygame.sprite.collide_mask(player,obj):
            # If an object collides with the updated mask
                collided_object = obj
                # obj is colliding with player
                break

        player.move(-dx, 0)
        # Player moved back to original spot
        player.update()
        # Updating rectangle and mask back to original
        return collided_object
        # If object will collide with player. return the object / If not, no item will be returned

    def handle_move(player, objects):
        keys = pygame.key.get_pressed()
    # Defining the handle_move procedure, which will register when the player enters specific keys that will allow them to move their character

        player.x_vel = 0
        vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
        collide_left = collide(player, objects, -PLAYER_VEL * 2)
        # Checking if player will collide with an object to their left
        collide_right = collide(player, objects, PLAYER_VEL * 2)
        # Checking if player will collide with an object to their right

        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)
        if keys[pygame.K_a] and not collide_right:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_d] and not collide_right:
            player.move_right(PLAYER_VEL) 
        # If left arrow click (and no potential block collisions), player moves left
        # If right arrow click (and no potential block collisions), player moves right

        vertical = [*vertical_collide]
        horizontal = [collide_left, collide_right]
        # Conditions to be checked (Left, right, and vertical collisions)

        for obj in vertical:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "fire":
            # If the player has collided with fire
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                global Count
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen

        for obj in horizontal:
        # For loop to check all objects that player can collide with
            if obj and obj.name == "spikes":
            # If the player has collided with spikes
                player.make_hit()
                # method being called, to put player into a hit state
            elif obj and obj.name == "coins":
            # If the player has collided with a coin
                objects.remove(obj)
                # The coin is removed from the screen
                Count = Count + 1
                # Global variable of: 'Count', is incremented by 1
                x = text(Count)
                # Defining x variable to update coin counter (Calling text() function)
                print(x)
                # Printing function to the screen
                
    def main(window):
        clock = pygame.time.Clock()
        background, bg_image = get_background()
    # Defining main window of the game, and creating clock and background / bg_image variables
        block_size = 96
        # Defining the block_size variable, for later use in declaring the sizes of blocks
        player = Player(100, 100, 50, 50)
        # Creating an instance of the Player class
        fire = Fire(2915, HEIGHT - block_size - 350, 16, 32)
        # Defining fire variable and calling the Fire class
        fire.on()
        # Fire is always on
        spikes = Spikes(1410, HEIGHT - block_size - 30, 16, 32)
        spikes2 = Spikes(1375, HEIGHT - block_size - 30, 16, 32)
        spikes3 = Spikes(1340, HEIGHT - block_size - 30, 16, 32)
        spikes4 = Spikes(1305, HEIGHT - block_size - 30, 16, 32)
        spikes5 = Spikes(1270, HEIGHT - block_size - 30, 16, 32)
        spikes6 = Spikes(1254, HEIGHT - block_size - 30, 16, 32)
        spikes7 = Spikes(block_size * 40, HEIGHT - block_size - 30, 16, 32)
        spikes8 = Spikes((block_size * 40) + 35, HEIGHT - block_size - 30, 16, 32)
        spikes9 = Spikes((block_size * 40) + 70, HEIGHT - block_size - 30, 16, 32)
        spikes10 = Spikes((block_size * 41) - 8.2, HEIGHT - block_size - 30, 16, 32)
        spikes11 = Spikes((block_size * 41) + 26.8, HEIGHT - block_size - 30, 16, 32)
        spikes12 = Spikes((block_size * 41) + 61.8, HEIGHT - block_size - 30, 16, 32)
        coin = Coin(300, HEIGHT - block_size - 64, 16, 32)
        coin2 = Coin(400, HEIGHT - block_size - 64, 16, 32)
        coin3= Coin(500, HEIGHT - block_size - 64, 16, 32)
        coin4 = Coin((block_size * 10) + 200, HEIGHT - block_size - 128, 16, 32)
        coin5 = Coin((block_size * 40), HEIGHT - block_size - 128, 16, 32)
        coin6 = Coin((block_size * 40) + 60, HEIGHT - block_size - 192, 16, 32)
        coin7 = Coin((block_size * 40) + 120, HEIGHT - block_size - 192, 16, 32)
        coin8 = Coin((block_size * 40) + 190, HEIGHT - block_size - 128, 16, 32)
        coin9 = Coin(block_size * 63, HEIGHT - block_size * 6.5, 16, 32)
        coin10 = Coin(block_size * 64, HEIGHT - block_size * 6.5, 16, 32)
        coin11 = Coin(block_size * 65, HEIGHT - block_size * 6.5, 16, 32)
        coin12 = Coin(block_size * 66, HEIGHT - block_size * 6.5, 16, 32)
        coin13 = Coin(block_size * 67, HEIGHT - block_size * 6.5, 16, 32)
        coin14 = Coin(block_size * 68, HEIGHT - block_size * 6.5, 16, 32)
        coin15 = Coin(block_size * 69, HEIGHT - block_size * 6.5, 16, 32)
        coin16 = Coin(block_size * 70, HEIGHT - block_size * 6.5, 16, 32)
        coin17 = Coin(block_size * 71, HEIGHT - block_size * 6.5, 16, 32)
        coin18 = Coin(block_size * 72, HEIGHT - block_size * 6.5, 16, 32)
        coin19 = Coin(block_size * 73, HEIGHT - block_size * 6.5, 16, 32)
        coin20 = Coin(block_size * 74, HEIGHT - block_size * 6.5, 16, 32)
        coin21 = Coin(block_size * 75, HEIGHT - block_size * 6.5, 16, 32)
        coin22 = Coin(block_size * 76, HEIGHT - block_size * 6.5, 16, 32)
        coin23 = Coin(block_size * 77, HEIGHT - block_size * 6.5, 16, 32)
        # Creating 12 instances of spikes and 23 instances of coins, each stored under a different variable name
        floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, (WIDTH * 5) // block_size)]
        # Creating the floor variable; create a number of blocks that will be duplicated to the left and right of the initial block (Working, for a scrolling background)
        objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),  
                    Block(block_size * 10, HEIGHT - block_size * 3, block_size), Brick(block_size * 12, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 10, HEIGHT - block_size * 2, block_size), Block(block_size * 9, HEIGHT - block_size * 2, block_size), Block(block_size * 11, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 11, HEIGHT - block_size * 3, block_size), Block(block_size * 11, HEIGHT - block_size * 4, block_size), Block(block_size * 15, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 15, HEIGHT - block_size * 3, block_size), Block(block_size * 15, HEIGHT - block_size * 2, block_size), Block(block_size * 16, HEIGHT - block_size * 2, block_size), 
                    Block(block_size * 16, HEIGHT - block_size * 3, block_size), Block(block_size * 17, HEIGHT - block_size * 2, block_size), Brick(block_size * 24, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 25, HEIGHT - block_size * 3, block_size), Brick(block_size * 26, HEIGHT - block_size * 3, block_size), Brick(block_size * 25, HEIGHT - block_size * 5, block_size),
                    Brick(block_size * 29, HEIGHT - block_size * 4, block_size), Brick(block_size * 30, HEIGHT - block_size * 4, block_size), Brick(block_size * 31, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 36, HEIGHT - block_size * 3, block_size), Block(block_size * 37, HEIGHT - block_size * 3, block_size), Block(block_size * 38, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 37, HEIGHT - block_size * 4, block_size), Block(block_size * 38, HEIGHT - block_size * 4, block_size), Block(block_size * 39, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 38, HEIGHT - block_size * 5, block_size), Block(block_size * 39, HEIGHT - block_size * 5, block_size), Block(block_size * 40, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 41, HEIGHT - block_size * 5, block_size), Block(block_size * 42, HEIGHT - block_size * 5, block_size), Block(block_size * 43, HEIGHT - block_size * 5, block_size),
                    Block(block_size * 42, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 4, block_size), Block(block_size * 43, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Block(block_size * 45, HEIGHT - block_size * 3, block_size), Block(block_size * 44, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 44, HEIGHT - block_size * 3, block_size), Brick(block_size * 49, HEIGHT - block_size * 3, block_size), Brick(block_size * 50, HEIGHT - block_size * 3, block_size),
                    Brick(block_size * 49, HEIGHT - block_size * 2, block_size), Brick(block_size * 50, HEIGHT - block_size * 2, block_size), Brick(block_size * 48, HEIGHT - block_size * 2, block_size), 
                    Brick(block_size * 51, HEIGHT - block_size * 2, block_size), Brick(block_size * 53, HEIGHT - block_size * 3, block_size), Brick(block_size * 54, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 58, HEIGHT - block_size * 2, block_size), Block(block_size * 59, HEIGHT - block_size * 2, block_size), Block(block_size * 60, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 59, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 3, block_size), Block(block_size * 60, HEIGHT - block_size * 4, block_size),
                    Brick(block_size * 63, HEIGHT - block_size * 6, block_size), Brick(block_size * 64, HEIGHT - block_size * 6, block_size), Brick(block_size * 65, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 66, HEIGHT - block_size * 6, block_size), Brick(block_size * 67, HEIGHT - block_size * 6, block_size), Brick(block_size * 68, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 69, HEIGHT - block_size * 6, block_size), Brick(block_size * 70, HEIGHT - block_size * 6, block_size), Brick(block_size * 71, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 72, HEIGHT - block_size * 6, block_size), Brick(block_size * 73, HEIGHT - block_size * 6, block_size), Brick(block_size * 74, HEIGHT - block_size * 6, block_size),
                    Brick(block_size * 75, HEIGHT - block_size * 6, block_size), Brick(block_size * 76, HEIGHT - block_size * 6, block_size), Brick(block_size * 77, HEIGHT - block_size * 6, block_size),
                    fire, spikes, spikes2, spikes3, spikes4, spikes5, spikes6, spikes7, spikes8, spikes9, spikes10, spikes11, spikes12, coin, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10,
                    coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22, coin23]
        # Floor broken into individual elements (that are added to the list)
        # Blocks / Bricks passed through (Coordinates) - y multiplied by a larger number, in order to be positioned higher on the screen
        # Block / Brick size passed through and all is stored in variable: objects
        # Fire variable passed through; fire is a sub-class of the superclass: Objects
        # All spikes are passed through; spikes are a sub-class of the superclass: Objects
        
        offset_x = 0
        # Stores by how much the screen is currently offset (How much it has moved to the left/right)
        scroll_area_width = 300
        # Amount of pixels to the left/ right, for the game to start scrolling

        run = True
        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
        # Allows the player to load the game and quit the game
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
                    # If space bar is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_UP and player.jump_count < 2:
                        player.jump()
                    # If up arrow key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_w and player.jump_count < 2:
                        player.jump()
                    # If the W key is pressed, player will jump (and double-jump)
                    elif event.key == pygame.K_p:
                        x = Pause_Game5()
                        print(x)
                    # If: 'p' is pressed, the pause menu will be loaded

            player.loop(FPS)
            fire.loop()
            handle_move(player, objects)
            draw(window, background, bg_image, player, objects, offset_x)
            texts = text(Count)
            print(texts)
            texts2 = text2(life_count)
            print(texts2)
            screen.blit((Lives), (22, 2))
            screen.blit((CoinImage), (120, 8))
            # Drawing the player, background, objects and the offset into the game

            if life_count <= 0:
                x = game_over()
                print(x)
            # If the player's life count is at 0, the game_over function will be printed

            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and (player.x_vel > 0)) or ((player.rect.left - offset_x <= scroll_area_width) and (player.x_vel < 0)):
            # If player is over the pixel limit to what is being shown on the window (Left and Right sides)
                offset_x += player.x_vel
                # Offset by the velocity of how much the player moved to the right

            if (player.rect.right >= 7500):
                # If the player's right directional movement exceeds 7500 pixels
                if Music == True:
                        x = play(True)
                        print(x)
                # If Music is True, play() function will be loaded with music
                else:
                    x = play(False)
                    print(x)
                # If Music is False, play() function will be loaded without music

            pygame.display.update()

        pygame.quit()
        quit()
        # Quitting the pygame program

    if __name__ == "__main__":
        main(window)
    # Calling main(window), if the player has just loaded the game

class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        # Defining the: 'Button' class, in addition to arguments

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    # Defining the: 'Update' Method (Updates button icons)

    def checkForInputButton (self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Played = play(Music)
            print(Played)
    # Defining the: 'CheckForInputButton' Function (Checks if the user has inputted any values, for the first button)

    def checkForInputButton2 (self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Volume = volume(Music)
            print(Volume)
    # Defining the: 'CheckForInputButton2' Function (Checks if the user has inputted any values, for the second button)

    def checkForInputButton3 (self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Options = options()
            print(Options)
    # Defining the: 'CheckForInputButton3' Function (Checks if the user has inputted any values, for the third button)

    def checkForInputLevel1 (self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            One = FirstLevel()
            print(One)
        # Defining the: 'CheckForInputLevel1' Function (Checks if the user has selected the first level)

    def checkForInputLevel2 (self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Two = SecondLevel()
            print(Two)
        # Defining the: 'CheckForInputLevel2' Function (Checks if the user has selected the second level)

    def checkForInputLevel3 (self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Three = ThirdLevel()
            print(Three)
        # Defining the: 'CheckForInputLevel3' Function (Checks if the user has selected the third level)

    def checkForInputLevel4 (self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Four = FourthLevel()
            print(Four)
        # Defining the: 'CheckForInputLevel4' Function (Checks if the user has selected the fourth level)

    def checkForInputLevel5 (self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Five = FifthLevel()
            print(Five)
        # Defining the: 'CheckForInputLevel5' Function (Checks if the user has selected the fifth level)

    def checkForInputBack (self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Main = mainmenu(False)
            print(Main)
    # Defining the: 'CheckForInputBack' Function (Checks if the user has inputted any values, for the back button)

    def checkForInputBackSelector(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Main = mainmenu(True)
            print(Main)
    # Defining the: 'CheckForInputBackSelector' Function (Checks if the user has inputted any values, for the back button)

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")
    # Defining the: 'ChangeColor' Function (Changes the colour of the text on a button, if pressed - IN-CASE OF REQUIRED USE)

    def checkForInputMusic(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            global Music
            Play = PlayMusic(True)
            print(Play)
            Music = True
    # Defining the: 'CheckForInputMusic' Function (Checks if the user has inputted any values, for the music button)

    def checkForInputNoMusic(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            global Music
            Play = PauseMusic(False)
            print(Play)
            Music = False
    # Defining the: 'CheckForInputNoMusic' Function (Checks if the user has inputted any values, for the no music button)

    def checkForInputGameOver(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Main = mainmenu(True)
            print(Main)
    # Defining the: 'CheckForInputGameOver' Function (Checks if the user has inputted any values, for the Back to Main Menu Button)

    def checkForInputContinue(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Played = play(Music)
            print(Played)
    # Defining the: 'CheckForInputContinue' Function (Checks if the user has inputted any values, for the Continue button)

    def checkForInputUnpause(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
    # Defining the: 'CheckForInputUnpause' Function (Checks if the user has inputted any values, for the Unpause button)

    def checkForInputlevel(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Played = play(Music)
            print(Played)
    # Defining the: 'CheckForInputlevel' Function (Checks if the user has inputted any values, for the level button)

    def checkForInputLevelSelector(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Played = play(Music)
            print(Played)
    # Defining the: 'CheckForInputLevelSelector' Function (Checks if the user has inputted any values, for the LevelSelector button)

    def checkForInputRestart(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            x = FirstLevel()
            print(x)
    # Defining the: 'CheckForInputRestart' Function (Checks if the user has inputted any values, for the Restart button)

    def checkForInputRestart2(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            x = SecondLevel()
            print(x)
    # Defining the: 'CheckForInputRestart2' Function (Checks if the user has inputted any values, for the Restart button)

    def checkForInputRestart3(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            x = ThirdLevel()
            print(x)
    # Defining the: 'CheckForInputRestart3' Function (Checks if the user has inputted any values, for the Restart button)

    def checkForInputRestart4(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            x = FourthLevel()
            print(x)
    # Defining the: 'CheckForInputRestart4' Function (Checks if the user has inputted any values, for the Restart button)

    def checkForInputRestart5(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            x = FifthLevel()
            print(x)
    # Defining the: 'CheckForInputRestart5' Function (Checks if the user has inputted any values, for the Restart button)

button_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Play Button.png")
button_surface = pygame.transform.scale(button_surface, (365.541, 355.3))
# Creating, and loading, the first button icon ('Play' Button)

button = Button(button_surface, 740, 590, "")
# Defining the: 'Button' Variable (Passing arguments into the Button() class)

button_surface2 = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Volume Button.png")
button_surface2 = pygame.transform.scale(button_surface2, (292.4328, 284.24))
# Creating, and loading, the second button icon ('Volume' Button)

button2 = Button(button_surface2, 220, 580, "")
# Defining the: 'Button2' Variable (Passing arguments into the Button() class)

button_surface3 = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Settings Button.png")
button_surface3 = pygame.transform.scale(button_surface3, (292.4328, 284.24))
# Creating, and loading, the second button icon ('Options' Button)

button3 = Button(button_surface3, 1250, 580, "")
# Defining the: 'Button3' Variable (Passing arguments into the Button() class)

level1_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level1.png")
level1_surface = pygame.transform.scale(level1_surface, ((300, 200)))
# Creating, and loading, the level 1 button icon

level1 = Button(level1_surface, 250, 385, "")
# Defining the: 'level1' Variable (Passing arguments into the Button() class)

level2_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level2.png")
level2_surface = pygame.transform.scale(level2_surface, ((290, 190)))
# Creating, and loading, the level 2 button icon

level2 = Button(level2_surface, 750, 395, "")
# Defining the: 'level2' Variable (Passing arguments into the Button() class)

level3_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level3.png")
level3_surface = pygame.transform.scale(level3_surface, ((290, 190)))
# Creating, and loading, the level 3 button icon

level3 = Button(level3_surface, 1250, 385, "")
# Defining the: 'level3' Variable (Passing arguments into the Button() class)

level4_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level4.png")
level4_surface = pygame.transform.scale(level4_surface, ((250, 150)))
# Creating, and loading, the level 4 button icon

level4 = Button(level4_surface, 440, 700, "")
# Defining the: 'level4' Variable (Passing arguments into the Button() class)

level5_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level5.png")
level5_surface = pygame.transform.scale(level5_surface, ((250, 150)))
# Creating, and loading, the level 5 button icon

level5 = Button(level5_surface, 1060, 700, "")
# Defining the: 'level5' Variable (Passing arguments into the Button() class)

backbutton_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Back Button.png")
backbutton_surface = pygame.transform.scale(backbutton_surface, ((100, 100)))
# Creating, and loading, the back button icon

backbutton = Button(backbutton_surface, 70, 70, "")
# Defining the: 'backbutton' Variable (Passing arguments into the Button() class)

backbuttonlevelselector_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Back Button.png")
backbuttonlevelselector_surface = pygame.transform.scale(backbutton_surface, ((100, 100)))
# Creating, and loading, the back button level selector icon

backbuttonlevelselector = Button(backbutton_surface, 70, 70, "")
# Defining the: 'backbutton' Variable (Passing arguments into the Button() class)

nomusicbutton_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/No Music Button.png")
nomuscibutton_surface = pygame.transform.scale(nomusicbutton_surface, (292.4328, 284.24))
# Creating, and loading, the No Music button icon

nomusicbutton = Button(nomusicbutton_surface, 1250, 580, "")
# Defining the: 'nomusicbutton' variable (Passing arguments into the Button() class)

musicbutton_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Volume Button.png")
musicbutton_surface = pygame.transform.scale(musicbutton_surface, (292.4328, 284.24))
# Creating, and loading, the Music button

musicbutton = Button(musicbutton_surface, 220, 580, "")
# Defining the: 'musicbutton' variable (Passing arguments into the Button() class)

GameOver_MainMenu_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/RTMM Button.png")
GameOver_MainMenu_surface = pygame.transform.scale(GameOver_MainMenu_surface, (420, 85.5))
# Creating, and loading, the GameOver_MainMenu button

GameOver_MainMenu = Button(GameOver_MainMenu_surface, 750, 600, "")
# Defining the: 'GameOver_MainMenu' variable (Passing arguments into the Button() class)

Continue_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Continue Button.png")
Continue_surface = pygame.transform.scale(Continue_surface, (274.5, 82.5))
# Creating, and loading, the Continue button

Continue = Button(Continue_surface, 750, 475, "")
# Defining the: 'Continue' variable (Passing arguments into the Button() class)

UnPause_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Play Button.png")
UnPause_surface = pygame.transform.scale(UnPause_surface, (273.75, 266.25))
# Creating, and loading, the Unpause button

UnPause = Button(UnPause_surface, 730, 520, "")
# Defining the: 'UnPause' variable (Passing arguments into the Button() class)

level_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Level Button.png")
level_surface = pygame.transform.scale(level_surface, (273.75, 266.25))
# Creating, and loading, the level button

level = Button(level_surface, 390, 520, "")
# Defining the: 'level' variable (Passing arguments into the Button() class)

restart_surface = pygame.image.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/Restart Button.png")
restart_surface = pygame.transform.scale(restart_surface, (318, 250))
# Creating, and loading, the restart button

restart = Button(restart_surface, 1075, 510, "")
# Defining the: 'restart' variable (Passing arguments into the Button() class)

def mainmenu(LevelSelectorMusic):
# Defining mainmenu function
    if LevelSelectorMusic == True and Music == True:
    # If the Player has just been came from the Level Selector Screen, with the music unmuted
         pygame.mixer.music.stop()
         # Stop Current Music track (LevelSelectorMusic)
         pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/MainMenuMusic.mp3")
         # Load the Main Menu Music
         pygame.mixer.music.play(-1)
         # Infinitly loop the playing of this track, whilst the player is on the main menu
         LevelSelectorMusic = False
         # LevelSelectorMusic Variable is set to False
    elif LevelSelectorMusic == False:
    # If the Player has just loaded up the game
        LevelSelectorMusic = False
        # LevelSelectorMusic Variable is set to False
    elif Music == False:
    # If Music is muted (= False)
        pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/MainMenuMusic.mp3")
        # Load Main Menu Music
        pygame.mixer.music.play(-1)
        # Infinitly loop the playing of this track, whilst the player is on the main menu
        pygame.mixer.music.pause()
        # Pause the track, as the music is currently muted

    while main_menu:
    # While loop that contains all code, for when the game is running  
        LevelSelectorMusic = False 
        # LevelSelectorMusic Variable is set to False
        pygame.display.set_caption("Velocity - Main Menu")
        # Setting an initial caption to the pygame window: 'Velocity - Main Menu')
        for event in pygame.event.get():
        # For any event that takes place in the main menu
            if event.type == pygame.QUIT:
            # If the player is quitting the game
                pygame.quit()
                # The game will quit
            if event.type == pygame.MOUSEBUTTONDOWN:
            # If the player has pressed the right mouse button down
                button.checkForInputButton(pygame.mouse.get_pos())
                # The input condition for the main (play) button will be checked
                button2.checkForInputButton2(pygame.mouse.get_pos())
                # The input condition for the Volume button will be checked
                button3.checkForInputButton3(pygame.mouse.get_pos())
                # The input condition for the Options button will be checked
            elif event.type == pygame.KEYDOWN:
            # If the player has pressed a key down
                if event.key == pygame.K_RETURN:
                # If the player has pressed the enter key down
                    Played = play(Music)
                    # Played is defined, and stores the play() function
                    print(Played)
                    # Variable: 'Played', is printed to the screen

        button.update()
        button.changeColor(pygame.mouse.get_pos())
        # Updating the Main Button Text colour, if hovered over

        button2.update()
        button2.changeColor(pygame.mouse.get_pos())
        # Updating the Volume Button Text colour, if hovered over

        button3.update()
        button3.changeColor(pygame.mouse.get_pos())
        # Updating the Settingds Button Text colour, if hovered over

        pygame.display.update()
        # Updating the overall display of the game

        screen.blit(main_menu_background, (0, 0))
        # Image is copied + updated onto the screen

pygame.mixer.music.load("C:/Users/olive/OneDrive/Desktop/Final NEA Code/Backgrounds/MainMenuMusic.mp3")
# Main Menu music will always be initially loaded, when the player first boots up the game
pygame.mixer.music.play(-1)
# The Menu music will automatically play indefinitely

main = mainmenu(LevelSelectorMusic)
# Defining main as the mainmenu() function
print(main)
# Prtinting variable: 'main', to the screen
pygame.quit()
# Quitting pygame entirely, when no menus are currently loaded