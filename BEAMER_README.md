# Beamer PPT自动生成工具使用说明

## 📖 简介

本工具可以从`PPT内容文档.md`自动生成LaTeX Beamer格式的演示文稿，支持：
- ✅ 4:3比例PPT
- ✅ 逐项动画效果（`\item<+->`）
- ✅ 中文支持
- ✅ 专业的学术风格
- ✅ 自动生成目录和章节

---

## 🚀 快速开始

### 1. 生成Beamer LaTeX文件

```bash
python3 generate_beamer_ppt.py
```

这将生成：`第一章/WSN_Chapter1_Beamer.tex`（共58页，969行LaTeX代码）

### 2. 编译为PDF

#### 方法1：使用XeLaTeX（推荐）

```bash
cd 第一章
xelatex WSN_Chapter1_Beamer.tex
xelatex WSN_Chapter1_Beamer.tex  # 编译两次生成正确目录
```

#### 方法2：使用Overleaf在线编译

1. 访问 [Overleaf](https://www.overleaf.com/)
2. 创建新项目 → 上传 `WSN_Chapter1_Beamer.tex`
3. 设置编译器为 **XeLaTeX**
4. 点击编译即可

#### 方法3：使用本地LaTeX编辑器

- **TeXstudio**: 设置编译器为XeLaTeX
- **TeXworks**: 选择XeLaTeX引擎
- **VS Code**: 安装LaTeX Workshop扩展

---

## 📦 系统要求

### Linux/Mac 安装LaTeX

```bash
# Ubuntu/Debian
sudo apt-get install texlive-xetex texlive-latex-extra texlive-fonts-recommended

# macOS (使用Homebrew)
brew install --cask mactex
```

### Windows 安装LaTeX

下载并安装 [MiKTeX](https://miktex.org/) 或 [TeX Live](https://www.tug.org/texlive/)

### 中文字体要求

需要系统安装以下字体（或修改LaTeX文件中的字体设置）：
- **宋体** (SimSun)
- **黑体** (SimHei)

**macOS用户**: 可以使用 `STSong` 和 `STHeiti` 替代
**Linux用户**: 安装中文字体包
```bash
sudo apt-get install fonts-wqy-microhei fonts-wqy-zenhei
```

---

## 🎨 Beamer主题和样式

### 当前设置

- **主题**: Madrid（经典学术风格）
- **颜色**: 深蓝色（darkblue）
- **比例**: 4:3
- **动画**: 逐项显示

### 自定义主题

在 `WSN_Chapter1_Beamer.tex` 中修改：

```latex
% 更改主题
\usetheme{Copenhagen}  % 其他选项: Berlin, AnnArbor, Dresden

% 更改颜色主题
\usecolortheme{whale}  % 其他选项: dolphin, seahorse, beaver

% 更改比例（16:9）
\documentclass[aspectratio=169]{beamer}
```

### 推荐主题组合

| 主题 | 适用场景 | 风格 |
|------|---------|------|
| Madrid + default | 学术报告 | 经典、专业 |
| Copenhagen + dolphin | 技术演讲 | 现代、简洁 |
| Berlin + beaver | 课堂教学 | 清晰、醒目 |
| Dresden + seahorse | 会议展示 | 优雅、正式 |

---

## ✨ 动画效果说明

### 已实现的动画

```latex
\item<+-> 内容项  % 逐项显示
```

效果：列表项会逐个出现，适合讲解要点

### 其他可用动画

**暂停命令**:
```latex
\pause  % 在当前位置暂停，点击后继续
```

**分步显示**:
```latex
\onslide<1>{第一步内容}
\onslide<2>{第二步内容}
\onslide<3>{第三步内容}
```

**条件显示**:
```latex
\only<1>{仅第1步显示}
\only<2->{从第2步开始显示}
```

**高亮效果**:
```latex
\alert<2>{在第2步高亮此内容}
```

---

## 📁 文件结构

```
WSN_PPT/
├── generate_beamer_ppt.py          # Beamer生成脚本
├── BEAMER_README.md                 # 本文档
└── 第一章/
    ├── PPT内容文档.md               # 源文档（输入）
    └── WSN_Chapter1_Beamer.tex     # 生成的Beamer文件（输出）
    └── WSN_Chapter1_Beamer.pdf     # 编译后的PDF（需手动编译）
```

---

## 🔧 自定义和扩展

### 添加图片

```latex
\begin{frame}
  \frametitle{示例图片}
  \begin{figure}
    \centering
    \includegraphics[width=0.6\textwidth]{path/to/image.png}
    \caption{图片说明}
  \end{figure}
\end{frame}
```

### 添加表格

```latex
\begin{frame}
  \frametitle{示例表格}
  \begin{table}
    \centering
    \begin{tabular}{lcc}
      \toprule
      项目 & 值1 & 值2 \\
      \midrule
      数据1 & 100 & 200 \\
      数据2 & 150 & 250 \\
      \bottomrule
    \end{tabular}
  \end{table}
\end{frame}
```

### 添加代码

```latex
\begin{frame}[fragile]  % 注意：需要添加fragile选项
  \frametitle{代码示例}
  \begin{verbatim}
  def hello():
      print("Hello, World!")
  \end{verbatim}
\end{frame}
```

---

## 🎯 进阶技巧

### 1. 两栏布局

```latex
\begin{frame}
  \frametitle{两栏布局}
  \begin{columns}
    \column{0.5\textwidth}
      左侧内容
    \column{0.5\textwidth}
      右侧内容
  \end{columns}
\end{frame}
```

### 2. 区块强调

```latex
\begin{frame}
  \frametitle{区块示例}
  \begin{block}{重要概念}
    这是一个重要的概念说明
  \end{block}

  \begin{alertblock}{注意}
    这是需要注意的内容
  \end{alertblock}

  \begin{exampleblock}{示例}
    这是一个示例
  \end{exampleblock}
\end{frame}
```

### 3. 覆盖效果（Overlay）

```latex
\begin{frame}
  \frametitle{覆盖效果}
  \begin{itemize}
    \item<1-> 第1步显示此项
    \item<2-> 第2步显示此项
    \item<3-> 第3步显示此项
    \item<1-2> 仅在第1-2步显示
  \end{itemize}
\end{frame}
```

---

## 🐛 常见问题

### 1. 编译错误："Font not found"

**解决方案**: 修改字体设置
```latex
% 将 SimSun 改为系统已安装的字体
\setCJKmainfont{STSong}  % macOS
\setCJKmainfont{Noto Sans CJK SC}  % Linux
```

### 2. 中文显示为方框

**原因**: 未使用XeLaTeX编译

**解决方案**: 确保使用XeLaTeX而非PDFLaTeX

### 3. 目录页码不正确

**解决方案**: 编译两次
```bash
xelatex WSN_Chapter1_Beamer.tex
xelatex WSN_Chapter1_Beamer.tex
```

### 4. 动画不显示

**原因**: 使用了不支持动画的PDF阅读器

**解决方案**: 使用以下阅读器
- Adobe Acrobat Reader
- Evince（Linux）
- Preview（macOS，部分支持）

---

## 📊 生成结果

使用本工具生成的PPT包含：

- **封面页**: 课程标题、作者信息
- **目录页**: 自动生成章节目录
- **58页内容**: 完整的第一章内容
- **逐项动画**: 所有列表项支持逐个显示
- **章节分隔**: 自动添加章节标题页

---

## 🔄 更新和维护

### 修改源内容

1. 编辑 `第一章/PPT内容文档.md`
2. 重新运行 `python3 generate_beamer_ppt.py`
3. 重新编译LaTeX文件

### 脚本改进建议

欢迎提出改进建议：
- 支持更多动画效果
- 自动添加图片
- 解析表格内容
- 支持更多Beamer主题

---

## 📚 参考资源

- **Beamer官方文档**: https://ctan.org/pkg/beamer
- **Overleaf Beamer教程**: https://www.overleaf.com/learn/latex/Beamer
- **LaTeX中文排版**: https://www.latexstudio.net/

---

## ✅ 检查清单

生成并编译PPT后，请检查：

- [ ] PDF生成成功
- [ ] 中文显示正确
- [ ] 比例为4:3
- [ ] 列表项动画正常工作
- [ ] 目录页码正确
- [ ] 章节分隔清晰
- [ ] 封面信息完整

---

**作者**: 自动生成工具
**版本**: v1.0
**更新日期**: 2025年2月
**支持**: 传感器网络技术与应用课程
