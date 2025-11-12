# 古文虚实词练习页面 - GitHub Pages 部署指南

## 📋 概述

本文档提供了使用增强版部署脚本将`wz.html`页面部署到GitHub Pages的详细指南。脚本设计为全交互式，可自动处理部署过程中的常见问题，并提供详细的指导。

## 🚀 部署脚本功能

增强版部署脚本(`deploy_to_github_pages.py`)具有以下功能：

- ✅ 自动检查Git环境和配置
- ✅ 交互式输入GitHub信息
- ✅ 自动初始化Git仓库并管理文件
- ✅ 提供详细的错误处理和故障排除建议
- ✅ 支持多种身份验证方式（密码/PAT）
- ✅ 自动处理常见的Git和GitHub问题
- ✅ 提供启用GitHub Pages的完整步骤
- ✅ 自动检测并创建缺失的`.gitignore`文件
- ✅ 支持处理已存在的仓库和未提交的更改

## 📁 文件准备

在运行部署脚本前，请确保以下文件存在于当前目录：

- `wz.html` - 古文虚实词练习页面
- `.gitignore` - Git忽略文件（脚本会自动创建）
- `deploy_to_github_pages.py` - 部署脚本

## 🛠️ 环境要求

- **Git**: 已安装并配置（脚本会自动检查）
- **Python**: 3.6或更高版本
- **GitHub账户**: 已注册的GitHub账号

## 📝 使用步骤

### 第1步：运行部署脚本

在命令行中执行以下命令：

```bash
python deploy_to_github_pages.py
```

### 第2步：环境检查

脚本会自动执行以下检查：

- **Git版本检查**：确认Git已正确安装
- **Git配置检查**：验证用户名和邮箱设置
- **凭证管理器检查**：在Windows系统上建议配置凭证管理器
- **必要文件检查**：确保`wz.html`和`.gitignore`文件存在

如果检查不通过，脚本会提供修复建议并允许你在交互式界面中进行设置。

### 第3步：Git仓库管理

- 如果Git仓库已存在，脚本会检查是否有未提交的更改
- 如需要，你可以选择提交这些更改
- 脚本会自动添加和提交`wz.html`和`.gitignore`文件

### 第4步：GitHub信息配置

脚本会提示你输入GitHub信息：

```
请输入GitHub信息：
GitHub用户名 [hzjcd]: 
仓库名称 [guwen-xiushi-ci]: 
```

你可以直接按Enter使用默认值，或输入自定义信息。

### 第5步：创建GitHub仓库

脚本会提供在GitHub网站上创建仓库的详细步骤：

1. 打开 https://github.com/new
2. 输入仓库名称
3. 选择公开或私有仓库
4. 不要初始化README、.gitignore或许可证
5. 点击"Create repository"

完成后按Enter继续。

### 第6步：推送代码

脚本会：
- 检查并配置Git分支
- 添加远程仓库
- 尝试拉取远程内容（如果有）
- 推送本地代码到GitHub

**重要**：推送时可能需要输入GitHub凭证。如果你忘记密码，可以使用个人访问令牌(PAT)代替。

### 第7步：启用GitHub Pages

部署成功后，脚本会显示启用GitHub Pages的详细步骤：

1. 访问你的GitHub仓库页面
2. 点击"Settings"
3. 找到"Pages"选项
4. 选择"Branch: main"作为源
5. 点击"Save"

## 🌐 访问你的页面

部署成功并启用GitHub Pages后，你的页面将通过以下地址访问：

```
https://[username].github.io/[repo_name]/wz.html
```

例如：
```
https://hzjcd.github.io/guwen-xiushi-ci/wz.html
```

**注意**：GitHub Pages可能需要1-10分钟来构建和发布你的站点。

## 🔄 后续更新

要更新已部署的页面：

1. 修改本地的`wz.html`文件
2. 运行以下Git命令：
   ```bash
   git add wz.html
   git commit -m "更新内容"
   git push origin main
   ```
3. 等待GitHub Pages重新构建（通常1-2分钟）

## ❓ 常见问题与解决方案

### 1. 推送失败，提示403错误

**原因**：访问权限问题

**解决方案**：
- 检查你的GitHub用户名和密码是否正确
- 尝试使用个人访问令牌(PAT)代替密码
- 确保你有权限访问该仓库

### 2. 推送失败，提示仓库未找到

**原因**：GitHub上尚未创建仓库或名称错误

**解决方案**：
- 确保已在GitHub上创建了正确名称的仓库
- 检查输入的用户名和仓库名是否正确

### 3. 推送失败，提示更新被拒绝

**原因**：远程仓库有本地没有的内容

**解决方案**：
- 先运行`git pull origin main --allow-unrelated-histories`
- 解决可能的合并冲突
- 然后重新尝试推送

### 4. GitHub Pages不显示页面

**原因**：可能未正确配置或构建未完成

**解决方案**：
- 确认GitHub Pages设置中的分支选择正确（应为main）
- 等待几分钟让GitHub完成构建
- 检查仓库中是否包含`wz.html`文件

### 5. 在微信中无法访问GitHub Pages

**原因**：微信对GitHub Pages有兼容性限制

**解决方案**：
- 考虑使用Gitee Pages或Coding Pages进行部署
- 这些国内托管服务在微信环境中通常有更好的兼容性

## 📱 微信环境特别说明

由于微信浏览器的限制，GitHub Pages在微信中可能无法正常访问。推荐的替代方案：

1. **Gitee Pages**：国内访问速度快，微信兼容性好
2. **Coding Pages**：同样具有良好的国内访问体验
3. **本地服务器方案**：使用`host_and_generate_qrcode.py`脚本在本地启动服务

## 🛡️ 安全提示

- 不要在代码中存储敏感信息
- 使用个人访问令牌时，请设置适当的权限范围
- 定期更新你的GitHub密码和访问令牌
- 确保你的`.gitignore`文件排除了敏感文件

## 📞 获取帮助

如果遇到脚本无法解决的问题：

1. 检查GitHub官方文档：https://docs.github.com/
2. 查看Git官方文档：https://git-scm.com/doc
3. 重新运行脚本，仔细阅读错误信息
4. 确保网络连接正常，能够访问GitHub

---

**文档更新时间**：2024年
**版本**：1.0.0

祝部署顺利！🎯