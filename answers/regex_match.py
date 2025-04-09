import re

def find_emails(text):
    """
    从文本中提取所有的电子邮件地址。
    
    参数:
        text (str): 要搜索的文本
        
    返回:
        list: 文本中找到的所有电子邮件地址的列表
    """
    # 电子邮件地址的正则表达式模式
    # 匹配用户名部分（字母、数字、点、下划线、百分号、加号和减号）
    # 然后是@符号
    # 然后是域名部分（字母、数字、点和连字符）
    # 最后是顶级域名（至少2个字母）
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # 使用findall方法查找所有匹配项
    emails = re.findall(pattern, text)
    return emails


def is_valid_phone_number(phone):
    """
    验证字符串是否为有效的中国手机号码。
    有效的手机号码应该:
    1. 长度为11位
    2. 以1开头
    3. 第二位是3-9之间的数字
    4. 全部由数字组成
    
    参数:
        phone (str): 要验证的电话号码字符串
        
    返回:
        bool: 如果是有效的手机号码则返回True，否则返回False
    """
    # 手机号码的正则表达式模式
    # ^表示开始，$表示结束，确保整个字符串匹配
    # 1表示以1开头
    # [3-9]表示第二位是3到9之间的数字
    # \d{9}表示后面是9个数字
    pattern = r'^1[3-9]\d{9}$'
    
    # 使用re.match检查是否匹配模式
    match = re.match(pattern, phone)
    return bool(match)


def extract_urls(text):
    """
    从文本中提取所有的URL链接。
    
    参数:
        text (str): 要搜索的文本
        
    返回:
        list: 文本中找到的所有URL的列表
    """
    # URL的正则表达式模式
    # 匹配http或https开头
    # 然后是://
    # 然后是域名部分
    # 可能有端口号
    # 可能有路径、查询参数等
    pattern = r'https?://[a-zA-Z0-9][-a-zA-Z0-9.]*[a-zA-Z0-9](:[0-9]{1,5})?(/[-a-zA-Z0-9%_.~#?&=]*)*'
    
    # 使用findall方法查找所有匹配项
    urls = re.findall(pattern, text)
    return urls 