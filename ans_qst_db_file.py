import sqlite3 as sq
from os.path import isfile
from collections.abc import Iterable

__author__ = "Nadav Shani Date: 29/4/2020 (for last version)"


class AnswersAndQuestionsDBClass:
    db_name = "top5.db"
    table_name = "questionsAndAnswers"
            
    def __init__(self):
        assert isfile(AnswersAndQuestionsDBClass.db_name), "Database doesn't exists!"

        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

    @staticmethod
    def create_connection():
        """ create a database connection to the SQLite database
            :return: Connection object or None
        """
        try:
            conn = sq.connect(AnswersAndQuestionsDBClass.db_name)
        except sq.Error as e:
            raise e
            
        return conn

    def insert_qst_ans(self, question, answer, multi=False):
        """
            inserts the database a question and answer
            :param question: an English question
            :param answer: question's English answer
            :param multi: multiple questions and answers
            :type question: Iterable
            :type answer: Iterable
            :type multi: bool
        """
        assert type(answer) == list or isinstance(answer, Iterable), "Answer must be string or Iterable object."
        assert type(question) == list or isinstance(question, Iterable), "Question must be string or Iterable object."

        command = "INSERT INTO %s " % AnswersAndQuestionsDBClass.table_name

        if not multi:
            command += "(question, answer) VALUES ('%s', '%s');" % (question, answer)
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

    def get_ans_qst_lst(self):
        """
        :return: list for questions and answers
        """
        command = "SELECT * FROM %s;" % AnswersAndQuestionsDBClass.table_name
        return list(self.cursor.execute(command))

    def close_db(self):
        """
        closes database
        """
        self.conn.close()
