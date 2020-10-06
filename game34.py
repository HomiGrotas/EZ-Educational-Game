import pygame
import time
import random
from math import ceil
from windows import img_background, img_eagle, img_spike2, img_spike1,\
    img_lavaPool, img_fireball, img_crouch_bubble, img_heal,\
    img_coin, img_bubble, img_crouch, img_char_bubble, img_character,\
    load_game_music, img_spike3, img_spike4, img_spike5, img_spike6,\
    img_game_over, turn_on_music_button, turn_off_music_button, exit_button,\
    punch_music, load_windows_music, exit_from_game
from main import username_input_win

__authors__ = "Yair Shalit & Eyal Engel"

################
#  Game file   #
################

# Initialize pygame
pygame.init()

# Creates a resolution for the game
win = pygame.display.set_mode((1200, 600))
img_background = pygame.transform.scale(img_background, (1200, 600))

img_time_bubble = pygame.transform.scale(img_bubble, (50, 50))

# Loading music - background music
load_game_music()

music_img = turn_off_music_button


# creating an object of player
class Player:

    ###########################################################################
    # __init__ function                                                       #
    #                                                                         #
    #   input: a character image (image), amount of life (int)                #
    #                                                                         #
    #   does: set character image, set health,  of                            #
    #         sets and resets immunity time and crouch time                   #
    ###########################################################################

    def __init__(self, img, health, x, y):

        self.img = img
        self.health = health
        self.x = x
        self.y = y
        self.is_jump = False
        self.jump_count = 12
        self.time_crouch = 0
        self.time_immune = 0

    ##########################################################################
    # __check_hit__ function                                                 #
    #                                                                        #
    #   input: a obstacle image (image)                                      #
    #                                                                        #
    #   does: Checks whether the player's character has been hit by an       #
    #         obstacle                                                       #
    ##########################################################################

    def check_hit(self, obs):
        global player
        if self.time_crouch < seconds:
            if(self.x > obs.x - obs.width) and(self.x < obs.x + obs.width):
                if ((obs.y - obs.height) < self.y < (obs.y + obs.height)):
                    if music_on:
                        pygame.mixer.Sound.play(punch_music)
                    self.time_immune = seconds + 2
                    self.health -= 1
        else:
            if(self.x > obs.x - obs.width) and (self.x < obs.x + obs.width):
                if (self.y > obs.y - obs.height - 5):
                    if (self.y < obs.y + obs.height - 20.0):
                        if music_on:
                            pygame.mixer.Sound.play(punch_music)
                        self.time_immune = seconds + 2
                        self.health -= 1

        if player.health == 0:
            end_game()

    ###########################################################################
    # __jump__ function                                                       #
    #                                                                         #
    #   input: a variable that determines whether the character jumps or      #
    #          lands                                                          #
    #                                                                         #
    #   does: The player's character will jump                                #
    #                                                                         #
    ###########################################################################

    def jump(self, neg):
        self.y -= (abs(self.jump_count * 2) ** 2) * neg * 0.13

    ###########################################################################
    # __crouch__ function                                                     #
    #                                                                         #
    #   input: nothing                                                        #
    #                                                                         #
    #   does: The player's character will crouch and the picture will         #
    #         change to crouching mode with protection                        #
    #                                                                         #
    ###########################################################################

    def crouch(self):
        if self.time_immune > seconds:
            self.img = img_crouch_bubble
        else:
            self.img = img_crouch
        self.time_crouch = seconds + 1.5

# End of class Player


