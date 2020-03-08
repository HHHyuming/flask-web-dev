from flask_restful import fields, marshal

# -------test fields -----------
from app.api.field_raw import TestRawField

resource_fields = {
    'task': fields.String,
    # todo_ep 为路由的endpoint
    'uri': fields.Url('todo_ep')
}
#  todo field
# ------- 通常用法
todo_resource_fields = {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
}

# -------重命名 字段
# attribute 指定解析的字段， default，默认值
todo_resource_fields2 = {
    'name': fields.String(attribute='address'),
    'address': fields.String,
    'xxx':fields.String(default='xxxxxxx')
}
# --------- 继承 fields.raw 自定义数据格式
todo_resource_fields_raw = {
    'name': fields.String(attribute='address'),
    'address': fields.String,
    'property': TestRawField(),
}
# --------- 列表
# name_list = {
#     'name_list': fields.List(fields.String(attribute='name'),attribute='name_list')
# }

name_list = {
    'name_list': fields.List(fields.String,attribute='name_list')
}
# ----- nested 与 list 嵌套
hobby_list = {
    'hobby': fields.String,
}

user_list = {
    'name': fields.String,
    'age': fields.Integer,
    'hobbys': fields.List(fields.String)
}

role_list = {
    'occupation': fields.String,
    'data': fields.Nested(user_list)
}


user_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

user_list_fields = {
    fields.List(fields.Nested(user_fields)),
}
