# 《操作系统》课程的相关资料

> 经典的408课程，也是本专业的专业必修课，其重要性不言而喻。
>
> 但是相比于其他三门408专业课，操作系统其实相对简单一些，因为其大致架构已经固定了，短时间内不会大变动，而作为软硬件之间的组成部分，操作系统既不像计算机组成原理那么底层，也不如高级语言那么有设计感....我是说这门课，学的比较浅，所以感觉没那么难罢了

## 使用环境

* AidLux 1.3.0.477(Linux环境基于Debian 10)

      实验1~4并不要求特定的Linux发行版，我用的这个就挺小众，也用的好好的。只是后来更新了安卓12，它总是被杀进程，遂弃用。
* Ubuntu 16.04.7 LTS

      仅实验5任务2需要用到这版系统。
* `gcc`, `vim`
* Visual Studio Code（用于整理代码）
* Microsoft Word（用于写实验报告）

## 教材

* 《计算机操作系统教程》 张尧学，宋虹，张高 编著，清华大学出版社

## 目录

### [实验1：进程管理与进程间通信](./实验1)

* [源文件](./实验1/Exp1/)
* 实验报告
  * 本次实验报告没有上传，反正也挺简单的，就是用gcc编译运行一下几个简单的C程序。

### [实验2：进程调度](./实验2)

* [源文件](./实验2/Exp2)
  * 初版：[`source_msvc.c`](./实验2/Exp2/source_msvc.c)，该文件是我在Windows上使用Visual Studio编译通过的，逻辑没问题，但语法并不契合gcc
  * 修改版：[`source_gcc.c`](./实验2/Exp2/source_gcc.c)，修改了初版中独属于msvc的语法，该版符合gcc语法，建议直接使用这个
* 实验报告：[Report.pdf](./实验2/Report.pdf)

### [实验3：内存页面置换算法](./实验3)

* 源文件：[`source_gcc.c`](./实验3/Exp3/source_gcc.c)
* 实验报告：[Report.pdf](./实验3/Report.pdf)

### [实验4：Linux系统状态信息查询](./实验4)

* [源文件](./实验4/Exp4)
  * 负载程序: [`load.c`](./实验4/Exp4/load.c)
  * 脚本1(用于题1)：[`meminfo.sh`](./实验4/Exp4/meminfo.sh)
  * 脚本2(用于讨论1)：[`meminfo_new.sh`](./实验4/Exp4/meminfo_new.sh)
  * 由于我使用的AidLux并非虚拟机，类似于WSL，所以可以使用整台设备的全部内存(8GB)。因此该程序设定的负载较高（10MB/s），以便于观察负载变化。若是使用VMware，请根据自己分配的内存情况手动降低负载调整(通过修改`load.c`，`while`循环中`malloc`和`memset`的值实现)
* [相关数据](./实验4/Exp4)
  * 题1数据：[1_meminfo.sh记录数据.txt](./实验4/Exp4/1_meminfo.sh记录数据.txt)
  * 题2数据：[2_vmstat记录数据.txt](./实验4/Exp4/2_vmstat记录数据.txt)
  * 讨论1数据：[ext_meminfo_new.sh记录数据.txt](./实验4/Exp4/ext_meminfo_new.sh记录数据.txt)
  * 这些数据是直接在Terminal上复制得来的，以便于导入Excel进行绘图。当然，不同人得出来的数据是不一样的，这里只是做个参考。
* 实验报告：[Report.pdf](./实验4/Report.pdf)

### [实验5：（期末实验）设备驱动程序](./实验5)

* [任务1](./实验5/Exp5_1/)
  * 构建脚本：[`Makefile`](./实验5/Exp5_1/Makefile)
  * 字符设备驱动程序：[`chardev.c`](./实验5/Exp5_1/chardev.c)
  * 测试脚本：[`test.c`](./实验5/Exp5_1/test.c)
* [任务2](./实验5/Exp5_2/)
  > **注意：** 本部分的代码调用了一些系统库，其中一部分在较新的内核中有改动，使该代码无法正常运行。而我又~~不愿意~~不懂该代码，所以选择安装旧版系统。需要使用内核大版本**3**或**4**的系统才可正常编译，如Ubuntu 16。(不清楚内核版本的可以在Terminal中输入`uname -r`查看)
  * 构建脚本：[`Makefile`](./实验5/Exp5_1/Makefile)
  * 块设备驱动程序：[`simp_blkdev.c`](./实验5/Exp5_2/simp_blkdev.c)
  * 代码来源于[2018-2019学年第一学期江苏大学操作系统课程设计教程](https://github.com/LeoB-O/OS-Curriculum-Design)第三题，修改了宏定义中的`SIMP_BLKDEV_BYTES`为50MB，因为原代码的256MB在VMware环境中太大，非常容易在安装模块时触发`Cannot allocate memory`错误。
* 实验报告：[Report.docx](./实验5/Report.docx)
