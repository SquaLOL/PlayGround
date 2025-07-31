
def ips_between(start, end):
    start_arr = start.split('.')
    end_arr = end.split('.')
    start = int(start_arr[0]) * 256**3 + int(start_arr[1]) * 256**2 + int(start_arr[2]) * 256 + int(start_arr[3]) * 1
    end = int(end_arr[0]) * 256**3 + int(end_arr[1]) * 256**2 + int(end_arr[2]) * 256 + int(end_arr[3]) * 1

    return end - start

print(ips_between("10.11.12.13", "10.11.13.0"))

# start_number += int(start_arr[1]) * 256**2
# end_number += int(end_arr[1]) * 256**2
#
# start_number += int(start_arr[2]) * 256
# end_number += int(end_arr[2]) * 256
#
# start_number += int(start_arr[3]) * 1
# end_number += int(end_arr[3]) * 1







