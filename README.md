```plain
[    0.000000] ShrimpOS 6.1.0-cjt (cjt@fuzhou) (clang 21.1.0, GNU ld 2.45) #1 SMP PREEMPT_DYNAMIC Tue Aug  5 06:54:25 UTC 2022
[    0.000000] Command line: init=/usr/bin/shrimp root=UUID=fujian-fuzhou quiet splash shell_on_fail
[    0.000000] BIOS-provided physical RAM map:
[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000003fffffff] usable
[    0.000000] DMI: ShrimpD, BIOS ShrimpD 08/05/2022
[    0.101221] Loading initial ramdisk...
[    9.982443] systemd[1]: Reached target Main User Target.
[    9.983001] systemd[1]: Reached target cjt_shrimp.

<<< Welcome to ShrimpOS 6.1.0 (x86_64) - tty1 >>>

shrimp login: cjt
Password:

[cjt@shrimp ~]$ cat ~/README.md
```

<div align="center">

# [[ 陈晋瑭 // chenjintang-shrimp ]]

**「火焰般的生命啊，随时可能熄灭。」**

<sub>福州 · 16 岁高中生 · 前算法竞赛选手 · osu! 重度玩家 · 啥都知道但啥都不明白</sub>

[![GitHub](https://img.shields.io/badge/GitHub-chenjintang--shrimp-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chenjintang-shrimp)
[![X](https://img.shields.io/badge/X-@cjt__shrimp-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/cjt_shrimp)
[![Blog](https://img.shields.io/badge/Blog-dev.cxshrimp.qzz.io-2EA043?style=for-the-badge&logo=astro&logoColor=white)](https://dev.cxshrimp.qzz.io)

[![Followers](https://img.shields.io/github/followers/chenjintang-shrimp?style=flat-square&logo=github&label=Followers&color=2ea043)](https://github.com/chenjintang-shrimp?tab=followers)
[![Stars](https://img.shields.io/github/stars/chenjintang-shrimp?style=flat-square&logo=github&label=Stars&color=2ea043)](https://github.com/chenjintang-shrimp?tab=repositories)
![Contributions](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2Fchenjintang-shrimp&query=%24.public_repos&label=Public%20Repos&style=flat-square&color=2ea043)
![Profile Views](https://komarev.com/ghpvc/?username=chenjintang-shrimp&style=flat-square&color=2ea043&label=Views)

<sub>

`C/C++` · `C#` · `Python` · `Rust` · `TypeScript` · `Typst` · `PowerShell`

</sub>

</div>

---

写代码这件事，最开始只是想让自己少干点重复的活。

后来发现要么自己去适应别人的工具，要么把工具改成自己顺手的形状。我大部分时间在做第二件事——把一个具体的小麻烦拆开，看到底是哪一层在碍事，然后往下钻一层，再钻一层，直到能自己决定它长什么样。

所以这里的仓库挺杂的：有人排座位排到崩溃，于是有了约束求解器；有还原软件老是吃掉系统改动，于是有了直接对磁盘下手的内核层工具；有台根本不存在的 16 位机器，于是我把它的 CPU、汇编器和 BASIC 解释器都写出来了。

早年那个「喜欢贡献但不太会创造」的我，现在看来说早了（x

---

```bash
[cjt@shrimp ~]$ ./contributions --last-year
```

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/heatmap-dark.svg">
  <img alt="GitHub contributions heatmap for the last year" src="assets/heatmap-light.svg">
</picture>

<sub>这张图不走第三方图表服务，由 [<code>scripts/gen-heatmap.py</code>](scripts/gen-heatmap.py) 直接读 GitHub GraphQL 的 contribution calendar 画出来。</sub>

<br>

<table>
<tr>
<td><img alt="Streak stats" src="https://streak-stats.demolab.com/?user=chenjintang-shrimp&theme=default&hide_border=true&locale=zh&card_width=420"></td>
<td><img alt="Most used languages" src="https://github-readme-stats.vercel.app/api/top-langs?username=chenjintang-shrimp&layout=compact&langs_count=6&hide_border=true"></td>
</tr>
</table>

</div>

---

```bash
[cjt@shrimp ~]$ ls -l /etc/profiles/per-user/bin
```

```plain
-rwxr-xr-x 1 cjt cjt ■■■  c / c++
-rwxr-xr-x 1 cjt cjt ■■■  c#
-rwxr-xr-x 1 cjt cjt ■■■  python
-rwxr-xr-x 1 cjt cjt ■■■  rust
-rwxr-xr-x 1 cjt cjt ■■■  typescript / javascript
-rwxr-xr-x 1 cjt cjt ■■■  assembly / basic (自产的)
-rw-r--r-- 1 cjt cjt ■■■  typst
-rwxr-xr-x 1 cjt cjt ■■■  bash / powershell

-rwxr-xr-x 1 cjt cjt 8.88 osu!
-rwxr-xr-x 1 cjt cjt 540  考试
```

日常环境是 Windows 11，加一台 Kubuntu，WSL 里再压着 Arch 和 Kali。哪个能跑就用哪个。

顺带一提，就算在 Linux 上我也是 `pwsh` 照用不误——不太接受反驳呢。

---

```bash
[cjt@shrimp ~]$ sudo lshw -short
```

```plain
H/W path    Device      Class       Description
===============================================
/1/0/0      yoga3pro    laptop      Lenovo Yoga 3 Pro (8GB / 256GB)
/1/1/0      se1         smartphone  Apple iPhone SE 1st gen (64GB)
/1/2/0      ip7         smartphone  Apple iPhone 7 (128GB)
/1/3/0      p30pro      smartphone  HUAWEI P30 Pro Sky-Blue (128GB)
/1/4/0      iwe         laptop      Lenovo 小新 14 Air IWE (i5 / 8GB / 256GB)
/1/5/0      ipad8       tablet      Apple iPad 8th gen (128GB)
/1/6/0      mbp16       laptop      MacBook Pro 16" 2019 (i9 / 32GB / 2TB / Touch Bar)
/1/7/0      p40prop     smartphone  HUAWEI P40 Pro+ 5G Black (512GB)
/1/8/0      are         laptop      Lenovo 小新 13 Pro ARE (R7 / 16GB / 512GB)
/1/9/0      mate60pro   smartphone  HUAWEI Mate 60 Pro 5G White (1TB)
/1/10/0     pura70prop  smartphone  HUAWEI Pura 70 Pro+ 5G White (1TB)
/1/11/0     fx607jvr    laptop      ASUS 天选 5 Pro FX607JVR Green (i9 / RTX 4060 / 32GB / 2TB)
/1/12/0     mi15ultra   smartphone  Xiaomi 15 Ultra 5G White (512GB)
```

老机器一台台留下来，是因为总有一台正好能跑通上一个跑不通的东西。

---

```bash
[cjt@shrimp ~]$ ls -l ~/work
```

## 主要在做的东西

### 🧊 [IceMelt](https://github.com/chenjintang-shrimp/IceMelt) · `C++`

把冰点、PowerShadow 这类还原软件拆开。

**WinDisk** 是内核驱动，直接构造 SCSI 请求打到磁盘 miniport——绕开文件系统，也绕开还原软件挂在上面那层过滤驱动。**KDU** 负责关掉驱动签名强制，让没有签名的 WinDisk 能加载，而且只在装载真被 `577` 拒绝的时候才用得上（判据是装载返回码，不是任何查询接口的读数）。

两者配合，在 NTFS 层面摘掉还原软件留下的注册表痕迹、换掉 SYSTEM hive，然后把机器交回给你重启。不替换任何驱动文件。

有意思的部分不在「绕过」，而在每一步都得可验证：装载返回码、hive 结构校验与校验和、裸盘写入前后的读回比对，少一步你就不知道到底成没成。

### 🪑 [PokeSeats 戳座](https://github.com/SECTL/PokeSeats) · `C#`

排座位在条件一多的时候，手工排就是纯折磨：近视的要往前调，动了一个又牵连好几个，最后效果还保证不了。

所以把它写成约束求解：硬性规则（隔几个人、跟谁不能坐、固定坐哪）当硬约束，身高梯度、各排均衡这类诉求按优先级逐层优化——每一层都证明了最优才往下走，最后拿到全局最优解。条件互相打架、真的解不出来时，会告诉你具体是哪几条规则在冲突。

求解默认走 OR-Tools 的 CP-SAT；目标是居中或两侧分布这类距离函数时交给 Z3，无解诊断也靠它的 UNSAT Core。几十人的教室基本是秒出。求解核心和 ImGui 桌面端之间用插件契约隔开，两边可以各自长。

### 🎮 [g0v0](https://github.com/GooGuTeam/g0v0-server) · `C#`

osu! 的私人服务器那一侧。

在 [g0v0-server](https://github.com/GooGuTeam/g0v0-server) 里我主要碰的是谱面用户标签、谱面打分接口、多人房间接口、游戏模式列表 API，以及用户信息接口的返回结构；顺带把中文用户名和 Unicode mention 一路修通——正则里一个 `\w` 就能让一整个中文社区的人 @ 不到彼此。

还往 [GooGuTeam/rosu-pp](https://github.com/GooGuTeam/rosu-pp) 里合了 Relax / Autopilot 的 pp 算法，让服务端算出来的成绩和玩家体感对得上。

### 🖥️ [Open16A](https://github.com/FireflyOpenSourceLab/Open16A) · `C#`

一套从零到能跑游戏的复古计算机：自研 16-bit 指令集、8 个通用寄存器、1 MiB 物理内存与分页映射、三种显示模式的视频设备、键盘与中断控制器，再加上汇编器、静态链接器、跑在 guest 里的 BASIC 解释器、LSP 语言服务器和 VS Code / Neovim 插件。

扩展卡是受信任的 .NET 插件，各自独立的 `AssemblyLoadContext`，用 1 KiB mailbox 快照做宿主与卡之间的协议——磁盘卡、嵌入汇编协处理器卡、回环卡都是这么挂上去的。

写它最大的收获不是模拟器本身，而是你一旦要同时扮演 CPU、链接器和编译器，就会明白那些平时被称作「约定」的东西到底在保护什么。

---

```bash
[cjt@shrimp ~]$ history | grep 游戏
```

```plain
2015  狂野飙车 8
2016  狂野飙车 8
2017  Minecraft（网易）
2018  Minecraft（网易）
2019  Minecraft（网易）
2020  Minecraft (Java)
2021  Minecraft (Java)
2022  Minecraft (Java)
2023  Phigros
2024  Phigros
2025  osu!
```

十年就换了四个游戏，然后停在了 osu!。

---

## 提交都散在哪些仓库

以下是按 GitHub 提交搜索口径数出来的（这个口径会漏掉用别的邮箱推的提交，实际只会更多）：

| 仓库 | 提交 | 我在做什么 |
| --- | ---: | --- |
| [SECTL/SecRandom](https://github.com/SECTL/SecRandom) | 139 | PySide6 迁移、延迟加载、语言包拆分、uv + CI 收尾 |
| [chenjintang-shrimp/redfox-bot](https://github.com/chenjintang-shrimp/redfox-bot) | 102 | 跨 Discord / QQ 的 osu! bot |
| [GooGuTeam/g0v0-server](https://github.com/GooGuTeam/g0v0-server) | 93 | 谱面标签、打分、多人房间、API 与中文支持 |
| [SECTL/PokeSeats](https://github.com/SECTL/PokeSeats) | 87 | 约束求解管线与桌面端 |
| [FireflyOpenSourceLab/Open16A](https://github.com/FireflyOpenSourceLab/Open16A) | 80 | 自研 ISA、模拟器、工具链 |
| [chenjintang-shrimp/IceMelt](https://github.com/chenjintang-shrimp/IceMelt) | 72 | WinDisk 驱动 + KDU 加载链 + hive 改写 |
| [Tinadec/TinadecOffice](https://github.com/Tinadec/TinadecOffice) | 56 | 双层编排 runtime 与 invoke-stream |
| [chenjintang-shrimp/SakuraIM-Core](https://github.com/chenjintang-shrimp/SakuraIM-Core) | 42 | 多 IM 消息中继核心 |
| [SECTL/Points](https://github.com/SECTL/Points) | 31 | 存储引擎（二进制 / CRC / 原子写）、C++26 反射、CMake → xmake |
| [hello8693/SecScoreDB](https://github.com/hello8693/SecScoreDB) | 31 | 成绩库 |
| [LKM-AHZ/LKM-service](https://github.com/LKM-AHZ/LKM-service) | 16 | 后端 |
| [SECTL/Luminalium2WPS](https://github.com/SECTL/Luminalium2WPS) | 15 | Linux 下绕开 RPC 接 WPS |

表里这 12 个仓库一共 764 次提交；把全部公开仓库算上，是 **1708** 次，散在 30 来个仓库里。剩下那些早年练手的就不展开了。

还有两个小的但挺喜欢的：[SecRandom.NewAlgorithm](https://github.com/chenjintang-shrimp/SecRandom.NewAlgorithm) 重写了一套份额欠账均衡的抽取算法，[VisionFair.bindings](https://github.com/chenjintang-shrimp/VisionFair.bindings) 把它移植成 C++ 引擎 + C ABI 动态库，再镜像出 Python / Rust / TypeScript 三套绑定，靠位级奇偶校验保证四条路径算出同一个数。

---

```bash
[cjt@shrimp ~]$ groups
```

```plain
GooGuTeam(admin)  SECTL  FireflyOpenSourceLab  Tinadec  LKM-AHZ  ProjectHazelita
```

在这些组织里多半是写代码的那个，偶尔也负责把别人的 PR 从「看着能过」改到「真的能过」。

---

```bash
[cjt@shrimp ~]$ cat /dev/shrimp/motto
```

```plain
火焰般的生命啊，随时可能熄灭。
那就趁还亮着的时候，多写点。
```

---

```bash
[cjt@shrimp ~]$ _
```

<div align="center">

[GitHub](https://github.com/chenjintang-shrimp) · [X / Twitter](https://x.com/cjt_shrimp) · [Blog](https://dev.cxshrimp.qzz.io)

<sub>If you're reading this at 1,200 characters per minute, I know exactly how you feel.</sub>

</div>
