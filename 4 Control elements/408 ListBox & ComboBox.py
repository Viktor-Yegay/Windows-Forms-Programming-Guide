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

        self.comboBox1.DataSource = self.phones
        self.comboBox1.DisplayMember = "Name"
        self.comboBox1.ValueMember = "Id"

        self.comboBox1.SelectedIndexChanged += self.comboBox1_SelectedIndexChanged

        self.listBox1.DisplayMember = "Name"
        self.listBox1.ValueMember = "Id"

    def comboBox1_SelectedIndexChanged(self, sender, EventArgs):
        self.phone = self.comboBox1.SelectedItem
        self.listBox1.Items.Add(self.phone)

    def _initialize_components(self):
        self.listBox1 = ListBox()
        self.comboBox1 = ComboBox()
        # 
        # listBox1
        # 
        self.listBox1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right
        self.listBox1.FormattingEnabled = True
        self.listBox1.Location = Point(12, 39)
        self.listBox1.Name = "listBox1"
        self.listBox1.Size = Size(246, 225)
        self.listBox1.TabIndex = 0
        # 
        # comboBox1
        # 
        self.comboBox1.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right
        self.comboBox1.FormattingEnabled = True
        self.comboBox1.Location = Point(12, 12)
        self.comboBox1.Name = "comboBox1"
        self.comboBox1.Size = Size(246, 21)
        self.comboBox1.TabIndex = 1
        # 
        # Form1
        # 
        self.ClientSize = Size(270, 285)
        self.Controls.Add(self.comboBox1)
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
