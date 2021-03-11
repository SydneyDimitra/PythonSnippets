"""Simple UI with 2 buttons."""
from PyQt4 import QtGui


class TwoButtonWindow(QtGui.QDialog):
    """Main class for UI launched from button"""
    def __init__(self, parent=None):
        """Initialise the UI.

        Args:
            parent (QtCore.QObject): Object to parent the dialog to.
        """
        super(TwoButtonWindow, self).__init__(parent=parent)
        self._setup_widgets()
        self._layout_widgets()
        self._connect_signals()
        self.selected_tag = None
        self.setWindowTitle("Visibility")

    def _setup_widgets(self):
        """Setup the widgets."""
        self.window_message = QtGui.QLabel("Turn visibility")

        self.turn_visibility_on = QtGui.QPushButton('ON')
        self.turn_visibility_off = QtGui.QPushButton('OFF')

    def _layout_widgets(self):
        """Lay out the widgets."""
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.addWidget(self.window_message)

        self.hbox_layout_buttons = QtGui.QHBoxLayout()
        self.main_layout.addLayout(self.hbox_layout_buttons)

        self.hbox_layout_buttons.addStretch()
        self.hbox_layout_buttons.addWidget(self.turn_visibility_on)
        self.hbox_layout_buttons.addWidget(self.turn_visibility_off)

        self.setLayout(self.main_layout)

    def _connect_signals(self):
        """Connect the signals."""
        self.turn_visibility_on.clicked.connect(self.visibility_on)

        self.turn_visibility_off.clicked.connect(self.visibility_off)

    def visibility_on(self):
        """Turn visibility on."""
        print "ON"

    def visibility_off(self):
        """Turn visibility off."""
        print "OFF"


def test_window():
    app = QtGui.QApplication([])
    window = TwoButtonWindow()
    window.show()
    app.exec_()


test_window()
