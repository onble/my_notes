### 准备工作

#### 启动框架

###### 在app.run中传递参数

- host
  - 传递0.0.0.0表示本机测试
  - 还可以直接传递本机ip，这样就可以在局域网中进行访问
- port 端口
  默认为5001，可以尝试设置为8080，这样就是默认访问端口了
- debug
  ture，打开调试，项目上线的时候应该关闭

###### 框架设置setting

```python
在app.py函数中加入下面一行代码
app.config.from_object(settings)
```

在项目根目录创建setting.py文件，填入下面代码
```python
# 配置文件
ENV = 'development'
DEBUG = True
```

为了能够正确访问静态的文件，需要设置：
```python
app = Flask(__name__, static_url_path='')
```



#### 绑定路由

可以在绑定路由的时候，添加`<int:num>`来在url中读取数字参数后传入装饰器修饰的函数中，若不写int则默认为字符串类型,这种行为被翻译为转换器，但支持类型不多，挺鸡肋。

在绑定路由的时候可以传递路径，这个路径就是url的访问路径

在绑定路由的时候可以传递参数methods=['GET', 'PSOT']，用来控制进入该路径的方法处理

#### 渲染模板

### 路由设置

#### request对象

引入flask下的该对象
```python
from flask import Flask, request
```

参考文档：https://dormousehole.readthedocs.io/en/latest/api.html#flask.Request

重要的属性

- path 返回请求的路径，就是去掉前面的ip地址和端口号，真正的请求地址
- headers 获取请求头
- full_path 返回的路径带?以及后面携带的参数
- args 返回字典类型的参数字典
- method 返回请求方式
- form 返回form表单携带的参数

#### 给路由设置小名

在路由的装饰函数后面传递参数endpoint='小名'
```python
@app.route('/', endpoint='index')
def index():
    pass
	return None
```

设置小名后就可以使用路由反向解析
```python
url = url_for('index')
```

