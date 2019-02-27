#!/bin/bash


/usr/sbin/sshd -D &


python /work/toDoListPro/manage.py runserver
