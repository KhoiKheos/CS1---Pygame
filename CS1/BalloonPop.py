# Import
import random
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time
from pygame import mixer


# Initialize
pygame.init()

# Create Window/Display
SCREEN_width = 1280
SCREEN_height = 720
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Balloon Pop")

# Background Sound
mixer.music.load("../Resources/Sound Effect/Bgm.wav")
pop_sound = mixer.Sound("../Resources/Sound Effect/Pop.wav")
mixer.music.play(-1)

# Initialize Clock for FPS
fps = 45
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height

# Images
imgBalloonRed = pygame.transform.scale(pygame.image.load('../Resources/redballoon.jpg').convert_alpha(), (240, 150))
imgBalloonGreen = pygame.transform.scale(pygame.image.load('../Resources/greenballoon.jpg').convert_alpha(), (240, 150))
imgBalloonBlue = pygame.transform.scale(pygame.image.load('../Resources/blueballoon.jpg').convert_alpha(), (240, 150))
imgBalloonYellow = pygame.transform.scale(pygame.image.load('../Resources/yellowballoon.jpg').convert_alpha(), (240, 150))
imgBalloonPink = pygame.transform.scale(pygame.image.load('../Resources/pinkballoon.jpg').convert_alpha(), (240, 150))
imgBalloonOrange = pygame.transform.scale(pygame.image.load('../Resources/orangeballoon.jpg').convert_alpha(), (240, 150))
imgBalloonDarkBlue = pygame.transform.scale(pygame.image.load('../Resources/darkblueballoon.jpg').convert_alpha(), (240, 150))
imgBalloonDarkGreen = pygame.transform.scale(pygame.image.load('../Resources/darkgreenballoon.jpg').convert_alpha(), (240, 150))
imgBalloonBonus = pygame.transform.scale(pygame.image.load('../Resources/bonusballoon.jpg').convert_alpha(), (240, 150))
imgBalloon = imgBalloonRed
rectBalloon = imgBalloon.get_rect()
rectBalloon.x, rectBalloon.y = 500, 300

# Variables
speed = 15
score = 0
startTime = time.time()
totalTime = 30
level = 1
levelUpScore = 20  # Points required to level up
escapeCount = 0
maxEscapes = 5

# Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

def resetBalloon():
    global imgBalloon, speed
    if should_spawn_bonus_balloon():
        imgBalloon = imgBalloonBonus
        speed = 30  # Faster speed for bonus balloon
    else:
        rectBalloon.x = random.randint(100, img.shape[1] - 100)
        rectBalloon.y = img.shape[0] + 50
        random_balloon_color = random.choice([imgBalloonRed, imgBalloonBlue, imgBalloonGreen, imgBalloonYellow, imgBalloonPink, imgBalloonOrange])  # Add more options if needed
        imgBalloon = random_balloon_color

def size_change():
    global  imgBalloonRed
    global imgBalloonBlue
    global imgBalloonGreen
    global imgBalloonYellow
    global imgBalloonPink
    global imgBalloonOrange
    global imgBalloonDarkBlue
    global imgBalloonDarkGreen
    size_reduction = level * 5  # Example: reduce size by 5 pixels per level
    pixel_width_new = max(100, 150 - size_reduction)  # Ensure a minimum size
    pixel_height_new = max(150, 200 - size_reduction)

    imgBalloonRed = pygame.transform.scale(pygame.image.load('../Resources/redballoon.jpg'),
                                           (pixel_width_new, pixel_height_new))
    imgBalloonGreen = pygame.transform.scale(pygame.image.load('../Resources/greenballoon.jpg'),
                                             (pixel_width_new, pixel_height_new))
    imgBalloonBlue = pygame.transform.scale(pygame.image.load('../Resources/blueballoon.jpg'),
                                            (pixel_width_new, pixel_height_new))
    imgBalloonYellow = pygame.transform.scale(pygame.image.load('../Resources/yellowballoon.jpg'),
                                              (pixel_width_new, pixel_height_new))
    imgBalloonPink = pygame.transform.scale(pygame.image.load('../Resources/pinkballoon.jpg'),
                                            (pixel_width_new, pixel_height_new))
    imgBalloonOrange = pygame.transform.scale(pygame.image.load('../Resources/orangeballoon.jpg'),
                                              (pixel_width_new, pixel_height_new))
    imgBalloonDarkGreen = pygame.transform.scale(pygame.image.load('../Resources/darkgreenballoon.jpg'),
                                                (pixel_width_new, pixel_height_new))
    imgBalloonDarkBlue = pygame.transform.scale(pygame.image.load('../Resources/darkblueballoon.jpg'),
                                                 (pixel_width_new, pixel_height_new))
