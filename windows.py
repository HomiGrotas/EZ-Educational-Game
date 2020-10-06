import pygame

# to able the changing of the window
from pygame.locals import RESIZABLE, VIDEORESIZE
from text_to_speech import Speak
from sys import exit as exit_sys

__author__ = "Nadav Shani"

###########################
# Windows file  - (class) #
###########################

# initialize pygame
pygame.init()

# gets information about the screen (is needed for size)
info = pygame.display.Info()


# loading photos
parent_directory = "pictures and music"
levels_buttons_he = pygame.image.load(parent_directory +
                                      "/windows_photos/levels_buttons_he.png")

main_background = pygame.image.load(parent_directory +
                                    "/windows_photos/background.png")

about_hebrew = pygame.image.load(parent_directory +
                                 "/windows_photos/aboutHE.png")

about_english = pygame.image.load(parent_directory +
                                  "/windows_photos/aboutEN.png")

icon = pygame.image.load(parent_directory +
                         "/windows_photos/logo.png")

intro_buttons_en = pygame.image.load(parent_directory +
                                     "/windows_photos/home_screen_b-EN.png")

intro_buttons_he = pygame.image.load(parent_directory +
                                     "/windows_photos/home_screen_b-HE.png")

start_buttons = pygame.image.load(parent_directory +
                                  "/windows_photos/levels_buttons_en.png")

hebrew_button = pygame.image.load(parent_directory +
                                  "/windows_photos/hebrewB.png")

english_button = pygame.image.load(parent_directory +
                                   "/windows_photos/englishB.png")

return_button = pygame.image.load(parent_directory +
                                  "/windows_photos/returnB.png")

exit_button = pygame.image.load(parent_directory +
                                "/windows_photos/exitB.png")

turn_off_music_button = pygame.image.load(parent_directory +
                                          "/windows_photos/no_musicB.png")

turn_on_music_button = pygame.image.load(parent_directory +
                                         "/windows_photos/musicB.png")

three_options_win_img = pygame.image.load(parent_directory +
                                          "/windows_photos/threeOptionsImg.png"
                                          )

speak_button_en = pygame.image.load(parent_directory +
                                    "/windows_photos/speak_button_en.png")

speak_button_he = pygame.image.load(parent_directory +
                                    "/windows_photos/speak_button_he.png")

top_five_en = pygame.image.load(parent_directory +
                                "/windows_photos/leaderboards_en.png")

top_five_he = pygame.image.load(parent_directory +
                                "/windows_photos/leaderboards_he.png")

rules_he = pygame.image.load(parent_directory +
                             "/windows_photos/rules_he.png")

rules_en = pygame.image.load(parent_directory +
                             "/windows_photos/rules_en.png")

username_input_en_img = pygame.image.load(parent_directory +
                                          "/windows_photos/username_win.png")

username_input_he_img = pygame.image.load(parent_directory +
                                          "/windows_photos/username_win_he.png"
                                          )

open_qst_he = pygame.image.load(parent_directory +
                                "/windows_photos/background_qst_he.png")

open_qst_en = pygame.image.load(parent_directory +
                                "/windows_photos/background_qst_en.png")

# load game photos
img_background = pygame.image.load(parent_directory +
                                   "/game_photos/img_background2.png")

img_character = pygame.image.load(parent_directory +
                                  "/game_photos/cartoon.png")

img_crouch = pygame.image.load(parent_directory +
                               "/game_photos/cartoon_crouch.png")

img_crouch_bubble = pygame.image.load(parent_directory +
                                      "/game_photos/char crouch bubble.png")

img_char_bubble = pygame.image.load(parent_directory +
                                    "/game_photos/char bubble.png")

img_fireball = pygame.image.load(parent_directory +
                                 "/game_photos/fireball.png")

img_lavaPool = pygame.image.load(parent_directory +
                                 "/game_photos/lava_pool.png")

img_eagle = pygame.image.load(parent_directory +
                              "/game_photos/eagle.png")

img_bubble = pygame.image.load(parent_directory +
                               "/game_photos/bubble.png")

img_coin = pygame.image.load(parent_directory +
                             "/game_photos/coin.png")

