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

        self.treeView1.BeforeSelect += self.treeView1_BeforeSelect
        self.treeView1.BeforeExpand += self.treeView1_BeforeExpand
        # заполняем дерево дисками
        TestWindow.FillDriveNodes()

    # событие перед раскрытием узла
    def treeView1_BeforeExpand(self, sender, TreeViewCancelEventArgs):
        TreeViewCancelEventArgs.Node.Nodes.Clear()
        dirs = []
        try:
            if Directory.Exists(TreeViewCancelEventArgs.Node.FullPath):
                dirs = Directory.GetDirectories(TreeViewCancelEventArgs.Node.FullPath)
                if dirs.Length != 0:
                    for (int i = 0 i < dirs.Length i++):
                        dirNode = TreeNode(DirectoryInfo(dirs[i]).Name)
                        TestWindow.FillTreeNode(dirNode, dirs[i])
                        TreeViewCancelEventArgs.Node.Nodes.Add(dirNode)
        except Exception:
            pass

    # событие перед выделением узла
    void treeView1_BeforeSelect(self, sender, TreeViewCancelEventArgs e)
    {
        e.Node.Nodes.Clear()
        string[] dirs
        try
        {
            if (Directory.Exists(e.Node.FullPath))
            {
                dirs = Directory.GetDirectories(e.Node.FullPath)
                if (dirs.Length != 0)
                {
                    for (int i = 0 i < dirs.Length i++)
                    {
                        TreeNode dirNode = new TreeNode(new DirectoryInfo(dirs[i]).Name)
                        FillTreeNode(dirNode, dirs[i])
                        e.Node.Nodes.Add(dirNode)
                    }
                }
            }
        }
        catch (Exception ex) { }
    }

    # получаем все диски на компьютере
    private void FillDriveNodes()
    {
        try
        {
            foreach (DriveInfo drive in DriveInfo.GetDrives())
            {
                TreeNode driveNode = new TreeNode { Text = drive.Name }
                FillTreeNode(driveNode, drive.Name)
                treeView1.Nodes.Add(driveNode)
            }
        }
        catch (Exception ex) { }
    }
    # получаем дочерние узлы для определенного узла
    private void FillTreeNode(TreeNode driveNode, string path)
    {
        try
        {
            string[] dirs = Directory.GetDirectories(path)
            foreach (string dir in dirs)
            {
                TreeNode dirNode = new TreeNode()
                dirNode.Text = dir.Remove(0, dir.LastIndexOf("\\") + 1)
                driveNode.Nodes.Add(dirNode)
            }
        }
        catch (Exception ex) { }


    def _InitializeComponent(self):
        self.treeView1 = TreeView()
        # 
        # treeView1
        # 
        self.treeView1.Dock = DockStyle.Fill
        self.treeView1.Location = Point(0, 0)
        self.treeView1.Name = "treeView1"
        self.treeView1.Size = Size(300, 300)
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
