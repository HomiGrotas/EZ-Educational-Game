from windows import Window, main_background, intro_buttons_en,\
    intro_buttons_he, start_buttons, about_hebrew, about_english,\
    levels_buttons_he, info, rules_en, rules_he, username_input_en_img,\
    username_input_he_img, open_qst_en, open_qst_he
from qst_win_keyboard_input import QstWinKeyboardInput as QstWin
from qst_win_3options import QstWin3Options
from leaderboard_window import LeaderBoardWin
from db_python_file import DBClass
from username_input import UsernameInput


__author__ = "Nadav Shani"

# get questions and answers from db
db_ans_qst = DBClass()

qst_and_ans_lvl12 = db_ans_qst.get_ans_qst_lst(1)
qst_and_ans_lvl3 = db_ans_qst.get_ans_qst_lst(3)

db_ans_qst.close_db()


###############################################################################
# intro_win function                                                          #
#   intro_win- introduction win - the path for all the windows                #
#   it's the main window of the program                                       #
#   input: current width (int / float) & current height,                      #
#   language (English / Hebrew)                                               #
#          play_music (boolean) - to play music (True / False)                #
#   does: creates a Window with labels and buttons                            #
###############################################################################
def intro_win(cur_w, cur_h, language, play_music, need_resize=True):

    # creating a Window object
    intro = Window(main_background, main_background, language, play_music,
                   cur_w, cur_h)

    # adding labels
    intro.featuresLst.append("label")
    intro.featuresArgs.append((("Welcome to EZ!", ""), 3, 10))
    intro.featuresLst.append("label")
    intro.featuresArgs.append((("You make it EZ.", ""), 1.5, 1.3))

    # adding buttons
    intro.featuresLst.append("button")
    intro.featuresArgs.append(((intro_buttons_en,
                                intro_buttons_he), 4, 4, (2, 2)))

    # add sentences to speak
    intro.buttons_info = ('Game', 'Leaderboard', 'Rules', 'About')

    # resize the window
    if need_resize:
        intro.resize((cur_w, cur_h))

    # the locations of the buttons and the next window in each option
    intro.run([(0.26, 0.43, 0.3, 0.4),  # <= locations of buttons
               (0.56, 0.74, 0.3, 0.4),  # <= locations of buttons
               (0.26, 0.43, 0.6, 0.7),  # <= locations of buttons
               (0.56, 0.74, 0.6, 0.7)],  # <= locations of buttons
              (start_win, top5_win,   # <= functions to call
               rules_win, about_win))   # <= functions to call


###############################################################################
# start_win function                                                          #
#   the window in which the user chooses a level to play                      #
#   input: current width (int / float) & current height,                      #
#   language (English / Hebrew)                                               #
#          play_music (boolean) - to play music (True / False)                #
#   does: creates a Window with labels and buttons                            #
###############################################################################
def start_win(cur_w, cur_h, language, play_music):
    # creating a Window object
    start = Window(main_background, main_background, language, play_music,
                   cur_w, cur_h, change_buttons_order=True)

    # adding buttons
    start.featuresLst.append("button")
    start.featuresArgs.append(((start_buttons, levels_buttons_he),
                               50, 5, (1, 2)))
    start.make_return_button()

    # resizing the window
    start.resize((cur_w, cur_h))
    start.buttons_info = ('level 1', 'level 2', 'level 3')

    # the locations of the buttons and the next window in each option
    start.run([(0.69, 0.77, 0.9, 1),   # <= locations of buttons
               (0.11, 0.34, 0.415, 0.565),   # <= locations of buttons
               (0.37, 0.61, 0.415, 0.565),   # <= locations of buttons
               (0.64, 0.881, 0.415, 0.565)],  # <= locations of buttons
              [intro_win, level_1, level_2, level_3])  # <= functions to call


###############################################################################
# top5_win function                                                           #
#   the window of the leaders board                                           #
#   input: current width (int / float) & current height,                      #
#   language (English / Hebrew)                                               #
#          play_music (boolean) - to play music (True / False)                #
#   does: creates a Window with labels and buttons                            #
###############################################################################
def top5_win(cur_w, cur_h, language, play_music):
    # creating a Window object
    top5win = LeaderBoardWin(main_background, main_background, language,
                             play_music, cur_w, cur_h)

    # add button
    top5win.make_return_button()

    # resizing the window
    top5win.resize((cur_w, cur_h))

    # the locations of the buttons and the next window in each option
    top5win.run([(0.69, 0.77, 0.9, 1)],       # <= locations of buttons
                [intro_win])   # <= functions to call


###############################################################################
# rules_win function                                                          #
#   the window of the rules                                                   #
#   input: current width (int / float) & current height,                      #
#   language (English / Hebrew)                                               #
#          play_music (boolean) - to play music (True / False)                #
#   does: creates a Window with labels and buttons                            #
###############################################################################
def rules_win(cur_w, cur_h, language, play_music):

    # creating a Window object
    rules = Window(rules_en, rules_he, language, play_music, cur_w, cur_h)

    # making a return button
    rules.make_return_button()

    with open("rules.txt", "r") as r:
        lines = r.read().split('\n')
        data = []
        for line in lines:
            data.append(line[:-1])
        rules.buttons_info = data

    # resizing the window
    rules.resize((cur_w, cur_h))

    # the locations of the buttons and the next window in each option
    rules.run([(0.69, 0.77, 0.9, 1)],      # <= locations of buttons
              [intro_win])  # <= functions to call


