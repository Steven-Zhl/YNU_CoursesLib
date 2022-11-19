# 《机器人学导论》课程的作业与实验
> 这是一门更注重于工程和硬件的课程，这门课的主题内容都是解决实际控制中的需求和问题的。
> 
> 包括如何操作舵机与伺服电机，PID控制体系，如何编程实现控制等等。可以说目前学的还比较基础，但这正是给之后打基础。我认为这门课虽然麻烦，但是是有意义的。
## 所用环境
* Windows 11
* Keil µVision 5（主要的IDE）
* mcuisp(for stm32)（用于串口通信与项目烧录）
* Visual Studio Code（C/C++ environment）
* Matlab R2022a（用于PID控制的仿真测试）
## 教材
* 《机器人系统设计及其应用技术》，赵建伟 主编，清华大学出版社
## 目录
### 实验1：配置开发环境
  即安装Keil µVision 5、mcuisp等软件，过程略
### [实验2：初试STM32编程控制](./实验2)
* [源文件](https://www.aliyundrive.com/s/NjsdjEs91J6)
  * 将`/CAR_STM32F103C6/Drivers/`、`/CAR_STM32F103C6/MDK-ARM/`和`/CAR_STM32F103C6/MDK-ARM/CAR_STM32F103C6/`路径下经编译的二进制文件删除，仅保留源文件。
* [实验报告](./实验2/Report.pdf)
* [实验要求](./实验2/实验要求.docx)
### [实验3：](./实验3)
### [实验4：Simulink仿真PID控制](./实验4)
* [源文件](./实验4/PID控制模型.slx)
* [绘图代码](实验4/PID_Drow.m)
* [实验报告](./实验4/Report.pdf)
* [实验要求](./实验4/实验要求.docx)