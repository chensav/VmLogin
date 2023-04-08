from VmLogin.api import API


class Local(API):
    def __init__(self, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "http://127.0.0.1:35000/api/v1"
        super().__init__('', **kwargs)

    from VmLogin.local.browser import start
    from VmLogin.local.browser import stop
    from VmLogin.local.browser import refresh
    from VmLogin.local.browser import open_url
    from VmLogin.local.browser import new_tab
    from VmLogin.local.browser import source
    from VmLogin.local.browser import find_element
    from VmLogin.local.browser import get_attribute
    from VmLogin.local.browser import send_keys
    from VmLogin.local.browser import active
    from VmLogin.local.browser import random_profile
    from VmLogin.local.browser import delete
    from VmLogin.local.browser import cookie_export
    from VmLogin.local.browser import cookie_import
    from VmLogin.local.browser import execute_script
    from VmLogin.local.browser import screen_shot
    from VmLogin.local.browser import get_cookies
    from VmLogin.local.browser import ready_state
    from VmLogin.local.browser import switch_frame
    from VmLogin.local.browser import switch_tab
    from VmLogin.local.browser import close_tab
    from VmLogin.local.browser import password_manager_leak_detection
    from VmLogin.local.browser import proxy_test
    from VmLogin.local.browser import restart
