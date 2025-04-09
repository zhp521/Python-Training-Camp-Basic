def calculate_area(length, width=None):
    """
    计算面积
    
    参数:
    - length: 长度
    - width: 宽度(可选)，如果不提供则计算正方形面积
    
    返回:
    - 计算得到的面积
    """
    if width is None:
        # 计算正方形面积
        return length * length
    else:
        # 计算长方形面积
        return length * width 