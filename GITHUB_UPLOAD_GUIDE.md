# GitHub 上传配置指南

## 🎯 目标仓库

- **URL**: https://github.com/vizn/ppcha-school-promotion.git
- **用途**: 中华书院菲律宾帕赛分校项目宣传资料

---

## 🔐 认证方法（三选一）

### 方法一：使用 GitHub Token（快速简单）

1. **获取 Token**:
   - 访问 https://github.com/settings/tokens
   - Generate new token (classic)
   - 勾选 `repo` 权限（Full control of private repositories）
   - Copy the token

2. **配置 git**:
   ```bash
   export GITHUB_TOKEN=your_token_here
   git config --global url."https://x-access-token@github.com/".insteadOf "https://github.com/"
   cd /root/.openclaw/workspace
   git push -u origin main
   ```

### 方法二：使用 SSH（推荐长期自动化）

1. **生成 SSH 密钥**:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. **添加公钥到 GitHub**:
   - `cat ~/.ssh/id_ed25519.pub` 复制内容
   - 访问 https://github.com/settings/ssh → New SSH key
   - Paste the public key

3. **配置 git 使用 SSH**:
   ```bash
   git config --global url."github.com:".insteadOf "https://github.com/"
   cd /root/.openclaw/workspace
   git push -u origin main
   ```

### 方法三：浏览器授权（临时推送）

直接在终端执行 `git push`，会弹出 GitHub 登录页面，输入账号密码即可。

---

## 📦 当前仓库内容

```bash
✅ README.md                    # 仓库说明文档
✅ .gitignore                   # Git 忽略配置
✅ 中华书院菲律宾项目资料.md    # 主宣传文档（约 13KB）
```

## 🚀 推送命令

```bash
cd /root/.openclaw/workspace
git add README.md .gitignore 中华书院菲律宾项目资料.md
git commit -m "提交：中华书院菲律宾帕赛分校项目宣传资料"
git push -u origin main
```

---

## 🔗 相关资源

- [GitHub Token 设置](https://github.com/settings/tokens)
- [SSH Keys 设置](https://github.com/settings/ssh)
- [仓库主页](https://github.com/vizn/ppcha-school-promotion)

---

*© 2026 中华书院·菲律宾帕赛分校*
