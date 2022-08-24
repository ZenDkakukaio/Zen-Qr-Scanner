from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from kivy.animation import Animation
from kivy.uix.image import Image as Imk

from controller.Scanner import MyScanner
import webbrowser
import re


import cv2
import numpy as np
from pyzbar.pyzbar import decode
import json

with open("media/media.json") as j:
    data = json.load(j)


obj_scanner = MyScanner()

class HomeApp(ScreenManager):

    data_logo = data["media1"]["1"]

    def __init__(self, **kwargs):
        super(HomeApp, self).__init__(**kwargs)
        self.link_decode = ""



    def scan(self):
        cap = cv2.VideoCapture(0)



        while True:

            ret, frame = cap.read()
            r = obj_scanner.decoder(frame)

            self.link_decode = str(r)
            pattern_https = re.search("https", self.link_decode)

            if pattern_https:
                webbrowser.open_new(self.link_decode)
                break



            else:
                print("Qr code non identifié...")





            cv2.imshow('ZEN SCANNER', frame)
            code = cv2.waitKey(10)
            if code == ord("q"):
                break



























