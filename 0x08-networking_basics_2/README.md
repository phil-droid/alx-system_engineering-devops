In computer networking, localhost is a hostname that refers to the current device used to access it. It is used to access the network services that are running on the host via the loopback network interface. Using the loopback interface bypasses any local network interface hardware.
IANA, who allocate IP addresses globally, have allocated the single IP address 0.0.0.0[1] to RFC 1122 section 3.2.1.3.

It is named there as "This host on this network"

RFC 1122 refers to 0.0.0.0 using the notation {0,0}. It prohibits this as a destination address in IPv4 and only allows it as a source address under specific circumstances.

A host may use 0.0.0.0 as its own source address in IP when it has not yet been assigned an address. Such as when sending the initial DHCPDISCOVER packet when using DHCP. 