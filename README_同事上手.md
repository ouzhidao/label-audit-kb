# 标签 AI 审核 — 同事上手指南

> 零基础 · 3 步完成 · 约 10 分钟

---

## 第一步：装 Trae CN 并配 API（只做一次）

1. 下载 Trae CN：https://trae.cn → 安装
2. 打开 → 右上角齿轮 ⚙️ →「模型」→「添加模型」
3. 填入：名称 `DeepSeek-V4-Pro` / API 地址 `https://api.deepseek.com/v1` / API Key `sk-xxx`（曹益发你）
4. 保存

---

## 第二步：下载知识库到桌面（只做一次）

打开 CMD（Win+R 输入 cmd），粘贴回车：

```
git clone https://github.com/ouzhidao/label-audit-kb.git %USERPROFILE%\Desktop\label-audit-kb
```

---

## 第三步：每次审核流程（1分钟）

1. 开 Trae CN →「打开文件夹」→ 选桌面 `label-audit-kb`
2. 左侧找到 `knowledge` → `启动指令.md` → 双击 → Ctrl+A → Ctrl+C
3. 右侧对话框 Ctrl+V 粘贴 → 回车
4. 拖入标签图片 → 输入 `请审核` → 回车
5. 等 15-30 秒出结果

---

## 知识库更新

曹益通知更新后，开 CMD 跑：

```
cd %USERPROFILE%\Desktop\label-audit-kb && git pull
```

---

## 注意

- 每次新开 Trae CN 窗口要重新粘贴启动指令
- 发现新错字截图发曹益
- 不要自己改知识库文件
- 不要问 AI 审核标签以外的问题
