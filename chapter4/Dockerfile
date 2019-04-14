# This file creates a container that runs Chrome, python and SSH services
# also the image include Django and selenium related dependency libraries,
# so it is base imge for selenium testing
#
# Author: Xavier 
# Date: 04/10/2019
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
    yum -y install openssh-server  && \
    yum -y install Xvfb && \
    yum -y install libXfont && \
    yum -y install xorg-x11-fonts*

RUN pip install --upgrade pip
RUN pip install Django
RUN pip install selenium
RUN pip install locust

RUN yum -y install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

RUN wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN chmod u+w /usr/bin

RUN cp chromedriver /usr/bin

RUN ssh-keygen -t dsa  -P "" -f  /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -t rsa  -P "" -f  /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t ecdsa -P "" -f  /etc/ssh/ssh_host_ecdsa_key
RUN ssh-keygen -t ed25519  -P "" -f  /etc/ssh/ssh_host_ed25519_key

# password is test
RUN useradd -m test -p "VJdx0yi1Y3LKc"

COPY ./toDoListPro/ /work/toDoListPro

EXPOSE 22 8000






