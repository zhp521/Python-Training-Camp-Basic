import requests

def get_website_content(url):
    """
    发送GET请求获取网页内容
    
    参数:
    - url: 目标网站URL
    
    返回:
    - 包含响应信息的字典: 
      {
        'status_code': HTTP状态码,
        'content': 响应内容文本,
        'headers': 响应头部信息
      }
    """
    # 发送GET请求
    response = requests.get(url)
    
    # 返回包含状态码、内容和头部信息的字典
    return {
        'status_code': response.status_code,
        'content': response.text,
        'headers': dict(response.headers)
    }

def post_data(url, data):
    """
    发送POST请求提交数据
    
    参数:
    - url: 目标网站URL
    - data: 要提交的数据字典
    
    返回:
    - 包含响应信息的字典:
      {
        'status_code': HTTP状态码,
        'response_json': 响应的JSON数据(如果有),
        'success': 请求是否成功(状态码为2xx)
      }
    """
    # 发送POST请求
    response = requests.post(url, json=data)
    
    # 检查是否包含JSON响应
    try:
        response_json = response.json()
    except ValueError:
        response_json = None
    
    # 检查是否成功 (2xx状态码)
    success = 200 <= response.status_code < 300
    
    # 返回包含状态码、响应JSON和成功标志的字典
    return {
        'status_code': response.status_code,
        'response_json': response_json,
        'success': success
    } 