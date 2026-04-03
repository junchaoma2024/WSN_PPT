#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Beamer PPT生成器
从PPT内容文档.md自动生成LaTeX Beamer演示文稿
"""

import re
import os

class BeamerGenerator:
    def __init__(self, md_file):
        self.md_file = md_file
        self.slides = []
        self.current_section = None

    def parse_markdown(self):
        """解析Markdown文档"""
        with open(self.md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 按---分割每一页
        pages = re.split(r'\n---+\n', content)

        for page in pages:
            if not page.strip():
                continue

            slide_data = self.parse_slide(page)
            if slide_data:
                self.slides.append(slide_data)

        return self.slides

    def parse_slide(self, page_content):
        """解析单页PPT内容"""
        lines = page_content.strip().split('\n')

        slide = {
            'title': '',
            'subtitle': '',
            'content': [],
            'table': None,
            'design_notes': '',
            'notes': ''
        }

        current_section = None
        table_lines = []
        in_table = False

        for line in lines:
            line_stripped = line.strip()

            # 检测表格
            if line_stripped.startswith('|') and '|' in line_stripped[1:]:
                if not in_table:
                    in_table = True
                    table_lines = []
                table_lines.append(line_stripped)
                continue
            elif in_table and not line_stripped.startswith('|'):
                # 表格结束
                if table_lines:
                    slide['table'] = self.parse_table(table_lines)
                    table_lines = []
                in_table = False

            # 提取标题
            if line_stripped.startswith('### '):
                # 这是章节标题，跳过
                continue
            elif line_stripped.startswith('**【标题】**'):
                slide['title'] = line_stripped.replace('**【标题】**', '').strip()
            elif line_stripped.startswith('**【内容要点】**'):
                current_section = 'content'
            elif line_stripped.startswith('**【PPT设计建议】**'):
                current_section = 'design'
            elif line_stripped.startswith('**【备注】**'):
                current_section = 'notes'
            elif line_stripped.startswith('## ') and '部分' in line_stripped:
                # 这是章节分隔，记录section
                self.current_section = line_stripped.replace('##', '').strip()
            elif current_section == 'content' and line_stripped.startswith('•'):
                # 内容要点
                slide['content'].append(line_stripped[1:].strip())
            elif current_section == 'content' and line_stripped.startswith('-'):
                # 子要点
                slide['content'].append('  ' + line_stripped[1:].strip())
            elif current_section == 'design':
                slide['design_notes'] += line_stripped + ' '
            elif current_section == 'notes':
                slide['notes'] += line_stripped + ' '

        # 处理最后的表格
        if in_table and table_lines:
            slide['table'] = self.parse_table(table_lines)

        # 只返回有标题或内容的slide
        if slide['title'] or slide['content'] or slide['table']:
            return slide
        return None

    def parse_table(self, table_lines):
        """解析Markdown表格"""
        if len(table_lines) < 2:
            return None

        # 第一行是表头
        header = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]

        # 第二行是分隔符，跳过
        # 从第三行开始是数据
        rows = []
        for line in table_lines[2:]:
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if cells:
                rows.append(cells)

        return {
            'header': header,
            'rows': rows,
            'column_count': len(header)
        }

    def generate_beamer_header(self):
        """生成Beamer文档头"""
        header = r"""\documentclass[aspectratio=43]{beamer}

% 使用主题
\usetheme{Madrid}
\usecolortheme{default}

% 中文支持
\usepackage{xeCJK}
\setCJKmainfont{SimSun}  % 宋体
\setCJKsansfont{SimHei}  % 黑体

% 其他包
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tikz}
\usepackage{amsmath}

% 设置颜色
\definecolor{darkblue}{RGB}{0,51,102}
\definecolor{lightblue}{RGB}{51,153,255}
\setbeamercolor{structure}{fg=darkblue}
\setbeamercolor{frametitle}{fg=white,bg=darkblue}

% 页脚设置
\setbeamertemplate{footline}[frame number]

% 导航符号
\setbeamertemplate{navigation symbols}{}

% 标题信息
\title{传感器网络技术与应用}
\subtitle{第一章：无线传感器网络概述与基本架构}
\author{马俊超}
\institute{江苏理工学院 电信学院信息工程系}
\date{\today}

\begin{document}

% 标题页
\begin{frame}
  \titlepage
\end{frame}

% 目录
\begin{frame}{目录}
  \tableofcontents
\end{frame}

"""
        return header

    def generate_beamer_footer(self):
        """生成Beamer文档尾"""
        return r"""
