import struct
import unittest
import uuid

from arpy import get_mac, arp_request

class TestGetMac(unittest.TestCase):
    
    def test_incorrect_interface(self):
        self.assertRaises(FileNotFoundError, get_mac, 'eth5')
    
    def test_success(self):
        actual = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))
        func_return = get_mac()
        self.assertEqual(func_return, actual)
    
    def test_interface_given_int(self):
        self.assertRaises(FileNotFoundError, get_mac, 4444)
    
    def test_interface_given_bool(self):
        self.assertRaises(FileNotFoundError, get_mac, True)


class TestArpRequest(unittest.TestCase):

    def test_incorrect_mac(self):
        self.assertRaises(struct.error, arp_request, 'eth0', 'fffffff')
    
    def test_incorrect_interface(self):
        self.assertRaises(OSError, arp_request, 'eth5')

    def test_interface_given_int(self):
        self.assertRaises(TypeError, arp_request, 4444)

    def test_interface_given_bool(self):
        self.assertRaises(TypeError, arp_request, False)

    def test_dest_ip_incorrect_format(self):
        self.assertRaises(OSError, arp_request, 'eth0', 'ff:ff:ff:ff:ff:ff', "192.4124.1233")

    def test_dest_ip_given_int(self):
        self.assertRaises(TypeError, arp_request, 'eth0', 'ff:ff:ff:ff:ff:ff', 4444)
    
    def test_dest_ip_given_bool(self):
        self.assertRaises(TypeError, arp_request, 'eth0', 'ff:ff:ff:ff:ff:ff', True)