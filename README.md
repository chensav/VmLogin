### VmLogin API

操作VmLogin API的方法

#### 安装

#### 源码安装

```bash
git clone 
cd VmLogin
pip install -r requirements.txt
```

#### pip安装

```bash
pip install VmLogin
```


#### 使用

```python
# 本地接口
from VmLogin.local import Local

online = Local()
# 重启VmLogin
data = online.restart()
```
```python
# 远程接口
from VmLogin.online import Online
token = "your token"
online = Online(token=token)
# 获取所有配置
data = online.get_profile_list()
```


