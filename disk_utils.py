import psutil
import datetime

def disk_usage():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Disk log: " + now)

    # disk_partitions.txt
    with open("DISK/disk_partitions.txt", "a") as f:
        f.write("\n" + str(now) + "\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")

        # TODO: Format output to make it more readable
        formatted_output = (
            f"{psutil.disk_partitions()}\n"
        )

        f.write(str(formatted_output) + "\n")
        f.close()

    # disk_usage.txt
    with open("DISK/disk_usage.txt", "a") as f2:
        f2.write("\n" + str(now) + "\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")

        formatted_output = (
            f"Total space: {psutil.disk_usage('/').total}\n"
            f"Used space: {psutil.disk_usage('/').used}\n"
            f"Free: {psutil.disk_usage('/').free}\n"
            f"Percentage: {psutil.disk_usage('/').percent}%\n"
        )

        f2.write(str(formatted_output) + "\n")
        f2.close()

    # disk_io.txt
    with open("DISK/disk_io.txt", "a") as f3:
        f3.write("\n" + str(now) + "\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")

        formatted_output = (
            # TODO: Format output to make it more readable
            f"{psutil.disk_io_counters(perdisk=True)}\n\n\n"
            
            f"Time spent reading from disk: {psutil.disk_io_counters().read_time}\n"
            f"Time spent writing to disk: {psutil.disk_io_counters().write_time}\n"
            f"Number of reads: {psutil.disk_io_counters().read_count}\n"
            f"Number of writes: {psutil.disk_io_counters().write_count}\n"
            f"Number of bytes read: {psutil.disk_io_counters().read_bytes}\n"
            f"Number of bytes write: {psutil.disk_io_counters().write_bytes}\n"
        )

        f3.write(str(formatted_output) + "\n")
        f3.close()