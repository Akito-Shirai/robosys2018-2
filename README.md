## robosys2018課題2  /16C1071 白井 晶斗
----
### 課題内容
ROSで何かを作り、
* GitHubにプッシュ
* Youtubeにアップ
----
### 取り組み内容
[課題１](https://github.com/Akito-Shirai/robosys2018)で行ったLEDを光らせるノードをROS化した。今回はトピック通信を行うにあたって、「blink」というトピック名で「go」というメッセージをパブリッシュすることで、サイコロを転がし、その出目に応じてLEDを点滅させた。
尚、「go」以外のメッセージは受け取らないようにしている。
* [動画](https://youtu.be/-tFhewsYASs)
----
### 使用したもの
* Raspberry Pi 3B+
* LED
* 抵抗
----
### 回路
* 回路は課題１と同様に、GPIO25ピンを使用した。
<img width="1123" alt="2018-12-30 13 48 31" src="https://user-images.githubusercontent.com/42163768/50544478-eec3f680-0c39-11e9-9169-f0ffaf5a98a8.png">

### 本プログラムの操作方法
```
$ roscore                                   #ノード間で行われるメッセージ通信の接続情報を管理するマスタを起動
$ rosrun rs2018 led_dice.py                 #ノードの実行 rosrun [パッケージ名] [ノード名]
$ rostopic pub /blink std_msgs/String go    #rostopic pub [トピック名] [メッセージ型] [パラメータ]
```
----
### 参考資料
* [ロボットシステム学2018 第11回講義資料](https://github.com/ryuichiueda/robosys2018/blob/master/11_ros.md)
* [sleep関数の３つの便利な使い方](https://www.sejuku.net/blog/21474)
