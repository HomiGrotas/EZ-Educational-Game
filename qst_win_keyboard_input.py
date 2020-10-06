import pygame
import random
from windows import Window, exit_from_game, exit_button, return_button,\
    button_click_music, turn_off_music_button, turn_on_music_button,\
    normal_cursor, x_cursor
from pygame.locals import VIDEORESIZE  # to able the changing of the window
from time import time

__author__ = "Nadav Shani"


#########################################################################
# making a questions window - inherits abilities from the normal window #
# it has the ability to get input from the user by keyboard             #
# gets in addition to window parameters:                                #
# qst (list) - all the possible questions                               #
# ans (list)- all the possible answers, level (int - 2/3)               #
#########################################################################
class QstWinKeyboardInput(Window):
    max_qst = 10

    def __init__(self, english_img, hebrew_img, language_app,
                 play_music, width, height, questions, answers, level):
        super().__init__(english_img, hebrew_img, language_app,
                         play_music, width, height)
        self.make_return_button()  # make return button
        self.input = ''  # default input

        # override current button in the window's features
        self.featuresLst = ["button", "button", "button"]
        self.featuresArgs = [(exit_button, 1.1, 1.1, (10, 10)),
                             (return_button, 1.34, 1.1, (10, 10))]

        if self.play_music:
            music_img = turn_on_music_button
        else:
            music_img = turn_off_music_button

        self.featuresArgs.append((music_img, 1.21, 1.105, (10, 10)))
        # for input
        self.featuresLst.append("label")

        # for input
        self.featuresArgs.append(("Type here the answer", 4.5, 2))

        self.questions = questions
        self.answers = answers
        self.answer = ''
        self.div_font = 35  # rate division of the font
        self.qst_amount = 0
        self.score = 0
        self.level = level  # Todo: calculate points by level and score
        self.featuresLst.append("label")  # for the question
        self.featuresLst.append("label")  # for the question
        self.featuresLst.append("label")  # for the score

        # for the score
        self.featuresArgs.append((f"Score: {self.score}", 1.18, 10))
        self.can_help = False

        # answers button (green, red, gray)
        self.color = \
            {
                "red": (255, 0, 0),
                "green": (0, 255, 0),
                "gray": (211, 211, 211),
            }

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

        print("level: ", level)

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

    #################################################################
    # pool_random_question                                          #
    # does: grill index and by it makes a question and answer       #
    #       add the question to the featuresArgs for painting label #
    #       (it's already in featuresLst)                           #
    #################################################################
    def pool_random_question(self):
        ind = random.randint(0, len(self.questions)-1)
        qst = self.questions[ind]
        self.answer = self.answers[ind].lower()

        print("ind:", len(self.featuresArgs) - 1)
        if len(qst) < 35:
            self.featuresArgs.append((qst, 3, 4))
            self.featuresArgs.append(("", 3, 4))
        else:
            ind2 = qst.rindex(" ", 0, 35)
            self.featuresArgs.append((qst[:ind2], 3, 4))
            self.featuresArgs.append((qst[ind2+1:], 3, 3))

    def resize(self, size):
        super().resize(size)
        self.create_ans_boxes()

    def create_ans_boxes(self):
        # for every button in the button_answers_loc_and_color
        for ind, (location, color) in\
                enumerate(self.button_answers_loc.items()):

            location = (int(self.curW / location[0]),
                        int(self.curW / location[1]),
                        int(self.curW) / 15, int(self.curH) / 10)
            pygame.draw.rect(self.win, color, location)
            if ind != 9:
                self.win.blit(self.font.render(str(ind + 1), True,
                              (0, 0, 0)), (location[0] + 32, location[1]+16))
            else:
                self.win.blit(self.font.render(str(ind + 1), True,
                              (0, 0, 0)), (location[0] + 20, location[1]+16))

    def show_correct_ans(self):
        self.featuresLst.append("label")
        self.featuresArgs.append((self.answer, 2.08, 1.35, (255, 0, 0)))
        self.resize((self.curW, self.curH))

    ##############################################################
    # run function                                               #
    #   main loop- the difference between this function to the   #
    #   regular one is here you can get input                    #
    #   it also check the input                                  #
    ##############################################################
    def run(self, buttons_loc, func_to_call):
        started_timer = False
        answered_by_button = False
        start = 0

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

                print(self.featuresArgs[6])
                self.featuresArgs.pop(5)
                self.featuresArgs.pop(5)  # change question

                self.pool_random_question()
                self.qst_amount += 1  # raise the question amount by one

                # show the changes
                self.resize((self.curW, self.curH))

                if self.qst_amount == self.max_qst:
                    print("ended questions")

                    self.win = pygame.display.set_mode((0, 0))

                    pygame.quit()
                    func_to_call[-1](self.language, self.play_music,
                                     self.curW, self.curH, self.level,
                                     self.score)

            # for event in the events of the game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    exit_from_game()

                elif event.type == pygame.KEYDOWN or answered_by_button:
                    need_resize = False
                    answered = False
                    key_name = "Empty"

                    if not answered_by_button:
                        key_name = pygame.key.name(event.key)

                    if key_name == 'return' or answered_by_button:
                        answered = True
                        need_resize = True
                        answered_by_button = False

                    if len(self.input) < 20:

                        if len(key_name) == 1:
                            self.input += key_name
                            need_resize = True

                        elif key_name == 'backspace':
                            self.input = self.input[:-1]
                            need_resize = True

                        elif key_name == 'space':
                            self.input += ' '
                            need_resize = True

                    # if a key that is needed was clicked
                    if need_resize:
                        self.win.blit(self.background, (0, 0))
                        if answered and not started_timer:
                            loc = list(self.button_answers_loc.keys())\
                                [self.qst_amount]

                            # if answered true
                            if self.input == self.answer:
                                self.button_answers_loc[loc]\
                                    = self.color["green"]
                                self.score += 1
                                # change the score
                                self.featuresArgs[3] = (f"Score: {self.score}",
                                                        1.18, 10)

                                self.featuresArgs.pop(5)  # change question
                                self.featuresArgs.pop(5)  # change question

                                # give another question
                                self.pool_random_question()
                                self.qst_amount += 1

                                # play correct answer effect
                                # pygame.mixer.Sound.play(correct_ans_effect)

                            else:  # if answered false
                                self.button_answers_loc[loc]\
                                    = self.color["red"]

                                self.show_correct_ans()
                                started_timer = True
                                start = time()

                            # anyway:
                            print(self.input, self.answer)
                            self.input = ''  # reset the input

                        # change the current input
                        self.featuresArgs[3] = (self.input, 4.5, 2)

                        # if answered 10 questions
                        if self.qst_amount == QstWinKeyboardInput.max_qst:
                            pygame.quit()
                            func_to_call[-1](self.language, self.play_music,
                                             self.curW, self.curH, self.level,
                                             self.score)

                        # if the window should keep running
                        if need_resize:
                            # make the changes
                            self.resize((self.curW, self.curH))
                            self.create_ans_boxes()

                # if there is a change in the size
                elif event.type == VIDEORESIZE:

                    self.resize(event.size)

                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_motion(buttons_loc)

                # if the user clicked on something with
                # the left side of the mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Set the x, y positions of the mouse click
                        x, y = event.pos

                        # checks if the loop needs to stop and checks
                        # gets the number of the function to run
                        # (it doesn't mean that the function will be called)
                        run, ind = self.check_button(buttons_loc, x, y)

                        if ind == len(buttons_loc) - 1:
                            exit_from_game()

                        if ind == 1:
                            run = True
                            answered_by_button = True

                        # if the app should go to another window
                        elif not run:
                            func_to_call[ind](self.curW, self.curH,
                                              self.language, self.play_music,
                                              )

                        # if the loop needs to continue
                        else:
                            # checks if it's one of the none-exit buttons
                            self.check_button_without_exit(x, y)

                        print(f'Clicked on screen: ({x},{y})')
        print("Window was closed")
