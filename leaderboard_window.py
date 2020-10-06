from windows import Window, top_five_en, top_five_he
from db_python_file import DBClass

__author__ = "Nadav Shani"


class LeaderBoardWin(Window):
    def __init__(self, english_img, hebrew_img, language_app, play_music,
                 cur_w, cur_h):

        super().__init__(english_img, hebrew_img, language_app, play_music,
                         cur_w, cur_h)

        # add an hidden label
        # reason: read this text first
        # (when it's in button info it's read last)
        self.featuresLst.append("label")
        self.featuresArgs.append((("Leaderboards", "Leaderboards"), 0.9, 0.9))

        # get top5 and add to screen
        self.top5 = DBClass().get_top5()
        self.add_top5_table_to_screen()

    def add_top5_table_to_screen(self):
        top_five_loc_lst = [(3.2, 3.2), (3.2, 2.28), (3.2, 1.78),
                            (3.2, 1.46), (3.2, 1.24)]

        self.featuresLst.append("button")
        temp = top_five_en
        if self.language == "Hebrew":
            temp = top_five_he
        self.featuresArgs.append((temp, 4, 15, (2.6, 1)))

        for ind, player in enumerate(self.top5):
            loc = top_five_loc_lst[ind]
            self.featuresLst.append("label")
            self.featuresLst.append("label")

            name = player[0]
            score = str(player[1])

            self.featuresArgs.append(((name, name), loc[0], loc[1]))
            self.featuresArgs.append(((score, score), 1.95, loc[1]))

    # override change_language method
    def change_language(self):
        temp = top_five_he
        if self.language == "Hebrew":
            temp = top_five_en
        self.featuresArgs[5] = (temp, 4, 15, (2.6, 1))

        super().change_language()
