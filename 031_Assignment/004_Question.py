# 4. Design automation script which accept two directory names and one file extension. Copy all 
# files with the specified extension from first directory into second directory. Second directory 
# should be created at run time. 
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe” 
# Demo is name of directory which is existing and contains files in it. We have to create new 
# Directory as Temp and copy all files with extension .exe from Demo to Temp.

import sys
import os
import shutil

def directory_scanner(src_dir, dest_dir):

    Ret = False

    Ret = os.path.exists(src_dir)

    if (Ret == False):
        print("Source directory does not exist")
        return
    
    Ret = os.path.isdir(src_dir)

    if(Ret == False):
        print("Source path is not a directory")
        return
    
    Ret = os.path.exists(dest_dir)

    if(Ret == False):
        os.mkdir(dest_dir)
        print("Directory created:", dest_dir)

    Extension = ".exe"

    for folder, subfolder, files in os.walk(src_dir):
            for file in files:
                if file.endswith(Extension):
                    Ret = os.path.join(folder,file)
                    dest_file = os.path.join(dest_dir, file)

                    shutil.copy(Ret,dest_file)  
                    print("Copied .exe file are - ",Ret)                              


    print("-" * 40)
    print("Copying completed successfully")

def main():
    if len(sys.argv) != 3:
        print("Usage: DirectoryCopy.py Demo Temp")
        return

    directory_scanner(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
