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

    def _InitializeComponent(self):
        self.imageList1 = ImageList()
        self.imageList1.Images.Add(Image.FromFile(r"F:\YandexDisk\BIM Planet No2\_test\IronMan32x32.png"))
        self.imageList1.Images.Add(Image.FromFile(r"F:\YandexDisk\BIM Planet No2\_test\CaptainAmerica32x32.png"))
        self.imageList1.Images.Add(Image.FromFile(r"F:\YandexDisk\Windows Forms Programming Guide\2\image.jpg"))
        self.checkBox1 = CheckBox()
        self.checkBox2 = CheckBox()
        self.checkBox3 = CheckBox()
        #
        # imageList1
        #
        self.imageList1.TransparentColor = Color.Transparent
        self.imageList1.Images.SetKeyName(0, "IronMan32x32.png")
        self.imageList1.Images.SetKeyName(1, "CaptainAmerica32x32.png")
        self.imageList1.Images.SetKeyName(2, "image.jpg")
        #
        # checkBox1
        #
        self.checkBox1.AutoSize = True
        self.checkBox1.ImageIndex = 0
        self.checkBox1.ImageList = self.imageList1
        self.checkBox1.Location = Point(30, 30)
        self.checkBox1.Name = "checkBox1"
        self.checkBox1.Size = Size(31, 16)
        self.checkBox1.TabIndex = 0
        self.checkBox1.UseVisualStyleBackColor = True
        #
        # checkBox2
        #
        self.checkBox2.AutoSize = True
        self.checkBox2.ImageIndex = 1
        self.checkBox2.ImageList = self.imageList1
        self.checkBox2.Location = Point(30, 60)
        self.checkBox2.Name = "checkBox2"
        self.checkBox2.Size = Size(31, 16)
        self.checkBox2.TabIndex = 1
        self.checkBox2.UseVisualStyleBackColor = True
        #
        # checkBox3
        #
        self.checkBox3.AutoSize = True
        self.checkBox3.ImageIndex = 2
        self.checkBox3.ImageList = self.imageList1
        self.checkBox3.Location = Point(30, 90)
        self.checkBox3.Name = "checkBox3"
        self.checkBox3.Size = Size(31, 16)
        self.checkBox3.TabIndex = 2
        self.checkBox3.UseVisualStyleBackColor = True
        #
        # Form1
        #
        self.ClientSize = Size(50, 150)
        self.Controls.Add(self.checkBox1)
        self.Controls.Add(self.checkBox2)
        self.Controls.Add(self.checkBox3)
        self.Name = "Form1"
        self.Text = "ImageList"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
