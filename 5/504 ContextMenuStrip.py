# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
from System.Drawing import *
from System.Windows.Forms import *
# from System.Collections.Generic import List


class TestWindow(Form):
    def __init__(self):
        self._InitializeComponent()

        self.buffer = ''

        self.textBox1.Multiline = True
        self.textBox1.Dock = DockStyle.Fill

        # создаем элементы меню
        self.copyMenuItem = ToolStripMenuItem("Копировать")
        self.pasteMenuItem = ToolStripMenuItem("Вставить")
        # добавляем элементы в меню
        # self.contextMenuStrip1.Items.AddRange(List[ToolStripItem]([self.copyMenuItem, self.pasteMenuItem]))
        self.contextMenuStrip1.Items.Add(self.copyMenuItem)
        self.contextMenuStrip1.Items.Add(self.pasteMenuItem)
        # ассоциируем контекстное меню с текстовым полем
        self.textBox1.ContextMenuStrip = self.contextMenuStrip1
        # устанавливаем обработчики событий для меню
        self.copyMenuItem.Click += self.copyMenuItem_Click
        self.pasteMenuItem.Click += self.pasteMenuItem_Click
    # вставка текста
    def pasteMenuItem_Click(self, sender, EventArgs):
        self.textBox1.Paste(self.buffer)
    # копирование текста
    def copyMenuItem_Click(self, sender, EventArgs):
        # если выделен текст в текстовом поле, то копируем его в буфер
        self.buffer = self.textBox1.SelectedText

    def _InitializeComponent(self):
        self.components = System.ComponentModel.Container()
        self.contextMenuStrip1 = ContextMenuStrip(self.components)
        self.textBox1 = TextBox()
        # 
        # contextMenuStrip1
        # 
        self.contextMenuStrip1.Name = "contextMenuStrip1"
        self.contextMenuStrip1.Size = Size(61, 4)
        # 
        # textBox1
        # 
        self.textBox1.Location = Point(12, 58)
        self.textBox1.Multiline = True
        self.textBox1.Name = "textBox1"
        self.textBox1.Size = Size(100, 20)
        self.textBox1.TabIndex = 1
        # 
        # Form1
        # 
        self.Size = Size(448, 408)
        self.Controls.Add(self.textBox1)
        self.Name = "Form1"
        self.Text = "ContextMenuStrip"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
