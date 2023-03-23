# CCNA



# 第一节 3-23

### Endpoints

终端设备

```
Laptop 笔记本
Table 移动终端
Printer 打印机
Server 服务器
Virtual Server 虚拟服务器
IP Phone
TelePersence 视频会议
Scanner
Camera
Secunity Camera
Console
```



### Intermediary Devices

中间转发设备

#### Switch

交换机

#### Layer 3 Switch

3层交换机，管理普通交换机

#### Router

路由器

#### Virtual Router

虚拟路由器

#### AP

无线接入点 AccessPoint

#### WLC

无线控制器 AP的头，控制AP,与AP一起配套实验

#### Firewall

硬件防火墙

#### ISP

入侵防御检测，保安

#### Server with Cisco DNA Center

很贵,灵魂，心脏

可以控制思科的所有设备

### 传输媒介

传输媒介

#### Ethemel Link



#### Serial Link



#### Wireless Link

无线传输媒介

### Services

服务

## 企业网络设备模型

- 网络

  互联网

  - 有线网

    - 局域网

      LAN

      - 以太网

    - 广域网

    - 城域网

  - 无线网

### 接入层

LAN Access

交换机：将所有终端连接在一起

### 核心层

LAN Core

3层交换机-核心交换机：连接一层交换机

路由器：转发数据至互联网

### 数据中心层

所有的Server连接交换机后与核心层的三层交换机连接

## 评价网络模型

- Topology

  拓扑

  - 物理拓扑

    - 总线型

      无冲突

    - 环形拓扑

      发送是单向的

      令牌环网

      无冲突

    - 星型拓扑

      依赖中心

    - 互联拓扑

      - 全互联

        两两之间全都连接在一起

        不怕某一根线断开

        城市与楼之间的互联较多

      - 半互联

  - 逻辑拓扑

    数据真实发送的路径

- Bitrate or bandwidth

  比特率和带宽

  ```
  1024Byte=1KB
  
  1000KB = 1MB
  
  1024KB = 1MiB
  ```

  

- Availability

  可用性

  ```
  可用性 = 工作时间/(工作时间+重启时间)
  ```

  

- Reliability

  可靠性

  ```
  可靠性=总服务时间/失败次数
  ```

  

- Scalability

  可扩展性

- Security

  安全性

- Quality of Service

  服务质量

- Cost

  开销

- Virtualization

  虚拟化

## 用户应用对网络的影响

- 平滑/激增
- 良性/贪婪
- 丢包
- 延迟