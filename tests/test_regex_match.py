"""
测试练习: 正则表达式匹配
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.regex_match import find_emails, is_valid_phone_number, extract_urls

def test_find_emails():
    """测试查找邮箱地址函数"""
    # 测试基本功能
    text = "联系方式: user@example.com 或者 admin@company.org"
    result = find_emails(text)
    
    assert isinstance(result, list), "返回值应该是列表"
    assert len(result) == 2, "应该找到2个邮箱"
    assert "user@example.com" in result, "邮箱列表应该包含'user@example.com'"
    assert "admin@company.org" in result, "邮箱列表应该包含'admin@company.org'"
    
    # 测试没有邮箱的情况
    assert find_emails("没有邮箱的文本") == [], "没有邮箱的文本应该返回空列表"
    
    # 测试复杂情况
    complex_text = """
    以下是几个邮箱地址:
    1. first.last@example.com
    2. username-123@mail.company.co.uk
    3. info@website.cn
    请选择一个与我们联系。这不是邮箱: just.a.phrase
    """
    result = find_emails(complex_text)
    assert len(result) == 3, "应该找到3个邮箱"
    assert "first.last@example.com" in result
    assert "username-123@mail.company.co.uk" in result
    assert "info@website.cn" in result

def test_is_valid_phone_number():
    """测试验证手机号码函数"""
    # 测试有效的手机号码
    assert is_valid_phone_number("13812345678") == True, "有效的手机号码应该返回True"
    assert is_valid_phone_number("15912345678") == True, "有效的手机号码应该返回True"
    assert is_valid_phone_number("18812345678") == True, "有效的手机号码应该返回True"
    
    # 测试无效的手机号码
    assert is_valid_phone_number("1381234567") == False, "少于11位的手机号码应该返回False"
    assert is_valid_phone_number("138123456789") == False, "超过11位的手机号码应该返回False"
    assert is_valid_phone_number("12812345678") == False, "不以13/14/15/16/17/18/19开头的号码应该返回False"
    assert is_valid_phone_number("电话13812345678") == False, "含有非数字的号码应该返回False"
    assert is_valid_phone_number("") == False, "空字符串应该返回False"

def test_extract_urls():
    """测试提取URL函数"""
    # 测试基本功能
    text = "访问 https://www.example.com 或 http://company.org/path 获取更多信息"
    result = extract_urls(text)
    
    assert isinstance(result, list), "返回值应该是列表"
    assert len(result) == 2, "应该找到2个URL"
    assert "https://www.example.com" in result, "URL列表应该包含'https://www.example.com'"
    assert "http://company.org/path" in result, "URL列表应该包含'http://company.org/path'"
    
    # 测试没有URL的情况
    assert extract_urls("没有URL的文本") == [], "没有URL的文本应该返回空列表"
    
    # 测试复杂情况
    complex_text = """
    以下是几个网址:
    1. https://www.example.com/products?id=123
    2. http://subdomain.website.co.uk/path/to/page.html
    3. https://api.site.org/v1/data
    4. www.simple-site.com
    """
    result = extract_urls(complex_text)
    assert len(result) >= 3, "应该至少找到3个URL"
    assert "https://www.example.com/products?id=123" in result
    assert "http://subdomain.website.co.uk/path/to/page.html" in result
    assert "https://api.site.org/v1/data" in result 