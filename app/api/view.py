from datetime import datetime
from functools import wraps

from flask_restful import Resource, marshal_with
from flask import request

from app.api.auth import auth_decorate
from app.api.field import resource_fields, todo_resource_fields, todo_resource_fields2, todo_resource_fields_raw, \
    name_list, role_list


class Hellworld(Resource):
    """
    显而易见，这是个helloworld
    """
    def get(self):
        return 'hello world'


class Test(Resource):
    """
    接口测试
    """
    def get(self):
        data = {'code':200,
                'data':[],
                'msg':'TEST IS OK !'}
        import os
        data['pat'] =         os.getcwd()

        return data



class TodoSimple(Resource):
    """
    一个simple，get 与 put使用
    """
    def __init__(self):
        self.todos = {}
    def get(self, todo_id):
        print(request.args)
        return {todo_id: self.todos[todo_id]}

    def put(self, todo_id):
        self.todos[todo_id] = request.form['data']
        return {todo_id: self.todos[todo_id]}


class MutilArg(Resource):
    """
    多参数返回 ---->   data,code_status,headers
    """
    def get(self):
        return '多参数返回',200,{'content-type':'json'}


class TestReqparse(Resource):
    """
    测试 reqparse
    """
    def get(self):
        from app.api.parse import test_parser
        # 加上 strick=True 严格模式,如果请求包含解析器未定义的参数，可以引发错误
        # args = test_parser.parse_args(strict=True)
        args = test_parser.parse_args()
        # obj = args.get('picture')
        # with open('./source/picture.jpg','wb') as f2:
        #     f2.write(obj.read())
        print(args)
        return {'args': args}


# --------------- 测试序列化 1 ---------------

# class TodoDao(object):
#     def __init__(self, todo_id, task):
#         self.todo_id = todo_id
#         self.task = task
#
#         # This field will not be sent in the response
#         self.status = 'active'

class Field:
    def __init__(self):
        self.name = 'xxx'
        self.address = 'xxxxxxxxxx'
        self.property = 'xx'
        self.name_list = ['ak','sa','jiek','matt',{'name':'me'}]
class Todo(Resource):
    """
    说明一下 marshal_with 和 marshal的区别
    1. ---------
    marshal(data, resource_fields)
    2. -----------
    @marshal_with(todo_resource_fields)
    def func():
        return data_or_obj
    """
    # @marshal_with(todo_resource_fields_raw)
    # def get(self, **kwargs):
    #     # return TodoDao(todo_id='my_todo', task='Remember the milk')
    #     # return {'name':'xxx','address':'xxx','date_updated':datetime.now()}
    #     return Field()

    @marshal_with(name_list)
    def get(self, **kwargs):
        # return TodoDao(todo_id='my_todo', task='Remember the milk')
        # return {'name':'xxx','address':'xxx','date_updated':datetime.now()}
        return Field()

class NestedTest(Resource):
    class User:
        def __init__(self, name='curry', age = 31):
            self.name = name
            self.age = age
            self.hobbys = []
    class Role:
        def __init__(self, occupation):
            self.occupation = occupation
            self.data = []
    @marshal_with(role_list)
    def get(self):
        """
        data
        :return:
        """
        human = self.Role('human')
        jake = self.User('jake ma',9999)
        jake.hobbys.append('make money')
        jake.hobbys.append('spend money')
        curry = self.User()
        curry.hobbys.append('paly ball')
        human.data.extend([jake,curry])

        return human



# @auth_decorate
class TestAuthentication(Resource):
    method_decorators = [auth_decorate]

    def get(self):
        return 'request success'

