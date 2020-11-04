import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Form, Button, FormBorderStyle
clr.AddReference('System.Drawing')
from System.Drawing import Size, Point, Color


class TestWindow(Form):
    def __init__(self):
        self.Text = 'Test'
        self.Size = Size(300, 300)
        self.FormBorderStyle = FormBorderStyle.Fixed3D
        self.CenterToScreen()
        self.BackColor = Color.Aquamarine
        self._initialize_components()

    def _initialize_components(self):
        self._btn_1 = Button()
        self._btn_1.BackColor = Color.Blue
        self._btn_1.Parent = self
        self._btn_1.Text = 'Press'
        self._btn_1.Location = Point(0, 0)
        self._btn_1.Size = Size(100, 25)
        self._btn_1.Click += self._button_click

        self._btn_2 = Button()
        self._btn_2.Parent = self
        self._btn_2.Text = 'Press'
        self._btn_2.Location = Point(100, 25)
        self._btn_2.Size = Size(100, 25)
        self._btn_2.Click += self._button_click

        self._btn_3 = Button()
        self._btn_3.Parent = self
        self._btn_3.Text = 'Press'
        self._btn_3.Location = Point(200, 50)
        self._btn_3.Size = Size(100, 25)
        self._btn_3.Click += self._button_click

    def _button_click(self, sender, event_args):
        print 'Hello world!'


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
