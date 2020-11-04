# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System import *
from System.Drawing import *
from System.Windows.Forms import *


class TestWindow(Form):
    def __init__(self):
        self._InitializeComponent()

    def _InitializeComponent(self):
        self.pictureBox1 = PictureBox()
        #
        # pictureBox1
        #
        self.pictureBox1.Dock = DockStyle.Fill
        self.pictureBox1.Image = Image.FromFile(r"F:\YandexDisk\Windows Forms Programming Guide\4\1.jpg")
        self.pictureBox1.Location = Point(0, 0)
        self.pictureBox1.Name = "pictureBox1"
        self.pictureBox1.Size = Size(292, 452)
        self.pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage
        self.pictureBox1.TabIndex = 0
        self.pictureBox1.TabStop = False
        #
        # Form1
        #
        self.Size = Size(292, 452)
        self.Controls.Add(self.pictureBox1)
        self.Name = "Form1"
        self.Text = "PictureBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
