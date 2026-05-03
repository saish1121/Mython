import sys
import os
import time
import schedule
import Thread_process
import shutil
import Email

def Directory_Open(Dir_Name):
    Ret = False

    Ret = os.path.exists(Dir_Name)
    if Ret == True:
        Ret = os.path.isdir(Dir_Name)
        if Ret == False:
            print("Unable to Create the File or the Folder")
    else:
        os.mkdir(Dir_Name)
        print("Directory has been created Successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    File_Name = os.path.join(Dir_Name,"System_File_%s.log"%timestamp)
    fobj = open(File_Name,"w")
    fobj.write("---- Paltfrom Surveillance System -----")

    Data = Thread_process.Thread_Count()
    
    Open_count = 0
    for info in Data:
        Open_count = Open_count + 1
        fobj.write(f"Process Name : {info.get('name')}\n")
        fobj.write(f"PID          : {info.get('pid')}\n")
        fobj.write(f"No Of Threads: {info.get('num_threads')}\n")
        fobj.write(f"CPU Percent  : {info.get('cpu_percent')}\n")
        fobj.write(f"Ram Percent  : {info.get('memory_percent')}\n")
        fobj.write("TimeStamp : %s\n"%{timestamp})
        fobj.write("Opened File - %s\n"%Open_count)

    fobj.close()

    return File_Name

def Read_Doc(Files):
    fobj = open(Files,"r")
    list_outcome = []
    Thread_count = []
    cpu_usage = []
    Ram_usage = []
    P_count = 0
    for F in fobj:
        if F.startswith("Process Name"):
            P_count = P_count + 1 
        elif F.startswith("No Of Threads"):
            list_outcome.append(F)

            value = int(F.split(":")[1].strip())
            Thread_count.append(value)        
        elif F.startswith("CPU Percent"):
            list_outcome.append(F)

            value = float(F.split(":")[1].strip())
            cpu_usage.append(value)

        elif F.startswith("Ram Percent"):
            list_outcome.append(F)
            
            value = float(F.split(":")[1].strip())
            Ram_usage.append(value)

    fobj.close()
    thread_filterd = list(filter(lambda x : x > 0,Thread_count))
    cpu_filtered = list(filter(lambda x: x > 0, cpu_usage))
    ram_filtered = list(filter(lambda x: x > 0, Ram_usage))

    if thread_filterd:
        top_thread = max(thread_filterd)
    else:
        top_thread = 0

    if cpu_filtered:
        top_cpu = max(cpu_filtered)
    else:
        top_cpu = 0

    if ram_filtered:
        top_ram = max(ram_filtered)
    else:
        top_ram = 0

    result = {
        "Total Processes": P_count,
        "Top CPU Usage": top_cpu,
        "Top Thread Usage": top_thread,
        "Top RAM Usage": top_ram,
        "All Thread Counts": Thread_count,
        "All CPU Usage": cpu_usage,
        "All RAM Usage": Ram_usage
    }

    return result

def Email_folder(Top):
    Folder_name = "Details"
    Ret = False
    Ret = os.path.exists(Folder_name)
    if Ret == True:
        Ret = os.path.isdir(Folder_name)
        if Ret == False:
            print("Unable to create the File or Folder Beacause - Already Present....")

    else:
        os.makedirs(Folder_name,exist_ok=True)
        print("Directory Created Successsfully.....")    

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    File = os.path.join(Folder_name,"Email_%s"%timestamp)
    fobj = open(File,"w")
    fobj.write("------ Email Summary Report ------\n\n")
    fobj.write(f"Total Processes   : {Top['Total Processes']}\n")
    fobj.write(f"Top CPU Usage     : {Top['Top CPU Usage']}\n")
    fobj.write(f"Top Thread Usage  : {Top['Top Thread Usage']}\n")
    fobj.write(f"Top RAM Usage     : {Top['Top RAM Usage']}\n")   

    print("Email summary file created successfully.")   

    return File 
            
    
def main():
    Border = "-"*50
    print(Border)
    print("---- Paltfrom Surveillance System -----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This scipt is used to : ")
            print("1.Used to Display Process Name")
            print("2.Used to Display PID")
            print("3.Used to Display CPU % Name")
            print("4.Used to Display Memory (RSS)")
            print("5.Used to Display Threads Count")
            print("6.Used to Display Open Files Count")
            print("7.Used to Display Open Timestamp")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")            

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time Travel - ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        # Apply the schedular
        Ret = Directory_Open(sys.argv[2])
        Ret_2 = Read_Doc(Ret)
        Ret_3 = Email_folder(Ret_2)
        Email.Send_Email(Ret_3)

        print("Platfrom Surveillance System started succesfully")
        print("Press Ctrl + C to stop the execution")
        
    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)
    
if __name__ == "__main__":
    main()