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
        self.button1.Click += self.button1_Click
        self.button2.Click += self.button2_Click
        self.openFileDialog1.Filter = "Text files(*.txt)|*.txt|All files(*.*)|*.*"
        self.saveFileDialog1.Filter = "Text files(*.txt)|*.txt|All files(*.*)|*.*"

    # сохранение файла
    def button2_Click(self, sender, EventArgs):
        if self.saveFileDialog1.ShowDialog() == DialogResult.Cancel:
            return
        # получаем выбранный файл
        self.filename = self.saveFileDialog1.FileName
        # сохраняем текст в файл
        System.IO.File.WriteAllText(self.filename, self.textBox1.Text)
        MessageBox.Show("Файл сохранен")

    # открытие файла
    def button1_Click(self, sender, EventArgs):
        if self.openFileDialog1.ShowDialog() == DialogResult.Cancel:
            return
        # получаем выбранный файл
        self.filename = self.openFileDialog1.FileName
        # читаем файл в строку
        fileText = System.IO.File.ReadAllText(self.filename)
        self.textBox1.Text = fileText
        MessageBox.Show("Файл открыт")

    def _InitializeComponent(self):
        self.button1 = Button()
        self.button2 = Button()
        self.textBox1 = TextBox()
        self.openFileDialog1 = OpenFileDialog()
        self.saveFileDialog1 = SaveFileDialog()
        #
        # button1
        #
        self.button1.Anchor = AnchorStyles.Bottom | AnchorStyles.Left
        self.button1.Location = Point(12, 189)
        self.button1.Name = "button1"
        self.button1.Size = Size(75, 23)
        self.button1.TabIndex = 0
        self.button1.Text = "Open"
        self.button1.UseVisualStyleBackColor = True
        self.button1.Click += self.button1_Click
        #
        # button2
        #
        self.button2.Anchor = AnchorStyles.Bottom | AnchorStyles.Right
        self.button2.Location = Point(175, 189)
        self.button2.Name = "button2"
        self.button2.Size = Size(75, 23)
        self.button2.TabIndex = 1
        self.button2.Text = "Save"
        self.button2.UseVisualStyleBackColor = True
        self.button2.Click += self.button2_Click
        #
        # textBox1
        #
        self.textBox1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right
        self.textBox1.Location = Point(12, 12)
        self.textBox1.Name = "textBox1"
        self.textBox1.Size = Size(238, 20)
        self.textBox1.TabIndex = 2
        #
        # openFileDialog1
        #
        self.openFileDialog1.FileName = "openFileDialog1"
        #
        # Form1
        #
        self.Size = Size(280, 260)
        self.Controls.Add(self.textBox1)
        self.Controls.Add(self.button2)
        self.Controls.Add(self.button1)
        self.Name = "Form1"
        self.Text = "OpenFileDialog & SaveFileDialog"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
