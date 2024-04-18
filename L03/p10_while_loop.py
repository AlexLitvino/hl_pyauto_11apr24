"""While, break, else, continue"""

# n = 13
# while True:
#     print(n)
#     n -= 1
#     if n == 6:
#         break
# else:
#     print('Ok')
# print('After while')
#print(n)

number_calibration = 0
i = 0
while True:
    packet = read_packet()
    if packet.status == 'Need calibration':
        calibrate()
    if packet.status == 'Calibrated':
        number_calibration += 1
        if number_calibration == 3:
            break

# do
# loop body
# while condition







"""
Task:
Request number from user and output square of number.
If user entered 'q', stop program
If user doesn't enter anything keep on requesting numbers.
"""