# creating an object of obstacle
class Obstacle:

    ###########################################################################
    # __init__ function                                                       #
    #                                                                         #
    #   input: an obstacle image (image), position -  width (int)             #
    #          and height (int), Latitude and longitude velocity (int)        #
    #                                                                         #
    #   does: set obstacle image, set position on the latitude,               #
    #         set position on the longitude,                                  #
    #         set longitudinal speed and set latitude speed                   #
    #                                                                         #
    #                                                                         #
    ###########################################################################

    def __init__(self, img, x, y, speed_x, speed_y):

        self.img = img
        self.x = x
        self.y = y
        self.speed_x = speed_x * lvl_speed
        self.speed_y = speed_y * lvl_speed
        self.width = 40
        self.height = 30

    ##########################################################################
    # __move__ function                                                      #
    #                                                                        #
    #   input: nothing                                                       #
    #                                                                        #
    #   does:  The player's character will move along the latitude           #
    #          and longitude                                                 #
    #                                                                        #
    ##########################################################################

    def move(self):

        self.x += self.speed_x
        self.y += self.speed_y

    #########################################################################
    # __restart__ function                                                  #
    #                                                                       #
    #   input: nothing                                                      #
    #                                                                       #
    #   does:  When one of the obstacles has already passed through         #
    #          the screen,                                                  #
    #   the function resets the location and speed of the obstacle          #
    #   to the initial position                                             #
    #                                                                       #
    #########################################################################

    def restart(self):
        lst = [
            img_fireball, img_lavaPool, img_eagle, img_spike1, img_spike2,
            img_spike3, img_spike4, img_spike5, img_spike6
            ]

        self.x = 1200

        self.speed_x = -10 * lvl_speed

        n = random.randint(0, 8)

        self.img = lst[n]

        if n == 0:
            self.y = random.randint(280, 400)
            self.speed_y = 0
        elif n == 1:
            self.y = 400
            self.speed_y = 0
        elif n == 2:
            self.y = 0
            self.speed_y = 3.8 * lvl_speed
        else:
            self.y = 350
            self.speed_y = 0
            self.height = 70

# End of class Obstacle


# creating an object of bonus
class Bonus:

    ##########################################################################
    # __init__ function                                                      #
    #                                                                        #
    #   input: nothing                                                       #
    #                                                                        #
    #   does:   Create a randomal bonus object (Coin, Immunity or Extra life)#
    #           with its image, in randomal y location (in range 200 - 300)  #
    #                                                                        #
    ##########################################################################

    def __init__(self):

        self.x = 1200
        self.y = random.randint(200, 330)
        self.speed_x = -10 * lvl_speed

        # bonuses = ["heal", "bubble", "coin"]
        n = random.randint(0, 2)

        if n == 1:
            self.img = img_bubble

        elif n == 2:
            self.img = img_coin

        else:
            m = random.randint(0, 5)
            if m == 0:
                self.img = img_heal
            else:
                self.img = img_coin

    ##########################################################################
    # __move__ function                                                      #
    #                                                                        #
    #   input: nothing                                                       #
    #                                                                        #
    #   does: move the bonus left according to its speed                     #
    #                                                                        #
    ##########################################################################

    def move(self):
        self.x += self.speed_x

    ##########################################################################
    # __check_get__ function                                                 #
    #                                                                        #
    #   input: the player object                                             #
    #                                                                        #
    #   does: check if the player 'touch' the bonus. If he does, the player  #
    #         get the bonus (Coin - increase the score_bonus by 25,          #
    #         Bubble - give the player 5 seconds of immunity, health -       #
    #         give the player extra life)                                    #
    #                                                                        #
    ##########################################################################

    def check_get(self, player):

        global score_bonus

        if self.x - 40 < player.x < self.x + 40:
            if self.y - 30 < player.y < self.y + 30:
                self.x = - 300

                if self.img == img_coin:
                    score_bonus += 25
                elif self.img == img_bubble:
                    player.time_immune = seconds + 5
                else:
                    if player.health <= 10:
                        player.health += 1

# End of class bonus

    ##########################################################################
    # __wait_to_start__ function                                             #
    #                                                                        #
    #   input: nothing                                                       #
    #                                                                        #
    #   does: stop the game until the user press the space button.           #
    #         the user still can exit the game.                              #
    ##########################################################################


