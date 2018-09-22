# -*- coding: UTF-8 -*-


import re

uname = ""
unameReg = re.compile(r"^\w.*")
passwd = ""
passwdReg = re.compile(r"^\w.*[_\*#]+.*")

while not uname:
    tmpUname = input("input a username:\n")
    if unameReg.match(tmpUname):
        uname = tmpUname

while not passwd:
    tmpPasswd = input("input a password:\n")
    if len(tmpPasswd) >= 6 and passwdReg.match(tmpPasswd):
        passwd = tmpPasswd

print("create success username: [ %s ] password [ %s ]" % (uname, passwd))
