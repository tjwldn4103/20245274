import os

base = input("폴더 경로 입력: ")


def listAll(path):

    print(path)

    for entry in os.scandir(path):

        if entry.is_dir():

            listAll(entry.path)


listAll(base)
