import werkzeug
from flask_restful import reqparse

test_parser = reqparse.RequestParser()
# type 为期待接受的数据类型，help为提示信息
# test_parser.add_argument('rate', type=int, help='Rate to charge for this resource')
# require 为必须参数
# test_parser.add_argument('name', required=True,help="Name cannot be blank!")
# action 如果要接受键的多个值作为列表，则可以传递 action='append',  如表单中的checkbox
# test_parser.add_argument('name', action='append')
# dest 请求的name字段，将会改名为public_name
# test_parser.add_argument('name', dest='public_name')
# 使用location参数来 , 从指定位置提取参数
# test_parser.add_argument('name', type=str, location='args')
# test_parser.add_argument('name', type=int, location='form')

# 如果上传的是一个文件
# From file uploads
# test_parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')
# 多个位置指定
# test_parser.add_argument('text', location=['headers', 'values'])

# ----------- 利用 type 属性进行校验参数

def validate_type(value):
    if not isinstance(value,int):
        raise TypeError('[value:%s] data type must be int or super class'%str(value))
    else:
        return value

test_parser.add_argument('type_arg',type=validate_type)