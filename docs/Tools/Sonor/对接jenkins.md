---
title: Sonor对接Jenkins
---

### SonarQube简介

    SonarQube是一个开源的代码质量管理平台，用于管理源代码的质量。它可以检测代码的错误、漏洞和代码异味，以及代码重复率。
    SonarQube支持多种编程语言，包括Java、C#、C、C++、PL/SQL、Python、JavaScript、TypeScript、Ruby、Go、PHP、HTML、CSS、XML等。


### SonarQube

1. 在SonarQube上创建项目, 添加 Project display name, Project key 点击Set Up按钮创建项目
    ![创建项目](../../img/Tools/Sonor/1.png)

### Jenkins
1. 在Jenkins上创建 freestyle 任务
    ![创建任务](../../img/Tools/Sonor/2.png)
2. 配置任务
    ![配置任务](../../img/Tools/Sonor/3.png)
    ![配置任务](../../img/Tools/Sonor/4.png)
    ![配置任务](../../img/Tools/Sonor/5.png)
    ![配置任务](../../img/Tools/Sonor/6.png)
    ![配置任务](../../img/Tools/Sonor/7.png)
    ![配置任务](../../img/Tools/Sonor/8.png)
    ![配置任务](../../img/Tools/Sonor/9.png)
3. 构建后操作

### 查看Sonor报告
1. 在SonarQube上查看报告(原则上需要无bug, 无漏洞, 无代码异味, 无重复率)
    ![查看报告](../../img/Tools/Sonor/10.png)