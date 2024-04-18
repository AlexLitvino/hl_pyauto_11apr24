"""
Bitwise operators
| & ^ ~ >> <<

Decimal to binary:
26 = 16 + 8 + 2 = 1 * 2^4 + 1 * 2^3 + 0 * 2^2 + 1 * 2^1 +  0 * 2^0 = 11010b
17 = 16 + 1 = 1 * 2^4 + 0 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0 = 10001b

1 byte = [0, 255]
7654321

|
00 - 0
01 - 1
10 - 1
11 - 1

&
00 - 0
01 - 0
10 - 0
11 - 1

^
00 - 0
01 - 1
10 - 1
11 - 0

~0 - 1
~1 - 0

1 >> 1 = 0
1 << 1 = 2
"""

# # Bitwise OR
# a = 3
# b = 2
# c = a | b
# print(f"{a:0>8b} {a}")
# print(f"{b:0>8b} {b}")
# print(f"{c:0>8b} {c}")


# # Bitwise AND
# a = 3
# b = 2
# c = a & b
# print(f"{a:0>8b} {a}")
# print(f"{b:0>8b} {b}")
# print(f"{c:0>8b} {c}")


# # Bitwise XOR (eXclusive OR)
# a = 3
# b = 2
# c = a ^ b
# print(f"{a:0>8b} {a}")
# print(f"{b:0>8b} {b}")
# print(f"{c:0>8b} {c}")

# # << Left shift
# a = 5
# b = a << 2
# print(f"{a:0>8b} {a}")
# print(f"{b:0>8b} {b}")

# # >> Right shift
# a = 5
# b = a >> 2
# print(f"{a:0>8b} {a}")
# print(f"{b:0>8b} {b}")


# # Inversion
# a = 13
# inv_a = ~a  # ~a = -a - 1
# inv_a_full = inv_a & 0xFF
# print(f"{a:0>8b} {a}")
# #print(f"{inv_a:0>8b} {inv_a}")
# print(f"{inv_a_full:0>8b} {inv_a_full}")
# print(a & inv_a)
# print((a | inv_a) & 0xFF)

"""
Task:
Sensor sends packets with environment data.
Packet structure is the following:
7-6 bits - sensor type
5-3 bit - temperature
2-0 bit - humidity
Bit order is big-endian (76543210)
"""
# data = 169
# print(f"{data:0>8b} {data}")
# sensor_type =
# temperature =
# humidity =