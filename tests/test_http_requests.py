"""
测试练习: HTTP请求
"""
import pytest
import sys
import os
import responses  # 需要安装：pip install responses

# 添加exercises目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 导入待测试的函数
from exercises.http_requests import get_website_content, post_data

@pytest.mark.skip(reason="需要网络连接，可能不稳定")
def test_get_website_content_live():
    """测试实际GET请求（需要网络）"""
    result = get_website_content('https://httpbin.org/get')
    
    assert isinstance(result, dict), "返回值应该是字典"
    assert 'status_code' in result, "字典应该包含'status_code'键"
    assert 'content' in result, "字典应该包含'content'键"
    assert 'headers' in result, "字典应该包含'headers'键"
    
    assert result['status_code'] == 200, "状态码应该是200"
    assert isinstance(result['content'], str), "内容应该是字符串"
    assert isinstance(result['headers'], dict), "头部信息应该是字典"

@responses.activate
def test_get_website_content_mock():
    """使用responses模拟GET请求"""
    # 配置模拟响应
    responses.add(
        responses.GET, 
        'https://example.com/test',
        json={'message': 'success'}, 
        status=200,
        headers={'Content-Type': 'application/json'}
    )
    
    # 测试函数
    result = get_website_content('https://example.com/test')
    
    # 验证结果
    assert isinstance(result, dict), "返回值应该是字典"
    assert result['status_code'] == 200, "状态码应该是200"
    assert '"message": "success"' in result['content'], "内容应该包含预期的JSON字符串"
    assert 'Content-Type' in result['headers'], "头部信息应该包含Content-Type"

@responses.activate
def test_post_data_mock():
    """使用responses模拟POST请求"""
    # 配置模拟响应
    responses.add(
        responses.POST, 
        'https://example.com/post',
        json={'status': 'created', 'id': 123}, 
        status=201
    )
    
    # 测试数据
    test_data = {'name': '张三', 'age': 25}
    
    # 测试函数
    result = post_data('https://example.com/post', test_data)
    
    # 验证结果
    assert isinstance(result, dict), "返回值应该是字典"
    assert result['status_code'] == 201, "状态码应该是201"
    assert isinstance(result['response_json'], dict), "response_json应该是字典"
    assert result['response_json']['status'] == 'created', "响应JSON应该包含正确数据"
    assert result['success'] is True, "success应该是True"

@responses.activate
def test_post_data_error_mock():
    """使用responses模拟POST请求错误"""
    # 配置模拟响应
    responses.add(
        responses.POST, 
        'https://example.com/error',
        json={'error': 'invalid data'}, 
        status=400
    )
    
    # 测试数据
    test_data = {'invalid': 'data'}
    
    # 测试函数
    result = post_data('https://example.com/error', test_data)
    
    # 验证结果
    assert result['status_code'] == 400, "状态码应该是400"
    assert result['success'] is False, "success应该是False" 