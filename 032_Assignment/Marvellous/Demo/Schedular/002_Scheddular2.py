import time
import datetime
import schedule

def fun():
    print("inside fun Function",datetime.datetime.now())

def main():
    print("Inside Marvellous Automations Script at ",datetime.datetime.now())
    
    schedule.every(20).seconds.do(fun)

    # problem with stuck after 20sec as we were not available
    
if __name__ == "__main__":
    main()