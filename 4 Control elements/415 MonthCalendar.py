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

        self.monthCalendar1.DateChanged += self.monthCalendar1_DateChanged

        self.monthCalendar1.AddBoldedDate(DateTime(2020, 10, 21))
        self.monthCalendar1.AddBoldedDate(DateTime(2020, 10, 22))
        self.monthCalendar1.AddAnnuallyBoldedDate(DateTime(2020, 10, 9))
        self.monthCalendar1.AddMonthlyBoldedDate(DateTime(2020, 10, 1))

        self.monthCalendar1.RemoveBoldedDate(DateTime(2020, 10, 21))
        self.monthCalendar1.RemoveBoldedDate(DateTime(2020, 10, 22))
        self.monthCalendar1.RemoveAnnuallyBoldedDate(DateTime(2020, 10, 9))
        self.monthCalendar1.RemoveMonthlyBoldedDate(DateTime(2020, 10, 1))

        self.monthCalendar1.TodayDate = DateTime(2015, 05, 22)
        self.monthCalendar1.ShowTodayCircle = True
        self.monthCalendar1.ShowToday = False
        self.monthCalendar1.SelectionStart = DateTime(2015, 05, 1)
        self.monthCalendar1.SelectionEnd = DateTime(2015, 05, 11)

    def monthCalendar1_DateChanged(self, sender, DateRangeEventArgs):
        self.label1.Text = "Вы выбрали: {0}".format(DateRangeEventArgs.Start.ToLongDateString())
        # или так - аналогичный код
        # self.label1.Text = "Вы выбрали: {0}".format(self.monthCalendar1.SelectionStart.ToLongDateString())

    def _InitializeComponent(self):
        self.monthCalendar1 = MonthCalendar()
        self.label1 = Label()
        self.SuspendLayout()
        #
        # monthCalendar1
        #
        self.monthCalendar1.Location = Point(67, 104)
        self.monthCalendar1.Name = "monthCalendar1"
        self.monthCalendar1.TabIndex = 0
        #
        # label1
        #
        self.label1.AutoSize = True
        self.label1.Location = Point(123, 48)
        self.label1.Name = "label1"
        self.label1.Size = Size(35, 13)
        self.label1.TabIndex = 1
        self.label1.Text = "label1"
        #
        # Form1
        #
        self.Size = Size(292, 452)
        self.Controls.Add(self.label1)
        self.Controls.Add(self.monthCalendar1)
        self.Name = "Form1"
        self.Text = "MonthCalendar"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
