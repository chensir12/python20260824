"""
    该案例演示了面向对象的应用
"""

class 浏览器:
    def __init__(self):
        self.插件 = None
    def add_plugin(self,插件名):
        self.插件 = 插件名

f_browser = 浏览器()
f_browser.add_plugin("油猴")
print(f_browser.插件)