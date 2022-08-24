from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder


from controller.home import HomeApp



import json
with open("media/media.json") as j:
    data = json.load(j)



class MyApp(MDApp):
    def build(self):
        self.title = "ZEN QR SCANNER"
        self.icon = data["media1"]["1"]
        self.theme_cls.theme_style = "Light"
        self.load_all_file_kv()

        return HomeApp()




    def load_all_file_kv(self):
        Builder.load_file("view/home.kv")





if __name__ ==   "__main__":
   obj = MyApp()
   obj.run()