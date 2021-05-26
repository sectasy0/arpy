from os import popen
from struct import pack, unpack
from os.path import exists

from socket import socket, AF_PACKET, SOCK_RAW, htons, inet_aton
from typing import List

def get_mac(interface: str = 'eth0') -> str:
    interface_path: str = f'/sys/class/net/{interface}/'
    if exists(interface_path):
        with open(f'{interface_path}address', 'r') as file:
            return file.readline().strip()
    else:
        raise FileNotFoundError(
            "The Interface doesn't exist or was incorrectly given")


def arp_request(interface: str = 'eth0', dest: str ='ff:ff:ff:ff:ff:ff', dest_ip: str = '192.168.16.20') -> str:
    split_char: str = ':'

    with socket(AF_PACKET, SOCK_RAW, htons(3)) as __sock:
        __sock.bind((interface, 0))

        source_mac: bytes = pack(
            '!BBBBBB', *[int(oc, 16) for oc in get_mac(interface).split(split_char)])

        dest_mac: bytes = pack(
            '!BBBBBB', *[int(oc, 16) for oc in dest.split(split_char)])

        ethernet_header: bytes = pack('!6s6sH',
                                      dest_mac,
                                      source_mac,
                                      0x0806    #  0x0806 = ARP
                                      )

        source_ip = popen(
            'ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' \
            | awk -F "/" \'{ print $1 }\'').read().strip()
        
        # ARP Request header, see RFC 826
        arp_header: bytes = pack('!HHBBH6s4s6s4s',
                                 0x0001,          # Hardware_type  ethernet
                                 0x0800,          # Protocol_type  TCP
                                 0x0006,          # Hardware addr len
                                 0x0004,          # Protocol addr len
                                 0x0001,          # Operation 1=request/2=reply
                                 source_mac,      # Source address
                                 inet_aton(source_ip),
                                 dest_mac,        # Destination adress
                                 inet_aton(dest_ip)
                                 )

        packet: bytes = ethernet_header + arp_header
        __sock.send(packet)

        raw_data: bytes = __sock.recv(42)
        raw_data = unpack('!6s6sH HHBBH6s4s6s4s', raw_data)

        if raw_data[7] == 2:
            unpacked_data: List[int] = unpack('!BBBBBB', raw_data[8])
            unpacked_data = [f'{x:02x}' for x in unpacked_data]
            return ':'.join(unpacked_data)

