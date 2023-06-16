import re
import sys


def extract_strings(macho_file_path, output_file_path):
    # 读取Mach-O文件中的字符串表
    with open(macho_file_path, 'rb') as f:
        macho_data = f.read()
    string_table_offset = int.from_bytes(
        macho_data[0x28:0x2C], byteorder='little')
    string_table_size = int.from_bytes(
        macho_data[0x2C:0x30], byteorder='little')
    string_table_data = macho_data[string_table_offset:
                                   string_table_offset+string_table_size]

    # 使用正则表达式匹配所有字符串
    string_regex = re.compile('[^\x00-\x1F\x7F-\xFF]+')
    strings = string_regex.findall(string_table_data.decode('utf-8'))

    # 输出所有字符串到文件中
    with open(output_file_path, 'w') as f:
        for s in strings:
            f.write(s + '\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python extract_strings.py <macho_file_path> <output_file_path>')
        sys.exit(1)
    macho_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    extract_strings(macho_file_path, output_file_path)
