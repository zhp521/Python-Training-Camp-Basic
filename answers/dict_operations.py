def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 创建字典的副本，避免修改原始字典
    result = students_dict.copy()
    
    if operation == "add":
        # 添加学生，需要两个参数：学生姓名和成绩
        student_name, score = args
        result[student_name] = score
        return result
    
    elif operation == "remove":
        # 删除学生，需要一个参数：学生姓名
        student_name = args[0]
        if student_name in result:
            del result[student_name]
        return result
    
    elif operation == "update":
        # 更新学生成绩，需要两个参数：学生姓名和新成绩
        student_name, new_score = args
        if student_name in result:
            result[student_name] = new_score
        return result
    
    elif operation == "get":
        # 获取学生成绩，需要一个参数：学生姓名
        student_name = args[0]
        if student_name in result:
            return result[student_name]
        return None 