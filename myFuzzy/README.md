# myFuzzy

利用模糊理論計算出權重值

## How to use

定義好你的資源使用率 `element-1.csv` 與 `element-2.csv`，並使用 `watch` 指令持續監控與執行 `myfuzzy.py`
```sh
$ watch -n 0.5 python myfuzzy.py host
//or
$ watch -n 0.5 python myfuzzy.py docker
```
