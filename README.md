# Python训练营基础和进阶部分

本项目包含一系列Python编程练习，涵盖了Python基础知识的各个方面。学生需要补全缺失的代码，并通过测试来验证自己的实现是否正确。

## 练习内容

### 第1部分: 基础入门
1. **hello_world.py**: print 输出语句
2. **data_types.py**: 变量和数据类型（整数、浮点数、字符串等）

### 第2部分: 控制结构
3. **if_else.py**: if-elif-else条件语句
4. **for_loop.py**: for循环
5. **while_loop.py**: while循环
6. **break_continue.py**: break和continue语句

### 第3部分: 函数和模块
7. **function_params.py**: 函数定义和参数
8. **math_module.py**: 使用math模块

### 第4部分: 数据结构
9. **list_operations.py**: 列表操作
10. **dict_operations.py**: 字典操作 
11. **set_operations.py**: 集合操作

### 第5部分: 字符串操作
12. **string_formatting.py**: 字符串格式化（f-strings）
13. **string_split.py**: 字符串分割（split方法）
14. **regex_match.py**: 正则表达式匹配

### 第6部分: 文件操作和网络
15. **file_operations.py**: 文件读写操作
16. **http_requests.py**: HTTP请求和响应处理

### 第7部分: 面向对象编程
17. **oop_basics.py**: 面向对象编程基础（类和对象）

## 使用方法

1. 打开对应的练习文件（如`exercises/if_else.py`）
2. 阅读文件顶部的说明，了解需要实现的功能
3. 在标记为`# 请在下方编写代码`的位置编写你的代码
4. 使用pytest运行测试，检查你的实现是否正确

## 建议学习顺序

建议按照上述编号顺序学习，从基础逐步深入：
1. 先掌握基础入门部分（输出、数据类型）
2. 学习控制结构（条件、循环）
3. 掌握函数定义与使用
4. 学习数据结构操作
5. 学习字符串处理（格式化、分割、正则表达式）
6. 学习文件操作和网络请求
7. 最后学习面向对象编程

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
│   ├── data_types.py
│   ├── if_else.py
│   ├── for_loop.py
│   ├── while_loop.py
│   ├── ...
│   ├── string_formatting.py
│   ├── string_split.py
│   ├── regex_match.py
│   ├── file_operations.py
│   ├── http_requests.py
│   └── oop_basics.py
├── tests/                 # 测试文件
│   ├── test_hello_world.py
│   ├── test_data_types.py
│   ├── ...
│   ├── test_string_split.py
│   ├── test_regex_match.py
│   ├── test_file_operations.py
│   ├── test_http_requests.py
│   └── test_oop_basics.py
└── requirements.txt       # 项目依赖
``` 
