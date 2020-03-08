from flask_restful import Api
from app.api.view import Hellworld, Test, TodoSimple, MutilArg, TestReqparse, Todo, NestedTest, TestAuthentication

api = Api()

# --------- hello world & test
api.add_resource(Hellworld,'/hello')
api.add_resource(Test,'/test',endpoint='end')

# -------------- 参数测试，get post
api.add_resource(TodoSimple, '/<string:todo_id>')

# ---------- restful 支持多种方式返回数据 data,code,headers


api.add_resource(MutilArg, '/MutilArg')

# --------------- 参数解析 reqparse
api.add_resource(TestReqparse, '/testreqparse')

# ---------- 测试序列化
api.add_resource(Todo, '/todo',endpoint='todo_ep')

api.add_resource(NestedTest, '/nested')

# ----------- 鉴权测试
api.add_resource(TestAuthentication, '/testAuthentication')
