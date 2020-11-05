# -*- coding: utf-8 -*-
import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import *


class TestWindow(Form):
    def __init__(self):
        self.Name = 'Form1'
        self.Text = 'Hello world'
        self.Size = Size(300, 300)

        # self.BackColor = Color.Aquamarine
        # self.BackColor = Color.FromArgb(255, 224, 192)

        # self._ImageList1 = ImageList()
        # self._ImageList1.ImageSize = Size(250, 250)
        # self._ImageList1.Images.Add(Image.FromFile(r"F:\YandexDisk\Windows Forms Programming Guide\2\image.jpg"))
        # self.BackgroundImage = self._ImageList1.Images[0]

        # self.BackgroundImageLayout = ImageLayout.Zoom

        # self.ControlBox = False

        # self.Cursor = Cursors.Cross

        # self.Enabled = True  # Если False, то не будет отображаться

        # self.Font = Font("GothicE", 8.25, FontStyle.Regular, GraphicsUnit.Point, 204)
        # self.Margin = Padding(4, 4, 4, 4)

        # self.ForeColor = Color.Red

        self.FormBorderStyle = FormBorderStyle.Fixed3D
        # self.FormBorderStyle = FormBorderStyle.FixedDialog
        # self.FormBorderStyle = FormBorderStyle.FixedSingle
        # self.FormBorderStyle = FormBorderStyle.FixedToolWindow
        # self.FormBorderStyle = FormBorderStyle.None
        # self.FormBorderStyle = FormBorderStyle.Sizable

        self.CenterToScreen()
        # self.Opacity = 0.5

        self.BackgroundImage = Image.FromFile(r"F:\YandexDisk\Windows Forms Programming Guide\2\image.jpg")
        self.BackgroundImageLayout = ImageLayout.Center
        # self.BackgroundImageLayout = ImageLayout.Zoom

        self._initialize_components()

    def _initialize_components(self):
        self._btn_1 = Button()
        self._btn_1.Location = Point(104, 200)
        self._btn_1.Name = 'button1'
        self._btn_1.Size = Size(75, 23)
        self._btn_1.TabIndex = 0
        self._btn_1.Text = 'button1'
        self._btn_1.UseVisualStyleBackColor = True
        self._btn_1.Parent = self
        self._btn_1.Click += self._button_click

    def _button_click(self, sender, event_args):
        MessageBox.Show("Доброго времени суток, Виктор")


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
