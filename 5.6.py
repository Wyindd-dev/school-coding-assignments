import os 
import time
def main():
    path = "C:\\Users\\User\\Desktop\\Python\\"
    files = os.listdir(path)
    for file in files:
        if
        os.path.isfile(os.path.join
        (path, file)):
            print(file)
            print("Last modified: %s" % time.ctime(os.path.getmtime(os.path.join(path, file))))
            print("Created: %s" % time.ctime(os.path.getctime(os.path.join(path, file))))
            print("Size: %s bytes" % os.path.getsize(os.path.join(path, file)))
            print()
        