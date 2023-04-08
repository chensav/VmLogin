from VmLogin.local import Local

online = Local()
data = online.restart()
print(data)
