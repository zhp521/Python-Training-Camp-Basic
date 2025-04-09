def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 创建学生列表的副本，避免修改原始列表
    result = students.copy()
    
    if operation == "add":
        # 添加学生，需要一个参数：学生姓名
        result.append(args[0])
    elif operation == "remove":
        # 删除学生，需要一个参数：学生姓名
        if args[0] in result:
            result.remove(args[0])
    elif operation == "update":
        # 更新学生，需要两个参数：原姓名和新姓名
        if args[0] in result:
            index = result.index(args[0])
            result[index] = args[1]
    
    return result 