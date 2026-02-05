#!/bin/bash
# Beamer PPT编译脚本

echo "=========================================="
echo "Beamer PPT 编译工具"
echo "=========================================="
echo ""

# 检查xelatex是否安装
if ! command -v xelatex &> /dev/null; then
    echo "❌ 错误: 未找到xelatex命令"
    echo ""
    echo "请先安装LaTeX发行版："
    echo "  Ubuntu/Debian: sudo apt-get install texlive-xetex texlive-latex-extra"
    echo "  macOS: brew install --cask mactex"
    echo "  或访问 https://www.overleaf.com/ 在线编译"
    exit 1
fi

# 切换到第一章目录
cd 第一章 || exit 1

TEX_FILE="WSN_Chapter1_Beamer.tex"

if [ ! -f "$TEX_FILE" ]; then
    echo "❌ 错误: 找不到文件 $TEX_FILE"
    echo "请先运行: python3 ../generate_beamer_ppt.py"
    exit 1
fi

echo "📄 正在编译: $TEX_FILE"
echo ""

# 第一次编译
echo "🔄 第一次编译（生成目录）..."
xelatex -interaction=nonstopmode "$TEX_FILE" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ 第一次编译完成"
else
    echo "❌ 第一次编译失败，查看详细错误："
    xelatex "$TEX_FILE"
    exit 1
fi

# 第二次编译
echo "🔄 第二次编译（更新引用）..."
xelatex -interaction=nonstopmode "$TEX_FILE" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✅ 第二次编译完成"
else
    echo "❌ 第二次编译失败，查看详细错误："
    xelatex "$TEX_FILE"
    exit 1
fi

# 清理临时文件
echo "🧹 清理临时文件..."
rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

PDF_FILE="${TEX_FILE%.tex}.pdf"

if [ -f "$PDF_FILE" ]; then
    echo ""
    echo "=========================================="
    echo "✅ 编译成功！"
    echo "=========================================="
    echo ""
    echo "📊 生成的PDF文件: 第一章/$PDF_FILE"
    echo ""

    # 尝试获取PDF信息
    if command -v pdfinfo &> /dev/null; then
        PAGES=$(pdfinfo "$PDF_FILE" 2>/dev/null | grep "Pages:" | awk '{print $2}')
        if [ -n "$PAGES" ]; then
            echo "📄 总页数: $PAGES"
        fi
    fi

    echo ""
    echo "💡 提示："
    echo "  - 使用PDF阅读器打开查看动画效果"
    echo "  - 推荐使用Adobe Acrobat Reader以获得最佳动画体验"
    echo ""
else
    echo "❌ 编译失败：未生成PDF文件"
    exit 1
fi
