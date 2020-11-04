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
        # установка начального адреса
        self.webBrowser1.Url = Uri("http://google.com")
        self.button1.Click += self.button1_Click

        # перейти к адресу в интернете
        #webBrowser1.Navigate("http:#google.com")
        # открыть документ на диске
        #webBrowser1.Navigate(@"F:\YandexDisk\Windows Forms Programming Guide\4\1.jpg")

    def button1_Click(self, sender, EventArgs):
        self.webBrowser1.Navigate(self.textBox1.Text)

    def _InitializeComponent(self):
        self.webBrowser1 = WebBrowser()
        self.textBox1 = TextBox()
        self.button1 = Button()
        #
        # webBrowser1
        #
        self.webBrowser1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right
        self.webBrowser1.Location = Point(12, 133)
        self.webBrowser1.MinimumSize = Size(20, 20)
        self.webBrowser1.Name = "webBrowser1"
        self.webBrowser1.Size = Size(224, 421)
        self.webBrowser1.TabIndex = 0
        #
        # textBox1
        #
        self.textBox1.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right
        self.textBox1.Location = Point(13, 13)
        self.textBox1.Name = "textBox1"
        self.textBox1.Size = Size(141, 20)
        self.textBox1.TabIndex = 1
        #
        # button1
        #
        self.button1.Anchor = AnchorStyles.Top | AnchorStyles.Right
        self.button1.Location = Point(160, 9)
        self.button1.Name = "button1"
        self.button1.Size = Size(75, 23)
        self.button1.TabIndex = 2
        self.button1.Text = "Перейти"
        self.button1.UseVisualStyleBackColor = True
        #
        # Form1
        #
        self.Size = Size(248, 566)
        self.Controls.Add(self.button1)
        self.Controls.Add(self.textBox1)
        self.Controls.Add(self.webBrowser1)
        self.Name = "Form1"
        self.Text = "WebBrowser"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
