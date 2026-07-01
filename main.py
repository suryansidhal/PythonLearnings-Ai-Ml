from pathlib import Path
import os

def createfile():
    try:
        name=input("Enter the name of the file:")
        path=Path(name)
        if not path.exists():
            with open(path, "w") as f:
                data=input("Enter the data to write in the file:")
                f.write(data)   
        else:
            print("File already exists")
    except Exception as e:
        print("Error:", e)


def readfile():
    name=input("Enter the name of the file to read:")
    path=Path(name)
    try:
        if path.exists():
            with open(path, "r") as f:
                data=f.read()
                print(f"Data in the file: {data}")
    except Exception as e:
        print("Error:", e)


def writefile():

    name=input("Enter the name of the file to write:")
    path=Path(name)
    try:
        if path.exists():
            print("want to change the title/file name,press 1")
            print("want to change content,press 2")
            print("if you want to overwrite the content,press 3")
            choice=int(input("Enter your choice:"))
            if choice==1:
                new_title=input("Enter the new title:")
                new_path=Path(new_title)
                if not new_path.exists():
                      path.rename(new_path)
                      print("File renamed successfully")
                else:
                    print("File with the new title already exists")
            elif choice==2:
                with open(path, "a") as f:
                    new_content=input("Enter the new content:")
                    f.write(new_content)
            elif choice==3:
                with open(path, "w") as f:
                    new_content=input("Enter the new content:")
                    f.write(new_content)
            else:
                print("Invalid choice")
        else:
            print("File does not exist")
    except Exception as e:
        print("Error:", e)


def deletefile():
    name=input("Enter the name of the file to delete:")
    path=Path(name)
    try:
        if path.exists():
            path.unlink()
            print("File deleted successfully")
        else:
            print("File does not exist")
    except Exception as e:
        print("Error:", e)


print("Click 1 for creating the file")
print("Click 2 for reading the file")
print("Click 3 for writing to the file")
print("Click 4 for deleting the file")

a=(int(input("Submit your choice:")))
if(a==1):
    createfile()
elif(a==2):
    readfile()
elif(a==3):
    writefile()
elif(a==4):
    deletefile()
   