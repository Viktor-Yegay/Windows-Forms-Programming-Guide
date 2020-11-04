# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System import *
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import List


class TestWindow(Form):
    def __init__(self):
        self._initialize_components()

        self.states = List[String](["Аргентина", "Бразилия", "Венесуэла", "Колумбия", "Чили"])

        # добавляем список элементов
        self.domainUpDown1.Items.AddRange(self.states)
        self.domainUpDown1.TextChanged += self.domainUpDown1_TextChanged

    # обработка изменения текста в элементе
    def domainUpDown1_TextChanged(self, sender, EventArgs):
        MessageBox.Show(self.domainUpDown1.Text)

    def _initialize_components(self):
        self.domainUpDown1 = DomainUpDown()
        # 
        # domainUpDown1
        # 
        self.domainUpDown1.Location = Point(65, 40)
        self.domainUpDown1.Name = "domainUpDown1"
        self.domainUpDown1.Size = Size(120, 20)
        self.domainUpDown1.Sorted = True
        self.domainUpDown1.TabIndex = 0
        self.domainUpDown1.Text = "domainUpDown1"
        self.domainUpDown1.Wrap = True
        # 
        # Form1
        # 
        self.ClientSize = Size(250, 100)
        self.Controls.Add(self.domainUpDown1)
        self.Name = "Form1"
        self.Text = "DomainUpDown"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
