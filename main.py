import cpu_utils
import mem_utils
import disk_utils
import logo
from time import sleep

# TODO: visualisation of data; other os resources; reports via email

# Main loop
logo.print_logo()
while True:
    cpu_utils.cpu_usage()
    mem_utils.mem_usage()
    disk_utils.disk_usage()
    sleep(5)


