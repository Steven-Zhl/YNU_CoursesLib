# 《图像理解与计算机视觉》课程的相关资料

> 这是一门注重实验的课，虽然会学习很多相关算法，但都是图像处理领域的经典算法，没那么难理解。
> 相比之下，将其用代码实现显得更有意义。
> 本课程几乎并不涉及人工智能和深度学习，但其中所学的处理方法往往被用于深度学习的图像预处理和结果的优化。

## 使用环境

* Windows 11
* Matlab R2022a
* Visual Studio Code（主要用于整理代码格式，并不重要）
* Microsoft Word（用于写实验报告）

## 教材

* 《数字图像处理（第四版）》，Rafael C. Gonzalez 等著，阮秋琦 等译，电子工业出版社，2020.05.
* 《数字图像处理》贾永红 著，武汉大学出版社，2015.07
* （老师自己做的PPT）

## 目录

### [实验1：图像变换](./实验1/)

* 主程序：[`Exp1.m`](./实验1/Code/Exp1.m)
* 完整项目：[Code](./实验1/Code)
* 实验报告：[Report.pdf](./实验1/Report.pdf)

### 实验1：References

> `equalizeImg(img, bin)` (灰度直方图均衡化)

* [图像数据的直方图 - MATLAB imhist - MathWorks 中国](https://ww2.mathworks.cn/help/images/ref/imhist.html?s_tid=doc_ta#buo3qek-1-binLocations)

### [实验2：图像滤波](./实验2/)

* 主程序：[`Exp2.m`](./实验2/Code/Exp2.m)
* 完整项目：[Code](./实验2/Code)
* 实验报告：[Report.pdf](./实验2/Report.pdf)

### 实验2：References

> `freq_laplace_filter()` (频域拉普拉斯滤波)

* [灰度图像的频率域滤波——拉普拉斯——高频提升（Matlab）_lengo的博客-CSDN博客](https://blog.csdn.net/lengo/article/details/100527930)

> (理解图像频域及频域滤波)

* [什么是图像上的频率？_Norstc的博客-CSDN博客_图像空间频率](https://blog.csdn.net/a493823882/article/details/117925648)
* [如何理解图像的频率域处理？ - 知乎](https://zhuanlan.zhihu.com/p/484475975)

### [实验3：图像复原](./实验3/)

* 主程序：[`Exp3.m`](./实验3/Code/Exp3.m)
* 完整项目：[Code](./实验3/Code)
* 实验报告：[Report.pdf](./实验3/Report.pdf)

### 实验3：References

* （无）

### [实验4：形态学处理](./实验4/)

* 主程序：[`Exp4.m`](./实验4/Code/Exp4.m)
* 完整项目：[Code](./实验4/Code)
* 实验报告：[Report.pdf](./实验4/Report.pdf)

### References

* （无）

### [实验5：图像分割](./实验5/)

* 主程序：[`Exp5.m`](./实验5/Code/Exp5.m)
* 完整项目：[Code](./实验5/Code)
* 实验报告：[Report.pdf](./实验5/Report.pdf)

### 实验5：References

* 有很多，但因为当时的搜索记录并未及时保留，暂无法列出。

### [实验6：图像描述](./实验6/)

* 主程序：[`Exp6.m`](./实验6/Code/Exp6.m)
* 完整项目：[Code](./实验6/Code)
  * 对于`sift`算法，需要下载`siftWin32.exe`文件，并将其放在Matlab安装路径的`bin`文件夹下才可使用。不提供具体下载链接了，自行搜索即可。
* 实验报告：[Report.pdf](./实验6/Report.pdf)

### 实验6：References

> (SIFT算法)

* [SIFT(2)——MATLAB实现SIFT详解_海淀摆烂王的博客-CSDN博客_matlab sift](https://blog.csdn.net/qq_20778015/article/details/83188551)
* [(原作者博客)Keypoint dectetor](https://www.cs.ubc.ca/~lowe/keypoints/)

> `Canny_edge_detect(img_gray)` (Canny算子边缘检测)

* [Canny边缘检测算法 - 知乎](https://zhuanlan.zhihu.com/p/99959996)

> `HOG(img_gray)` (HOG特征算法)

* [【特征检测】HOG特征算法_hujingshuang的博客-CSDN博客_hog特征检测](https://blog.csdn.net/hujingshuang/article/details/47337707)

### [实验7：计算机视觉典型应用](./实验7/)

* 主程序：[`Exp7.m`](./实验7/Code/Exp7.m)
* 完整项目：[Code](./实验7/Code)
  * 该程序不包含测试视频`pedestrian.avi`，请自行下载后移动至`./实验7/Code`文件夹下。
  * 该程序中不包含测试数据集`Girl2`，请自行下载解压后移动至`./实验7/Code/tracker/`文件夹下。
  * 这两份文件老师应当会提供的
* 实验报告：[Report.pdf](./实验7/Report.pdf)

### 实验7：References

> `frame_difference_3(video, frame_num)` (三帧差分法)

* [初学者做三帧差分（matlab代码）_qq_45087091的博客-CSDN博客](https://blog.csdn.net/qq_45087091/article/details/94625040)

> `gauss_bg_modeling(video)` (混合高斯背景建模)

* [matlab 混合高斯背景建模的实现_大米粥哥哥的博客-CSDN博客_高斯混合模型背景建模matlab](https://blog.csdn.net/qq_38204686/article/details/104508018)

> (KCF 运动目标追踪)

* [(原理讲解)KCF跟踪算法原理 入门详解 - Jerry_Jin - 博客园](https://www.cnblogs.com/jins-note/p/10215511.html)
* [(代码调试)KCF代码调试并显示效果（matlab）_無負今日的博客-CSDN博客_kcf算法matlab代码](https://blog.csdn.net/weixin_44100850/article/details/102840630)
* [(原版代码)João F. Henriques](https://www.robots.ox.ac.uk/~joao/downloads/tracker_release2.zip)
* [(原论文)Your Title](https://www.robots.ox.ac.uk/~joao/publications/henriques_tpami2015.pdf)
* [(相关测试集下载)Visual Tracker Benchmark](http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html)
