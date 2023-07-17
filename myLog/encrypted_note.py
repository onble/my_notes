import os
import random


def get_markdown_files(folder_path):
    """
    获取所有以.md结尾的文件
    :param folder_path:
    :return:
    """
    markdown_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files


def get_markdown_files_without_encrypted(folder_path):
    markdown_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                encrypted_file = file_path[:-3] + '_encrypted.md'
                if not os.path.exists(encrypted_file):
                    if not file_path.endswith('_encrypted.md') and not file_path.endswith('_decrypted.md'):
                        markdown_files.append(file_path)
    return markdown_files


def get_markdown_files_without_decrypted(folder_path):
    markdown_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_encrypted.md'):
                file_path = os.path.join(root, file)
                encrypted_file = file_path[:-13] + '_decrypted.md'
                if not os.path.exists(encrypted_file):
                    if not file_path.endswith('_decrypted.md'):
                        markdown_files.append(file_path)
    return markdown_files


def read_file_contents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def encrypt_content(content):
    seed_key = random.randint(1000000, 9999999)  # 生成7位随机整数作为种子
    random.seed(seed_key)  # 设置随机种子

    length = len(content)  # 加密字符串的长度
    mapping = list(range(length))  # 生成从0到length的整数列表
    random.shuffle(mapping)  # 打乱列表顺序

    encrypted_content = [None] * length
    for i, char in enumerate(content):
        encrypted_content[mapping[i]] = char  # 按照打乱后的列表进行映射

    encrypted_content = ''.join(encrypted_content)  # 将新的字符串拼接

    encrypted_content_with_key = 'seed=' + str(seed_key) + '\n' + encrypted_content  # 将种子密钥与加密内容拼接

    return encrypted_content_with_key


def decrypt_content(encrypted_content):
    """
    解密加密内容
    :param encrypted_content:
    :return:
    """
    lines = encrypted_content.split('\n')  # 按换行符分割加密内容
    seed_key = int(lines[0].split('=')[1])  # 提取种子密钥
    encrypted_content = '\n'.join(lines[1:])  # 提取加密内容

    random.seed(seed_key)  # 设置随机种子

    length = len(encrypted_content)  # 加密字符串的长度
    mapping = list(range(length))  # 生成从0到length的整数列表
    random.shuffle(mapping)  # 打乱列表顺序

    original_content = [None] * length
    for i in range(length):
        original_content[i] = encrypted_content[mapping[i]]  # 按照逆映射后的列表进行还原

    return ''.join(original_content)  # 将还原后的字符串拼接并返回


def write_encrypted_file(file_path, content):
    file_name, file_ext = os.path.splitext(file_path)
    new_file_path = file_name + '_encrypted' + file_ext
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def write_decrypted_file(file_path, content):
    file_name, file_ext = os.path.splitext(file_path)
    new_file_path = file_name.replace('_encrypted', '_decrypted') + file_ext
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def delete_encrypted_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_encrypted.md'):
                file_path = os.path.join(root, file)
                os.remove(file_path)


def delete_decrypted_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_decrypted.md'):
                file_path = os.path.join(root, file)
                os.remove(file_path)


def clear_encrypted_files():
    # 指定当前文件夹路径
    current_folder = '.'  # 当前文件夹路径，可以根据实际情况修改
    # 删除以_encrypted.md结尾的文件
    delete_encrypted_files(current_folder)


def clear_decrypted_files():
    # 指定当前文件夹路径
    current_folder = '.'  # 当前文件夹路径，可以根据实际情况修改
    # 删除以_encrypted.md结尾的文件
    delete_decrypted_files(current_folder)


def encrypt_markdown():
    # 获取当前文件夹下及子文件夹与子文件夹的子文件下的所有以.md结束的文件
    current_folder = '.'  # 当前文件夹路径，可以根据实际情况修改
    markdown_files = get_markdown_files_without_encrypted(current_folder)

    # 读取符合规则的文件内容并进行加密处理后写入新文件
    for file_path in markdown_files:
        file_contents = read_file_contents(file_path)
        encrypted_content = encrypt_content(file_contents)
        write_encrypted_file(file_path, encrypted_content)
    print('新加密的笔记：', markdown_files)


def decrypt_markdown():
    # 获取当前文件夹下及子文件夹与子文件夹的子文件下的所有以.md结束的文件
    current_folder = '.'  # 当前文件夹路径，可以根据实际情况修改
    markdown_files = get_markdown_files_without_decrypted(current_folder)

    # 读取符合规则的文件内容并进行加密处理后写入新文件
    for file_path in markdown_files:
        file_contents = read_file_contents(file_path)
        decrypted_content = decrypt_content(file_contents)
        write_decrypted_file(file_path, decrypted_content)
    print('新解密的笔记：', markdown_files)


def main():
    encrypt_markdown()


def my_test():
    # 获取当前文件夹下及子文件夹与子文件夹的子文件下的所有以.md结束的文件
    current_folder = '.'  # 当前文件夹路径，可以根据实际情况修改
    # print(get_markdown_files_without_decrypted(current_folder))
    # decrypt_markdown()
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('_decrypted_encrypted.md'):
                file_path = os.path.join(root, file)
                os.remove(file_path)


if __name__ == '__main__':
    main()
    # my_test()
    # clear_encrypted_files()
    # clear_decrypted_files()
    decrypt_markdown()  # 解密所有的markdown文件
