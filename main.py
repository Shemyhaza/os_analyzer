import psutil
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from time import sleep

# Logo
def print_logo():
    print("""
                                 _                        
                                | |                       
  ___   ___     ____ ____   ____| |_   _ _____ ____  ____ 
 / _ \ /___)   / _  |  _ \ / _  | | | | (___  ) _  )/ ___)
| |_| |___ |  ( ( | | | | ( ( | | | |_| |/ __( (/ /| |    
 \___/(___/    \_||_|_| |_|\_||_|_|\__  (_____)____)_|    
                                  (____/                  
                           
                                  """)

# CPU
def cpu_usage():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)

    # cpu_times.txt
    with open("CPU/cpu_times.txt", "a") as f:
        f.write("\n" + str(now) + "\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")
        cpu_times = psutil.cpu_times()

        formatted_output = (
            f"Time spent by normal processes executing in user mode: {cpu_times.user:.2f}s\n"
            f"Time spent by processes executing in kernel mode: {cpu_times.system:.2f}s\n"
            f"Time spent doing nothing: {cpu_times.idle:.2f}s\n"
            f"Time spent waiting for I/O to complete: {cpu_times.iowait:.2f}s\n"
            f"Time spent for servicing hardware interrupts: {cpu_times.irq:.2f}s\n"
            f"Time spent for servicing software interrupts: {cpu_times.softirq:.2f}s\n"
        )

        f.write(formatted_output + "\n")
        f.close()

    # cpu_stats.txt
    with open("CPU/cpu_stats.txt", "a") as f2:
        f2.write("\n" + str(now) + "\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")
        cpu_stats = psutil.cpu_stats()

        formatted_output = (
            f"Number of physical cores only: {psutil.cpu_count(logical=False)}"
            f"Number of context switches (voluntary + involuntary) since boot: {cpu_stats.ctx_switches:.2f}\n"
            f"Number of interrupts since boot: {cpu_stats.interrupts:.2f}\n"
            f"Number of software interrupts since boot: {cpu_stats.soft_interrupts:.2f}\n"
            f"Number of software interrupts since boot: {cpu_stats.soft_interrupts:.2f}\n"
            f"Number of system calls since boot.Always set to 0 on Linux: {cpu_stats.syscalls:.2f}\n"
        )

        f2.write(formatted_output + "\n")
        f2.close()

    # cpu_freq.txt
    with open("CPU/cpu_freq.txt", "a") as f3:
        f3.write("\n" + str(now) + "\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")
        cpu_freq = psutil.cpu_freq()

        formatted_output = (
            f"Current CPU frequency: {cpu_freq.current:.2f}Mhz\n"
            f"Min CPU frequency: {cpu_freq.min:.2f}Mhz\n"
            f"Max CPU frequency: {cpu_freq.max:.2f}Mhz\n"
            f"Avg system load in % values: {[x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]}%\n"
        )

        f3.write(formatted_output + "\n")
        f3.close()


print_logo()

# TODO: visualisation of data; other os resources; reports via emial

# Main loop
while True:
    cpu_usage()
    sleep(5)


