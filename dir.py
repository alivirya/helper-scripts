#!/usr/bin/python3
import os
import re

class DirectoryActivities:
    def __init__(self):
        self.chdir = os.getcwd() + "/"

    def cleanNonVideoFiles(self):
        for file in os.listdir(self.chdir):
            if not file.endswith(".mkv"):
                os.remove(file)

    def renameVideos(self):
        for file in os.listdir(self.chdir):
            if file.endswith(".mkv"):
                dst = self.checkPatterns(file)
                src = self.chdir + file
                dst = self.chdir + dst + ".mkv"

                os.rename(src, dst)

    def checkPatterns(self, check):
        patterns = ["S\d{1,2}E\d{1,2}", "\dx\d{1,2}"]
        for i in patterns:
            match = re.findall(i, check)
            if len(match) != 0:
                return match[0]

    def vidCleanUp(self):
        self.cleanNonVideoFiles()
        self.renameVideos()

if __name__ == "__main__":
    dir = DirectoryActivities()
    dir.vidCleanUp()
