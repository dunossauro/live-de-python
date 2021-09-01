from selenium import webdriver


def set_proxy(ip: str, port: int):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', ip)
    profile.set_preference('network.proxy.socks_port', port)
    profile.set_preference('network.proxy.socks_version', 5)
    profile.set_preference('network.proxy.socks_remote_dns', True)
    profile.update_preferences()
    return profile


driver = webdriver.Firefox(firefox_profile=set_proxy('127.0.0.1', 9050))
