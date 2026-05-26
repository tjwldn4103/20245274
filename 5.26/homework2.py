import os

base = input("폴더 경로 입력: ")


def find_txt(path):

    for entry in os.scandir(path):

      
        if entry.is_file():

       
            if entry.name.endswith(".txt"):

                print(entry.path)

      
        elif entry.is_dir():

            find_txt(entry.path)


find_txt(base)
