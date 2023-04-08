def start(self, profile_id: str = None, skiplock: bool = False, block: bool = False):
    """
    启动配置
    :param profile_id: 浏览器配置文件ID
    :param skiplock: 跳过会话锁启动浏览器
    :param block: 接口将持续阻塞中, 直到浏览器进程创建成功后才返回结果 (for V1.3.7.7)
    :return:
    """
    params = {
        'profileId': profile_id,
        'skiplock': skiplock,
        'block': block,
    }
    return self.query('/profile/start', params)


def stop(self, profile_id: str = None, force: bool = False, block: bool = False):
    """
    启动配置
    :param profile_id: 浏览器配置文件ID
    :param force: 强制关闭浏览器 [移动仿真]建议为 true, 以免无法关闭浏览器
    :param block: 接口持续阻塞中, 直到浏览器进程结束 (for V1.3.7.7)
    :return:
    """
    params = {
        'profileId': profile_id,
        'force': force,
        'block': block,
    }
    return self.query('/profile/stop', params)


def refresh(self, profile_id: str = None):
    """
    刷新配置
    :param profile_id: 浏览器配置文件ID
    :return:
    """
    params = {
        'profileId': profile_id,
    }
    return self.query('/profile/refresh', params)


def open_url(self, profile_id: str = None, url: str = None):
    """
    打开网址
    :param profile_id: 浏览器配置文件ID
    :param url: 网址
    :return:
    """
    params = {
        'profileId': profile_id,
        'url': url,
    }
    return self.query('/profile/openurl', params)


def new_tab(self, profile_id: str = None, url: str = None):
    """
    新建标签页
    :param profile_id: 浏览器配置文件ID
    :param url: 网址
    :return:
    """
    params = {
        'profileId': profile_id,
        'url': url,
    }
    return self.query('/profile/newtab', params)


def source(self, profile_id: str = None):
    """
    获取配置源码
    :param profile_id: 浏览器配置文件ID
    :return:
    """
    params = {
        'profileId': profile_id,
    }
    return self.query('/profile/source', params)


def find_element(self, profile_id: str = None, function: str = None, args: str = None, click: bool = False,
                 index: int = 0):
    """
    查找元素
    :param profile_id: 浏览器配置文件ID
    :param function: 查找元素的函数名
    :param args: 参数为 function函数的传参，如：findElementByID(args)
    :param click: 找到指定元素后是否点击操作 true:点击 false:不点击
    :param index: 元素有多个时，指定点击第几个元素。从0开始，-1 为随机元素其中一个，配合 click = true 时使用
    :return:

    """
    params = {
        'profileId': profile_id,
        'function': function,
        'args': args,
        'click': click,
        'index': index,
    }
    return self.query('/profile/findElement', params)


def get_attribute(self, profile_id: str = None, args: str = None):
    """
    获取元素属性
    :param profile_id: 浏览器配置文件ID
    :param args: 一般是通过findElement查找元素后得到的Element_ID结合成的JSON串。如：[{“ELEMENT”: “95365abe-6746-4703-8cfd-6316580f5289”, “element-6066-11e4-a52e-4f735466cecf”: “95365abe-6746-4703-8cfd-6316580f5289”}, “value”] 这个就是取 95365abe-6746-4703-8cfd-6316580f5289 元素的 value 值。
    :return:
    """
    params = {
        'profileId': profile_id,
        'args': args,
    }
    return self.query('/profile/getAttribute', params)


def send_keys(self, profile_id: str = None, element_id: str = None, value: str = None):
    """
    发送文字到网页中

    :param profile_id: 浏览器配置文件ID
    :param element_id: 通过findElement查找元素后得到的elementId
    :param value: 向这个网页控件中发送字符串（ Enter Escape Tab vkLeft vkUp vkRight vkDown vkDelete vkEnd vkHome vkBack）
    :return:
    """
    params = {
        'profileId': profile_id,
        'elementId': element_id,
        'value': value,
    }
    return self.query('/profile/sendKeys', params)


def active(self, profile_id: str = None, active: bool = True):
    """
    检查配置文件是否正在运行

    :param profile_id: 浏览器配置文件ID
    :param active: true: 激活当前配置浏览器到最前面 false: 默认
    :return:
    """
    params = {
        'profileId': profile_id,
        'active': active,
    }
    return self.query('/profile/active', params)


def random_profile(self, platform: str = None, lang_hdr: str = None, accept_language: str = None,
                   time_zone: str = None):
    """
    随机获取配置信息

    :param platform: 平台类型 Windows Linux Macintosh Android iPhone Chrome Firefox Edge
    :param lang_hdr: 语言 en-US
    :param accept_language: 语言 en-US,en;q=0.9
    :param time_zone: 时区 America/New_York
    :return:
    """
    params = {
        'platform': platform,
        'langHdr': lang_hdr,
        'acceptLanguage': accept_language,
        'timeZone': time_zone,
    }
    return self.query('/profile/randomProfile', params)


