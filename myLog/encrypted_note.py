import os
import random


def get_markdown_files(folder_path):
    """
    获取所有以.md结尾的文件
    :param folder_path:
    :return:所有以.md结尾的文件的列表
    """
    markdown_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files


def get_markdown_files_without_encrypted(folder_path):
    """
    获取所有需要加密的.md文件的路径
    :param folder_path:
    :return:所有需要加密的.md文件的路径组成的列表
    """
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


def get_markdown_files_without_decrypted(folder_path) -> list:
    """
    获取所有需要解密的md文件的路径
    :param folder_path:文件夹路径
    :return:包含所有未被解密的加密文件路径的列表
    """
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


def read_file_contents(file_path) -> str:
    """
    读取文件内容
    :param file_path:文件路径
    :return:文件内的字符串
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def encrypt_content(content: str) -> str:
    """
    加密内容

    加密算法：首先随机生成一个7位数的整数记录为seed_key，然后根据内容的长度length，生成一个从1-length的整数序列列表，作为映射表
    随后使用random模块进行随机打乱列表的顺序，根据打乱的顺序进行映射加密后的字符串
    在加密的字符串前记录seed后返回加密后的字符串
    :param content:未加密的文本内容
    :return:加密后的文本内容
    """
    seed_key = random.randint(1000000, 9999999)  # 生成7位随机整数作为种子
    random.seed(seed_key)  # 设置随机种子

    length = len(content)  # 加密字符串的长度
    mapping = list(range(length))  # 生成从0到length的整数列表
    random.shuffle(mapping)  # 打乱列表顺序

    encrypted_content = [''] * length
    for i, char in enumerate(content):
        encrypted_content[mapping[i]] = char  # 按照打乱后的列表进行映射

    encrypted_content = ''.join(encrypted_content)  # 将新的字符串拼接

    encrypted_content_with_key = 'seed=' + str(seed_key) + '\n' + encrypted_content  # 将种子密钥与加密内容拼接

    return encrypted_content_with_key


def decrypt_content(encrypted_content):
    """
    解密加密内容
    :param encrypted_content: 被加密的内容
    :return:解密后的内容
    """
    lines = encrypted_content.split('\n')  # 按换行符分割加密内容
    seed_key = int(lines[0].split('=')[1])  # 提取种子密钥
    encrypted_content = '\n'.join(lines[1:])  # 提取加密内容

    random.seed(seed_key)  # 设置随机种子

    length = len(encrypted_content)  # 加密字符串的长度
    mapping = list(range(length))  # 生成从0到length的整数列表
    random.shuffle(mapping)  # 打乱列表顺序

    original_content = [''] * length
    for i in range(length):
        original_content[i] = encrypted_content[mapping[i]]  # 按照逆映射后的列表进行还原

    return ''.join(original_content)  # 将还原后的字符串拼接并返回


def write_encrypted_file(file_path, content):
    """
    写下加密后的文件内容

    将加密后的内容写在与源文件同一路径下
    :param file_path: 被加密文件的路径
    :param content: 加密后的内容
    :return:
    """
    file_name, file_ext = os.path.splitext(file_path)
    new_file_path = file_name + '_encrypted' + file_ext
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def write_decrypted_file(file_path, content):
    """
    写下解密后的文件内容

    将解密后的内容写在与源文件同一路径下
    :param file_path:被解密的文件的路径
    :param content:解密后的内容
    :return:
    """
    file_name, file_ext = os.path.splitext(file_path)
    new_file_path = file_name.replace('_encrypted', '_decrypted') + file_ext
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def delete_encrypted_files(folder_path='.'):
    """
    删除所有的被加密的文件
    :param folder_path: 清除的路径，默认为当前文件夹
    :return:
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_encrypted.md'):
                file_path = os.path.join(root, file)
                os.remove(file_path)


def delete_decrypted_files(folder_path='.'):
    """
    删除所有的被解密的文件
    :param folder_path: 清除的路径，默认为当前文件夹
    :return:
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('_decrypted.md'):
                file_path = os.path.join(root, file)
                os.remove(file_path)


def clear_encrypted_files(current_folder='.'):
    """
    删除所有被加密的文件
    :param current_folder: 清除的文件夹路径，默认为当前文件夹
    :return:
    """
    # 删除以_encrypted.md结尾的文件
    delete_encrypted_files(current_folder)


def clear_decrypted_files(current_folder='.'):
    """
    删除所有被解密的文件
    :param current_folder: 清除的文件夹路径，默认为当前文件夹
    :return:
    """
    # 删除以_encrypted.md结尾的文件
    delete_decrypted_files(current_folder)


def clear_all(current_folder='.'):
    """
    清除所有被程序生成的文件
    :param current_folder: 清除路径
    :return:
    """
    clear_encrypted_files(current_folder)
    clear_decrypted_files(current_folder)


def encrypt_markdown(current_folder='.'):
    """
    加密markdown文件
    :param current_folder:解密的文件夹路径，默认为当前文件夹路径
    :return:
    """
    # 获取当前文件夹下及子文件夹与子文件夹的子文件下的所有以.md结束的文件
    markdown_files = get_markdown_files_without_encrypted(current_folder)

    # 读取符合规则的文件内容并进行加密处理后写入新文件
    for file_path in markdown_files:
        file_contents = read_file_contents(file_path)
        encrypted_content = encrypt_content(file_contents)
        write_encrypted_file(file_path, encrypted_content)
    print('新加密的笔记：', markdown_files)


def decrypt_markdown(current_folder='.'):
    """
    解密markdown文件
    :param current_folder:解密的文件夹路径，默认为当前文件夹路径
    :return:
    """
    # 获取当前文件夹下及子文件夹与子文件夹的子文件下的所有以.md结束的文件
    markdown_files = get_markdown_files_without_decrypted(current_folder)

    # 读取符合规则的文件内容并进行加密处理后写入新文件
    for file_path in markdown_files:
        file_contents = read_file_contents(file_path)
        decrypted_content = decrypt_content(file_contents)
        write_decrypted_file(file_path, decrypted_content)
    print('新解密的笔记：', markdown_files)


def main():
    """
    主函数，默认运行脚本该函数的功能
    :return:
    """
    folder = '.'  # 进行操作的文件夹路径
    encrypt_markdown(folder)  # 加密所有的markdown文件
    decrypt_markdown(folder)  # 解密所有的markdown文件


def my_test():
    """
    测试函数，供开发测试
    :return:
    """
    pass


if __name__ == '__main__':
    main()
    # my_test()
    # clear_all()
