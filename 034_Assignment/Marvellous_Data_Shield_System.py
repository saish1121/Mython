import sys
import schedule
import time
import Open_Source_Folder


def main():

    border = "-" * 50
    print(border)
    print("---- Marvellous Data Shield System -----")
    print(border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ("--h", "--H"):
            print("1. Text auto backup at given time")
            print("2. Backup only new and updated files")
            print("3. Create archive of backup periodically")

        elif sys.argv[1] in ("--u", "--U"):
            print("Usage:")
            print("ScriptName.py TimeInterval SourceDirectory")

        else:
            print("Invalid Option")

    elif len(sys.argv) == 3:

        interval = int(sys.argv[1])
        source = sys.argv[2]

        print("Time interval:", interval)
        print("Directory:", source)

        # Run immediately
        Open_Source_Folder.MarvellousDataSheildStart(source)

        # Schedule
        schedule.every(interval).minutes.do(
           Open_Source_Folder.MarvellousDataSheildStart, source
        )

        print("System Started. Press Ctrl + C to stop.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Arguments")

    print(border)


if __name__ == "__main__":
    main()
