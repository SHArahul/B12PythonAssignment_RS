import psutil
import traceback

CPU_Threshold = 80.0
print("Monitoring CPU Usage...")
print("In order to stop the monitoring manually press 'Control+C' ")

try:
    while True:
        try:
            cpu_usage = psutil.cpu_percent(interval=1)  #Measure overall cpu usage over 1 second
            print(f"Current CPU usage:{cpu_usage}")     #Gives continous cpu usage incase the threshold did not 80% there will be a blank screen
            if cpu_usage >= CPU_Threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}")

        except (psutil.Error,ValueError) as e:  #handle specific psutil related errors
            print("Error retriving CPU usage:",e)
            traceback.print_exc()   #prints full traceback, help understand the error

        except Exception as e:
            print("Unexpected error occured:",e)
            

except KeyboardInterrupt:            #catches the keyboard interrupt by user command like 'control+c'
    print("Monitoring stopped by user...")                



