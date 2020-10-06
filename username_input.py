import pygame
from pygame.locals import VIDEORESIZE  # to able the changing of the window
from windows import Window, exit_from_game
from db_python_file import DBClass
__author__ = "Nadav Shani"


class UsernameInput(Window):
    def __init__(self, english_img, hebrew_img, language_app, play_music,
                 cur_w, cur_h, score):

        super().__init__(english_img, hebrew_img, language_app, play_music,
                         cur_w, cur_h, False)

        self.input = ""  # username input
        self.score = score  # score from the game

        self.featuresLst.append("label")  # for username input
        self.featuresArgs.append(((self.input, self.input), 3.5, 2.173))
        self.db = DBClass()

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
                    need_resize = False  # clicked on available key
                    answered = False  # pressed enter

                    key_name = pygame.key.name(event.key)

                    if key_name == 'return':
                        answered = True

                    if len(self.input) < 10:
                        if len(key_name) == 1:
                            self.input += key_name
                            need_resize = True

                        elif key_name == 'backspace':
                            self.input = self.input[:-1]
                            need_resize = True

                        elif key_name == 'space':
                            self.input += ' '
                            need_resize = True

                    if need_resize:
                        self.featuresArgs[4] = ((self.input, self.input),
                                                3.5, 2.173)

                        self.resize((self.curW, self.curH))

                    elif answered:
                        self.db.insert_player(self.input, self.score)
                        self.db.close_db()

                        print(f"answered - {self.input}, score: {self.score}")
                        func_to_call[1](self.curW, self.curH, self.language,
                                        self.play_music)

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

                        if ind == 1:
                            self.db.insert_player(self.input, self.score)
                            self.db.close_db()

                            func_to_call[1](self.curW, self.curH,
                                            self.language, self.play_music)

                        # exit button
                        if ind == len(buttons_loc) - 1:
                            exit_from_game()

                        # if the app should go to another window
                        elif not run:
                            func_to_call[ind](self.curW, self.curH,
                                              self.language, self.play_music)

                        # if the loop needs to continue
                        else:
                            # checks if it's one of the none-exit buttons
                            print("reached here")
                            self.check_button_without_exit(x, y)

                        print(f'Clicked on screen: ({x},{y})')
        print("Window was closed")