def wait_to_start():

    global run

    wait = True

    win.blit(img_background, (0, 0))
    win.blit(exit_button, (1134, 528))
    win.blit(font.render("Press space to start", 1, (0, 0, 0)), (420, 300))
    pygame.display.update()

    while wait:

        user_keys = pygame.key.get_pressed()
        if user_keys[pygame.K_SPACE]:
            wait = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if x in range(1130, 1240) and y in range(536, 579):
                    wait = False
                    run = False

    ##########################################################################
    # __calc_lifes__ function                                                #
    #                                                                        #
    #   input: level(int) and the amount of questions answered is correct    #
    #                                                                        #
    #   does: Calculate the amount of life according to the number of        #
    #         questions answered correctly                                   #
    #                                                                        #
    ##########################################################################


def calc_lifes(level, correct_qst):

    if level == 1:
        lifes = correct_qst // 3

    elif level == 2:
        lifes = correct_qst // 2

    else:
        lifes = correct_qst

    if lifes == 0:
        lifes = 1

    return lifes

##############################################################################
# __draw_game__ function                                                     #
#                                                                            #
#   input: the background image (image), the player object (player object),  #
#         list of the obstacles (list of obstacle objects), bonuses          #
#         (list of bonuses objects), the current score.                      #
#                                                                            #
#   does: blit the background, the player, the obstacles, the bonuses,       #
#         images of hearts like the amount of lifes the player has and the   #
#         music and exit buttons. blit the score to the screen.              #
#         if the player is immune, blit an image of shield and the amount    #
#         of seconds of immunity left                                        #
#                                                                            #
##############################################################################


def draw_game(background, player, obstacles, bonuses, score):

    win.blit(background, (0, 0))

    win.blit(player.img, (player.x, player.y))

    for obs in obstacles:
        win.blit(obs.img, (obs.x, obs.y))

    for bonus in bonuses:
        win.blit(bonus.img, (bonus.x, bonus.y))

    win.blit(font.render("Score: " + str(score), 1, (0, 0, 0)), (400, 10))

    for i in range(player.health):
        win.blit(img_heal, (720 + 40 * i, 0))

    win.blit(music_img, (1084, 528))

    win.blit(exit_button, (1134, 528))

    if player.time_immune > seconds:
        win.blit(img_time_bubble, (300, 0))
        win.blit(font.render(str(ceil(player.time_immune - seconds)),
            1, (0, 0, 0)), (280, 10))

##############################################################################
# __change_music__ function                                                  #
#                                                                            #
#   input: boolean global variable that tell if the music is on.             #
#          boolean variable of the current picture of the music button.      #
#                                                                            #
#   does: if the music is on, turn it off and change the picture of the      #
#         music button.                                                      #
#         if the music is off, turn it on and change the picture of the      #
#         music button.                                                      #
#                                                                            #
##############################################################################


def change_music():
    global music_on
    global music_img
    if music_on:
        pygame.mixer.music.pause()
        music_on = False
        music_img = turn_on_music_button
    else:
        pygame.mixer.music.unpause()
        music_on = True
        music_img = turn_off_music_button


##############################################################################
# __end_game__ function                                                      #
#                                                                            #
#   input: nothing                                                           #
#                                                                            #
#   does: blit the image of "Game Over" and wait 5 seconds.                  #
#         blit the final score and wait 5 seconds.                           #
#         (while it wait, you still can exit the game).                      #
#                                                                            #
##############################################################################

def end_game():
    run = True
    start = time.time()
    pygame.mixer.music.fadeout(7000)

    win.blit(img_background, (0, 0))
    win.blit(img_game_over, (170, 5))
    win.blit(exit_button, (1134, 528))
    pygame.display.update()

    while time.time() < start + 5 and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if x in range(1130, 1240) and y in range(536, 579):
                    run = False

    win.blit(img_background, (0, 0))

    win.blit(end_font.render("Your Final Score: " + str(score), 1, (0, 0, 0)), (280, 300))
    win.blit(exit_button, (1134, 528))
    pygame.display.update()

    while time.time() < start + 10 and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if x in range(1130, 1240) and y in range(536, 579):
                    run = False


lvl_speed = 1
run = True
music_on = True
score_bonus = 0

