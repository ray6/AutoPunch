AutoPunch
===
## 系統環境
python 3.7.4
pip 19.0.3

## 下載firefox webdriver
[下載webdriver](https://github.com/mozilla/geckodriver/releases)
下載完把webdriver跟py檔放一起
電腦裡要有firefox瀏覽器，沒有的記得安裝
## 設定
1. 先安裝套件
    ```=shell script
    virtualenv venv
    pip install -r requirement.txt
    ```
2. 在`AutoRegister.py` 把 `username` 跟 `passwd` 改成自己的帳密。
3. 把對應路徑填到`SignIn.bat`和`SighOut.bat`裡
## 設定排程工作
到電腦的 控制台 > 系統及安全性 > 系統工作管理工具 > 工作排程器
點選建立工作
##### 一般
1. 打名稱 `SignIn` (簽到用)
2. 安全性選項選`不論使用者登陸與否均執行`
##### 動作
1. 點 `新增`
2. 程式或指令碼 用瀏覽檔案找到 `SignIn.bat`
3. 確定
##### 觸發程序
1. 點 `新增`
2. 設定要執行程式的時間，記得`已啟用`有被勾選
3. 確定

最後用完按確定建立工作，再建立一個自動執行SignOut.bat (簽退用)的工作。
建完後可以再`工作排程器程式庫`看到剛剛建的工作就完成了。
