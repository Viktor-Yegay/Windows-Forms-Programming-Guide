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
        self.nameBox.Validating += self.nameBox_Validating
        self.ageBox.Validating += self.ageBox_Validating

    def nameBox_Validating(self, sender, CancelEventArgs):
        if System.String.IsNullOrEmpty(self.nameBox.Text):
            self.errorProvider1.SetError(self.nameBox, "Не указано имя!")
        elif self.nameBox.Text.Length < 4:
            self.errorProvider1.SetError(self.nameBox, "Слишком короткое имя!")
        else:
            self.errorProvider1.Clear()

    def ageBox_Validating(self, sender, CancelEventArgs):
        # age = 0
        if System.String.IsNullOrEmpty(self.ageBox.Text):
            self.errorProvider1.SetError(self.ageBox, "Не указан возраст!")
        # elif not System.Int32.TryParse(self.ageBox.Text, age):
        elif not self.ageBox.Text.isdigit():
            self.errorProvider1.SetError(self.ageBox, "Некорретный возраст!")
        else:
            self.errorProvider1.Clear()

    def _InitializeComponent(self):
        self.components = System.ComponentModel.Container()
        self.label1 = Label()
        self.label2 = Label()
        self.nameBox = TextBox()
        self.ageBox = TextBox()
        self.errorProvider1 = ErrorProvider(self.components)
        #
        # label1
        #
        self.label1.AutoSize = True
        self.label1.Location = Point(26, 38)
        self.label1.Name = "label1"
        self.label1.Size = Size(72, 13)
        self.label1.TabIndex = 0
        self.label1.Text = "Введите имя"
        #
        # label2
        #
        self.label2.AutoSize = True
        self.label2.Location = Point(26, 94)
        self.label2.Name = "label2"
        self.label2.Size = Size(93, 13)
        self.label2.TabIndex = 0
        self.label2.Text = "Введите возраст"
        #
        # nameBox
        #
        self.nameBox.Location = Point(29, 55)
        self.nameBox.Name = "nameBox"
        self.nameBox.Size = Size(171, 20)
        self.nameBox.TabIndex = 1
        #
        # ageBox
        #
        self.ageBox.Location = Point(29, 110)
        self.ageBox.Name = "ageBox"
        self.ageBox.Size = Size(171, 20)
        self.ageBox.TabIndex = 1
        #
        # errorProvider1
        #
        self.errorProvider1.ContainerControl = self
        #
        # Form1
        #
        self.Size = Size(283, 182)
        self.Controls.Add(self.ageBox)
        self.Controls.Add(self.nameBox)
        self.Controls.Add(self.label2)
        self.Controls.Add(self.label1)
        self.Name = "Form1"
        self.Text = "ErrorProvider"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
