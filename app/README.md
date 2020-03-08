##### 响应格式 --- json
```python
# 默认
{'message':'', 'code':0,'data':['data',{}]}
# 有异常时
{'message':'error_msg', 'code':'error_code','data':['data',{}]}
```

#### flask 官方推荐的目录结构
本项目中结构比较乱，可参考官方推荐
```python
myapi/
    __init__.py
    app.py          # this file contains your app and routes
    resources/
        __init__.py
        foo.py      # contains logic for /Foo
        bar.py      # contains logic for /Bar
    common/
        __init__.py
        util.py     # just some common infrastructure
```

