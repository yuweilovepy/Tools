# -*- coding:utf-8 -*-

import sys
from pathlib import Path

class DirectionTree(object):
    """
    @pathname:目标目录
    @filename:要保存的目录
    """

    def __init__(self,pathname='.',filename='tree.txt'):
        super(DirectionTree,self).__init__()
        self.pathname=Path(pathname)
        self.filename=filename
        self.tree=''

    def set_path(self,pathname):
        self.pathname=Path(pathname)

    def set_filename(self,filename):
        self.filename=filename

    def generate_tree(self,n=0):
        if self.pathname.is_file():
            self.tree+='    |'*n+'-'*4+self.pathname.name+'\n'

        elif self.pathname.is_dir():
            self.tree+='    |'*n+'-'*4+str(self.pathname.relative_to(self.pathname.parent))+\
                        '\\'+'\n'

            for cp in self.pathname.iterdir(): #返回一个迭代器包含p下所有文件夹和文件
                self.pathname=Path(cp)
                self.generate_tree(n+1)


    def save_file(self):
        with open(self.filename,'w') as f:
            f.write(self.tree)


if __name__=="__main__":
    dirtree=DirectionTree()
    #命令参数为1时生成当前目录数
    if len(sys.argv)==1:
        dirtree.set_path(Path.cwd())
        dirtree.generate_tree()
        print  dirtree.tree

    # 命令参数为2 且目录存在
    elif len(sys.argv)==2 and Path(sys.argv[1]).exists:
        dirtree.set_path(sys.argv[1])
        dirtree.generate_tree()
        print  dirtree.tree

    #命令参数为3并且目录存在
    elif len(sys.argv)==3 and Path(sys.argv[1]).exists:
        dirtree.set_path(sys.argv[1])
        dirtree.generate_tree()
        dirtree.set_filename(sys.argv[2])
        dirtree.save_file()

    else:
        print u"命令行参数太多，请检查"















        
