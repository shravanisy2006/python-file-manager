from pathlib import Path
import os

def readfilesfolders():
    path = Path('')
    items = list(path.rglob('*'))
    for i , items in enumerate(items):
        print (f"{i+1} : {items}")


def createfile():
    try:
        readfilesfolders()
        name = input("Please enter the name of your file: ")
        p=Path(name)
        if not p.exists() :
            with open(p ,'w') as fs:
                data = input("Enter the content you want to include in your file.")
                fs.write(data)

            print("File Created Succesfuully!")

        else:
            print("This file alreadye exists!")

    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        readfilesfolders()
        name = input("Enter the name of the file you want to read.")
        p=Path(name)
        if p.exists() and p.is_file():
            with open (p,'r') as fs:
                data = fs.read()
                print(data)
            print("Data within file read successfully!")

        else:
            print("File does not exists!")

    except Exception as err:
        print(f"An error occured as {err}.")


def updatefile():
    try:
        readfilesfolders()
        name = input("Enter the name of the file you want to update.")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of the file.")
            print("press 2 for overwritting the data of the file.")
            print("Press 3 for appending data in the file.")

            res=int(input("Enter your chouce: "))
            if res == 1:
                name2 = input("Enter the new name of your file.")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open (p,'w') as fs:
                    data = input("Tell what you want to write this will overwrite the data:")
                    fs.write(data)

            if res == 3:
                with open (p,'a') as fs:
                    data = input("Tell what you want to write this will append the data:")
                    fs.write(" " + data)

    except Exception as err:
        print(f"An error occured as {err}")


def deletefile():
    try:
        readfilesfolders()
        name = input("Enter the file name you want to delete.")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("The file is delete successfully.")

        else:
            print("No file exists with that name.")

    except Exception as err:
        print(f"An error occured as {err}")


print("Press 1 for creating a file.")
print("Press 2 for reading a file.")
print("Press 3 for updating a file.")
print("Press 4 for deleting a file.")

check=int(input("Enter your choice: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()
