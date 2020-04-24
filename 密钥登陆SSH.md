# 使用密钥来登录SSH

## 生成密钥对

```shell
ssh-keygen -b 4096 -t rsa
```

SSH密钥现在应该位于`〜/ .ssh`中。您可以使用以下命令查看您的密钥文件：

```sh
ls ~/.ssh
```

你应该在这里看到2个文件：

* id_rsa.pub：公钥，服务器用。

* id_rsa：私钥，客户端用。

## 客户端配置

### 添加密钥到ssh-agent密钥管理器

添加私钥到客户机的ssh-agent密钥管理器

```shell
ssh-add ~/.ssh/id_rsa
```

如果添加出错，可能是`OpenSSH Authentication Agent`服务没启动

- Windows：服务管理启动服务

- Linux：

  ```shell
  eval `ssh-agent -s`
  ssh-add
  ```

其它命令

```shell
#查看ssh-agent中的密钥
ssh-add -l
#从ssh-agent中删除密钥
ssh-add -d ~/.ssh/id_rsa
#-D：删除ssh-agent中的所有密钥
```

### 配置密钥使用规则

在`~/.ssh`目录下新建一个`config`配置文件

编辑config文件,修改如下内容

```ini
# 例子
Host Raspberry
HostName ipORhostname
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
User pi
```

## 服务器配置

使用用户名密码通过SSH登录

进入**用户文件夹**（默认）

运行以下命令来创建`.ssh`文件夹和`authorized_keys`文件：

```sh
mkdir .ssh
cd .ssh
touch authorized_keys
chmod 700 ~/.ssh/
chmod 600 ~/.ssh/authorized_keys
```

注意：

* 文件权限必须设置为700和600

* authorized_keys文件是公钥，可以直接使用公钥改名，或者使用以下命令传输(Linux)

  ```shell
  cat ~/.ssh/id_rsa.pub | ssh -p 22 pi@192.168.1.2 'cat >>.ssh/authorized_keys'
  ```

## 测试

```shell
ssh -T user@host
```

## 使用Putty连接

putty使用的密钥格式与OpenSSH的格式不一样，所以我们要转换私钥为`.ppk`格式才能给putty使用

### 转换私钥

这里需要使用puttygen软件进行转换

1. 打开puttygen
2. Load入私钥
3. 点击Save private key 进行保存

### 连接

1. 打开putty
2. Session->Host Name输入主机地址
3. Connection->Data->Auto-login username输入自动登录的用户名
4. Connection->SSH->Auth->Private key file for authentication选择ppk密钥
5. 回到Session->Saved Sessions保存Session

## 设置仅允许密钥登录

确保你可以使用密钥登录成功。为了提高安全性，您可以从Raspberry Pi中删除密码身份验证。这将禁止通过SSH登录任何用户的密码。在禁用密码验证之前，使用密钥登录非常重要。

删除密码验证不是必需的，但会进一步提高安全性。如果您选择执行此步骤，请登录到Raspberry Pi并运行以下命令编辑SSH配置文件：

```shell
sudo nano /etc/ssh/sshd_config
```

找到行`'#PasswordAuthentication yes'`。我们需要通过删除＃然后将yes更改为no来取消注释。按下CTRL + O保存文件或CTRL + X关闭文件，然后按Y保存。

现在只需使用以下命令重新启动SSH服务：

```shell
sudo /etc/init.d/ssh restart
```

您现在应该可以使用SSH密钥登录到您的服务器。