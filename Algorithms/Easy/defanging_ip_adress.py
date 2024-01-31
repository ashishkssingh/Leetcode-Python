"""
1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
"""


class IpDefanging(object):
    def defangIPaddr(self, address) -> str:
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")


if __name__ == "__main__":
    ip_address1 = "1.1.1.1"
    ip_address2 = "255.100.50.0"

    print(IpDefanging().defangIPaddr(address=ip_address1))
    print(IpDefanging().defangIPaddr(address=ip_address2))