def should_spawn_bonus_balloon():
    return random.randint(1, 100) <= 3  # 5% chance to spawn bonus balloon

def main_menu():
    menu = True
    while menu:
        SCREEN.fill((0, 0, 0))  # Black background
        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 60)
        text = font.render('Balloon Pop Game', True, (255, 255, 255))
        start_btn = font.render('Start', True, (200, 200, 200))
        background = pygame.image.load('../Resources/Siuuu.jpg')
        background = pygame.transform.scale(background, (SCREEN_width, SCREEN_height))
        SCREEN.blit(background, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        button_rect = start_btn.get_rect(center=(SCREEN_width // 2, SCREEN_height // 2))

        if button_rect.collidepoint(mouse_pos):
            start_btn = font.render('Start', True, (255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return  # Exit menu

        SCREEN.blit(text, (320, 150))
        SCREEN.blit(start_btn, button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()
        clock.tick(15)


def end_game_screen(score,a):
    end_game = True
    while end_game:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
        text_score = font.render(f'Your Score: {score}', True, (200, 200, 200))
        restart_btn = font.render('Restart', True, (200, 200, 200))
        background = pygame.image.load('../Resources/Siuuu.jpg')
        background = pygame.transform.scale(background, (SCREEN_width, SCREEN_height))
        SCREEN.blit(background, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        button_rect = restart_btn.get_rect(center=(SCREEN_width // 2, SCREEN_height // 2 + 100))

        if button_rect.collidepoint(mouse_pos):
            restart_btn = font.render('Restart', True, (255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True  # Signal to restart the game

        SCREEN.blit(text_score, (450, 350))
        SCREEN.blit(restart_btn, button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        pygame.display.update()
        clock.tick(15)

def chca(): #cơ hội cho ai !!!
    global  score
    global speed
    cohoi = random.randint(1,5)
    if cohoi == 1:
        score +=10
    elif cohoi == 2:
        score -= 1
    elif cohoi == 3:
        speed +=5
        score +=2
    elif cohoi == 4:
        score -= score
        score += 1
    else:
        speed -= 2


# Main loop
main_menu()  # Add this line to call the menu
start = True
while start:
   start = True
   while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    timeRemain = int(totalTime -(time.time()-startTime))
    if timeRemain <0:
            restart = end_game_screen(score, 'Congrats')
            if restart:
                score = 0
                startTime = time.time()
                speed = 15
                escapeCount = 0
                level = 1
                resetBalloon()
                SCREEN.fill((255, 255, 255))
                font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
                textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
                textTime = font.render(f'Time UP', True, (50, 50, 255))
                SCREEN.blit(textScore, (450, 350))
                SCREEN.blit(textTime, (530, 275))
                continue
            else:
                break
    else:
        # OpenCV
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)

        rectBalloon.y -= speed  # Move the balloon up
        # check if balloon has reached the top without pop
        if rectBalloon.y < 0:
            if imgBalloon != imgBalloonBonus:  # Don't count escape if it's the bonus balloon
                escapeCount += 1
            resetBalloon()
            if escapeCount >= maxEscapes:
                game_over = end_game_screen(score, "Game Over")  # Show "Game Over" screen
                if game_over:
                    score = 0
                    level = 1
                    speed = 15
                    escapeCount = 0
                    startTime = time.time()
                    resetBalloon()
                    continue
                else:
                    break
            else:
                speed += 1  # Increase speed for each escape, optional
        if hands:
            hand = hands[0]
            x, y = hand['lmList'][8]
            if rectBalloon.collidepoint(x, y):
                if imgBalloon == imgBalloonBonus:
                    score += 500  # Add 10 seconds if bonus balloon is popped
                resetBalloon()
                resetBalloon()
                score += 10
                speed += 0.5
                pop_sound.play()
                if score >= level * levelUpScore:
                    level += 1
                    speed += 1
                    if level == 3:
                        size_change()
                    elif level == 5:
                        chca()

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        SCREEN.blit(frame, (0, 0))
        SCREEN.blit(imgBalloon, rectBalloon)

        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
        textScore = font.render(f'Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
        textLevel = font.render(f'Level: {level}', True, (50, 50, 255))
        textEscape = font.render(f'Escape: {escapeCount}', True, (50, 50, 255))
        SCREEN.blit(textEscape, (1000,85))
        SCREEN.blit(textScore, (35, 35))
        SCREEN.blit(textTime, (1000, 35))
        SCREEN.blit(textLevel, (35, 85))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)