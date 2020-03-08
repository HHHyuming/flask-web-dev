import datetime
import decimal
import uuid

from flask import jsonify, Flask


app = Flask(__name__)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def xx(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    # print(error.xx())
    response = jsonify(error.xx())
    print(response), type(jsonify(error.xx()))
    response.status_code = error.status_code
    return response

@app.route('/foo')
def get_foo():
    raise InvalidUsage('This view is gone', status_code=410)
from flask.json import JSONEncoder as BaseJSONEncoder
class JSONEncoder(BaseJSONEncoder):

    def default(self, o):
        """
        如有其他的需求可直接在下面添加
        :param o:
        :return:
        """
        if isinstance(o, datetime.datetime):
            # 格式化时间
            return o.strftime("%Y-%m-%d")
        if isinstance(o, datetime.date):
            # 格式化日期
            return o.strftime('%Y-%m-%d')
        if isinstance(o, decimal.Decimal):
            # 格式化高精度数字
            return str(o)
        if isinstance(o, uuid.UUID):
            # 格式化uuid
            return str(o)
        if isinstance(o, bytes):
            # 格式化字节数据
            return o.decode("utf-8")
        return super(JSONEncoder, self).default(o)

app.json_encoder = JSONEncoder
@app.route('/time')
def test_time():
    return jsonify(datetime.datetime.now())

if __name__ == '__main__':
    app.run(debug=True)
    # print(dict(()))