def delete(self, profile_id: str = None):
    """
    删除一个配置文件本地临时文件夹

    :param profile_id: 浏览器配置文件ID
    :return:
    """
    params = {
        'profileId': profile_id,
    }
    return self.query('/profile/delete', params)


def cookie_export(self, profile_id: str = None):
    """
    从配置文件导出cookie

    :param profile_id: 浏览器配置文件ID
    :return:
    """
    params = {
        'profileId': profile_id,
    }
    return self.query('/profile/cookies/export/webext', params)


def cookie_import(self, profile_id: str = None, body: str = None):
    """
    将cookie导入配置文件浏览器

    :param profile_id: 浏览器配置文件ID
    :param body: cookie json (need base64 encode )
    :return:
    """
    params = {
        'profileId': profile_id,
        'body': body,
    }
    return self.send_request('POST', '/profile/cookies/import/webext', params)


def execute_script(self, profile_id: str = None, body: str = None):
    """
    执行js脚本

    :param profile_id: 浏览器配置文件ID
    :param body: js code (need base64 encode )
    :return:
    """
    params = {
        'profileId': profile_id,
        'body': body,
    }
    return self.send_request('POST', '/profile/ExecuteScript', params)


def screen_shot(self, profile_id: str = None, body: str = None):
    """
    截图

    :param profile_id: 浏览器配置文件ID
    :param body: 图片的本机绝对路径地址 (need base64 encode )
    :return:
    """
    params = {
        'profileId': profile_id,
        'body': body,
    }
    return self.send_request('POST', '/profile/ScreenShot', params)


def get_cookies(self, profile_id: str = None, all: int = 0):
    """
    获取配置文件的cookie

    :param profile_id: 浏览器配置文件ID
    :param all: 0: No:0 Yes:1
    :return:
    """
    params = {
        'profileId': profile_id,
        'all': all,
    }
    return self.send_request('POST', '/profile/getCookies', params)


def ready_state(self, profile_id: str = None):
    """
    询问当前页面也没有加载完成(

    :param profile_id: 浏览器配置文件ID
    :return:
    """
    params = {
        'profileId': profile_id,
    }
    return self.send_request('POST', '/profile/readyState', params)


def switch_frame(self, profile_id: str = None, args: str = None):
    """
    切换到指定的frame

    :param profile_id: 浏览器配置文件ID
    :param args:FrameName（支持base64编码）
    :return:
    """
    params = {
        'profileId': profile_id,
        'args': args,
    }
    return self.query('/profile/SwitchToFrame', params)


def switch_tab(self, profile_id: str = None, id: str = None):
    """
    切换到指定的tab

    :param profile_id: 浏览器配置文件ID
    :param id: /profile/start 返回的地址和端口（value）拼接/json（例如：http://127.0.0.1:18500/json）返回的tab列表（json）中的id 字段
    :return:
    """
    params = {
        'profileId': profile_id,
        'id': id,
    }
    return self.query('/profile/bringToFront', params)


def close_tab(self, profile_id: str = None, id: str = None):
    """
    关闭指定的tab

    :param profile_id: 浏览器配置文件ID
    :param id: /profile/start 返回的地址和端口（value）拼接/json（例如：http://
    :return:
    """
    params = {
        'profileId': profile_id,
        'id': id,
    }
    return self.query('/profile/page/close', params)


def password_manager_leak_detection(self, profile_id: str = None, enable: bool = False):
    """
    密码泄露检测

    :param profile_id: 浏览器配置文件ID
    :param body: 关闭:false 开启:true 默认关闭
    :return:
    """
    params = {
        'profileId': profile_id,
        'enable': enable,
    }
    return self.send_request('POST', '/profile/browser/password_manager_leak_detection', params)


def proxy_test(self, proxy_type: str = None, proxy_server: str = None, proxy_port: str = None, **kwargs):
    """
    代理测试

    :param proxy_type: 代理类型 http socks5
    :param proxy_server: 代理服务器地址
    :param proxy_port: 代理服务器端口
    :kwarg proxy_username: 代理服务器用户名
    :kwarg proxy_password: 代理服务器密码
    :kwarg timeout: 超时时间
    :kwarg urlindex: 代理测试网址选项 0 = lumtest 1 = vmlogin 2 = ip-api.com
    :return:
    """
    params = {
        'proxyType': proxy_type,
        'proxyServer': proxy_server,
        'proxyPort': proxy_port,
        'proxyUsername': kwargs.get('proxy_username', None),
        'proxyPassword': kwargs.get('proxy_password', None),
        'timeout': kwargs.get('timeout', 10),
        'urlindex': kwargs.get('urlindex', 0),
    }
    return self.query('/proxy/test', params)


def restart(self):
    """
    重启服务

    :return:
    """
    return self.query('/client/restart')