img_heal = pygame.image.load(parent_directory +
                             "/game_photos/health_pic.png")

img_spike1 = pygame.image.load(parent_directory +
                               "/game_photos/spike1 copy.png")

img_spike2 = pygame.image.load(parent_directory +
                               "/game_photos/spike2 copy.png")

img_spike3 = pygame.image.load(parent_directory +
                               "/game_photos/spike3 copy.png")

img_spike4 = pygame.image.load(parent_directory +
                               "/game_photos/spike4 copy.png")

img_spike5 = pygame.image.load(parent_directory +
                               "/game_photos/spike5 copy.png")

img_spike6 = pygame.image.load(parent_directory +
                               "/game_photos/spike6 copy.png")

img_game_over = pygame.image.load(parent_directory + "/game_photos/over.png")

# load game music
button_click_music = pygame.mixer.Sound(parent_directory +
                                        "/music/button_click_music.wav")

punch_music = pygame.mixer.Sound(parent_directory +
                                 "/music/Punch Sound Effect.wav")

# load windows effects (wrong/ correct answer)

correct_ans_music = pygame.mixer.Sound(parent_directory +
                                       "/music/Correct Sound Effect.wav")
wrong_ans_music = pygame.mixer.Sound(parent_directory +
                                     "/music/Wrong Sound Effect.wav")


# loading windows music
def load_windows_music():
    pygame.mixer.music.load(parent_directory + "/music/backgroundMusic.mp3")

    # playing background music forever
    pygame.mixer.music.play(-1)


# loading game music
def load_game_music():
    pygame.mixer.music.load(parent_directory + '/music/game_music.mp3')

    # playing background music forever
    pygame.mixer.music.play(-1)


# setting volume to the background music
pygame.mixer.music.set_volume(0.3)
pygame.mixer.Sound.set_volume(button_click_music, 0.9)

# arrow cursor
normal_cursor = (16, 19), (0, 0), (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132,
                                   0, 130,
                                   0, 129, 0, 128, 128, 128, 64, 128, 32, 128,
                                   16, 129, 240, 137, 0, 148,
                                   128, 164, 128, 194, 64, 2, 64, 1, 128),\
                                   (128, 0, 192, 0, 224, 0, 240, 0,
                                    248, 0, 252, 0, 254, 0, 255, 0, 255, 128,
                                    255, 192, 255, 224, 255, 240,
                                    255, 240, 255, 0, 247, 128, 231, 128, 195,
                                    192, 3, 192, 1, 128)

# cursor in shape of cross
x_cursor = (8, 8), (4, 4), (24, 24, 24, 231, 231, 24, 24, 24),\
           (0, 0, 0, 0, 0, 0, 0, 0)


