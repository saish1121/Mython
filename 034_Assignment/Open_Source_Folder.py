import os
import Created_Backup_Storage_Folder


def MarvellousDataSheildStart(source):

    collected_files = []

    if os.path.exists(source) and os.path.isdir(source):

        for root, dirs, files in os.walk(source):
            for file in files:
                full_path = os.path.join(root, file)
                collected_files.append(full_path)

        Created_Backup_Storage_Folder.Storage_Folder(source, collected_files)

    else:
        print("Invalid Source Directory")
