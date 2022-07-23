#!/usr/bin/env python3

#
# 誰も隠すことはできません
#
# ▓▓ __\«\_/»/__ ▓▓
# ▓▓------☼------▓▓
# //{(*)>-v-<(*)}\
# |||(○_/•|•\_○)|||
# |||\((▼▼▼▼▼))/|||
# /|||\\▼▲▲▲▼//|||\
#
#

try:
    from termcolor import colored
    from pyfiglet import figlet_format
    from src.ips import IPv4Sweep
    from datetime import datetime
    from sys import exit
    import os
except ImportError:
    raise RuntimeError("Important modules are missing!\nYou need to install the requirements!")


# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   0.0.4                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

y = "\033[0;33m"
b = "\033[0;34m"
g = "\033[0;32m"
w = "\033[0;37m"
r = "\033[0;31m"


if __name__ == "__main__":
    print(colored(figlet_format("OVAX", font="isometric1"), "green"))
    print(f"{w}[{y}*{w}] Welcome to Ovax! {b}|{w} Version 0.0.4")
    print(f"{b}=" * 55)

    try:
        ipv4_addr = str(input(f"{w}[{y}*{w}] Enter the IPv4 address {b}->{w} "))
        if ipv4_addr == 'x' or ipv4_addr == 'exit':
            exit(0)

        start_range = int(input(f"{w}[{y}*{w}] Enter the start range {b}->{w} "))
        if start_range == 0:
            exit(0)

        last_range = int(input(f"{w}[{y}*{w}] Enter the last range {b}->{w} "))
        if last_range == 0:
            exit(0)

        ping_count = str(input(f"{w}[{y}*{w}] Enter the ping count {b}->{w} "))
        if ping_count == 'x' or ping_count == 'exit':
            exit(0)

        icmp_sweep = IPv4Sweep(
            ipv4_addr,
            last_range,
            start_range,
            ping_count
        )
        scan_start = datetime.now()

        print(f"\n{w}[{y}*{w}] Start scanning at {scan_start}")
        print(f"{b}=" * 55)

        icmp_sweep.create_output_file()
        icmp_sweep.get_status()

        print(f"{b}=" * 55)
        print(f"{w}[{y}*{w}] IPSweep done in {datetime.now() - scan_start}\n")
    except KeyboardInterrupt:
        print(f"\n{w}[{r}-{w}] Ctrl+C pressed.INTERRUPTED!")
        exit(1)
    except ValueError:
        print(f"{w}[{r}-{w}] Invalid input!")
    except IndexError:
        print(f"{w}[{r}-{w}] Invalid input!")
