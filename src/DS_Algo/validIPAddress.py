# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address 
# or "Neither" if IP is not a correct IP of any type.

# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. 
# For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", 
#     "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:1 <= xi.length <= 4
#     xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, 
# while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

# Constraints:
# queryIP consists only of English letters, digits and the characters '.' and ':'.

# Time Complexity:O(n)
# Space Complexity: O(1)  — no extra space used beyond a few variables.

# Explanation
# To validate whether a given string queryIP is a valid IPv4, IPv6, or Neither, we can implement a parser that checks the format and rules for each type.
# IPv4 Rules:
#     Must have 4 parts separated by ..
#     Each part must be a number between 0 and 255.
#     No leading zeros (e.g., "01" is invalid).
#     Only digits allowed.
# IPv6 Rules:
#     Must have 8 parts separated by :.
#     Each part must be 1 to 4 characters long.
#     Valid characters: 0-9, a-f, A-F.
#     Leading zeros are allowed.

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if not 0 <= int(part) <= 255:
                    return False
                if part[0] == '0' and len(part) > 1:
                    return False
            return True

        def isIPv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            hex_digits = '0123456789abcdefABCDEF'
            for part in parts:
                if not (1 <= len(part) <= 4):
                    return False
                if not all(c in hex_digits for c in part):
                    return False
            return True

        if isIPv4(queryIP):
            return "IPv4"
        elif isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"


sol = Solution()

print(sol.validIPAddress("192.168.1.1"))        # IPv4
print(sol.validIPAddress("192.168.01.1"))       # Neither
print(sol.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # IPv6
print(sol.validIPAddress("2001:db8:85a3::8A2E:037j:7334"))            # Neither
print(sol.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334")) # Neither
       