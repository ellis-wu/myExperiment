# My Experiment

資料夾結構如下
```txt
myExperiment
  ├── c-socket
  ├── host-monitor
  ├── my-php
  ├── myFuzzy
  └── python-requests
```

## How to use

將說明如何使用本研究的方法，動態改變 `HAProxy` 中 `Weight Round-Robin` 之權重值

### Step 0

在主節點安裝 `Rabbitmq`

> 安裝方式請參考：[Rabiitmq install](https://gist.github.com/ellisMing/0919c7bf7c0bacc5e6b5e63ff665d3df)

### Step 1

在主節點與每台工作節點安裝 `not-docker-monitor`

> 安裝方式請參考：[not-docker-monitor](https://github.com/kairen/not-docker-monitor)

配置 `not-docker-monitor` 中的 config 檔案：
* 設定 `[rabbit_messaging]` 中的 `host` 為主節點之 IP 位置：

* 為每台節點設定其對應的角色：
```txt
[role]
master node -> consumer
work node   -> producer
```

### Step 2
