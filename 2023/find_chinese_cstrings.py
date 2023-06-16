import re
import sys
from urllib import parse
import json
import os


def octal_to_hex(octal_number):
    # 八进制转成十进制数据
    decimal_number = int(octal_number, 8)
    # Unicode 字符串按位运算
    valide_number = decimal_number & 0xFF
    # 转成可用的十六进制数据
    hex_number = hex(valide_number)[1:]
    return hex_number


def hex_to_chinese(x):
    y = x.encode('unicode_escape')
    z = y.decode('utf-8').replace('\\x', '%')
    # 兼容多余的 \\ 符号
    z = z.replace('\\', '')
    un = parse.unquote(z)
    return un


def convert_octal_to_hex(input_str):
    octal_numbers = re.findall(r'\\37777777\d{3}', input_str)
    # print(octal_numbers)
    for octal_number in octal_numbers:
        octal_number = octal_number[1:]  # 去掉开头的反斜杠
        # print("octal_number", octal_number)

        # 八进制转成十进制数据，并且转成可用的十六进制数据
        hex_number = octal_to_hex(octal_number)

        hex_str = "\\" + hex_number
        input_str = input_str.replace("\\" + octal_number, hex_str)
    return input_str


def dispose_line(input_str):
    # 1. 从 "Swift \37777777744\37777777670\37777777655" 找到 "\37777777744\37777777670\37777777655"
    start_index = input_str.find(r"\37777777")
    if start_index < 0:
        return None
    octal_str = input_str[start_index:]
    # print("octal_str", octal_str)

    # 2. 将 "\37777777744\37777777670\37777777655" 作为八进制，转成 十六进制
    output_str = convert_octal_to_hex(input_str)
    # print("output_str", output_str)
    return hex_to_chinese(output_str)


# python3 find_chinese_strings.py HDFindStringDemo
if __name__ == '__main__':
    print("start")
    input_file = sys.argv[1]
    os.system(f"otool -V -X -s __TEXT __cstring {input_file} > cstring.txt")

    file_path = 'cstring.txt'
    output_data = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()  # 去掉换行符
            value = dispose_line(line)
            if value:
                output_data.append(value)

    output_file_path = 'cstring_output.json'
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print("已将字符串以JSON数组形式写入cstring_output.json文件")
    print("end")
