"""
测试练习: 字符串格式化
"""
import pytest
import sys
import os

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.string_formatting import format_student_info

def test_format_student_info():
    """测试学生信息格式化函数"""
    # 测试格式化结果
    result = format_student_info("张三", 18)
    assert "姓名: 张三" in result
    assert "年龄: 18" in result
    
    result = format_student_info("李四", 20)
    assert "姓名: 李四" in result
    assert "年龄: 20" in result 