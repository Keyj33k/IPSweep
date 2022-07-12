#!/usr/bin/env python3

try:
    from subprocess import CalledProcessError
    from subprocess import check_output
    from pyfiglet import figlet_format
    from datetime import datetime
    from sys import exit
    import os
    
except ImportError:
    raise RuntimeError("Important modules are missing!\nTry 'pip install -r requirements.txt'")

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   0.0.1                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #


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

                print(
                    f"\033[0;37m[\033[0;32m+\033[0;37m] Host",
                    f"{remove_last_octet + str(icmp_request)} is reachable"
                )

                with open(f"ipsweep_output.txt", "a") as logf:
                    logf.write(f"Host {remove_last_octet + str(icmp_request)} is reachable\n")
            except KeyboardInterrupt:
                print("\033[0;37m[\033[0;31m-\033[0;37m] You pressed Ctrl+C.INTERRUPTED!")
                exit(1)
            except CalledProcessError:
                print(
                    f"\033[0;37m[\033[0;31m-\033[0;37m] Host",
                    f"{remove_last_octet + str(icmp_request)} is not reachable"
                )


if __name__ == "__main__":
    print(figlet_format(
        "ipsweep",
        "epic"
    ))
    print(
        "\033[0;37m[\033[0;33m*\033[0;37m] Welcome to",
        "IPSweep! \033[0;34m|\033[0;37m Version 0.0.1"
    )
    print("\033[0;34m=" * 65)

    while True:
        try:
            ipv4_addr = str(input(
                "\033[0;37m[\033[0;33m*\033[0;37m] Enter the " +
                "IPv4 address \033[0;34m->\033[0;37m "
            ))
            if ipv4_addr == 'x' or ipv4_addr == 'exit':
                exit(0)

            start_range = int(input(
                "\033[0;37m[\033[0;33m*\033[0;37m] Enter the " +
                "start range \033[0;34m->\033[0;37m "
            ))
            if start_range == 0:
                exit(0)

            last_range = int(input(
                "\033[0;37m[\033[0;33m*\033[0;37m] Enter the " +
                "last range \033[0;34m->\033[0;37m "
            ))
            if last_range == 0:
                exit(0)

            icmp_sweep = IPv4Sweep(
                ipv4_addr,
                last_range,
                start_range
            )
            scan_start = datetime.now()

            print(f"\n\033[0;37m[\033[0;32m+\033[0;37m] Start scanning at {scan_start}")
            print("\033[0;34m=" * 65)

            icmp_sweep.create_output_file()
            icmp_sweep.get_status()

            print("\033[0;34m=" * 65)
            print(
                f"\033[0;37m[\033[0;32m+\033[0;37m] IPSweep",
                f"done in {datetime.now() - scan_start}"
            )
        except KeyboardInterrupt:
            print("\n\033[0;37m[\033[0;31m-\033[0;37m] Ctrl+C pressed.INTERRUPTED!")
            exit(1)
        except ValueError:
            print("\033[0;37m[\033[0;31m-\033[0;37m] Invalid input!")
        except IndexError:
            print("\033[0;37m[\033[0;31m-\033[0;37m] Invalid input!")
