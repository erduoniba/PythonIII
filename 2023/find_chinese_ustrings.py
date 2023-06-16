import sys
import re
import json
import os


def otool_hex_to_str(otool_output):
    # 提取十六进制数据
    hex_data = re.findall(r'\t([0-9a-fA-F ]+)', otool_output)
    # print("hex_data", hex_data)

    # 将十六进制数据连接成一个字符串
    hex_str = ''.join(hex_data).replace(' ', '')
    # print("hex_str", hex_str)

    # 将十六进制数据转换为字节串
    byte_data = bytes.fromhex(hex_str)
    # print("byte_data", byte_data)

    # 尝试以UTF-16编码解码字节串
    decoded_str = byte_data.decode('utf-16', errors='ignore')
    # print("decoded_str", decoded_str)

    # 使用正则表达式匹配所有非空字符
    all_strings = re.findall(r'[^\x00]+', decoded_str)
    # print("all_strings", all_strings)

    return all_strings


# python3 find_chinese_utrings.py HDFindStringDemo
if __name__ == '__main__':
    print("start")
    input_file = sys.argv[1]
    os.system(f"otool  -X -s __TEXT __ustring  {input_file} > ustring.txt")

    with open('ustring.txt', 'r') as f:
        otool_output = f.read()
    all_strings = otool_hex_to_str(otool_output)
    with open('ustring_output.json', 'w', encoding='utf-8') as f:
        json.dump(all_strings, f, ensure_ascii=False, indent=2)
    print("已将字符串以JSON数组形式写入ustring_output.json文件")
    print("end")