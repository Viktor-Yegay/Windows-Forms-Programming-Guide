# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
from System.Drawing import *
from System.Windows.Forms import *


class TestWindow(Form):
    def __init__(self):
        self._InitializeComponent()
        self.ShowInTaskbar = False
        self.notifyIcon1.Click += self.notifyIcon1_Click

        # задаем иконку всплывающей подсказки
        self.notifyIcon1.BalloonTipIcon = ToolTipIcon.Info
        # задаем текст подсказки
        self.notifyIcon1.BalloonTipText = "Нажмите, чтобы отобразить окно"
        # устанавливаем зголовк
        self.notifyIcon1.BalloonTipTitle = "Подсказка"
        # отображаем подсказку 12 секунд
        self.notifyIcon1.ShowBalloonTip(12)

    def notifyIcon1_Click(self, sender, EventArgs):
        self.WindowState = FormWindowState.Normal

    def _InitializeComponent(self):
        self.components = System.ComponentModel.Container()
        self.notifyIcon1 = NotifyIcon(self.components)
        #
        # notifyIcon1
        #
        self.notifyIcon1.Icon = Icon(r"F:\YandexDisk\Windows Forms Programming Guide\4\api_interface_icon.ico")
        self.notifyIcon1.Text = "Show form"
        self.notifyIcon1.Visible = True
        #
        # Form1
        #
        self.Size = Size(248, 566)
        self.Name = "Form1"
        self.Text = "NotifyIcon"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
