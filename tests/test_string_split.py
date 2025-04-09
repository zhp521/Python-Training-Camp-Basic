"""
测试练习: 字符串分割
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.string_split import extract_keywords, parse_csv_line, extract_name_and_domain

def test_extract_keywords():
    """测试提取关键词函数"""
    # 测试基本功能
    text = "Python 编程 学习 字符串 分割"
    result = extract_keywords(text)
    
    assert isinstance(result, list), "返回值应该是列表"
    assert len(result) == 5, "应该提取出5个关键词"
    assert "Python" in result, "关键词列表应该包含'Python'"
    assert "编程" in result, "关键词列表应该包含'编程'"
    assert "学习" in result, "关键词列表应该包含'学习'"
    
    # 测试空字符串
    assert extract_keywords("") == [], "空字符串应该返回空列表"
    
    # 测试只有一个关键词
    assert extract_keywords("Python") == ["Python"], "单个关键词应该返回包含该关键词的列表"

def test_parse_csv_line():
    """测试解析CSV行函数"""
    # 测试基本功能
    csv_line = "张三,25,北京,工程师"
    result = parse_csv_line(csv_line)
    
    assert isinstance(result, list), "返回值应该是列表"
    assert len(result) == 4, "应该解析出4个字段"
    assert result[0] == "张三", "第一个字段应该是'张三'"
    assert result[1] == "25", "第二个字段应该是'25'"
    assert result[2] == "北京", "第三个字段应该是'北京'"
    assert result[3] == "工程师", "第四个字段应该是'工程师'"
    
    # 测试空字段
    csv_line_with_empty = "李四,,上海,设计师"
    result = parse_csv_line(csv_line_with_empty)
    assert result[1] == "", "空字段应该解析为空字符串"
    
    # 测试空行
    assert parse_csv_line("") == [""], "空行应该返回包含一个空字符串的列表"

def test_extract_name_and_domain():
    """测试提取电子邮件用户名和域名函数"""
    # 测试基本功能
    email = "user@example.com"
    username, domain = extract_name_and_domain(email)
    
    assert username == "user", "用户名应该是'user'"
    assert domain == "example.com", "域名应该是'example.com'"
    
    # 测试复杂用户名
    email = "first.last@company.org"
    username, domain = extract_name_and_domain(email)
    assert username == "first.last", "用户名应该是'first.last'"
    assert domain == "company.org", "域名应该是'company.org'"
    
    # 测试子域名
    email = "admin@mail.example.co.uk"
    username, domain = extract_name_and_domain(email)
    assert username == "admin", "用户名应该是'admin'"
    assert domain == "mail.example.co.uk", "域名应该包含完整的域名部分" 