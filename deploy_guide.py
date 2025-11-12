#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
古文虚实词练习页面 - 免费托管部署指南

本脚本提供将HTML页面部署到各种免费托管服务的详细步骤和命令。
"""

import os
import platform
import subprocess
import sys

# 定义不同托管服务的部署指南
deployment_guides = {
    "github_pages": {
        "name": "GitHub Pages",
        "website": "https://pages.github.com/",
        "steps": [
            "1. 在GitHub上创建一个新的仓库（可以是公共或私有仓库）",
            "2. 初始化本地git仓库并提交文件：",
            "   git init",
            "   git add wz.html",
            "   git commit -m '初始提交：古文虚实词练习页面'",
            "3. 连接到GitHub仓库：",
            "   git remote add origin https://github.com/你的用户名/你的仓库名.git",
            "4. 推送到GitHub：",
            "   git push -u origin main",
            "5. 在GitHub仓库设置中启用GitHub Pages，选择main分支",
            "6. 部署后访问地址：https://你的用户名.github.io/你的仓库名/wz.html"
        ],
        "pros": ["完全免费", "无流量限制", "与GitHub集成", "支持自定义域名"],
        "cons": ["部署速度较慢（通常需要几分钟）", "不支持服务器端代码"]
    },
    "netlify": {
        "name": "Netlify",
        "website": "https://www.netlify.com/",
        "steps": [
            "1. 访问 Netlify 官网并注册/登录账号",
            "2. 点击 'New site from Git' 按钮",
            "3. 选择 'GitHub' 并授权",
            "4. 选择你的仓库",
            "5. 配置部署设置（保持默认即可）：",
            "   - Build Command: 留空（静态网站）",
            "   - Publish Directory: 留空（根目录）",
            "6. 点击 'Deploy Site' 按钮",
            "7. 部署后可设置自定义域名"
        ],
        "pros": ["免费计划慷慨", "部署速度快", "自动HTTPS", "预览部署", "分支部署"],
        "cons": ["免费版有带宽限制（每月100GB）", "一些高级功能需付费"]
    },
    "vercel": {
        "name": "Vercel",
        "website": "https://vercel.com/",
        "steps": [
            "1. 访问 Vercel 官网并注册/登录账号",
            "2. 点击 'New Project' 按钮",
            "3. 导入你的GitHub仓库",
            "4. 保持默认设置，点击 'Deploy'",
            "5. 部署完成后可获得免费的vercel.app子域名"
        ],
        "pros": ["免费计划丰富", "部署速度极快", "自动HTTPS", "预览URL", "团队协作"],
        "cons": ["免费版有一些限制", "主要针对前端项目优化"]
    },
    "coding_pages": {
        "name": "Coding Pages（腾讯云开发者平台）",
        "website": "https://coding.net/",
        "steps": [
            "1. 注册/登录 Coding 账号",
            "2. 创建一个新项目和代码仓库",
            "3. 将HTML文件上传到仓库",
            "4. 在项目设置中找到 '静态网站' 或 'Coding Pages' 选项",
            "5. 选择分支并启用静态网站服务",
            "6. 获取访问域名"
        ],
        "pros": ["国内访问速度快", "免费额度充足", "支持自定义域名", "提供免费SSL证书"],
        "cons": ["需要实名认证", "部分功能可能不如GitHub Pages成熟"]
    },
    "gitee_pages": {
        "name": "Gitee Pages（码云）",
        "website": "https://gitee.com/",
        "steps": [
            "1. 注册/登录 Gitee 账号",
            "2. 创建一个新仓库",
            "3. 上传 wz.html 文件",
            "4. 进入仓库，点击 '服务' -> 'Gitee Pages'",
            "5. 选择分支并点击 '启动服务'",
            "6. 获取访问地址"
        ],
        "pros": ["国内访问速度快", "部署简单", "免费使用"],
        "cons": ["免费版需实名认证", "每个账号限制创建5个Pages站点", "部分功能受限"]
    }
}

def print_header():
    """打印脚本头部信息"""
    header = """
    ===================================================
                古文虚实词练习页面部署指南
    ===================================================
    
    本指南提供了将HTML页面部署到各种免费托管服务的详细步骤，
    以实现页面的长期稳定访问，无需依赖本地服务器。
    """
    print(header)

def print_guide(guide):
    """打印指定托管服务的详细部署指南"""
    print(f"\n[服务] {guide['name']}")
    print(f"[官网] {guide['website']}")
    print("\n[部署步骤]:")
    for step in guide['steps']:
        print(f"  {step}")
    print("\n[优点]:")
    for pro in guide['pros']:
        print(f"  ✅ {pro}")
    print("\n[缺点]:")
    for con in guide['cons']:
        print(f"  ❌ {con}")
    print("\n" + "="*50)

def create_gitignore():
    """创建.gitignore文件"""
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# 操作系统文件
.DS_Store
Thumbs.db

# 编辑器文件
.idea/
.vscode/
*.swp
*.swo
*~

# 环境变量
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# 日志
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# 其他
qrcode.png
"""
    
    if not os.path.exists('.gitignore'):
        with open('.gitignore', 'w', encoding='utf-8') as f:
            f.write(gitignore_content.strip())
        print("已创建 .gitignore 文件")
    else:
        print(".gitignore 文件已存在")

def main():
    """主函数"""
    print_header()
    
    # 创建合理的.gitignore文件
    create_gitignore()
    
    print("\n以下是几种推荐的免费托管服务：")
    
    # 打印所有服务的简要信息
    for i, (key, guide) in enumerate(deployment_guides.items(), 1):
        print(f"{i}. {guide['name']}")
    
    # 打印所有服务的详细指南
    print("\n\n详细部署指南：")
    for guide in deployment_guides.values():
        print_guide(guide)
    
    print("\n\n部署完成后，您可以：")
    print("1. 使用新的在线URL更新二维码")
    print("2. 分享链接给用户或学生")
    print("3. 随时更新代码并重新部署")
    print("\n提示：对于微信环境，建议使用国内服务（如Gitee Pages或Coding Pages）以获得更好的访问体验。")

if __name__ == "__main__":
    main()