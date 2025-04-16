"""
测试练习: 文件处理
"""
import pytest
import sys
import os
import tempfile
import codecs

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.file_operations import read_file, write_file

def test_read_file():
    """测试读取文件函数"""
    # 创建临时文件
    fd, temp_path = tempfile.mkstemp(text=True)
    os.close(fd)
    
    # 使用UTF-8编码写入内容
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write("这是一个测试文件内容\n第二行内容")
    
    try:
        # 测试读取文件
        content = read_file(temp_path)
        
        # 验证内容
        assert isinstance(content, str), "返回值应该是字符串"
        assert "这是一个测试文件内容" in content, "返回的内容应该包含原始文件内容"
        assert "第二行内容" in content, "返回的内容应该包含原始文件内容"
    finally:
        # 删除临时文件
        try:
            os.unlink(temp_path)
        except:
            pass  # 忽略删除失败的错误

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
        with open(temp_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert content == test_content, "文件内容应该与写入的内容一致"
    finally:
        # 清理临时文件
        if os.path.exists(temp_path):
            try:
                os.unlink(temp_path)
            except:
                pass  # 忽略删除失败的错误 