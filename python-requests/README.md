# Python HTTP Requests Testing

使用執行緒發送請求，並計算其回應時間。

## How to use

#### @baseRequests.py

`baseRequests.py` 會顯示以下資訊：

1. total requests：總共請求次數
2. fail requests：總共失敗次數
3. total time：所有請求回應花費的時間
4. average time：每個請求的平均回應時間

使用 `baseRequests.py` 及其結果如下：

```sh
$ python baseRequests.py http://10.21.20.106/load.php 10
total requests:10
fail requests:0
total time:2.71364283562
average time:0.271364283562
```

#### @detailRequests.py

`detailRequests.py` 會顯示以下資訊：

1. 每個節點所接受到的`請求次數`、`請求回應的總時間`與`平均回應時間`
2. total requests：總共請求次數
3. fail requests：總共失敗次數
4. total time：所有請求回應花費的時間
5. average time：每個請求的平均回應時間

使用 `detailRequests.py` 及其結果如下：

```sh
$ python detailRequests.py http://10.21.20.106/load.php 10
slave-1  ->  10 1.83622527122 0.183622527122
total requests:10
fail requests:0
total time:1.83622527122
average time:0.183622527122
```

#### @normalRequest.py

`normalRequest.py` 與前面兩者測試方式不同，會以批量的方式將請求全部發送完畢。

> [範例]<br/>
> 若指定總共發送 200 次請求，則會先隨機產生一個`批量次數`(批量次數為整數，且其數值10-30有70%機率、30-70有20%機率以及70-100有10%機率)，然後利用執行緒將此`批量次數`發送出去，發送完畢後在產生一個`停滯時間`(停滯時間為浮點數，其數值0-2有80%機率、2-5有15%機率以及5-10有5%機率)，等待`停滯時間`後，在產生`批量次數`，重複以上步驟，直到 200 次請求發送完畢。

`normalRequest.py` 會顯示以下資訊：

1. 列出請求的進度
2. 發送的總執行時間
3. 每個節點所接受到的`請求次數`、`請求回應的總時間`與`平均回應時間`
4. total requests：總共請求次數
5. fail requests：總共失敗次數
6. total time：所有請求回應花費的時間
7. average time：每個請求的平均回應時間

使用 `normalRequest.py` 及其結果如下：

```sh
$ python normalRequest.py http://10.21.20.106/load.php 200
Progress...
Completed 100 requests
Completed 200 requests

task total time :  17.2303068638
slave-1 -> 200 , 122.307845354 , 0.61153922677
total requests : 200
fail requests : 0
total time : 122.307845354
average time : 0.61153922677
```
