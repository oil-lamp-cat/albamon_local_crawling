import os
import csv
import datetime

log_file_name = 'log.txt'

def test_data():
    today = datetime.date()
    data = [
        {'date' : today,
         'local' : '하성면'
        }
    ]

def log_exist_check():
    if os.path.isfile(log_file_name):
        print("log 파일 존재")
    else:
        f = open("log.txt", 'w')
        f.close()
        print("log 파일 생성")
        
def load_log():
    f = open("log.txt", 'r')
    lines = f.readlines()
    f.close()
    print(lines)
    