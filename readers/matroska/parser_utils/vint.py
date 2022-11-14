from typing.io import BinaryIO


def get_int_from_bytes(b: bytes):
    return int(b.hex(), base=16)


def reseek_by_num_bits(f: BinaryIO, num_bits: int):
    f.seek(-(num_bits // 8), 1)


def find_one_bit_in_byte(b: bytes):
    b_int = get_int_from_bytes(b)
    one_index = -1
    for i in range(8):
        if b_int & 1 == 1:
            one_index = 8 - i
        b_int = b_int >> 1
    return one_index


def parse_data_size(f: BinaryIO):
    num_bits_parsed = 0
    while True:
        current_byte = f.read(1)
        one_bit_loc = find_one_bit_in_byte(current_byte)
        if one_bit_loc < 0:
            num_bits_parsed += 8
        else:
            return num_bits_parsed + one_bit_loc


def select_tail_bits(full_data: bytes, num_bits_to_keep: int):
    mask = 0
    for _ in range(num_bits_to_keep):
        mask = (mask << 1) + 1
    bits = get_int_from_bytes(full_data)
    return bits & mask


def parse_data(f: BinaryIO, data_size: int) -> int:
    if data_size == 0:
        return 0
    full_data = f.read(data_size)
    data_without_size_bits = select_tail_bits(full_data, data_size)
    return data_without_size_bits


def parse_vint(f: BinaryIO) -> int:
    vint_data_num_bits = parse_data_size(f)
    reseek_by_num_bits(f, vint_data_num_bits)
    vint_data = parse_data(f, vint_data_num_bits)
    return vint_data
