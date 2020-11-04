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

        #Добавление элементов
        countries = Array[object](["Бразилия", "Аргентина", "Чили", "Уругвай", "Колумбия"])
        self.listBox1.Items.AddRange(countries)

        #Вставка элементов
        self.listBox1.Items.Insert(1, "Парагвай")

        #Удаление элементов
        #listBox1.Items.Remove("Чили")
        #listBox1.Items.RemoveAt(1)
        #listBox1.Items.Clear()

        #Доступ к элементам списка
        #string firstElement = listBox1.Items[0]
        #int number = listBox1.Items.Count()

        #Выделение элементов списка
        self.listBox1.SetSelected(2, True) # будет выделен третий элемент

    def _InitializeComponent(self):
        self.listBox1 = ListBox()
        # 
        # listBox1
        # 
        self.listBox1.FormattingEnabled = True
        #self.listBox1.Items.AddRange(new object[] {
        #"Бразилия",
        #"Аргентина",
        #"Чили",
        #"Уругвай",
        #"Колумбия"})
        self.listBox1.Location = Point(54, 72)
        self.listBox1.Name = "listBox1"
        self.listBox1.Size = Size(149, 134)
        self.listBox1.TabIndex = 0
        # 
        # Form1
        # 
        self.Size = Size(305, 287)
        self.Controls.Add(self.listBox1)
        self.Name = "Form1"
        self.Text = "ListBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
