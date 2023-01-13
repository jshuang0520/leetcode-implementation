class Solution:
    """Time taken
    00 : 01 : 40
    """
    def defangIPaddr(self, address: str) -> str:
        address = address.replace(".", "[.]")
        return address
