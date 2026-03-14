import time
import datetime
import schedule

def Fun():
    print("inside fun Function",datetime.datetime.now())


def Gun():
    print("inside Gun Function",datetime.datetime.now())

def main():
    print("Inside Marvellous Automations Script at ",datetime.datetime.now())
    
    schedule.every(20).seconds.do(Gun)
    schedule.every(1).minute.do(Fun)

    while True:
        schedule.run_pending()
        time.sleep(1)    
if __name__ == "__main__":
    main()