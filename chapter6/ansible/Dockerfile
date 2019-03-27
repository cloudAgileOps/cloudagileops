# This file creates a container that runs Centos with ssh enabled
# also the image is for ansible demo
#
# Author: James Wang
# Date: 03/27/2019

# 从基础镜像centos继承
FROM centos

# 维护者的邮件地址
MAINTAINER yuwang1974@hotmail.com


# 安装基本的工具和sshd
RUN yum -y install epel-release && \
    yum -y install which && \
    yum -y install wget && \
    yum -y install sudo && \
    yum -y install unzip && \
    yum -y install net-tools && \
    yum -y install openssh-server


# 为sshd产生key
RUN ssh-keygen -t dsa  -P "" -f  /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -t rsa  -P "" -f  /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t ecdsa -P "" -f  /etc/ssh/ssh_host_ecdsa_key
RUN ssh-keygen -t ed25519  -P "" -f  /etc/ssh/ssh_host_ed25519_key


# 添加用户test, 并将密码设置为test
RUN useradd -m test -p "VJdx0yi1Y3LKc"

# 将用户test增加到组wheel中
RUN usermod -a -G wheel test

# 改变组wheel的属性，使其支持免密码sudo
RUN sed -i 's/# %wheel/%wheel/' /etc/sudoers

# 复制启动脚本到容器
COPY startup.sh /


# 修改脚本为可执行权限
RUN chmod u+x /startup.sh

# 设置容器启动时的命令
ENTRYPOINT "/startup.sh"
