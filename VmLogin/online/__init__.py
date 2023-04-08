from VmLogin.api import API


class Online(API):
    def __init__(self, token: str = '', **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://api.vmlogin.com/v1"
        super().__init__(token, **kwargs)

    from VmLogin.online.groups import create_group
    from VmLogin.online.groups import remove_group
    from VmLogin.online.groups import rename_group
    from VmLogin.online.groups import get_group_list
    from VmLogin.online.groups import profile_bind_group
    from VmLogin.online.groups import profile_unbind_group

    from VmLogin.online.profiles import create_profile
    from VmLogin.online.profiles import remove_profile
    from VmLogin.online.profiles import get_profile_detail
    from VmLogin.online.profiles import update_profile
    from VmLogin.online.profiles import share_profile
    from VmLogin.online.profiles import cache_share_profile
    from VmLogin.online.profiles import transfer_profile
    from VmLogin.online.profiles import release_profile
    from VmLogin.online.profiles import get_profile_list
