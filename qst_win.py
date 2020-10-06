import pygame
import random
from windows import Window
from pygame.locals import VIDEORESIZE  # to able the changing of the window

__author__ = "Nadav Shani"


###############################################################################
# making a questions window - inherits abilities from the normal window       #
# it has the ability to get input from the user                               #
###############################################################################
class QstWin(Window):
    def __init__(self, english_img, hebrew_img, language_app, play_music, width, height, questions, answers, level):
        super().__init__(english_img, hebrew_img, language_app, play_music, width, height)
        self.make_return_button()
        self.input = ''
        self.featuresLst.insert(4, "label")
        self.featuresArgs.insert(4, ("Enter answer here", 3, 3.5))
        self.questions = questions
        self.answers = answers
        self.answer = None
        self.level = level
        self.featuresLst.append("label")

    #################################################################
    # pool_random_question                                          #
    # does: grill index and by it makes a question and answer       #
    #       add the question to the featuresArgs for painting label #
    #       (it's already in featuresLst)                           #
    #################################################################
    def pool_random_question(self):
        ind = random.randint(0, len(self.questions)-1)
        qst = self.questions[ind]
        self.answer = self.answers[ind]
        self.featuresArgs.append((qst, 3, 4.5))

    ##############################################################
    # run function                                               #
    #   main loop- the difference between this function to the   #
    #   regular one is here you can get input                    #
    #   it also check the input                                  #
    ##############################################################
    def run(self, buttons_loc, func_to_call):
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

            # for event in the events of the game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    print(self.featuresLst, self.featuresArgs)
                    need_resize = False
                    key_name = pygame.key.name(event.key)
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
                        if self.input == self.answer:
                            self.featuresArgs.pop(5)
                            self.pool_random_question()
                            self.input = ''
                        self.featuresArgs.pop(4)
                        self.featuresArgs.insert(4, (self.input, 3, 3.5))
                        self.resize((self.curW, self.curH))

                # if there is a change in the size
                elif event.type == VIDEORESIZE:
                    self.resize(event.size)

                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_motion(buttons_loc)

                # if the user clicked on something with the left side of the mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Set the x, y positions of the mouse click
                        x, y = event.pos

                        # checks if the loop needs to stop and checks
                        # gets the number of the function to run (it doesn't mean that the function will be called)
                        run, ind = self.check_button(buttons_loc, x, y)

                        if ind == len(buttons_loc) - 1:
                            run = False
                            pygame.quit()

                        # if the app should go to another window
                        elif not run:
                            func_to_call[ind](self.curW, self.curH, self.language, self.play_music)

                        # if the loop needs to continue
                        else:
                            # checks if it's one of the none-exit buttons
                            self.check_button_without_exit(x, y)

                        print(f'Clicked on screen: ({x},{y})')
        print("Window was closed")
