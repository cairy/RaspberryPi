# 搭建git远程仓库

>  远程仓库使用bare git repository

## 什么是bare git repository？

> 英文原版：[What is a bare git repository?](http://www.saintsjd.com/2011/01/what-is-a-bare-git-repository/)

**使用该`git init`命令创建的存储库与使用`git init --bare`命令创建的存储库有什么区别？**

使用该`git init`命令创建的存储库称为工作目录。在存储库的顶级文件夹中，您会发现两件事：

1. 一个.git子文件夹，其中包含与您的存储库相关的所有修订版本历史记录
2. 工作树，或checked out的副本。

使用创建的存储库`git init --bare`称为裸存储库。它们的结构与工作目录略有不同。首先，它们不包含源代码的工作副本或checked out副本。其次，裸仓库将修订历史记录存储在根文件夹中，而不是.git子文件夹中。注意：裸存储库通常会使用`.git`后缀。

**应该使用哪一个？**

好了，使用`git init`创建工作存储库是为了... **work**。在这里，您将实际编辑，添加和删除文件以及使用`git commit`保存更改。如果是在开发电脑上开始项目，意味着会在其中添加，编辑和删除项目文件，请使用`git init`。注意：如果您是使用`git clone`了一个存储库，将会有一个带有.git后缀的**工作**存储库，里面将有工作文件的副本可以进行编辑。

使用`git init --bare`创建的裸仓库用于... **共享**。如果你是一个团队的开发人员合作，并需要一个地方来共享存储库的变化，那么你将要在一个集中的地方建立裸储存库，所有用户都可以push他们的文件变化（通常是容易的选择是[github.com](http://github.com/)） 。由于git是一种分布式版本控制系统，因此没有人可以直接在共享的集中式存储库中编辑文件。相反，开发人员将克隆共享的裸存储库，在其存储库的工作副本中进行本地更改，然后push回共享的裸存储库以使其他用户可以使用其更改。

因为没有人直接对共享裸仓库中的文件进行编辑，所以不需要工作树。实际上，当用户将代码推送到存储库时，工作树只会妨碍并引起冲突。这就是为什么存在裸存储库并且没有可用树的原因。

**总结一下**

我用`git init`或`git clone`创建工作目录，当我想要我本地的dev的机器的`myproject`项目中添加，修改和删除文件。

当我准备好了，使用`git push`分享我的local changes到`myproject.git`裸仓库（通常是类似[github.com](http://github.com/)的远程服务器上），这样其他开发人员可以访问我的local changes。

## 服务端搭建

```shell
mkdir repository-git
git init --bare repository-git/
chown -R git:git repository-git/
```

## 客户端配置

1. ssh密钥登录已配置
2. 设置本地仓库的remote:`ssh://user@host[:port]/bare-repository-path`
3. 推送