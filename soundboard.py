

import requests
from PyQt5 import QtWidgets, uic, QtCore
import sys

from gui.main import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, secret, url="http://127.0.0.1:3000", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.secret = secret
        self.url = url

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.dorf.pressed.connect(self.play_dorf)
        self.ui.wald.pressed.connect(self.play_wald)
        self.ui.schmiede.pressed.connect(self.play_schmiede)
        self.ui.tempel.pressed.connect(self.play_tempel)
        self.ui.hoele.pressed.connect(self.play_hoele)
        self.ui.taverne.pressed.connect(self.play_taverne)
        self.ui.kampf.pressed.connect(self.play_kampf)
        self.ui.wald_nachts.pressed.connect(self.play_wald_nachts)

    def play_dorf(self):
        self.play("https://www.youtube.com/watch?v=Wd3kd0zY2bQ")

    def play_kampf(self):
        self.play("https://www.youtube.com/watch?v=ELbwc7r4MUo")

    def play_wald_nachts(self):
        self.play("https://www.youtube.com/watch?v=ybTXj_OE4-k")

    def play_wald(self):
        self.play("https://www.youtube.com/watch?v=HAw37tUHcOo")

    def play_schmiede(self):
        self.play("https://www.youtube.com/watch?v=pRkFl9j3NLk")

    def play_tempel(self):
        self.play("https://www.youtube.com/watch?v=bD4L0j5SrFM")

    def play_hoele(self):
        self.play("https://www.youtube.com/watch?v=QTj6EFaz1Es")

    def play_taverne(self):
        self.play("https://www.youtube.com/watch?v=KecVJnJcSI4")



    def play(self, stream_url="https://www.youtube.com/watch?v=pRkFl9j3NLk&list=PLbHUA-o_5dgJbOXwtdVx--gTnmWfiyyys&index=54"):
        command = f"play {stream_url}"
        payload = {'command': command, 'secret': self.secret}
        r = requests.post(f"{self.url}/v1/do", json=payload)
        print(r.content)
