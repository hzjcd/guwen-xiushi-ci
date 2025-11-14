#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
古文虚实词练习页面 - GitHub Pages 部署脚本（增强版）

本脚本自动执行将HTML页面部署到GitHub Pages的流程，包括：
1. 检查Git环境和配置
2. 初始化Git仓库
3. 添加文件并提交
4. 连接到GitHub仓库
5. 推送到GitHub
6. 提供启用GitHub Pages的指引

增强功能：
- 交互式输入GitHub信息
- 更完善的错误处理
- 详细的部署日志
- 支持多种身份验证方式
- 自动处理常见部署问题
"""

import os
import subprocess
import sys
import time
import re

def print_title(title):
    """打印带分隔符的标题"""
    print(f"\n{'-' * 60}")
    print(f"{title.center(60)}")
    print(f"{'-' * 60}")

def run_command(command, cwd=None, quiet=False):
    """执行命令并返回结果，处理编码问题"""
    if not quiet:
        print(f"执行命令: {command}")
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd, 
            check=False,  # 设置为False以便自定义错误处理
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        
        # 输出标准输出
        if result.stdout and not quiet:
            print(f"输出: {result.stdout.strip()}")
            
        # 输出错误输出（如果有）
        if result.stderr and not quiet:
            print(f"错误输出: {result.stderr.strip()}")
            
        # 检查返回码
        if result.returncode != 0 and not quiet:
            print(f"命令执行失败，返回码: {result.returncode}")
            
        return {
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        }
    except Exception as e:
        if not quiet:
            print(f"执行命令时发生异常: {str(e)}")
        return {
            'stdout': '',
            'stderr': str(e),
            'returncode': 1
        }

def check_git_installed():
    """检查Git是否安装并返回版本信息"""
    print("检查Git是否已安装...")
    result = run_command("git --version")
    
    if result['returncode'] == 0:
        version_match = re.search(r'git version (\S+)', result['stdout'])
        if version_match:
            version = version_match.group(1)
            print(f"✅ Git已安装: {version}")
            return True, version
        else:
            print("⚠️ Git已安装，但无法识别版本")
            return True, "unknown"
    else:
        print("❌ Git未安装！")
        print("请先安装Git: https://git-scm.com/")
        return False, None

def check_git_config():
    """检查Git配置并返回用户名和邮箱（自动模式）"""
    print("检查Git配置...")
    name_result = run_command("git config user.name")
    email_result = run_command("git config user.email")
    
    name = name_result['stdout'].strip() if name_result['returncode'] == 0 else ""
    email = email_result['stdout'].strip() if email_result['returncode'] == 0 else ""
    
    if not name or not email:
        print("❌ Git配置不完整！自动设置默认配置...")
        # 自动设置默认配置
        name = "hzjcd"
        email = "3357883100@qq.com"
        run_command(f"git config --global user.name '{name}'")
        run_command(f"git config --global user.email '{email}'")
        print(f"✅ Git配置已自动设置为：")
        print(f"• 用户名: {name}")
        print(f"• 邮箱: {email}")
    else:
        print(f"✅ Git用户名: {name}")
        print(f"✅ Git邮箱: {email}")
    
    return True, name, email

def check_git_credentials():
    """检查Git凭证管理器（自动模式）"""
    print("检查Git凭证管理器...")
    # 检查Windows凭证管理器并自动配置
    if sys.platform.startswith('win'):
        result = run_command("git config credential.helper", quiet=True)
        if 'manager' not in result['stdout']:
            print("⚠️ 自动配置Git凭证管理器以便保存GitHub密码")
            run_command("git config --global credential.helper manager")
            print("✅ Git凭证管理器已配置")
    return True

def check_required_files():
    """检查必要文件是否存在（自动模式）"""
    print("检查必要文件...")
    
    files_to_check = ['html_files/wz.html']
    missing_files = []
    
    for file in files_to_check:
        if not os.path.exists(file):
            missing_files.append(file)
            print(f"❌ 缺少文件: {file}")
        else:
            print(f"✅ 找到文件: {file}")
    
    # 如果缺少.gitignore，自动创建
    if not os.path.exists('.gitignore'):
        print("⚠️ 缺少.gitignore文件，自动创建...")
        with open('.gitignore', 'w', encoding='utf-8') as f:
            f.write("# 操作系统文件\n.DS_Store\nThumbs.db\n\n# IDE文件\n.idea/\n.vscode/\n*.swp\n*.swo\n*~\n\n# 临时文件\n*.tmp\n*.temp\n\n# Python文件\n__pycache__/\n*.pyc\n\n# 环境变量\n.env\n.env.local\n.env.development.local\n.env.test.local\n.env.production.local\n")
        print("✅ .gitignore文件已自动创建")
    else:
        print(f"✅ 找到文件: .gitignore")
    
    return len(missing_files) == 0

def initialize_git_repo():
    """初始化Git仓库（自动模式）"""
    if os.path.exists('.git'):
        print("ℹ️ Git仓库已存在")
        # 自动提交所有未提交的更改
        status = run_command("git status --porcelain")
        if status['stdout'].strip():
            print("⚠️ 仓库中有未提交的更改，自动提交...")
            run_command("git add .")
            run_command("git commit -m '自动提交：更新文件'")
        return True
    
    print("初始化Git仓库...")
    result = run_command("git init")
    if result['returncode'] == 0:
        print("✅ Git仓库初始化成功")
        return True
    else:
        print("❌ Git仓库初始化失败！")
        return False

def remove_zz_file():
    """从Git仓库中移除zz.html文件"""
    print("从Git仓库中移除zz.html文件...")
    # 检查zz.html是否在Git跟踪中
    result = run_command("git ls-files | grep zz.html")
    if result['stdout'].strip() == 'zz.html':
        # 从Git中移除文件
        result = run_command("git rm zz.html")
        if result['returncode'] == 0:
            print("✅ 成功从Git仓库中移除zz.html文件")
            return True
        else:
            print(f"❌ 从Git仓库中移除zz.html文件失败: {result['stderr']}")
            return False
    else:
        print("ℹ️ zz.html文件不在Git仓库中，跳过移除操作")
        return True

def add_and_commit_files():
    """添加文件并提交"""
    print("添加文件到Git...")
    result = run_command("git add html_files/wz.html .gitignore html_files/")
    
    if result['returncode'] != 0:
        print("⚠️ 添加文件可能失败，尝试添加所有文件")
        run_command("git add .")
    
    print("提交文件...")
    commit_result = run_command("git commit -m '初始提交：古文虚实词练习页面'")
    
    if commit_result['returncode'] != 0:
        if "nothing to commit" in commit_result['stderr'] or "nothing to commit" in commit_result['stdout']:
            print("ℹ️ 没有新文件需要提交")
            return True
        else:
            print(f"⚠️ 提交遇到问题，但将继续执行: {commit_result['stderr']}")
    else:
        print("✅ 文件提交成功")
    
    return True

def get_github_info(saved_username=None, saved_repo=None):
    """获取GitHub用户名和仓库名（自动模式）"""
    print("\n自动配置GitHub信息：")
    
    # 直接使用预设值
    username = "hzjcd"
    repo_name = "guwen-xiushi-ci"
    
    print(f"• GitHub用户名: {username}")
    print(f"• 仓库名称: {repo_name}")
    
    return username, repo_name

def create_github_repo(username, repo_name):
    """提示用户在GitHub上创建仓库（自动模式）"""
    print_title("在GitHub上创建仓库")
    print(f"请确保你已经在GitHub上创建了仓库：")
    print(f"1. 打开 https://github.com/new")
    print(f"2. 仓库名称输入: {repo_name}")
    print(f"3. 选择公开或私有仓库")
    print(f"4. 不要初始化README、.gitignore或许可证")
    print(f"5. 点击'Create repository'")
    
    print("\n重要提示：")
    print("• 如果你尚未创建仓库，推送步骤将会失败")
    print("• 请确保你已登录GitHub账户")
    print("• 3秒后继续执行...")
    
    # 等待3秒自动继续
    time.sleep(3)
    
    return f"https://github.com/{username}/{repo_name}.git"

def connect_and_push(repo_url):
    """连接到GitHub仓库并推送"""
    print_title("连接到GitHub并推送")
    
    # 检查并配置分支
    branch_result = run_command("git branch --show-current")
    current_branch = branch_result['stdout'].strip() if branch_result['returncode'] == 0 else ""
    
    if not current_branch:
        print("创建main分支...")
        run_command("git checkout -b main")
        current_branch = "main"
    
    print(f"当前分支: {current_branch}")
    
    # 检查是否已存在远程仓库
    remotes = run_command("git remote -v")
    
    if "origin" in remotes['stdout']:
        print("远程仓库已存在，更新URL...")
        run_command(f"git remote set-url origin {repo_url}")
    else:
        print("添加远程仓库...")
        run_command(f"git remote add origin {repo_url}")
    
    # 提示用户关于身份验证
    print("\nℹ️ 推送时可能需要输入GitHub凭证")
    print("• 对于HTTPS连接，你可以使用个人访问令牌(PAT)作为密码")
    print("• 如果你忘记密码，可以使用GitHub网页版创建个人访问令牌")
    print("• 个人访问令牌创建地址: https://github.com/settings/tokens")
    
    # 先尝试拉取（如果远程已有内容）
    print("\n尝试拉取远程内容...")
    pull_result = run_command(f"git pull origin {current_branch} --allow-unrelated-histories")
    
    # 推送本地分支到远程
    print(f"\n推送文件到GitHub {current_branch} 分支...")
    push_result = run_command(f"git push -u origin {current_branch}")
    
    if push_result['returncode'] == 0:
        print("✅ 推送成功！")
        return True
    else:
        print("❌ 推送失败！")
        print("\n错误详情：")
        print(push_result['stderr'] or push_result['stdout'])
        
        # 提供故障排除建议
        print("\n故障排除建议：")
        if "403" in push_result['stderr'] or "403" in push_result['stdout']:
            print("• 检查你的GitHub凭证是否正确")
            print("• 尝试使用个人访问令牌代替密码")
            print("• 确保你的账户有权限访问该仓库")
        elif "not found" in push_result['stderr'] or "not found" in push_result['stdout']:
            print("• 确保仓库已在GitHub上创建")
            print("• 检查用户名和仓库名是否正确")
        elif "updates were rejected" in push_result['stderr']:
            print("• 远程仓库可能有你本地没有的内容")
            print("• 尝试先拉取远程内容，解决冲突后再推送")
        
        return False

def show_github_pages_instructions(username, repo_name):
    """显示启用GitHub Pages的指引"""
    print_title("启用GitHub Pages")
    print("请按照以下步骤启用GitHub Pages：")
    print(f"1. 访问你的GitHub仓库页面: https://github.com/{username}/{repo_name}")
    print("2. 点击顶部导航栏中的'Settings'")
    print("3. 在左侧菜单中找到'Pages'")
    print("4. 在'Source'部分，选择'Branch: main'，然后点击'Save'")
    print("5. 稍等几分钟，GitHub Pages会自动构建你的站点")
    
    print("\n✅ 部署成功后，你的页面将可以通过以下地址访问：")
    print(f"https://{username}.github.io/{repo_name}/html_files/wz.html")
    
    print("\n🔄 后续更新步骤：")
    print("1. 修改本地html_files/wz.html文件")
    print("2. 运行: git add html_files/wz.html")
    print("3. 运行: git commit -m '更新内容'")
    print("4. 运行: git push origin main")
    print("5. 等待GitHub Pages重新构建")

def main():
    """主函数"""
    print_title("古文虚实词练习页面 - GitHub Pages 部署脚本")
    
    # 步骤1: 检查环境
    print_title("环境检查")
    git_installed, git_version = check_git_installed()
    if not git_installed:
        print("\n❌ 部署失败：请先安装Git")
        return
    
    git_config_valid, git_name, git_email = check_git_config()
    if not git_config_valid:
        print("\n❌ 部署失败：请先配置Git用户名和邮箱")
        return
    
    # 步骤2: 准备工作
    print_title("准备工作")
    check_git_credentials()
    
    # 从Git仓库中移除zz.html文件（如果存在）
    remove_zz_file()
        
    if not check_required_files():
        print("\n❌ 部署失败：缺少必要文件")
        return
    
    # 步骤3: Git操作
    print_title("Git操作")
    if not initialize_git_repo():
        print("\n❌ 部署失败：Git仓库初始化失败")
        return
    
    add_and_commit_files()
    
    # 步骤4: GitHub配置
    print_title("GitHub配置")
    # 使用检测到的Git用户名作为默认GitHub用户名
    default_username = git_name
    default_repo = "guwen-xiushi-ci"
    
    username, repo_name = get_github_info(default_username, default_repo)
    
    print(f"\n使用以下GitHub信息：")
    print(f"• 用户名: {username}")
    print(f"• 仓库名: {repo_name}")
    
    # 步骤5: 创建仓库和推送
    repo_url = create_github_repo(username, repo_name)
    
    print_title("开始部署")
    push_success = connect_and_push(repo_url)
    
    if push_success:
        # 步骤6: 显示启用GitHub Pages的指引
        show_github_pages_instructions(username, repo_name)
        
        print("\n" + "="*60)
        print("🎉 部署流程已完成！")
        print("="*60)
        print("\n📝 重要提醒：")
        print("• GitHub Pages可能需要1-10分钟来构建和发布你的站点")
        print("• 如果遇到访问问题，请检查GitHub Pages设置是否正确")
        print("• 对于微信环境访问，GitHub Pages可能有兼容性问题")
        print("• 如需在微信中正常访问，建议考虑使用Gitee Pages或Coding Pages")
    else:
        print("\n" + "="*60)
        print("❌ 部署流程未完成，请解决上述问题后重试")
        print("="*60)
        print("\n🔄 你可以重新运行此脚本来再次尝试部署")

if __name__ == "__main__":
    main()
