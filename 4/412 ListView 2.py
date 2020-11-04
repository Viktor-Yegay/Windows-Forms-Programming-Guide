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
        self.listViewItem1 = ListViewItem("Аргентина", 0)
        self.listViewItem2 = ListViewItem("Бразилия", 1)
        self.listViewItem3 = ListViewItem("Уругвай", 2)
        self.listView1 = ListView()
        self.imageList1 = ImageList()
        self.imageList1.Images.Add(Image.FromFile(r"F:\YandexDisk\Windows Forms Programming Guide\4\Аргентина.png"))
        self.imageList1.Images.Add(Image.FromFile(r"F:\YandexDisk\Windows Forms Programming Guide\4\Бразилия.png"))
        self.imageList1.Images.Add(Image.FromFile(r"F:\YandexDisk\Windows Forms Programming Guide\4\Уругвай.png"))
        # 
        # listView1
        # 
        self.listView1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right
        self.listView1.HideSelection = False
        self.listView1.Items.AddRange(System.Array[ListViewItem]([
            self.listViewItem1,
            self.listViewItem2,
            self.listViewItem3]))
        self.listView1.LargeImageList = self.imageList1
        self.listView1.Location = Point(12, 12)
        self.listView1.Name = "listView1"
        self.listView1.Size = Size(276, 276)
        self.listView1.SmallImageList = self.imageList1
        self.listView1.TabIndex = 0
        self.listView1.UseCompatibleStateImageBehavior = False
        # 
        # imageList1
        # 
        self.imageList1.TransparentColor = Color.Transparent
        self.imageList1.Images.SetKeyName(0, "Аргентина.png")
        self.imageList1.Images.SetKeyName(1, "Бразилия.png")
        self.imageList1.Images.SetKeyName(2, "Уругвай.png")
        # 
        # Form1
        # 
        self.ClientSize = Size(300, 300)
        self.Controls.Add(self.listView1)
        self.Name = "Form1"
        self.Text = "ListView"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
