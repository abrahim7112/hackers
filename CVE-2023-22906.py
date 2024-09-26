import os
import socket
import multiprocessing
import subprocess
import telnetlib

ascii_art = r"""
 ██████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██████╗ ██████╗       ██████╗ ██████╗  █████╗  ██████╗  ██████╗ 
██╔════╝██║   ██║██╔════╝    ╚════██╗██╔═████╗╚════██╗╚════██╗      ╚════██╗╚════██╗██╔══██╗██╔═████╗██╔════╝ 
██║     ██║   ██║█████╗█████╗ █████╔╝██║██╔██║ █████╔╝ █████╔╝█████╗ █████╔╝ █████╔╝╚██████║██║██╔██║███████╗ 
██║     ╚██╗ ██╔╝██╔══╝╚════╝██╔═══╝ ████╔╝██║██╔═══╝  ╚═══██╗╚════╝██╔═══╝ ██╔═══╝  ╚═══██║████╔╝██║██╔═══██╗
╚██████╗ ╚████╔╝ ███████╗    ███████╗╚██████╔╝███████╗██████╔╝      ███████╗███████╗ █████╔╝╚██████╔╝╚██████╔╝
 ╚═════╝  ╚═══╝  ╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝╚═════╝       ╚══════╝╚══════╝ ╚════╝  ╚═════╝  ╚═════╝ 
"""

def pinger(job_q, results_q):
    """
    Do Ping
    :param job_q:
    :param results_q:
    :return:
    """
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def get_my_ip():
    """
    Find my IP address
    :return:
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except socket.error:
        print("Unable to determine the IP address. Please check your network connection.")
        return None


def map_network(pool_size=255):
    """
    Maps the network
    :param pool_size: amount of parallel ping processes
    :return: list of valid ip addresses
    """

    ip_list = list()

    # get my IP and compose a base like 192.168.1.xxx
    my_ip = get_my_ip()

    if my_ip is None:
        return ip_list

    ip_parts = my_ip.split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    # prepare the jobs queue
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    # cue the ping processes
    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    # collect the results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list


def connect_to_qubo_device(ip):
    tn = telnetlib.Telnet(ip)
    tn.interact()



if __name__ == '__main__':
    print(ascii_art)
    print('Mapping the network...')
    lst = map_network()
    print("Valid IP's on this network:")
    print(lst)

    successful_ips = []
    for ip in lst:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                result = s.connect_ex((ip, 23))
                if result == 0:
                    tn = telnetlib.Telnet(ip, timeout=2)
                    successful_ips.append(ip)
        except:
            pass

    if successful_ips:
        for successful_ip in successful_ips:
            print("Found a Qubo device. To connect to the device, type telnet " + successful_ip)
            connect_decision = input("Would you like to connect to the Qubo device at {}? (yes/no): ".format(successful_ip)).strip().lower()
            if connect_decision == 'yes':
                connect_to_qubo_device(successful_ip)
    else:
        print("Qubo device not found on this network.")
