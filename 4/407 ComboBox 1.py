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
        # добавляем один элемент
        self.comboBox1.Items.Add("Парагвай")
        # добавляем набор элементов
        self.comboBox1.Items.AddRange(Array[String](["Уругвай", "Эквадор"]))
        # добавляем один элемент на определенную позицию
        self.comboBox1.Items.Insert(1, "Боливия")

        ## удаляем один элемент
        #comboBox1.Items.Remove("Аргентина")
        ## удаляем элемент по индексу
        #comboBox1.Items.RemoveAt(1)
        ## удаляем все элементы
        #comboBox1.Items.Clear()

        #comboBox1.Items[0] = "Парагвай"

        self.comboBox1.Sorted = True

    def _InitializeComponent(self):
        self.comboBox1 = ComboBox()
        # 
        # comboBox1
        # 
        self.comboBox1.FormattingEnabled = True
        self.comboBox1.Items.AddRange(Array[object]([
            "Бразилия",
            "Аргентина",
            "Чили",
            "Венесуэла",
            "Колумбия"]))
        self.comboBox1.Location = Point(77, 82)
        self.comboBox1.Name = "comboBox1"
        self.comboBox1.Size = Size(121, 21)
        self.comboBox1.TabIndex = 0
        # 
        # Form1
        # 
        self.Size = Size(305, 287)
        self.Controls.Add(self.comboBox1)
        self.Name = "Form1"
        self.Text = "ComboBox"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
