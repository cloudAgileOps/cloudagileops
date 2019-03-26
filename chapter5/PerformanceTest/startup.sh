#!/bin/bash


/usr/sbin/sshd -D &


python /work/toDoListPro/manage.py runserver 0.0.0.0:8000
