import psutil
import os
import time

def Thread_Count():
    for proc in psutil.process_iter():
        try:
            Cpu = proc.cpu_percent()
        except:
            pass
    time.sleep(2)
    
    Thread_List = []
    for proc in psutil.process_iter():
        try:

            info = proc.as_dict(attrs=["name","pid","num_threads",])

            try :
                info["name"] = proc.name()
                info["pid"] = proc.pid
                info["num_threads"] = proc.num_threads()
                info["cpu_percent"] = proc.cpu_percent(None)
                info["memory_percent"] = proc.memory_percent()

                Thread_List.append(info)

            except:
                pass            
        except:
            print("Access Denied into log file.")

    return Thread_List