\end{document}
"""

    def escape_latex(self, text):
        """转义LaTeX特殊字符"""
        # 基本转义
        replacements = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}',
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text

    def format_content_item(self, item, level=0):
        """格式化内容项，添加动画效果"""
        # 判断缩进级别
        indent = '  ' * level

        # 清理前导空格来判断实际级别
        clean_item = item.lstrip()
        actual_indent = len(item) - len(clean_item)

        if actual_indent > 2:
            # 子项
            return f"    \\item<+-> {self.escape_latex(clean_item)}"
        else:
            # 主项
            return f"  \\item<+-> {self.escape_latex(clean_item)}"

    def generate_table(self, table_data):
        """生成表格的LaTeX代码"""
        if not table_data:
            return ""

        col_count = table_data['column_count']
        # 使用l（左对齐）作为默认对齐方式
        col_spec = 'l' * col_count

        latex = "  \\begin{table}\n"
        latex += "    \\centering\n"
        latex += "    \\small\n"  # 使用较小字体
        latex += f"    \\begin{{tabular}}{{{col_spec}}}\n"
        latex += "      \\toprule\n"

        # 表头
        header_cells = [self.escape_latex(cell) for cell in table_data['header']]
        latex += "      " + " & ".join(header_cells) + " \\\\\n"
        latex += "      \\midrule\n"

        # 数据行（添加动画效果）
        for i, row in enumerate(table_data['rows']):
            row_cells = [self.escape_latex(cell) for cell in row]
            # 添加逐行显示动画
            latex += f"      \\onslide<{i+1}->{{" + " & ".join(row_cells) + " \\\\}\n"

        latex += "      \\bottomrule\n"
        latex += "    \\end{tabular}\n"
        latex += "  \\end{table}\n"

        return latex

    def generate_slide(self, slide_data):
        """生成单个幻灯片的LaTeX代码"""
        if not slide_data['title']:
            return ""

        # 开始frame（如果有表格，需要添加allowframebreaks选项）
        if slide_data['table']:
            latex = "\\begin{frame}[allowframebreaks]\n"
        else:
            latex = "\\begin{frame}\n"

        latex += f"  \\frametitle{{{self.escape_latex(slide_data['title'])}}}\n\n"

        # 内容
        if slide_data['content']:
            latex += "  \\begin{itemize}\n"
            for item in slide_data['content']:
                latex += self.format_content_item(item) + "\n"
            latex += "  \\end{itemize}\n"

        # 表格
        if slide_data['table']:
            if slide_data['content']:
                latex += "\n  \\vspace{0.3cm}\n\n"  # 添加间距
            latex += self.generate_table(slide_data['table'])

        # 结束frame
        latex += "\\end{frame}\n\n"

        return latex

    def generate_section_slide(self, section_title):
        """生成章节分隔幻灯片"""
        latex = "\\section{" + self.escape_latex(section_title) + "}\n"
        latex += "\\begin{frame}\n"
        latex += "  \\begin{center}\n"
        latex += "    \\Huge " + self.escape_latex(section_title) + "\n"
        latex += "  \\end{center}\n"
        latex += "\\end{frame}\n\n"
        return latex

    def generate_beamer(self, output_file):
        """生成完整的Beamer文档"""
        # 解析markdown
        print("正在解析Markdown文档...")
        self.parse_markdown()
        print(f"共解析到 {len(self.slides)} 页PPT")

        # 生成LaTeX代码
        print("正在生成Beamer LaTeX代码...")
        latex_content = self.generate_beamer_header()

        # 记录章节
        sections = {
            '第一部分': '课程绪论',
            '第二部分': '无线传感器网络基本架构'
        }

        current_section_added = set()

        for i, slide in enumerate(self.slides):
            # 检查是否需要添加章节
            if i == 20 and '第二部分' not in current_section_added:
                latex_content += self.generate_section_slide("无线传感器网络基本架构")
                current_section_added.add('第二部分')
            elif i == 0:
                latex_content += "\\section{课程绪论}\n\n"
                current_section_added.add('第一部分')

            latex_content += self.generate_slide(slide)

        latex_content += self.generate_beamer_footer()

        # 写入文件
        print(f"正在写入文件 {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)

        print(f"✓ Beamer LaTeX文件生成成功: {output_file}")
        print(f"\n编译说明:")
        print(f"  使用XeLaTeX编译: xelatex {output_file}")
        print(f"  或使用: xelatex {output_file} && xelatex {output_file}")
        print(f"  （编译两次以生成正确的目录和引用）")


def main():
    # 输入输出文件
    md_file = "第一章/PPT内容文档.md"
    output_file = "第一章/WSN_Chapter1_Beamer.tex"

    if not os.path.exists(md_file):
        print(f"错误: 找不到文件 {md_file}")
        return

    # 生成Beamer
    generator = BeamerGenerator(md_file)
    generator.generate_beamer(output_file)


if __name__ == "__main__":
    main()
