"""
how to use this file ?

1.copy and past this file in that folder where you want to arrange clutter file.
2.then run this file.

"""

import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def getfileExtension(file):
    return os.path.splitext(file)[1].lower()

def moveFiles(folder,files):
    for file in files:
        os.replace(file,f"{folder}/{file}")

def main():
    files = os.listdir()
    files.remove("Clutter_Clear.py")

    createIfNotExist("Images")
    createIfNotExist("Docs")
    createIfNotExist("Media")
    createIfNotExist("Others")

    imgExts = [".png",".jpg",".jpeg"]
    images =[ file for file in files if getfileExtension(file) in imgExts]
    moveFiles('Images',images)

    docExts = [".txt",".docx",".doc",".pdf"]
    docs =[ file for file in files if getfileExtension(file) in docExts]
    moveFiles('Docs',docs)

    mediaExts = [".mp4",".mp3",".flv",".mkv"]
    medias =[ file for file in files if getfileExtension(file) in mediaExts]
    moveFiles('Media',medias)

    others = []
    for file in files:
        ext = getfileExtension(file)
        if ext not in imgExts and ext not in docExts and ext not in mediaExts and  os.path.isfile(file):
            others.append(file)
    moveFiles('Others',others)

if __name__ == "__main__":
    main()