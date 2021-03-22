import os
import sys

import hydra
from PyQt5 import QtWidgets
from omegaconf import DictConfig, OmegaConf

from soundboard import MainWindow

@hydra.main(config_name="./config/main.yaml")
def run(cfg: DictConfig):

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow(cfg["token"])
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()