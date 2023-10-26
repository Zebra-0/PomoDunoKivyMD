from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp

class HotReaload(MDApp):
    KV_FILES = [r'app/pomodoro.kv']
    DEBUG = True
    def build_app(self):
        return Builder.load_file(r'app/pomodoro.kv')


HotReaload().run()
