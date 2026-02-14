import time
import os
import shutil


def Required_Files(backup_folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    required_folder = f"Required_Files_{timestamp}"

    os.makedirs(required_folder, exist_ok=True)

    collected = []

    for root, dirs, files in os.walk(backup_folder):
        for file in files:

            if file.lower().endswith(".py"):

                src = os.path.join(root, file)
                dest = os.path.join(required_folder, file)

                shutil.copy2(src, dest)
                collected.append(src)

    print("Required .py files extracted successfully")

    return required_folder
