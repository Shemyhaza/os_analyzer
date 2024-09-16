import psutil
import datetime

def mem_usage():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("MEM log: " + now)

    # mem_usage.txt
    with open("MEM/mem_usage.txt", "a") as f:
        f.write("\n" + str(now) + "\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")
        mem_virtual = psutil.virtual_memory()
        mem_dict = mem_virtual._asdict()

        for key in mem_dict:
            if key != 'percent':
                mem_dict[key] = mem_dict[key] / (1024 ** 3)

        formatted_output = (
            f"Total physical memory (exclusive swap): {mem_dict['total']:.2f} GB\n"
            f"Available memory: {mem_dict['available']:.2f} GB\n"
            f"Memory usage: {mem_dict['percent']:.2f}%\n"
            f"Used memory: {mem_dict['used']:.2f} GB\n"
            f"Free memory: {mem_dict['free']:.2f} GB\n"
            f"Active memory: {mem_dict['active']:.2f} GB\n"
            f"Inactive memory: {mem_dict['inactive']:.2f} GB\n"
            f"Buffers: {mem_dict['buffers']:.2f} GB\n"
            f"Cached: {mem_dict['cached']:.2f} GB\n"
            f"Shared: {mem_dict['shared']:.2f} GB\n"
            f"Slab: {mem_dict['slab']:.2f} GB\n"
        )

        f.write(formatted_output + "\n")
        f.close()

    # mem_swap.txt
    with open("MEM/mem_swap.txt", "a") as f2:
        f2.write("\n" + str(now) + "\n¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")
        mem_swap = psutil.swap_memory()
        mem_dict = mem_swap._asdict()

        for key in mem_dict:
            if key != 'percent':
                mem_dict[key] = mem_dict[key] / (1024 ** 3)

        formatted_output = (
            f"Total swap memory: {mem_dict['total']:.2f} GB\    n"
            f"Used swap memory: {mem_dict['used']:.2f} GB\n"
            f"Free swap memory: {mem_dict['free']:.2f} GB\n"
            f"Swap memory usage: {mem_dict['percent']:.2f}%\n"
            f"Swap sin: {mem_dict['sin']:.2f}\n"
            f"Swap sout: {mem_dict['sout']:.2f}\n"
        )

        f2.write(formatted_output + "\n")
        f2.close()