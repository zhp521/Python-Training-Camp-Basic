"""
测试练习: 文件处理
"""
import pytest
import sys
import os
import tempfile

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.file_operations import read_file, write_file

def test_read_file():
    """测试读取文件函数"""
    # 创建临时文件
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
        temp.write("这是一个测试文件内容\n第二行内容")
        temp_path = temp.name
    
    try:
        # 测试读取文件
        content = read_file(temp_path)
        
        # 验证内容
        assert isinstance(content, str), "返回值应该是字符串"
        assert "这是一个测试文件内容" in content, "返回的内容应该包含原始文件内容"
        assert "第二行内容" in content, "返回的内容应该包含原始文件内容"
    finally:
        # 删除临时文件
        os.unlink(temp_path)

def test_write_file():
    """测试写入文件函数"""
    # 创建临时文件路径
    temp_path = tempfile.mktemp()
    test_content = "这是要写入文件的测试内容"
    
    try:
        # 测试写入文件
        result = write_file(temp_path, test_content)
        
        # 验证返回值
        assert isinstance(result, bool), "返回值应该是布尔类型"
        assert result is True, "成功写入应该返回True"
        
        # 验证文件内容
        with open(temp_path, 'r') as f:
            content = f.read()
            assert content == test_content, "文件内容应该与写入的内容一致"
    finally:
        # 清理临时文件
        if os.path.exists(temp_path):
            os.unlink(temp_path) 