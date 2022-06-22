from ui.compiled.everycloud_ui import Ui_EveryCloud
from window_styles.frameless import Frameless
from window_styles.draggable import Draggable


class EveryCloud(Ui_EveryCloud, Draggable, Frameless):
    def __init__(self, parent=None):
        super(EveryCloud, self).__init__(parent)
        self.setup_flags(self)
        self.setupUi(self)
