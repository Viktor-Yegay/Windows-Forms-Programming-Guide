# -*- coding: utf-8 -*-
import clr
clr.AddReference('System')
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
from System.Drawing import *
from System.Windows.Forms import *


class Form1(Form):
    def __init__(self):
        # InitializeComponent()
        self.FormBorderStyle = FormBorderStyle.None
        self.BackColor = Color.Yellow
        self.moveStart = Point()
        button1 = Button()
        button1.Location = Point(
                X = (self.Width - button1.Width) / 2,
                Y = (self.Height - button1.Height) / 2)
        button1.Text = "Закрыть"
        button1.Click += self.button1_Click
        self.Controls.Add(button1) # добавляем кнопку на форму
        self.Load += self.Form1_Load
        self.MouseDown += self.Form1_MouseDown
        self.MouseMove += self.Form1_MouseMove

    def button1_Click(self, sender, EventArgs):
        self.Close()

    def Form1_Load(self, sender, EventArgs):
        myPath = System.Drawing.Drawing2D.GraphicsPath()
        # создаем эллипс с высотой и шириной формы
        myPath.AddEllipse(0, 0, self.Width, self.Height)
        # создаем с помощью элипса ту область формы, которую мы хотим видеть
        myRegion = Region(myPath)
        # устанавливаем видимую область
        self.Region = myRegion

    def Form1_MouseDown(self, sender, MouseEventArgs):
        # если нажата левая кнопка мыши
        if MouseEventArgs.Button == MouseButtons.Left:
            self.moveStart = Point(MouseEventArgs.X, MouseEventArgs.Y)

    def Form1_MouseMove(self, sender, MouseEventArgs):
        # если нажата левая кнопка мыши
        if (MouseEventArgs.Button == MouseButtons.Left) != 0:
            # получаем новую точку положения формы
            deltaPos = Point(MouseEventArgs.X - self.moveStart.X, MouseEventArgs.Y - self.moveStart.Y)
            # устанавливаем положение формы
            self.Location = Point(self.Location.X + deltaPos.X, self.Location.Y + deltaPos.Y)


if __name__ == "__main__":
    d = Form1()
    d.ShowDialog()
