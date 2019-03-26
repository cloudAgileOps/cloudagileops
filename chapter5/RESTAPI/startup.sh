#!/bin/bash


/usr/sbin/sshd -D &


python /work/restserver.py
