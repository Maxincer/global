#!usr/bin/env/python38
# coding: utf-8
# Author: Maxincer
# CreateDateTime: 20201113T1830

"""
This script is to upload shared data to global database
"""
from datetime import datetime

from pymongo import MongoClient

from WindPy import w


class UpdateDBGlobal:
    def __init__(self):
        self.str_today = datetime.today().strftime('%Y%m%d')
        self.server_mongodb = MongoClient('mongodb://localhost:27017/')
        self.db_global = self.server_mongodb['global']
        self.col_trdcalendar = self.db_global['trade_calendar']
        w.start()

    def upload_trdcalendar(self):
        wtdays = w.tdays("2020-01-01", "2020-12-31", "")
        list_str_trddates = [_.strftime('%Y%m%d') for _ in wtdays.Data[0]]
        self.col_trdcalendar.delete_many({'Year': '2020'})
        self.col_trdcalendar.insert_one({'Year': '2020', 'Data': list_str_trddates})

    def run(self):
        self.upload_trdcalendar()
        print('Done')


if __name__ == '__main__':
    task = UpdateDBGlobal()
    task.run()







