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

    def _InitializeComponent(self):
        self.treeNode1 = TreeNode("Персики")
        self.treeNode2 = TreeNode("Бананы")
        self.treeNode3 = TreeNode("Клубника")
        self.treeNode4 = TreeNode("Фрукты", Array[TreeNode]([
            self.treeNode1,
            self.treeNode2,
            self.treeNode3]))
        self.treeNode5 = TreeNode("Помидоры")
        self.treeNode6 = TreeNode("Огурцы")
        self.treeNode7 = TreeNode("Овощи", Array[TreeNode]([
            self.treeNode5,
            self.treeNode6]))
        self.treeNode8 = TreeNode("Продукты", Array[TreeNode]([
            self.treeNode4,
            self.treeNode7]))
        self.treeView1 = TreeView()
        # 
        # treeView1
        # 
        self.treeView1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right
        self.treeView1.Location = Point(12, 12)
        self.treeView1.Name = "treeView1"
        self.treeNode1.Name = "Узел3"
        self.treeNode1.Text = "Персики"
        self.treeNode2.Name = "Узел4"
        self.treeNode2.Text = "Бананы"
        self.treeNode3.Name = "Узел5"
        self.treeNode3.Text = "Клубника"
        self.treeNode4.Name = "Узел1"
        self.treeNode4.Text = "Фрукты"
        self.treeNode5.Name = "Узел6"
        self.treeNode5.Text = "Помидоры"
        self.treeNode6.Name = "Узел7"
        self.treeNode6.Text = "Огурцы"
        self.treeNode7.Name = "Узел2"
        self.treeNode7.Text = "Овощи"
        self.treeNode8.Name = "Узел0"
        self.treeNode8.Text = "Продукты"
        self.treeView1.Nodes.AddRange(Array[TreeNode]([self.treeNode8]))
        self.treeView1.Size = Size(276, 276)
        self.treeView1.TabIndex = 0
        # 
        # Form1
        # 
        self.ClientSize = Size(300, 300)
        self.Controls.Add(self.treeView1)
        self.Name = "Form1"
        self.Text = "TreeView"


if __name__ == "__main__":
    test = TestWindow()
    test.ShowDialog()
