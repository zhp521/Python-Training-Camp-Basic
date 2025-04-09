"""
测试练习: print 输出语句
"""
import pytest
import sys
import os
import io

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.hello_world import print_hello_world

def test_hello_world(capsys):
    """测试输出判断函数"""
    # 调用函数
    print_hello_world()
    
    # 捕获标准输出
    captured = capsys.readouterr()
    
    # 检查输出内容
    assert "Hello, World!" in captured.out 