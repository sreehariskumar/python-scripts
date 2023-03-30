import os
import posixpath
from termcolor import colored  # for colored output

def find_largest_file(directory):
    largest = 0
    largest_file = ""

    for item in os.walk(directory):
        curDir = item[0]
        subDirs = item[1]
        subFiles = item[2]

        for subFile in subFiles:
            absPath = posixpath.join(curDir, subFile)

            if absPath:
                size = posixpath.getsize(absPath)

                if size > largest:
                    largest = size
                    largest_file = absPath

    return (largest_file, largest)


directory = input("Enter the directory name: ")
files = []

for item in os.walk(directory):
    curDir = item[0]
    subDirs = item[1]
    subFiles = item[2]

    for subFile in subFiles:
        absPath = posixpath.join(curDir, subFile)

        if absPath:
            size = posixpath.getsize(absPath)
            files.append((absPath, size))

# sort the files in descending order of their size
files = sorted(files, key=lambda x: x[1], reverse=True)

max_len = max(len(file[0]) for file in files)

for file in files:
    filename = file[0]
    size = file[1]

    # format the size with appropriate unit
    if size >= 1024**3:
        size_str = "{:.2f} GB".format(size/(1024**3))
    else:
        size_str = "{:.2f} MB".format(size/(1024**2))

    # display the filename in red and the size in green
    #print(colored(filename, "red"), "-", colored(size_str, "green"))
    print(colored("{:<{}}".format(filename, max_len), "red"), "-", colored(size_str, "green"))
