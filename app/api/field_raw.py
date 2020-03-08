from flask_restful import fields


class TestRawField(fields.Raw):
    def format(self, value):
        return '可自定义 改变数据结构'