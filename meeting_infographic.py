#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Meeting Infographic Generator
Creates a visually compelling infographic for weekly meeting content
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from datetime import datetime
import matplotlib.font_manager as fm

# 设置中文字体支持
import platform
if platform.system() == 'Darwin':  # macOS
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti SC', 'STHeiti', 'SimHei']
elif platform.system() == 'Windows':
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
else:  # Linux
    plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Set up the figure with professional styling
plt.rcParams['axes.edgecolor'] = '#2C3E50'
plt.rcParams['axes.linewidth'] = 0.5

# Create figure with more compact dimensions
fig, ax = plt.subplots(figsize=(12, 9))
fig.patch.set_facecolor('#F8F9FA')
ax.set_facecolor('#FFFFFF')

# Remove axes
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.axis('off')

# Color scheme - professional corporate palette
colors = {
    'primary': '#2C3E50',      # Dark blue-gray
    'accent1': '#E74C3C',      # Strategic red
    'accent2': '#F39C12',      # Achievement gold
    'accent3': '#27AE60',      # Success green
    'neutral': '#95A5A6',      # Gray
    'background': '#ECF0F1'    # Light background
}

# Header section - more compact
header_box = FancyBboxPatch((0.5, 8.2), 11, 0.7,
                           boxstyle="round,pad=0.05",
                           facecolor=colors['primary'],
                           edgecolor='none',
                           alpha=0.9)
ax.add_patch(header_box)

# Header text
ax.text(6, 8.55, '周会重点信息图',
        fontsize=18, fontweight='bold',
        color='white', ha='center', va='center')

# Date
current_date = datetime.now().strftime('%Y年%m月%d日')
ax.text(11.4, 8.55, current_date,
        fontsize=8, color='white',
        ha='right', va='center', alpha=0.8)

# Main content sections arranged in a more compact grid
sections = [
    {
        'title': '安全提醒',
        'content': '所有人出行注意保暖和安全',
        'position': (0.5, 7.0),
        'size': (3.4, 1.0),
        'color': colors['accent3']
    },
    {
        'title': '成绩亮点',
        'content': '生态链、大家电、手机各项成绩前列\n超预期表现',
        'position': (4.0, 7.0),
        'size': (3.4, 1.0),
        'color': colors['accent2']
    },
    {
        'title': '价值观优先',
        'content': '永远是分公司第一考量\n· 愿意给新人机会\n· 晋升/价值观优先\n· 定期清退损害利益人员',
        'position': (7.6, 7.0),
        'size': (3.4, 1.0),
        'color': colors['primary']
    },
    {
        'title': '新品挑战',
        'content': '当前挑战：56% TOP21/22，全国BOT',
        'position': (0.5, 5.5),
        'size': (5.2, 1.2),
        'color': colors['accent1']
    },
    {
        'title': '改善动作',
        'content': '· 门店宣传\n· 与合作商沟通交流\n· 提升合作商重视度\n· 后期整合含对投',
        'position': (6.3, 5.5),
        'size': (4.7, 1.2),
        'color': colors['accent2']
    },
    {
        'title': '市场动作',
        'content': '· 万人拍活动\n· 购机用户二次引流\n· 老带新策略',
        'position': (0.5, 3.8),
        'size': (3.4, 1.2),
        'color': colors['accent3']
    },
    {
        'title': '表彰大会',
        'content': '1月28日召开店长/总结大会\n对战功突出人员进行表彰',
        'position': (4.0, 3.8),
        'size': (3.4, 1.2),
        'color': colors['primary']
    },
    {
        'title': '时间线',
        'content': '当前 → 改善中 → 1月28日',
        'position': (7.6, 3.8),
        'size': (3.4, 1.2),
        'color': colors['neutral']
    }
]

# Create section boxes with professional styling
for section in sections:
    x, y = section['position']
    w, h = section['size']

    # Section box
    box = FancyBboxPatch((x, y), w, h,
                        boxstyle="round,pad=0.05",
                        facecolor=section['color'],
                        edgecolor=colors['primary'],
                        linewidth=0.8,
                        alpha=0.85)
    ax.add_patch(box)

    # Section title
    ax.text(x + w/2, y + h - 0.15, section['title'],
            fontsize=10, fontweight='bold',
            color='white', ha='center', va='top')

    # Section content
    ax.text(x + 0.15, y + h - 0.4, section['content'],
            fontsize=7, color='white',
            ha='left', va='top',
            linespacing=1.3)

# Add connecting lines to show flow (removed for compactness)
# connections = [
#     ((3.9, 7.5), (4.0, 7.5)),  # From safety to achievements
#     ((7.5, 7.5), (7.6, 7.5)), # From achievements to values
# ]

# for start, end in connections:
#     ax.plot([start[0], end[0]], [start[1], end[1]],
#             color=colors['neutral'], linewidth=1, alpha=0.4)

# Footer with company info - more compact
footer_text = "分公司周会信息图 • " + current_date
ax.text(6, 0.3, footer_text,
        fontsize=7, color=colors['neutral'],
        ha='center', va='center', alpha=0.6)

# Ensure tight layout and professional spacing
plt.tight_layout()
plt.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.05)

# Save as high-quality PNG
plt.savefig('/Users/tigerqiao/my-notion-html/meeting_infographic_compact.png',
            dpi=300, bbox_inches='tight',
            facecolor=fig.get_facecolor(),
            edgecolor='none')

plt.show()
print("Infographic created successfully at: /Users/tigerqiao/my-notion-html/meeting_infographic_compact.png")