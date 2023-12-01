# Hound-Detector
【猎犬嗅探】，探测出Web应用的指纹信息。  

      / \__
     (    @\___
     /         O
    /   (_____/  Author:dddinmx
    /_____/      Hound Detector  

### 安装使用  
#### 通用安装
``安装方法: git clone https://github.com/dddinmx/Hound-Detector.git``  
``pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/``  
#### MacOS  
``安装方法: 下载 Hound-darwin-amd64可执行文件``  
``给予可执行权限: chmod u+x ./Hound-darwin-amd64``  
#### Linux
``安装方法: 下载 Hound-linux-amd64可执行文件``  
``给予可执行权限: chmod u+x ./Hound-linux-amd64``  

#### 使用
``usage: Hound.py [-h] [-u URL] [-f FILE]``  
``python3 Hound.py -u url``  
``可执行文件: ./Hound-darwin-amd64 -f url.txt``  

### 功能  
- [x] 识别单个URL指纹  
- [x] 识别多个URL，放进同一txt文件中，一行一个URL  
- [x] 加入Wappalyzer插件比对，增加指纹准确率  


### 截图  
<img width="1219" alt="image" src="https://github.com/dddinmx/Hound-Detector/assets/19663680/f5db0a6a-acdc-4b81-984b-1d1587af97dc">
