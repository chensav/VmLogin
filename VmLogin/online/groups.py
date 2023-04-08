def create_group(self, name: str = None, orderby: int = 0):
    """
    创建分组
    :param name: 分组名称
    :param orderby: 排序

    :return:
    """
    params = {
        'name': name,
        'orderby': orderby,
    }
    return self.query('/tag/create', params)


def remove_group(self, tag_id: str = None):
    """
    删除分组
    :param tag_id: 分组ID

    :return:
    """
    params = {
        'tagId': tag_id,
    }
    return self.query('/tag/remove', params)


def rename_group(self, name: str = None, tag_id: str = None, orderby: int = 0):
    """
    重命名分组
    :param name: 分组名称
    :param tag_id: 分组ID
    :param orderby: 排序
    """
    params = {
        'name': name,
        'tagId': tag_id,
        'orderby': orderby,
    }
    return self.query('/tag/rename', params)


def get_group_list(self):
    """
    获取分组列表
    :return:
    """
    return self.query('/tag/list')


def profile_bind_group(self, tag_id: str = None, profile_id: str = None):
    """
    绑定分组
    :param tag_id: 分组ID
    :param profile_id: 账号ID
    :return:
    """
    params = {
        'tagId': tag_id,
        'profileId': profile_id,
    }
    return self.query('/tag/profile/add', params)


def profile_unbind_group(self, tag_id: str = None, profile_id: str = None):
    """
    解绑分组
    :param tag_id: 分组ID
    :param profile_id: 账号ID
    :return:
    """
    params = {
        'tagId': tag_id,
        'profileId': profile_id,
    }
    return self.query('/tag/profile/remove', params)
