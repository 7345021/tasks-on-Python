# 41.Реализуйте RLE алгоритм: реализуйте модуль сжатия и
# восстановления данных. Входные и выходные данные хранятся
# в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W
with open('41_RLE1_decoded.txt', 'r') as data:
    my_text = data.read()


def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode_rle(my_text)
print('Сжатый текст: ', str_code)

with open('41_RLE2_encoded.txt', 'r') as data:
    my_text2 = data.read()


def decoding_rle(ss: str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decode = decoding_rle(my_text2)
print('Восстановленный текст: ', str_decode)
