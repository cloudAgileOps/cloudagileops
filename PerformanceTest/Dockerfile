# This file creates a container that runs Chrome, python and SSH services
# also the image include Django and selenium related dependency libraries,
# so it is base imge for selenium testing
#
# Author: James Wang
# Date: 02/26/2019
FROM centos

# MAINTAINER
MAINTAINER yuwang1974@hotmail.com


RUN yum -y install epel-release && \
    yum -y install which && \
    yum -y install wget && \
    yum -y install sudo && \
    yum -y install unzip && \
    yum -y install python-pip && \
    yum -y install net-tools && \
    yum -y install openssh-server 

RUN pip install --upgrade pip
RUN pip install django
RUN pip install locust



RUN ssh-keygen -t dsa  -P "" -f  /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -t rsa  -P "" -f  /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t ecdsa -P "" -f  /etc/ssh/ssh_host_ecdsa_key
RUN ssh-keygen -t ed25519  -P "" -f  /etc/ssh/ssh_host_ed25519_key

# password is test
RUN useradd -m test -p "VJdx0yi1Y3LKc"

COPY ./toDoListPro/ /work/toDoListPro

COPY startup.sh /

EXPOSE 22 8000

ENTRYPOINT "/startup.sh"





