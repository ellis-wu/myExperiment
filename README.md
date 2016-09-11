# My Experiment

資料夾結構如下：
```txt
myExperiment/
  ├── c-socket/
  ├── host-monitor/
  ├── my-php/
  ├── myFuzzy/
  └── python-requests/
```

## How To Use

將說明如何使用本研究的方法，動態改變`HAProxy`中`Weight Round-Robin`之權重值。

### Step 1 - Rabbitmq

在主節點安裝`Rabbitmq`。

> 安裝方式請參考：[Rabiitmq install](https://gist.github.com/ellisMing/0919c7bf7c0bacc5e6b5e63ff665d3df)

### Step 2 - not-docker-monitor

在主節點與每台工作節點安裝`not-docker-monitor`。

> 安裝方式請參考：[not-docker-monitor](https://github.com/kairen/not-docker-monitor)

配置`not-docker-monitor`中的 Config 檔案：
* 設定`[rabbit_messaging]`中的`host`為主節點之 IP 位置：

* 為每台節點設定其對應的角色：
  ```txt
  [role]
  master node -> consumer
  work node   -> producer
  ```

### Step 3 - HAProxy

在主節點上安裝`HAProxy`。

> 安裝方式請參考：[HAProxy install](https://gist.github.com/ellisMing/f1fa4f236d041f55e3b4)

HAProxy Config 檔中，需進行負載平衡之節點請務必填寫 port，範例如下：
```txt
listen www-balancer
    bind 0.0.0.0:9090
    balance roundrobin
    server web1 0.0.0.0:9000 check weight 1 maxconn -1
    server web2 0.0.0.0:9001 check weight 1 maxconn -1
```

### Step 4 - 開始動態改變 HAProxy 權重

利用`watch`指令監控及執行`myFuzzy`資料夾中的`myFuzzy.py`：
```sh
$ watch -n 0.5 python myFuzzy.py host
```

主要分為兩種模式：
  * host：對虛擬機進行動態改變權重
  * docker：對 docker container 進行動態改變權重
