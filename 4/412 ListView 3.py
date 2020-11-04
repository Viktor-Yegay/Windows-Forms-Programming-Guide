# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
from System.Drawing import *
from System.Windows.Forms import *
from System.IO import *


class TestWindow(Form):
    def __init__(self):
        self._InitializeComponent()

        self.listView1.SmallImageList = self.imageList1

    def button1_Click(self, sender, EventArgs):
        path = self.textBox1.Text
        # получаем все файлы
        files = Directory.GetFiles(path)
        # перебор полученных файлов
        for file in files:
            lvi = ListViewItem()
            # установка названия файла
            lvi.Text = file.Remove(0, file.LastIndexOf('\\') + 1)
            lvi.ImageIndex = 0 # установка картинки для файла
            # добавляем элемент в ListView
            self.listView1.Items.Add(lvi)

    def _InitializeComponent(self):
        self.textBox1 = TextBox()
        self.button1 = Button()
        self.listView1 = ListView()
        self.imageList1 = ImageList()
        self.imageList1.Images.Add(Image.FromFile(r"F:\YandexDisk\Windows Forms Programming Guide\4\Аргентина.png"))
        # 
        # textBox1
        # 
        self.textBox1.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right
        self.textBox1.Location = Point(12, 12)
        self.textBox1.Name = "textBox1"
        self.textBox1.Size = Size(195, 20)
        self.textBox1.TabIndex = 0
        # 
        # button1
        # 
        self.button1.Anchor = AnchorStyles.Top | AnchorStyles.Right
        self.button1.Location = Point(213, 12)
        self.button1.Name = "button1"
        self.button1.Size = Size(75, 20)
        self.button1.TabIndex = 1
        self.button1.Text = "Показать"
        self.button1.UseVisualStyleBackColor = True
        self.button1.Click += System.EventHandler(self.button1_Click)
        # 
        # listView1
        # 
        self.listView1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right
        self.listView1.HideSelection = False
        self.listView1.Location = Point(12, 38)
        self.listView1.Name = "listView1"
        self.listView1.Size = Size(276, 250)
        self.listView1.TabIndex = 2
        self.listView1.UseCompatibleStateImageBehavior = False
        self.listView1.View = View.SmallIcon
        # 
        # imageList1
        # 
        self.imageList1.TransparentColor = System.Drawing.Color.Transparent
        self.imageList1.Images.SetKeyName(0, "Аргентина.png")
        # 
        # Form1
        # 
        self.ClientSize = Size(300, 300)
        self.Controls.Add(self.listView1)
        self.Controls.Add(self.button1)
        self.Controls.Add(self.textBox1)
        self.Name = "Form1"
        self.Text = "ListView"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
