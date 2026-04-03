# Beamer PPT 快速开始指南 🚀

## 一键生成PPT（推荐）

### 步骤1：生成LaTeX源文件
```bash
python3 generate_beamer_ppt.py
```

**输出**: `第一章/WSN_Chapter1_Beamer.tex`

### 步骤2：编译为PDF

#### 选项A：使用本地LaTeX（需要安装XeLaTeX）
```bash
./compile_beamer.sh
```

#### 选项B：使用Overleaf在线编译（推荐新手）
1. 访问 https://www.overleaf.com/
2. 注册/登录账号
3. 创建新项目 → 上传 `WSN_Chapter1_Beamer.tex`
4. 设置编译器为 **XeLaTeX**（左上角菜单）
5. 点击"重新编译"按钮

---

## ✨ 功能特性

### ✅ 已实现
- 4:3比例PPT（适合投影）
- 58页完整内容
- **逐项动画**：列表项逐个显示
- **表格动画**：表格行逐行显示
- 自动目录和章节分隔
- 中文支持
- 专业学术风格（Madrid主题）

### 📊 动画效果预览

**列表动画**（每点击一次显示一项）：
```
点击1: • 第一项
点击2: • 第一项
       • 第二项
点击3: • 第一项
       • 第二项
       • 第三项
```

**表格动画**（每点击一次显示一行）：
```
点击1: 表头
       第1行
点击2: 表头
       第1行
       第2行
点击3: 表头
       第1行
       第2行
       第3行
```

---

## 📂 生成的文件

```
第一章/
├── PPT内容文档.md              ← 源文档（输入）
├── WSN_Chapter1_Beamer.tex     ← 生成的LaTeX（中间产物）
└── WSN_Chapter1_Beamer.pdf     ← 最终PPT（输出）
```

---

## 🎨 自定义样式

### 更改主题
编辑 `WSN_Chapter1_Beamer.tex`，修改第4行：

```latex
\usetheme{Madrid}  → \usetheme{Copenhagen}
```

### 更改比例（16:9）
编辑第1行：

```latex
\documentclass[aspectratio=43]{beamer}  → \documentclass[aspectratio=169]{beamer}
```

### 更改颜色
编辑第19-22行：

```latex
\definecolor{darkblue}{RGB}{0,51,102}    → 改为你想要的RGB值
\definecolor{lightblue}{RGB}{51,153,255}
```

### 推荐主题

| 主题名称 | 风格 | 适用场景 |
|---------|------|---------|
| Madrid ⭐ | 经典、专业 | 学术报告（当前使用） |
| Copenhagen | 现代、简洁 | 技术演讲 |
| Berlin | 清晰、醒目 | 课堂教学 |
| Dresden | 优雅、正式 | 会议展示 |
| AnnArbor | 传统、稳重 | 答辩 |

---

## ⚙️ 系统要求

### 本地编译需要：
- Python 3.x
- XeLaTeX（TeXLive 2020+或MiKTeX）
- 中文字体（宋体、黑体）

### 在线编译（Overleaf）：
- 只需浏览器
- 无需安装任何软件 ✨

---

## 🐛 常见问题

### Q1: 编译失败："Font not found"
**A**: 系统缺少中文字体

**解决方案**：
```latex
% 修改 WSN_Chapter1_Beamer.tex 第9-10行
\setCJKmainfont{SimSun}  → \setCJKmainfont{你系统的中文字体}
\setCJKsansfont{SimHei}  → \setCJKsansfont{你系统的黑体}

% macOS: 使用 STSong 和 STHeiti
% Linux: 使用 WenQuanYi Micro Hei 或 Noto Sans CJK SC
```

### Q2: 中文显示为方框
**A**: 未使用XeLaTeX编译

**解决方案**: 确保使用 `xelatex` 而非 `pdflatex`

### Q3: 动画不工作
**A**: PDF阅读器不支持动画

**解决方案**: 使用支持的阅读器：
- ✅ Adobe Acrobat Reader（最佳）
- ✅ Evince（Linux）
- ✅ Preview（macOS，部分支持）
- ❌ Chrome浏览器（不支持）

### Q4: 目录页码不正确
**A**: 需要编译两次

**解决方案**:
```bash
xelatex WSN_Chapter1_Beamer.tex
xelatex WSN_Chapter1_Beamer.tex  # 第二次
```

---

## 📖 详细文档

更多信息请参阅：
- **详细使用说明**: `BEAMER_README.md`
- **Beamer官方文档**: https://ctan.org/pkg/beamer
- **Overleaf教程**: https://www.overleaf.com/learn/latex/Beamer

---

## 🎓 演示技巧

### 课堂使用建议
1. **投影前测试**：确保动画在投影仪上正常工作
2. **使用翻页笔**：每次点击显示一项，控制节奏
3. **预览模式**：使用双屏模式查看备注
4. **PDF全屏**：F5或Ctrl+L进入全屏演示模式

### 动画节奏
- **慢速讲解**：逐项显示，每项详细讲解
- **快速浏览**：连续点击，快速过渡
- **重点强调**：在关键项处暂停，详细说明

---

## 📝 修改内容

### 修改源文档
1. 编辑 `第一章/PPT内容文档.md`
2. 重新运行 `python3 generate_beamer_ppt.py`
3. 重新编译LaTeX文件

### 直接修改LaTeX
- 优点：精确控制样式和布局
- 缺点：下次运行生成脚本会覆盖

---

## 🌟 最佳实践

1. ✅ **先生成，后微调**：自动生成后再手动调整细节
2. ✅ **保留源文件**：保存 `.tex` 文件方便以后修改
3. ✅ **版本控制**：使用Git管理不同版本
4. ✅ **备份PDF**：重新生成前备份当前版本

---

**祝你演示成功！** 🎉

如有问题，请查阅 `BEAMER_README.md` 获取更多帮助。