# The three obstacles that appear at the start of the game -
# an obstacle image (image), position -  width (int), position -  height (int),
# spped -  width (int) and speed -  height (int)
obstacles = [Obstacle(img_fireball, 1900, random.randint(300, 430), -10, 0),
             Obstacle(img_lavaPool, 1600, 400, -10, 0),
             Obstacle(img_eagle, 1200, 0, -10, 3.8)]

bonuses = []


neg = 1
score = 0

# The tens digit in time - its use in scoring --- Integer
tens_seconds_amount = 0

# Set fonts and sizes for text
font = pygame.font.SysFont("calisto", 30, True)
end_font = pygame.font.SysFont("calisto", 70, True)

# clock - global variable - FPS - frame per second --- Double
clock = pygame.time.Clock()

wait_to_start()
# A variable that shows how much time has passed since
# the start of the game --- Double
start_ticks = pygame.time.get_ticks()
player = None


def game(language_app, play_music, cur_w, cur_h, level, score_ans):

    global run, tens_seconds_amount, lvl_speed, score, seconds, player

    # Creates a Player type object
    player = Player(img_character, calc_lifes(level, score_ans), 130, 385)

    # As long as the game is running and the user has earned life in the game
    while player.health >= 1 and run:
        print(f"Score {score}, Level {level}, answered {score_ans},"
              f" lifes {player.health}")

        clock.tick(30)

        # The seconds that have passed since running the game
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        pygame.display.update()

        # Paint the objects on the screen --- using 'draw_game' function
        draw_game(img_background, player, obstacles, bonuses, score)

        # Always check that the user did not press the exit game
        # or the Pygame exit button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if x in range(1080, 1150) and y in range(520, 600):
                    change_music()

                elif x in range(1130, 1240) and y in range(536, 579):
                    run = False

        # Checks whether 10 seconds have passed, and updates the speed
        if int(seconds) / 10 == tens_seconds_amount:
            tens_seconds_amount += 1

            lvl_speed += 0.1

            bonuses.append(Bonus())

        # Calculate the score and print it
        score = int(seconds * tens_seconds_amount - (
                    tens_seconds_amount - 1) * 10) + score_bonus

        # if the player stopped crouching, change the image
        #  of the player to the normal.
        if player.time_crouch < seconds:
            player.img = img_character

        # if the player is immune, change the image of the player
        #  to img_char_bubble.
        if player.time_immune > seconds:
            player.img = img_char_bubble

        # get the keys the ussr press
        keys = pygame.key.get_pressed()

        if not player.is_jump:
            # if the user pressed K_SPACE and the player isn't crouching,
            # the player begins to jump.
            if keys[pygame.K_SPACE]:
                if player.time_crouch < seconds:
                    player.is_jump = True
                # if the player is crouching, the player stops crouching
                # and starts jumping.
                else:
                    player.time_crouch = seconds

        else:
            # calculations for the jumping
            # according to the 'neg' variable, the player jumps or lands.
            if player.jump_count >= -12:
                neg = 1
                if player.jump_count < 0:
                    neg = -1
                player.jump(neg)
                player.jump_count -= 1
            else:
                player.jump_count = 12
                player.is_jump = False

        if keys[pygame.K_DOWN]:
            if not player.is_jump:
                player.crouch()

        # for any obstacle in the list of the obstacles that on the screen
        for obs in obstacles:
            if obs.x < 160 and player.time_immune < seconds:
                player.check_hit(obs)
            if obs.x > -200:
                obs.move()
            else:
                obs.restart()

        # for the bonus that on the screen
        for bonus in bonuses:
            bonus.check_get(player)
            if bonus.x > 0:
                bonus.move()
            else:
                bonuses.remove(bonus)

    # Getting out of the game
    if run:
        print("loading")
        if play_music:
            print("error here")
            load_windows_music()
        print("calling for next win")
        username_input_win(cur_w, cur_h,
                           language_app, not play_music, score)
    exit_from_game()


#  language_app, play_music, cur_w, cur_h, level, score_ans