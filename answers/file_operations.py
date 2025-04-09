def read_file(file_path):
    """
    读取文本文件内容
    
    参数:
    - file_path: 文件路径
    
    返回:
    - 文件内容字符串
    """
    # 使用with语句自动关闭文件
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    """
    写入内容到文本文件
    
    参数:
    - file_path: 文件路径
    - content: 要写入的内容
    
    返回:
    - 是否写入成功的布尔值
    """
    try:
        # 使用with语句自动关闭文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception:
        return False 