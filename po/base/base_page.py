import os
from pywinauto.application import Application
from pywinauto import mouse

os.path.abspath(".")


class Starter:
    def open(self,exe_path):
        app = Application(backend='uia').start(exe_path)
        win = app.window(found_index=1, top_level_only=False)
        return win

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver   
        
    # id定位
    def by_id(self, s_id, control_type=None):     
        return self.driver.child_window(auto_id=s_id, control_type=control_type)

    # class定位
    def child_window(self, **params):
        return self.driver.child_window(params)
    
    # 用鼠标点击坐标
    def mouse_click(self, x, y):
        mouse.click(coords=(x,y))
    
 
  