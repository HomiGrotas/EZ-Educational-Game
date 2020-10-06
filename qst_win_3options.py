import random
import pygame
from windows import Window, three_options_win_img, exit_from_game,\
    exit_button, turn_on_music_button, turn_off_music_button, return_button,\
    button_click_music, x_cursor, normal_cursor, correct_ans_music,\
    wrong_ans_music
from pygame.locals import VIDEORESIZE  # to able the changing of the window
from time import time
__author__ = "Nadav Shani"


##############################################################################
# making a questions window - inherits abilities from the normal window      #
# it has the ability to get input from the user by buttons                   #
# gets in addition to window parameters:  qst (list)                         #
# - all the possible questions                                               #
#   ans (list)- all the possible answers                                     #
##############################################################################
class QstWin3Options(Window):
    def __init__(self, english_img, hebrew_img, language_app, play_music,
                 width, height, qst, ans):
        super().__init__(english_img, hebrew_img, language_app, play_music,
                         width, height)
        self.qst_lst = qst
        self.answers_lst = ans

        # override current button in the window's features
        self.featuresLst = ["button", "button", "button"]
        self.featuresArgs = [(exit_button, 1.1, 1.1, (10, 10)),
                             (return_button, 1.34, 1.1, (10, 10))]

        if self.play_music:
            music_img = turn_on_music_button
        else:
            music_img = turn_off_music_button

        self.featuresArgs.append((music_img, 1.21, 1.105, (10, 10)))
        self.level = 1  # ToDo: calculate final score by level
        self.div_font = 40  # rate division of the font
        self.font2 = pygame.font.Font(None, int((self.curW + self.curH) / 35))
        self.score = 0  # the current score (0-10)
        self.qst_amount = 0  # amount of questions that have been asked
        self.max_qst = 10  # max amount of questions
        self.qst = ''  # questions - (string)
        self.ans = ''  # answer - (string)

        # (answer, ind ) => the index will be replaced
        self.button1 = ["string", 1]
        self.button2 = ["string", 2]
        self.button3 = ["string", 3]

        # the buttons - (answer, index)
        self.buttons = [self.button1, self.button2, self.button3]

        # the buttons locations
        self.buttons_loc = (10, 1.7), (3.1, 1.7), (1.85, 1.7)
        self.wrong_ans1 = ''  # wrong answer (string)
        self.wrong_ans2 = ''

        self.can_help = False  # prevent speak sentences method

        # adding the question button
        self.featuresLst.append("button")
        self.featuresArgs.append((three_options_win_img, 20, 4.5, (1.4, 2)))

        # adding question
        self.featuresLst.append("label")
        self.featuresLst.append("label")
        if len(self.qst) < 30:
            self.featuresArgs.append((self.qst, 12, 3))
            self.featuresArgs.append(("", 12, 3))
        else:
            ind = qst.index(" ", 30)
            self.featuresArgs.append((qst[:ind], 12, 3.2))
            self.featuresArgs.append((qst[ind+1:], 12, 2.8))

        # adding score
        self.featuresLst.append("label")
        self.featuresArgs.append((f"Score: {self.score}", 1.18, 10))

        # answers button (green, red, gray)
        self.color = \
            {
                "red": (255, 0, 0),
                "green": (0, 255, 0),
                "gray": (211, 211, 211),
            }

        # the buttons locations and colors
        self.button_answers_loc = \
            {
                (1.2, 10): self.color["gray"],
                (1.2, 6.5): self.color["gray"],
                (1.2, 4.8): self.color["gray"],
                (1.2, 3.8): self.color["gray"],
                (1.2, 3.15): self.color["gray"],
                (1.09, 10): self.color["gray"],
                (1.09, 6.5): self.color["gray"],
                (1.09, 4.8): self.color["gray"],
                (1.09, 3.8): self.color["gray"],
                (1.09, 3.15): self.color["gray"],
            }

        # makes place to the answers in the lists
        for _ in range(3):
            self.featuresLst.append("label")
            self.featuresArgs.append((None, 1, 1))

        # choose question and answers locations
        # (this method calls to another method which
        # choose question and answers)
        self.choose_loc_ans_qst()

    # override mouse motion method
    def mouse_motion(self, buttons_loc):
        x, y = pygame.mouse.get_pos()
        if self.on_button(buttons_loc + [(0.84, 0.92, 0.9, 1)], x, y) != -1:
            pygame.mouse.set_cursor(*x_cursor)
        else:
            pygame.mouse.set_cursor(*normal_cursor)

    # override check button without exit method
    def check_button_without_exit(self, x, y):
        # the location of the buttons:
        buttons_loc = (
            (0.84, 0.92, 0.9, 1),
        )

        ind = self.on_button(buttons_loc, x, y)
        if ind != -1:
            # play click sound
            if self.play_music:
                pygame.mixer.Sound.play(button_click_music)

            # call the function
            self.change_music()

    # override change music method
    def change_music(self):
        if self.play_music:
            pygame.mixer.music.pause()
            self.play_music = False
            music_img = turn_off_music_button
        else:
            pygame.mixer.music.unpause()
            self.play_music = True
            music_img = turn_on_music_button

        self.featuresArgs[2] = (music_img, 1.21, 1.105, (10, 10))
        self.resize((self.curW, self.curH))

    ##########################################################################
    # choose_loc_ans_qst method                                              #
    # does: calls the choose question and answers                            #
    # method and chooses answers locations                                   #
    ##########################################################################
    def choose_loc_ans_qst(self):
        # calls method to choose question and answer
        self.choose_qst_ans()
        ind_chosen = []

        # find available index
        def find_ind():
            for index in range(3):
                if index not in ind_chosen:
                    ind_chosen.append(index)
                    return index

        # adding answer
        ind = random.randint(0, 2)
        loc = self.buttons_loc[ind]
        self.buttons[ind][1] = ind
        self.buttons[ind][0] = self.ans
        self.featuresArgs[7] = (self.ans, *loc)
        ind_chosen.append(ind)

        # adding two wrong answers for two buttons
        # first wrong answer
        ind = find_ind()
        loc = self.buttons_loc[ind]
        self.buttons[ind][1] = ind
        self.buttons[ind][0] = self.wrong_ans1
        self.featuresArgs[8] = (self.wrong_ans1, *loc)

        # second wrong answer
        ind = find_ind()
        loc = self.buttons_loc[ind]
        self.buttons[ind][1] = ind
        self.buttons[ind][0] = self.wrong_ans2
        self.featuresArgs[9] = (self.wrong_ans2, *loc)

    def show_correct_ans(self):
        self.featuresLst.append("label")
        self.featuresArgs.append((self.ans, 2.08, 1.35, (255, 0, 0)))
        self.resize((self.curW, self.curH))

    ##########################################
    # choose question and answer method      #
    # it randoms a question and it answer,   #
    # and randoms two incorrect answers      #
    ##########################################
    def choose_qst_ans(self):
        length = len(self.qst_lst)-1  # length of the question list

        # random an question and its answer
        ind = random.randint(0, length)
        self.qst = self.qst_lst[ind]
        self.ans = self.answers_lst[ind]

        # randoms 2 incorrect answers
        ind = random.randint(0, length-1)
        self.wrong_ans1 = self.answers_lst[ind]
        self.wrong_ans2 = self.answers_lst[ind+1]

        # change the question in the feature args list

        if len(self.qst) < 35:
            self.featuresArgs[4] = (self.qst, 12, 3)
            self.featuresArgs[5] = ("", 12, 3)
        else:
            try:
                ind = self.qst.index(" ", 30)
            except ValueError:
                ind = self.qst.index(" ", 20)

            self.featuresArgs[4] = (self.qst[:ind], 12, 3.2)
            self.featuresArgs[5] = (self.qst[ind+1:], 12, 2.8)

    #################################################################
    # resize method                                                 #
    # (override)                                                    #
    # add to the resize function - call the create answers boxes    #
    #################################################################
    def resize(self, size):
        super().resize(size)
        self.create_ans_boxes()

    ########################################################################
    # create answers paint boxes method                                    #
    # it create 10 boxes to the answers and paint every box in its color   #
    ########################################################################
    def create_ans_boxes(self):
        # for every button in the button_answers_loc_and_color
        for ind, (location, color) in\
                enumerate(self.button_answers_loc.items()):

            location = (int(self.curW / location[0]),
                        int(self.curW / location[1]),
                        int(self.curW) / 15, int(self.curH) / 10)
            pygame.draw.rect(self.win, color, location)
            if ind != 9:
                self.win.blit(self.font2.render(str(ind + 1), True, (0, 0, 0)),
                              (location[0] + 32, location[1] + 16))
            else:
                self.win.blit(self.font2.render(str(ind + 1), True, (0, 0, 0)),
                              (location[0] + 20, location[1] + 16))

    ##############################################################
    # run function                                               #
    #   main loop- the difference between this function to the   #
    #   regular one is here you can get input                    #
    #   it also check the input                                  #
    ##############################################################
    def run(self, buttons_loc, func_to_call):
        started_timer = False
        start = None

        # makes a clock
        clock = pygame.time.Clock()

        # adding the location of the exit button
        buttons_loc.append((0.92, 1, 0.9, 1))
        print("run function-- working")
        run = True
        while run:
            clock.tick(60)

            # update the screen
            pygame.display.update()

            if started_timer and time() - start > 3:
                started_timer = False

                # show results of the wrong answer
                self.featuresArgs = self.featuresArgs[:-1]
                self.featuresLst = self.featuresLst[:-1]
                self.choose_loc_ans_qst()  # change question and answers
                self.qst_amount += 1  # raise the question amount by one

                # show the changes
                self.resize((self.curW, self.curH))

                if self.qst_amount == self.max_qst:
                    print("ended questions")

                    func_to_call[-1](self.language, self.play_music,
                                     self.curW, self.curH, self.level,
                                     self.score)
                    exit_from_game()
                    print("start game")

            # for event in the events of the game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                # if there is a change in the size
                elif event.type == VIDEORESIZE:
                    self.resize(event.size)

                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_motion(buttons_loc)

                # if the user clicked on something
                # with the left side of the mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Set the x, y positions of the mouse click
                        x, y = event.pos

                        # checks if the loop needs to stop and checks
                        # gets the number of the function to run
                        # (it doesn't mean that the function will be called)
                        run, ind = self.check_button(buttons_loc, x, y)

                        # if it's an answer button
                        if 0 < ind < 4:
                            if not started_timer:
                                answered_true = False

                                # location of current paint box
                                loc = list(self.button_answers_loc.keys())
                                loc = loc[self.qst_amount]

                                ind = ind-1  # change to range of 0-2

                                # check which button was pressed
                                for button in self.buttons:
                                    # check answer
                                    if button[1] == ind:
                                        if button[0] == self.ans:
                                            answered_true = True

                                if answered_true:
                                    print("answered true")
                                    if self.play_music:
                                        pygame.mixer.Sound.play(
                                            correct_ans_music)

                                    self.score += 1  # raise the score by one

                                    # change the score
                                    self.featuresArgs[6] = (
                                        f"Score: {self.score}", 1.18, 10)

                                    # change color of paint box
                                    self.button_answers_loc[loc] =\
                                        self.color["green"]

                                    # change question and answers
                                    self.choose_loc_ans_qst()

                                    # raise the question amount by one
                                    self.qst_amount += 1

                                    # show the changes
                                    self.resize((self.curW, self.curH))

                                    if self.qst_amount == self.max_qst:
                                        print("ended questions")

                                        pygame.quit()
                                        func_to_call[-1](self.language,
                                                         self.play_music,
                                                         self.curW, self.curH,
                                                         self.level,
                                                         self.score
                                                         )
                                        print("start game")

                                else:  # if didn't answer true
                                    print("wrong")
                                    if self.play_music:
                                        pygame.mixer.Sound.play(
                                            wrong_ans_music)
                                    self.show_correct_ans()
                                    started_timer = True
                                    start = time()
                                    self.button_answers_loc[loc] =\
                                        self.color["red"]
                            run = True  # if it's on timer keep running

                        # exit button
                        elif ind == len(buttons_loc) - 1:
                            run = False
                            pygame.quit()

                        # if the app should go to another window
                        elif not run:
                            func_to_call[ind](self.curW, self.curH,
                                              self.language, self.play_music)

                        # if the loop needs to continue
                        else:
                            # checks if it's one of the none-exit buttons
                            self.check_button_without_exit(x, y)

                        print(f'Clicked on screen: ({x},{y})')
        print("Window was closed")
