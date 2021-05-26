# arpy (Only for linux)
> Library allows send arp/rarp request in your LAN network.

![Python version][python-image]


## Usage example

A few motivating and useful examples of how arpy can be used.


```python
from arpy import arp_request

# returns mac address of 192.168.16.20
arp_request(dest_ip='192.168.16.20')

# you can pass your interface name as well
arp_request(interface='eth1', dest_ip='192.168.16.20')

```

#### Get your mac address
This library provides fetch your mac address by the interface name

```python
from arpy import get_mac

get_mac() # Default eth0

get_mac(interface='eth1')

```

## Release History

* 1.0
    * arp request.
    * get your mac address
    * tests.

## Meta

Piotr Markiewicz – [@LinkedIn](https://www.linkedin.com/in/piotr-markiewicz-a44b491b1/) – sectasy0@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/sectasy0](https://github.com/sectasy0)

## Contributing

1. Fork it (<https://github.com/sectasy0/arpy>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

[python-image]: https://img.shields.io/badge/python-3.8-blue