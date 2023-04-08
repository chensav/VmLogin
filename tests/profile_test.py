from VmLogin.online import Online

local = Online('')
body = {
    "name": "test1"
}
data = local.create_profile(body)
print(data)
profile_id = data['value']

data = local.update_profile(profile_id, body)
print(data)

data = local.get_profile_detail(profile_id)
print(data)

data = local.share_profile(profile_id, 'chensav@163.com')
print(data)

data = local.cache_share_profile(profile_id, 'chensav@163.com')
print(data)

data = local.transfer_profile(profile_id, 'chensav@163.com')
print(data)

data = local.release_profile(profile_id)
print(data)

data = local.remove_profile(profile_id)
print(data)

data = local.remove_profile(profile_id)
print(data)
