import sys
import re
import lief


def find_chinese_strings(data):
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    return pattern.findall(data)


def main(file_path):
    binary = lief.parse(file_path)
    for section in binary.sections:
        if section.size > 0:
            data = section.content
            data_str = ''.join([chr(x) for x in data])
            chinese_strings = find_chinese_strings(data_str)
            if chinese_strings:
                print(f"在 {section.name} 中找到中文字符串:")
                for s in chinese_strings:
                    print(s)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python script.py <MachO文件路径>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)


# 判断string是否是中文
def disposeString(string):
    if string:
        if len(string) > 0:
            for s in string:
                if u'\u4e00' <= s <= u'\u9fff':
                    return True
    return False