# creating an object of window - doesn't must to be the main window
class Window:
    # features in all the Window objects
    load_windows_music()
    pygame.display.set_caption("EZ - learn English with the Zoo")
    pygame.display.set_icon(icon)

    ###########################################################################
    # __init__ function                                                       #
    #   input: english and hebrew images (image),                             #
    #   language of the window (Hebrew / English), play music (boolean)       #
    #          width (int) and height (int) of the window                     #
    #   does: set title, create pygame window,                                #
    #   makes font according to the windows size                              #
    #   change background & language button (image)                           #
    #    according to the language og the window                              #
    #                                                                         #
    #   qualities: english & hebrew _image (image),                           #
    #              featuresLst- types of objects on the screen(button / label)#
    #              featuresArgs (the arguments for the functions              #
    #              of the windows features)                                   #
    #              background (hebrew / english image),                       #
    #              font (default type, the size of the window / 30)           #
    #              win (pygame surface),                                      #
    #              curW & curH (int -> the current size of the window)        #
    #              buttons info (the buttons text)                            #
    ###########################################################################
    def __init__(self, english_img, hebrew_img, language_app, play_music,
                 cur_w, cur_h, change_buttons_order=False):

        # setting parameters to the object's qualities
        self.hebrew_image = hebrew_img
        self.play_music = play_music
        self.english_image = english_img
        self.background = english_img
        self.language = language_app
        self.change_buttons_order = change_buttons_order

        # adding the exit, language and music buttons
        # list of the images and labels
        self.featuresLst = ["button", "button", "button", "button"]

        # features properties
        self.featuresArgs = [(exit_button, 1.1, 1.1, (10, 10)), ]
        self.div_font = 30  # rate division of the font

        # no sentences to speak in addition to the question and answers
        self.buttons_info = ()
        self.can_help = True

        self.curW, self.curH = cur_w, cur_h
        self.font = pygame.font.Font(
            None, int((self.curW + self.curH) / self.div_font))
        self.win = pygame.display.set_mode((self.curW, self.curH), RESIZABLE)

        print(self.curW, self.curH)

        # making the language button and checks background
        img = english_button
        temp = speak_button_en
        if self.language == "Hebrew":
            # it will change when we call the resize function
            img = hebrew_button
            self.background = hebrew_img
            temp = speak_button_he

        if self.play_music:
            music_img = turn_on_music_button
        else:
            music_img = turn_off_music_button

        self.featuresArgs.append((temp, 550, 1.1, (10, 10)))
        self.featuresArgs.append((img, 1.34, 1.1, (10, 10)))
        self.featuresArgs.append((music_img, 1.21, 1.105, (10, 10)))

    ###########################################################################
    # resize function                                                         #
    #    input: the current size of the window (int - width, int - height)    #
    #    does: resize all the features in the current window (in featuresLst) #
    #    and draw them                                                        #
    #          resize the background image and draw it, update curH & curW,   #
    #          update the size font to the size of the width and height / 30  #
    #    how: every feature in featuresLst has its arguments in featuresArgs. #
    #    The arguments in the                                                 #
    #         index of 0 and 1 show with how many to divide the               #
    #         width and height and to get the                                 #
    #         location of the drawing.                                        #
    #    why: It's the best way to keep proportion in the window.             #
    ###########################################################################
    def resize(self, size):
        print("called - resize")
        self.curW, self.curH = size

        # change font and background to the current size
        self.font = pygame.font.Font(
            None, int((self.curW + self.curH) / self.div_font))
        self.win = pygame.display.set_mode(size, RESIZABLE)

        # draw the background in its new size
        self.win.blit(self.transform_img(self.background, (1, 1)), (0, 0))

        # change the size and the location of the features
        for ind, elem in enumerate(self.featuresLst):
            if elem == "button":
                scale = self.featuresArgs[ind][3]

                try:
                    if self.language == "English":
                        img = self.featuresArgs[ind][0][0]
                    else:
                        img = self.featuresArgs[ind][0][1]
                except TypeError:  # if there is just one type of buttons
                    img = self.featuresArgs[ind][0]
                transformed_img = self.transform_img(img, scale)

                # Call the function of the button with the parameters
                self.draw_button(transformed_img, self.featuresArgs[ind][1],
                                 self.featuresArgs[ind][2])

            else:  # if it's a label
                if self.can_help:
                    if self.language == "English":
                        text = self.featuresArgs[ind][0][0]
                    else:
                        text = self.featuresArgs[ind][0][1]

                else:
                    text = self.featuresArgs[ind][0]
                if len(self.featuresArgs[ind]) < 4:
                    self.label(text, self.featuresArgs[ind][1],
                               self.featuresArgs[ind][2])
                else:
                    self.label(text, self.featuresArgs[ind][1],
                               self.featuresArgs[ind][2],
                               color=self.featuresArgs[ind][3])

            # ind += 1 - Doesnt needed?

    ###############################################################
    # transform_img function                                      #
    #   input: img (image), scale (size)                          #
    #   does: changes the size of the image according             #
    #   to the size of the window                                 #
    ###############################################################
    def transform_img(self, img, scale):
        img = pygame.transform.scale(img, (int(self.curW / scale[0]),
                                     int(self.curH / scale[1])))

        return img

    ###########################################################################
    # label function                                                          #
    #   input: text to write (string), div_x (int) and div_y (int)            #
    #                                                                         #
    #   does: draw the message in black in the width / div_x & height / div_y #
    #   on the window                                                         #
    ###########################################################################
    def label(self, msg, div_x, div_y, color=(255, 255, 255)):

        # write the label:
        x, y = self.curW / div_x, self.curH / div_y
        text = self.font.render(msg, 0, color)
        self.win.blit(text, (x, y))

    ###########################################################################
    # on_button function                                                      #
    # input: locations of buttons to checks, x & y of the press               #
    # output: if it isn't a location of a button it returns -1. Otherwise,    #
    #         it returns the index of the button that was pressed.            #
    #                                                                         #
    ###########################################################################
    def on_button(self, buttons_loc, x, y):
        ind = -1
        for num, button in enumerate(buttons_loc):
            if (x > button[0] * self.curW) and (x < button[1] * self.curW):

                # if the y of the click is between the height of
                # the window * the ration of the y of the button
                # for example: if the max ratio is 0.3 and the height is 1000
                # the max y of the button will be 300
                if (y > button[2] * self.curH) and (y < button[3] * self.curH):
                    ind = num
        return ind

    #######################################
    # text to speech                      #
    # call a function that start threading#
    # for saying as fast as possible      #
    #######################################
    def say_all(self):
        if self.language == "English":
            s = Speak()
            for ind, item in enumerate(self.featuresLst):
                if item == "label":
                    s.start_say(self.featuresArgs[ind][0][0])
            for sen in self.buttons_info:
                s.start_say(sen)
            del s

    ###########################################################################
    # check_button_without_exit function                                      #
    #   input: the x & y (the location) of the click                          #
    #   does: checks buttons that haven't option to change                    #
    #   window (language button / music button)                               #
    #   there is another function that has the ability to move between windows#
    ###########################################################################
    def check_button_without_exit(self, x, y):
        # the location of the buttons:
        buttons_loc = ((0.77, 0.84, 0.9, 1),  # music button
                       (0.84, 0.92, 0.9, 1),  # change language button
                       (0.011, 0.09, 0.9, 1)  # speak button
                       )
        # functions to run for every coordinate in buttons_loc
        func = (self.change_language,
                self.change_music,
                self.say_all
                )

        ind = self.on_button(buttons_loc, x, y)
        if ind != -1:
            # play click sound
            if self.play_music:
                pygame.mixer.Sound.play(button_click_music)

            # call the function
            func[ind]()

    ###########################################################################
    # check_button function                                                   #
    #   input: location of buttons (list), the x (int)                        #
    #   and y (int) of the press                                              #
    #   does: checks if a button from the button_loc was pressed              #
    #         if it was pressed the function will return False to stop the    #
    #         current window and exit / move to another window                #
    #         and it will also return the index of the button that was pressed#
    ###########################################################################
    def check_button(self, buttons_loc, x, y):
        keep_running = True
        ind = self.on_button(buttons_loc, x, y)
        if ind != -1:
            keep_running = False  # stop running and moving to another window
            # play sound of click (because the button was clicked)
            if self.play_music:
                pygame.mixer.Sound.play(button_click_music)

        return keep_running, ind

    ###########################################################################
    # draw_button function                                                    #
    #   input: image of button (image), the div_x (float / int) and           #
    #   div_y (float / int)                                                   #
    #   does: draw a button in the location of the x / div_x and y / div_y    #
    #   why: to keep the ratio of the window                                  #
    ###########################################################################
    def draw_button(self, button, div_x, div_y):
        x, y = self.curW / div_x, self.curH / div_y
        self.win.blit(button, (x, y))

    ###########################################################################
    # make_return_button function                                             #
    #   input: None                                                           #
    #   does: adds to the featuresLst the type of the feature (button),       #
    #         adds to the featuresArgs the image of the back button,          #
    #         the div_x & div_y of the location of the button                 #
    #         and the size of the button                                      #
    ###########################################################################
    def make_return_button(self):
        self.featuresLst.append("button")
        self.featuresArgs.append((return_button, 1.5, 1.1, (10, 10)))

    ##########################################################################
    # change_music function                                                  #
    #   input: Nothing                                                       #
    #   does: checks if music is playing and pause / unpause                 #
    #   how: changes self.play and uses the pygame functions pause / unpause #
    #        and calls the resize function                                   #
    ##########################################################################
    def change_music(self):
        if self.play_music:
            pygame.mixer.music.pause()
            self.play_music = False
            music_img = turn_off_music_button
        else:
            pygame.mixer.music.unpause()
            self.play_music = True
            music_img = turn_on_music_button

        self.featuresArgs[3] = (music_img, 1.21, 1.105, (10, 10))
        self.resize((self.curW, self.curH))

    ###########################################################################
    # change_language function                                                #
    #   input: None                                                           #
    #   does: change language from hebrew to english or opposite by:          #
    #         checks the current language of the window                       #
    #         changes the language button and the background to the           #
    #         other language                                                  #
    #                                                                         #
    #   how: it changes the arguments in the featuresArgs to the image        #
    #   of the other                                                          #
    #        language and then calls the                                      #
    #        resize function (to make those changes)                          #
    ###########################################################################
    def change_language(self):
        if self.language == "English":
            self.language = "Hebrew"
            img = self.hebrew_image
            img2 = hebrew_button  # language button
            speak_temp = speak_button_he

        else:
            self.language = "English"
            img = self.english_image
            img2 = english_button
            speak_temp = speak_button_en

        self.background = img

        self.featuresArgs[2] = (img2, 1.34, 1.1, (10, 10))
        self.featuresArgs[1] = (speak_temp, 550, 1.1, (10, 10))
        self.resize((self.curW, self.curH))

    ###################################################################
    # mouse_motion function                                           #
    #   input: button_loc (the locations of the buttons)              #
    #   does: gets the coordinates of the mouse,                      #
    #         checks if the coordinates are a part of a button,       #
    #         if it is- it changes the shape of the mouse cursor      #
    ###################################################################
    def mouse_motion(self, buttons_loc):
        x, y = pygame.mouse.get_pos()
        if self.on_button(buttons_loc + [(0.77, 0.84, 0.9, 1),
                                         (0.84, 0.92, 0.9, 1)], x, y) != -1:
            pygame.mouse.set_cursor(*x_cursor)
        else:
            pygame.mouse.set_cursor(*normal_cursor)

    ###########################################################################
    # run function                                                            #
    #   this function runs the window with its while loop                     #
    #   it's the main function of the window                                  #
    #   input: locations of buttons and the next window/s                     #
    #                                                                         #
    #   does: appends the location of the exit and music button               #
    #   to the locations of buttons                                           #
    #         (because every window has this button),                         #
    #         runs the while loop and updating the display of the window,     #
    #         checks the events of the window and calls some functions        #
    #         if it's needed                                                  #
    ###########################################################################
    def run(self, buttons_loc, func_to_call):
        print("called - run")

        # adding the location of the exit button
        buttons_loc.append((0.92, 1, 0.9, 1))

        # setting clock
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            # update the screen
            pygame.display.update()

            # for event in the events of the game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    exit_from_game()

                # if there is a change in the size
                elif event.type == VIDEORESIZE:
                    self.resize(event.size)

                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_motion(buttons_loc)

                # if the user clicked on something
                # with the left side of the mouse
                elif event.type == pygame.MOUSEBUTTONDOWN\
                        and event.button == 1:

                    # Set the x, y positions of the mouse click
                    x, y = event.pos

                    # checks if the loop needs to stop and checks
                    # gets the number of the function to run
                    # (it doesn't mean that the function will be called)
                    run, ind = self.check_button(buttons_loc, x, y)

                    if ind == len(buttons_loc) - 1:
                        run = False
                        exit_from_game()

                    # if the app should go to another window
                    elif not run:
                        if self.language == "Hebrew":
                            if self.change_buttons_order and ind != 0:
                                ind = len(func_to_call) - ind
                        func_to_call[ind](self.curW, self.curH, self.language,
                                          self.play_music)

                    # if the loop needs to continue
                    else:
                        # checks if it's one of the none-exit buttons
                        self.check_button_without_exit(x, y)

                    print(f'Clicked on screen: ({x},{y})')


#################################################
# exit_from_program_function                    #
#   does: exit from pygame                      #
#   should do: Disconnect from the database     #
#################################################
def exit_from_game():
    print("-------------EXIT-------------")
    Speak.speak = False
    pygame.quit()
    exit_sys()
