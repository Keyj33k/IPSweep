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
#   Version :   0.0.2                     #
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

                print(
                    f"{w}[{g}+{w}] Host",
                    f"{remove_last_octet + str(icmp_request)} is reachable"
                )

                with open(f"ipsweep_output.txt", "a") as logf:
                    logf.write(f"Host {remove_last_octet + str(icmp_request)} is reachable\n")
            except KeyboardInterrupt:
                print(f"{w}[{r}-{w}] You pressed Ctrl+C.INTERRUPTED!")
                exit(1)
            except CalledProcessError:
                print(
                    f"{w}[{r}-{w}] Host",
                    f"{remove_last_octet + str(icmp_request)} is not reachable"
                )


if __name__ == "__main__":
    print(figlet_format(
        "ipsweep",
        "epic"
    ))
    print(
        f"{w}[{y}*{w}] Welcome to",
        f"IPSweep! {b}|{w} Version 0.0.1"
    )
    print(f"{b}=" * 65)

    while True:
        try:
            ipv4_addr = str(input(
                f"{w}[{y}*{w}] Enter the " +
                f"IPv4 address {b}->{w} "
            ))
            if ipv4_addr == 'x' or ipv4_addr == 'exit':
                exit(0)

            start_range = int(input(
                f"{w}[{y}*{w}] Enter the " +
                f"start range {b}->{w} "
            ))
            if start_range == 0:
                exit(0)

            last_range = int(input(
                f"{w}[{y}*{w}] Enter the " +
                f"last range {b}->{w} "
            ))
            if last_range == 0:
                exit(0)

            icmp_sweep = IPv4Sweep(
                ipv4_addr,
                last_range,
                start_range
            )
            scan_start = datetime.now()

            print(f"\n{w}[{g}+{w}] Start scanning at {scan_start}")
            print(f"{b}=" * 65)

            icmp_sweep.create_output_file()
            icmp_sweep.get_status()

            print(f"{b}=" * 65)
            print(
                f"{w}[{g}+{w}] IPv4 Sweep",
                f"done in {datetime.now() - scan_start}"
            )
        except KeyboardInterrupt:
            print(f"\n{w}[{r}-{w}] Ctrl+C pressed.INTERRUPTED!")
            exit(1)
        except ValueError:
            print(f"{w}[{r}-{w}] Invalid input!")
        except IndexError:
            print(f"{w}[{r}-{w}] Invalid input!")