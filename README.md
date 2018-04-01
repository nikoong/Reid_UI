# Reid_UI
a simple Re-id UI based on PyQt4
一个简单的行人再识别窗口，基于PyQt4

1. 打开ui：在该目录下打开终端输入：python min_win_test.py

2. ui文件夹中的文件：

        min_win_test.py  :，ui的内在逻辑编写;
        min_win.ui       :ui的窗口布局，可用Qt Creator打开，做控件布局;
        Ui_min_win.py    :min_win.ui转换成的python文件，供min_win_test.py调用;
        Ui_min_win.pyc   :缓存文件;
        pic_rc.py        :资源文件;
        pic_rc.pyc       :资源文件;

3. 修改说明
唯一需要看和修改的是min_win_test.py文件中的两个函数。我在代码中留有详细注释，可以直接看代码。

        （1）on_pushButton_3_clicked：这个函数只涉及到选择图片的默认路径问题。

        （2）on_pushButton_2_clicked：该函数负责ui中“搜索”按钮的逻辑。其中"图片特征提取和比对"的代码我没有写，
        但在相应位置留了注释，需要自己添加。


