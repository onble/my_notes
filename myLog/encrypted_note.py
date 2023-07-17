import os


def get_markdown_files(folder_path):
    markdown_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files


def read_file_contents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def my_test():
    pass


def main():
    # 获取当前文件夹下及子文件夹与子文件夹的子文件下的所有以.md结束的文件
    current_folder = '.'  # 当前文件夹路径，可以根据实际情况修改
    markdown_files = get_markdown_files(current_folder)

    # 读取符合规则的文件内容
    for file_path in markdown_files:
        file_contents = read_file_contents(file_path)
        print(f'File: {file_path}')
        print('Contents:')
        print(file_contents)
        print('---')


if __name__ == '__main__':
    main()
    # my_test()
