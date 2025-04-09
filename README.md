# Python训练营

## 练习内容

1. **基础入门**
   - hello_world.py: print 输出语句

2. **控制结构**
   - if_else.py: if-elif-else条件语句
   - for_loop.py: for循环
   - while_loop.py: while循环
   - break_continue.py: break和continue语句

3. **函数和模块**
   - function_params.py: 函数定义和参数
   - math_module.py: 使用math模块

4. **数据结构**
   - list_operations.py: 列表操作
   - dict_operations.py: 字典操作 
   - set_operations.py: 集合操作

5. **字符串操作**
   - string_formatting.py: 字符串格式化

## 使用方法

1. 打开对应的练习文件（如`exercises/if_else.py`）
2. 阅读文件顶部的说明，了解需要实现的功能
3. 在标记为`# 请在下方编写代码`的位置编写你的代码
4. 使用pytest运行测试，检查你的实现是否正确

## 运行测试

可以使用以下命令运行测试：

```bash
# 安装依赖
pip install -r requirements.txt

# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_if_else.py
```

## 评分标准

测试结果只有通过和不通过两种状态：
- 通过：所有测试用例都符合预期
- 不通过：至少有一个测试用例失败

## 目录结构

```
Python-Training-camp/
├── exercises/             # 练习题目
│   ├── hello_world.py
│   ├── if_else.py
│   ├── for_loop.py
│   └── ...
├── tests/                 # 测试文件
│   ├── test_hello_world.py
│   ├── test_if_else.py
│   ├── test_for_loop.py
│   └── ...
├── answers/               # 参考答案
│   ├── hello_world.py
│   ├── if_else.py
│   ├── for_loop.py
│   └── ...
└── requirements.txt       # 项目依赖
``` 