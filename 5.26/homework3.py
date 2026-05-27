import os

dir1 = input("첫 번째 디렉토리 이름: ")
dir2 = input("두 번째 디렉토리 이름: ")

def get_files(path):
    files = {}

    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                files[entry.name] = {
                    "path": entry.path,
                    "size": entry.stat().st_size
                }

    return files


def same_content(path1, path2):
    with open(path1, "rb") as f1:
        data1 = f1.read()

    with open(path2, "rb") as f2:
        data2 = f2.read()

    return data1 == data2


files1 = get_files(dir1)
files2 = get_files(dir2)

print("첫 번째 디렉토리 파일 개수:", len(files1))
print("두 번째 디렉토리 파일 개수:", len(files2))

if len(files1) == len(files2):
    print("파일 개수: 같음")
else:
    print("파일 개수: 다름")

for name in files1:
    if name in files2:
        print("\n파일 이름:", name)

        if files1[name]["size"] == files2[name]["size"]:
            print("크기: 같음")
        else:
            print("크기: 다름")

        if same_content(files1[name]["path"], files2[name]["path"]):
            print("내용: 같음")
        else:
            print("내용: 다름")
    else:
        print("\n", name, "파일은 두 번째 디렉토리에 없음")

for name in files2:
    if name not in files1:
        print("\n", name, "파일은 첫 번째 디렉토리에 없음")
