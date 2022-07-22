#!/usr/bin/env python3

try:
    from subprocess import CalledProcessError
    from subprocess import check_output
    from pyfiglet import figlet_format
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
#   Version :   0.0.3                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

y = "\033[0;33m"
b = "\033[0;34m"
g = "\033[0;32m"
w = "\033[0;37m"
r = "\033[0;31m"


class IPv4Sweep:

    def __init__(
            self,
            ipv4_address: str,
            max_range: int,
            min_range: int
    ):
        self.min_range = min_range
        self.max_range = max_range
        self.ipv4_address = ipv4_address

    @staticmethod
    def create_output_file():
        try:
            if not os.path.isfile("ipsweep_output.txt"):
                open("ipsweep_output.txt", "w")
        except Exception as excerr:
            print(excerr)
            exit(1)

    def get_status(self):
        mod_ipv4_address = self.ipv4_address.split(".")
        remove_last_octet = mod_ipv4_address[0] + "." + \
                            mod_ipv4_address[1] + "." + \
                            mod_ipv4_address[2] + "."

        for icmp_request in range(
                self.min_range,
                self.max_range + 1
        ):
            try:
                check_output([
                    "ping", "-c", "2",
                    remove_last_octet + str(icmp_request)
                ])

                print(f"{w}[{g}+{w}] Host {remove_last_octet + str(icmp_request)} is reachable")

                with open(f"ipsweep_output.txt", "a") as logf:
                    logf.write(f"Host {remove_last_octet + str(icmp_request)} is reachable\n")
            except KeyboardInterrupt:
                print(f"{w}[{r}-{w}] You pressed Ctrl+C.INTERRUPTED!")
                exit(1)
            except CalledProcessError:
                print(f"{w}[{r}-{w}] Host {remove_last_octet + str(icmp_request)} is not reachable")