def convert_to_bin():
    bin_dict = {}
    for i in range(256):
        bin_value = format(i, '08b')
        bin_dict[i] = bin_value
    return bin_dict


print(convert_to_bin())
