import sys
import re
from urllib import parse


def octal_to_hex(octal_str):
    decimal_num = int(octal_str, 8)
    hex_num = hex(decimal_num)[2:]
    return hex_num.zfill(2)


def printChinese(x):
    y = x.encode('unicode_escape')
    z = y.decode('utf-8').replace('\\x', '%')
    # 兼容多余的 \\ 符号
    z = z.replace('\\', '')
    un = parse.unquote(z)
    print(un)
    return un


def convert_octal_to_hex(input_str):
    octal_numbers = re.findall(r'\\37777777\d{3}', input_str)
    print(octal_numbers)
    for octal_number in octal_numbers:
        print(octal_number)
        octal_number = octal_number[1:]  # 去掉开头的反斜杠
        print("octal_number", octal_number)

        decimal_number = int(octal_number, 8)
        valide_number = decimal_number & 0xFF
        hex_number = hex(valide_number)[1:]

        hex_str = "\\" + hex_number
        input_str = input_str.replace("\\" + octal_number, hex_str)
    return input_str


input_str = r"\37777777746\37777777630\37777777657\37777777744\37777777670\37777777672 \37777777744\37777777670\37777777655"
input_str = r"\37777777625\37777777623\37777777620\37777777741\37777777700\37777777616\37777777617\37777777614\37777777615\37777777612\37777777613\37777777610\37777777611\37777777606\37777777607\37777777737\37777777734\37777777735\37777777732\37777777733\37777777730\37777777731\37777777726\37777777727\37777777724\37777777725\37777777722\37777777723\37777777720\37777777721\37777777716\37777777717\37777777714\37777777715\37777777712\37777777713\37777777710\37777777711\37777777706\37777777707\37777777704\37777777777\37777777774\37777777775\37777777772\37777777773\37777777770\37777777771\37777777766\37777777767\37777777764\37777777765\37777777762\37777777763\37777777760\37777777761\37777777756\37777777757\37777777754\37777777755\37777777752\37777777753\37777777750\37777777751\37777777746\37777777747\37777777744"
output_str = convert_octal_to_hex(input_str)
print("output_str:", output_str)

printChinese(output_str)


def otool_hex_to_str(otool_output):
    # 提取十六进制数据
    hex_data = re.findall(r'\t([0-9a-fA-F ]+)', otool_output)

    # 将十六进制数据连接成一个字符串
    hex_str = ''.join(hex_data).replace(' ', '')

    # 将十六进制数据转换为字节串
    byte_data = bytes.fromhex(hex_str)

    # 尝试以UTF-16编码解码字节串
    decoded_str = byte_data.decode('utf-16', errors='ignore')

    # 使用正则表达式匹配所有非空字符
    all_strings = re.findall(r'[^\x00]+', decoded_str)

    return all_strings


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("用法: python otool_hex_to_str.py <otool输出>")
    else:
        all_strings = otool_hex_to_str(sys.argv[1])
        for s in all_strings:
            print(s)