###############################################################################
# about_win function                                                          #
#   the window about the game: its goal and developers                        #
#   input: current width (int / float) & current height,                      #
#   language (English / Hebrew)                                               #
#          play_music (boolean) - to play music (True / False)                #
#   does: creates a Window with labels and buttons                            #
###############################################################################
def about_win(cur_w, cur_h, language, play_music):

    # creating a Window object
    about = Window(about_english, about_hebrew, language,
                   play_music, cur_w, cur_h)

    # adding buttons
    about.make_return_button()

    with open("about.txt", "r") as r:
        lines = r.read().split('\n')
        data = []
        for line in lines:
            data.append(line[:-1])
        about.buttons_info = data

    # resizing the window
    about.resize((cur_w, cur_h))

    # the locations of the buttons and the next window in each option
    about.run([(0.69, 0.77, 0.9, 1)],      # <= locations of buttons
              [intro_win])  # <= functions to call


###############################################################################
# questions_win function                                                      #
#   the window of the questions and riddles to the user  (by keyboard)        #
#   input: current width (int / float) & current height,                      #
#   language (English / Hebrew)                                               #
#          play_music (boolean) - to play music (True / False)                #
#   does: creates a Window with labels and buttons                            #
###############################################################################
def qst_win(cur_w, cur_h, language, play_music, level, qst, ans):
    # creating a Window object
    qst = QstWin(open_qst_en, open_qst_he, language, play_music, cur_w, cur_h,
                 qst, ans, level)

    qst.pool_random_question()  # pool random question from the qst list
    qst.can_speak = False  # prevent to speak sentences

    # resizing the window
    qst.resize((cur_w, cur_h))

    # the locations of the buttons and the next window in each option
    qst.run([(0.77, 0.84, 0.9, 1),   # <= locations of buttons
             (0.629, 0.729, 0.495, 0.57)],   # <= locations of buttons
            [start_win, start_game])                 # <= functions to call


###############################################
# qst window                                  #
# makes a window with 3 options to answer     #
###############################################
def three_options_win(cur_w, cur_h, language, play_music, qst, ans):
    # creating a Window object
    qst = QstWin3Options(main_background, main_background, language,
                         play_music, cur_w, cur_h, qst, ans)

    # resizing the window
    qst.resize((cur_w, cur_h))

    # the locations of the buttons and the next window in each option
    qst.run([(0.77, 0.84, 0.9, 1), (0.09, 0.285, 0.51, 0.7),
             (0.31, 0.5, 0.51, 0.7),  # <= locations of buttons
             (0.53, 0.72, 0.51, 0.7)],      # <= locations of buttons
            [start_win, start_game])                 # <= functions to call


def username_input_win(cur_w, cur_h, language, play_music, score):
    username_win = UsernameInput(username_input_en_img, username_input_he_img,
                                 language, play_music, cur_w, cur_h, score)

    # add button
    username_win.make_return_button()

    # resizing the window
    username_win.resize((cur_w, cur_h))

    # text to speech sentences
    username_win.buttons_info = ("please choose your username", "accept",
                                 "press enter to confirm or click accept")

    # the locations of the buttons and the next window in each option
    username_win.run([(0.69, 0.77, 0.9, 1),
                      (0.78, 8.92, 0.466, 0.533)],   # <= locations of buttons
                     [intro_win, top5_win])   # <= functions to call


###############################################################################
# level 3 qst_win function                                                    #
# calls the qst_win with level3                                               #
###############################################################################
def level_3(cur_w, cur_h, language, play_music):
    qst_win(cur_w, cur_h, language, play_music, 3,
            [qst[0] for qst in qst_and_ans_lvl3],
            [ans[1] for ans in qst_and_ans_lvl3])


###############################################################################
# level 2 qst_win function                                                    #
# calls the qst_win with level2                                               #
###############################################################################
def level_2(cur_w, cur_h, language, play_music):
    qst_win(cur_w, cur_h, language, play_music, 2,
            [qst[0] for qst in qst_and_ans_lvl3],
            [ans[1] for ans in qst_and_ans_lvl3])


###############################################################################
# level 1 qst_win function                                                    #
# calls the qst_win with level1                                               #
###############################################################################
def level_1(cur_w, cur_h, language, play_music):
    three_options_win(cur_w, cur_h, language, play_music,
                      [qst[0] for qst in qst_and_ans_lvl12],
                      [ans[1] for ans in qst_and_ans_lvl12])


######################
# start game method  #
######################
def start_game(language_app, play_music, cur_w, cur_h, level, ans_score):

    # because there aren't functions in the game
    # file I have to import the file from this function
    # otherwise, the game will start automatically
    import game34
    game34.game(language_app, play_music, cur_w, cur_h, level, ans_score)


###########################
# does: start the program #
###########################
def main():
    intro_win(int(info.current_w / 1.3), int(info.current_h / 1.5),
              "English", True, need_resize=False)


if __name__ == "__main__":
    main()
