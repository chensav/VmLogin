from VmLogin.online import Online

online = Online(token="")

data = online.create_group("test")
print(data)
