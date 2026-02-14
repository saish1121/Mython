import os
import time
import shutil
import hashlib
import zipfile
import Required_Files
import Email

# ---------------- CHECKSUM ---------------- #
def Check_Sum(filepath):
    hobj = hashlib.md5()

    with open(filepath, "rb") as fobj:
        while chunk := fobj.read(1024):
            hobj.update(chunk)

    return hobj.hexdigest()


# ---------------- ZIP FUNCTION ---------------- #
def Zip_Folder(folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = f"{folder}_{timestamp}.zip"

    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as Zobj:

        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, folder)

                Zobj.write(full_path, relative)

    Email.Send_Email(zip_name)
    return zip_name

# ---------------- BACKUP HISTORY ---------------- #
def Backup_History(folder):

    date = time.strftime("%Y-%m-%d")
    log_file = "Backup_History.log"

    zip_file = Zip_Folder(folder)
    zip_size = os.path.getsize(zip_file)

    count = 0

    with open(log_file, "a") as fobj:   # append mode

        fobj.write("\n" + "-" * 50 + "\n")
        fobj.write("Welcome to Backup Files\n")
        fobj.write(f"Date: {date}\n\n")

        for root, dirs, files in os.walk(folder):
            for file in files:
                fobj.write(f"File: {file}\n")
                count += 1

        fobj.write(f"\nTotal Files: {count}\n")
        fobj.write(f"Zip Size: {zip_size} bytes\n")
        fobj.write("-" * 50 + "\n")

    print("Backup History Updated Successfully")

    Email.Send_Email(log_file)


# ---------------- STORAGE FUNCTION ---------------- #
def Storage_Folder(source, file_list):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = f"Backup_{timestamp}"

    os.makedirs(backup_folder, exist_ok=True)

    for file in file_list:

        rel_path = os.path.relpath(file, source)
        dest = os.path.join(backup_folder, rel_path)

        os.makedirs(os.path.dirname(dest), exist_ok=True)

        if os.path.exists(dest):

            if Check_Sum(file) != Check_Sum(dest):
                shutil.copy2(file, dest)
                print("Updated:", file)

            else:
                print("Already Exists:", file)

        else:
            shutil.copy2(file, dest)
            print("Copied:", file)

    # Extract only .py files
    req_folder = Required_Files.Required_Files(backup_folder)

    # Create zip + history
    Backup_History(req_folder)

    print("Backup Completed Successfully")




