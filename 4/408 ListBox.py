# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
from System.Drawing import *
from System.Windows.Forms import *
from System.Collections.Generic import List


class TestWindow(Form):
    def __init__(self):
        self._initialize_components()

        self.phones = List[Phone]([
            Phone(Id=11, Name="Samsung Galaxy Ace 2", Year=2012),
            Phone(Id=12, Name="Samsung Galaxy S4", Year=2013),
            Phone(Id=13, Name="iPhone 6", Year=2014),
            Phone(Id=14, Name="Microsoft Lumia 435", Year=2015),
            Phone(Id=15, Name="Xiaomi Mi 5", Year=2015)
        ])

        self.listBox1.DataSource = self.phones
        self.listBox1.DisplayMember = "Name"
        self.listBox1.ValueMember = "Id"

        self.listBox1.SelectedIndexChanged += self.listBox1_SelectedIndexChanged

    def listBox1_SelectedIndexChanged(self, sender, EventArgs):
        # получаем id выделенного объекта
        id = int(self.listBox1.SelectedValue)

        # получаем весь выделенный объект
        phone = self.listBox1.SelectedItem
        MessageBox.Show(id.ToString() + ". " + phone.Name)

    def _initialize_components(self):
        self.listBox1 = ListBox()
        #
        # listBox1
        #
        self.listBox1.FormattingEnabled = True
        self.listBox1.Location = Point(38, 52)
        self.listBox1.Name = "listBox1"
        self.listBox1.Size = Size(120, 95)
        self.listBox1.TabIndex = 0
        #
        # Form1
        #
        self.Size = Size(416, 479)
        self.Controls.Add(self.listBox1)
        self.Name = "Form1"
        self.Text = "ListBox"


class Phone(object):
    def __init__(self, Id, Name, Year):
        self._Id = Id
        self._Name = Name
        self._Year = Year

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, value):
        self._Id = value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value

    @property
    def Year(self):
        return self._Year

    @Year.setter
    def Year(self, value):
        self._Year = value


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
