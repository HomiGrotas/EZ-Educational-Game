import sqlite3 as sq
from os.path import isfile
from collections.abc import Iterable

__author__ = "Nadav Shani Date: 03/06/2020 (for last version)"


class DBClass:
    db_name = "top5.db"
    table_name_qst_levels_12 = "questionsAndAnswersLevel12"
    table_name_qst_level3 = "questionsAndAnswersLevel3"
    table_name_players = "top5"
            
    def __init__(self):
        """
        check if the db exist,
        creates connection to db
        and makes a cursor
        """
        assert isfile(DBClass.db_name), "Database doesn't exists!"

        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

    @staticmethod
    def create_connection():
        """ create a database connection to the SQLite database
            :return: Connection object or None
        """
        try:
            conn = sq.connect(DBClass.db_name)
        except sq.Error as e:
            raise e
            
        return conn

    def insert_qst_ans(self, question, answer, level, multi=False):
        """
            inserts the database a question and answer
            :param question: an English question
            :param answer: question's English answer
            :param multi: multiple questions and answers
            :param level: question level (1 - 3)
            :type question: Iterable
            :type answer: Iterable
            :type multi: bool
        """
        assert type(answer) == list or isinstance(answer, Iterable),\
            "Answer must be string or Iterable object."

        assert type(question) == list or isinstance(question, Iterable), \
            "Question must be string or Iterable object."

        assert 1 <= level <= 3, "Unknown level"

        if level == 3:
            table_name = DBClass.table_name_qst_level3
        else:
            table_name = DBClass.table_name_qst_levels_12

        command = "INSERT INTO %s " % table_name

        if not multi:
            command += "(question, answer) VALUES ('%s', '%s');" % (question,
                                                                    answer)
        else:
            command += "(question, answer) VALUES"
            for qst, ans in zip(question, answer):
                command += f"\n('{qst}', '{ans}'),"
            command = command[:-1] + ";"

        print(command)
        try:
            print(command)
            self.cursor.execute(command)
        except sq.Error as e:
            raise e
        self.conn.commit()

    def get_ans_qst_lst(self, level):
        """
        :param level: question level (1 - 3)
        :return: list for questions and answers
        """
        assert 1 <= level <= 3, "Unknown level"

        if level == 3:
            table_name = DBClass.table_name_qst_level3
        else:
            table_name = DBClass.table_name_qst_levels_12

        command = "SELECT * FROM %s;" % table_name
        return list(self.cursor.execute(command))

    def insert_player(self, name, score):
        """
        inserts player name and score to top5 db
        :param name: player's name (str)
        :param score: player's score (int)
        :return: None
        """
        command = "UPDATE %s " % self.table_name_players
        command += "SET name_player = '%s', score = %d " % (name, score)
        command += "WHERE name_player = ( "
        command += "SELECT name_player "
        command += "FROM %s " % self.table_name_players
        command += "WHERE score < %d " % score
        command += "ORDER BY score ASC "
        command += "LIMIT 1 );"

        self.cursor.execute(command)
        self.conn.commit()

    def get_top5(self):
        """
        :return: list of the top5 players with their score
        """
        command = "SELECT * FROM top5 ORDER BY score DESC;"
        return list(self.cursor.execute(command))[:5]

    def close_db(self):
        """
        closes database
        """
        try:
            self.conn.close()
        except Exception as e:
            print(e)
