# 使用说明

## ssh连接

- 主机名：`raspberrypi.local`
- 用户名 : `pi`
- 密码 : `raspberry`

## 创建目录

```shell
cd /
sudo mkdir scripts
```

## 下载文件

```shell
cd scripts
sudo wget https://github.com/cairy/RaspberryPi/raw/master/%E8%B0%83%E9%80%9F%E9%A3%8E%E6%89%87/fan_speed.py
sudo wget https://github.com/cairy/RaspberryPi/raw/master/%E8%B0%83%E9%80%9F%E9%A3%8E%E6%89%87/run-fan.service
#添加执行权限
sudo chmod 755 fan_speed.py
sudo chmod 777 run-fan.service
```

## 创建服务

```shell
#先拷贝
sudo cp run-fan.service /etc/systemd/system
#启动
sudo systemctl start run-fan.service
#设置开机启动
sudo systemctl enable run-fan.service
```

