def create_profile(self, body: object = None):
    """
    创建
    :return:
    """
    params = {
        "Body": body,
    }
    return self.send_request('POST', '/profile/create', params)


def update_profile(self, profile_id: str = None, body: object = None):
    """
    更新配置

    :param profile_id: 配置ID
    :param body: 账号信息
    :return:
    """
    params = {
        'profileId': profile_id,
        'Body': body,
    }
    return self.query('/profile/update', params)


def get_profile_detail(self, profile_id: str = None):
    """
    获取配置详情
    :param profile_id: 配置ID
    :return:

    """
    params = {
        'profileId': profile_id,
    }
    return self.query('/profile/detail', params)


def share_profile(self, profile_id: str = None, account: str = ''):
    """
    分享配置
    :param profile_id: 浏览器配置文件ID（多条以,拼接
    :param account: 用户名
    :return:
    """
    params = {
        'profileId': profile_id,
        'account': account,
    }
    return self.query('/profile/share', params)


def cache_share_profile(self, profile_id: str = None, account: str = ''):
    """
    分享配置
    :param profile_id: 浏览器配置文件ID（多条以,拼接
    :param account: 用户名
    :return:
    """
    params = {
        'profileId': profile_id,
        'account': account,
    }
    return self.query('/profile/cancelShare', params)


def transfer_profile(self, profile_id: str = None, account: str = ''):
    """
    转移配置
    :param profile_id: 浏览器配置文件ID（多条以,拼接
    :param account: 用户名
    :return:
    """
    params = {
        'profileId': profile_id,
        'account': account,
    }
    return self.query('/profile/transferOwnership', params)


def release_profile(self, profile_id: str = None):
    """
    释放配置
    :param profile_id: 浏览器配置文件ID（多条以,拼接
    :return:
    """
    params = {
        'profileId': profile_id,
    }
    return self.query('/profile/release', params)


def remove_profile(self, profile_id: str = None):
    """
    删除
    :param profile_id: 浏览器配置文件ID（多条以,拼接）
    :return:
    """
    params = {
        'profileId': profile_id,
    }
    return self.query('/profile/remove', params)


def get_profile_list(self, search: str = None, tag: str = None, format: str = None, page: str = None, limit: str = 10):
    """
    获取配置列表
    :param search: 搜索关键字
    :param tag: 分组
    :param format: “1”: 将返回值unix时间戳格式化输出
    :param page: 分页页码
    :param limit: 每页显示多少条记录, 默认500, 最大1000
    :return:
    """
    params = {
        'search': search,
        'tag': tag,
        'format': format,
        'page': page,
        'limit': limit,
    }
    return self.query('/profile/list', params)
