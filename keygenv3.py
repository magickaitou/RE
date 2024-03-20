# Bài genkey này cơ bản là lấy len của Name sau đó biến đổi thành số khác (tuyến tính)
# Sau đó đổi dạng lưu trữ sang IEEE, lây lodword
# Nối thêm vào lodowrd => Key (Lưu ý là số nguyên có dấu nha) %i :>>>>

def ieee(num):
    # This function converts a positive integer to IEEE 754 double-precision format
    exp_bias = 1023
    sign_bit = 0
    number = num
    
    total = 64  # IEEE double uses 64 bits 
    if (number <=0):
        result = "1"
        number = -number
    else: 
        result = "0"

    # Convert the input number to binary string
    number_bin = bin(number)[2:]  # Remove '0b' prefix
    print("Binary representation:", number_bin)

    # Calculate the exponent
    exp = len(number_bin) - 1 + exp_bias
    exp_bin = bin(exp)[2:].zfill(11)  # Convert to binary and zero-pad to 11 bits
    print("Exponent:", exp_bin)

    # Calculate the mantissa
    mantissa = number_bin[1:].ljust(52, '0')  # Remove the first bit and pad with zeros to 52 bits
    print("Mantissa:", mantissa)

    # Combine sign bit, exponent, and mantissa to form the IEEE 754 representation
    result = str(sign_bit) + exp_bin + mantissa

    print("IEEE 754 representation:", result)
    result = int(result, 2)
    result = str(hex(result))[2:]
    return result

name = input("Enter your name: ")
length = len(name)
print(length)

# Some operations...
edx = 0x875CD * length  & 0xFFFFFFFF
result = edx * 0x51EB851F
eax = (result >> 32) // 32  # Shift right by 32 bits and then divide by 32
result = eax * 0xFFFFFC90 & 0xFFFFFFFF

print("Result:", result)

# Convert the result to IEEE 754 representation
str_hex = str(ieee(result))
print("Converted to IEEE 754:", str_hex)
# Extract the last 8 bytes
eax = int(str_hex[-8:], 16) 
if eax & (1 << 31):  # Nếu bit cao nhất (63) được đặt
    eax -= 1 << 32
a2 = str(eax) + "-x019871"
print("Final result:", a2)

#1 work
