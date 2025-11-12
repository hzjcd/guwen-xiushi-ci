# 古文虚实词练习页面 - GitHub Pages 部署指南

## 准备工作

1. **确保Git已安装**
   - 检查Git版本：`git --version`
   - 如果未安装，请从 [https://git-scm.com/](https://git-scm.com/) 下载安装

2. **配置Git信息**
   ```bash
   git config --global user.name "你的GitHub用户名"
   git config --global user.email "你的GitHub邮箱"
   ```
   
   （当前已配置：用户名: hzjcd, 邮箱: 3357883100@qq.com）

## 本地仓库初始化（已完成）

- ✅ Git仓库已初始化
- ✅ 文件已添加到暂存区
- ✅ 已配置.gitignore文件

## 手动部署步骤

### 1. 在GitHub上创建仓库

1. 访问 [https://github.com/new](https://github.com/new)
2. 仓库名称：`guwen-xiushi-ci`
3. 选择公开或私有仓库
4. 不要勾选"Initialize this repository with a README"（因为我们已有本地文件）
5. 点击"Create repository"

### 2. 连接到GitHub仓库并推送

在本地项目文件夹中执行以下命令：

```bash
# 设置远程仓库地址
git remote add origin https://github.com/hzjcd/guwen-xiushi-ci.git

# 推送文件到GitHub
git push -u origin main
```

**注意**：如果这是首次推送到GitHub，系统可能会提示你输入GitHub凭证（用户名和密码/令牌）。建议使用[个人访问令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)代替密码。

### 3. 启用GitHub Pages

1. 访问你的GitHub仓库页面: [https://github.com/hzjcd/guwen-xiushi-ci](https://github.com/hzjcd/guwen-xiushi-ci)
2. 点击顶部导航栏中的"Settings"
3. 在左侧菜单中找到"Pages"
4. 在"Source"部分，选择"Branch: main"，然后点击"Save"
5. 稍等几分钟，GitHub Pages会自动构建你的站点

## 访问地址

部署成功后，你的页面将可以通过以下地址访问：

[https://hzjcd.github.io/guwen-xiushi-ci/wz.html](https://hzjcd.github.io/guwen-xiushi-ci/wz.html)

## 后续更新方法

当你需要更新页面内容时，只需执行以下步骤：

1. 修改本地的`wz.html`文件
2. 提交更改：
   ```bash
   git add wz.html
   git commit -m "更新内容说明"
   git push origin main
   ```
3. 等待几分钟，GitHub Pages会自动更新你的站点

## 注意事项

1. **微信访问限制**：GitHub Pages在微信内置浏览器中可能存在访问限制，建议提示用户在外部浏览器中打开，或考虑使用国内的托管服务如Gitee Pages或Coding Pages。

2. **部署时间**：GitHub Pages通常需要1-5分钟来构建和发布你的站点。

3. **自定义域名**：如需使用自定义域名，请参考[GitHub Pages自定义域名文档](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)。

4. **更新二维码**：部署成功后，可以使用新的URL生成新的二维码，替换当前的`qrcode.png`文件。

## 常见问题排查

- **推送失败**：检查网络连接、GitHub凭证是否正确、仓库是否存在
- **页面未更新**：清除浏览器缓存，等待几分钟后重试
- **样式或脚本不加载**：确保HTML中的路径引用正确，使用相对路径

---

祝你部署顺利！如有任何问题，请参考[GitHub Pages官方文档](https://docs.github.com/en/pages)。