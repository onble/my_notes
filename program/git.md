## git登录

#### 修改全局用户名邮箱

```
git config --global user.name "(你自己的登录名)"
git config --global user.emial "(你自己用的登陆邮箱)"
```

#### 修改代理

```
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
```

##### 查看当前代理

```
git config --global http.proxy
```



## 创建项目与维护

##### 初始化

1. 进入要管理的目录
2. 输入`git inint`回车

##### 查看文件状态

`git status`回车，检测当前目录下文件的状态
文件的状态：

- 红色：未管理的文件新修改的文件
- 绿色，添加到管理的文件

##### 查看历史提交哦

`git log`

##### 添加文件

`git add 文件名`
一般使用`git add .`将所有的文件加入管理

##### 提交到本地仓库

`git commit -m '记录信息'`

##### 回滚到之前的版本

```
git log
git reset --hard 复制版本号
```

##### 回滚到之后的版本

```
git reflog
git reset --hard 版本号
```

#### 分支

##### 查看分支

`git branch`

##### 图形展示分支变化

`git log --garph`
`git log --graph ==pretty=format:"%h %s"`

##### 新建分支

`git branch 分支名`

##### 切换分支

`git checkout 已存在的分支名`

##### 合并到主分支

```
git checkout master
git merge bug
```

##### 删除无用分支

`git branch -d bug`

#### 上传

##### 给远程仓库起名字

`git remote add 仓库名 远程仓库地址`

##### 向远程推送代码

`git push 仓库名 分支名`
``git push -u 仓库名 分支名`这个-u表示设置一个默认参数，下次输入`git push`就等同于这行代码

#### 下载克隆

##### 克隆

`git clone 远程仓库地址`

##### 拉取同步

需要先克隆，然后项目被修改后再拉取

`git pull 仓库别名 分支名`

#### 提交记录合并

```
git rebase -i HEAD~3    合并前三条记录
git rebase -i 某次的版本号    合并到版本号
上面两种方式非常不建议将已经提交到网络的版本合并进来，只在本地这样合并
```

#### 配置

- 项目配置文件：项目/.git/config
  ```
  git config --local user.name 'onble'
  git config --local user.email 'onble@qq.com'
  ```

- 全局配置文件：~/.gitconfig
  ```
  git config --global user.name 'onble'
  git config --global user.email 'onble@qq.com'
  ```

- 系统配置文件：/etc/.gitconfig
  ```
  git config --system user.name 'onble'
  git config --system user.email 'onble.qq.com'
  ```

### 其他衍生

#### 开源协议

- GPL
  最广泛使用
  最严格的一种
  linux使用该协议
  修改使用GPL的软件在发布的时候必须也使用GPL协议
- Apache 2.0
  要保留原作者的信息且加上自己的作者信息
- BSD
  不允许衍生作品署名原作者
- MIT
  必须尊重原作者，提及原作者
- Mozilla
  修改后的代码必须发布出来
