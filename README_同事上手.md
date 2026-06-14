# 标签 AI 审核 — 同事上手指南

> 零基础 · 4 步完成 · 约 15 分钟

---

## 第一步：装 Trae CN 并配 API（只做一次）

1. 下载 Trae CN：https://trae.cn → 安装
2. 打开 → 右上角齿轮 ⚙️ →「模型」→「添加模型」
3. 填入：名称 `DeepSeek-V4-Pro` / API 地址 `https://api.deepseek.com/v1` / API Key `sk-xxx`（曹益发你）
4. 保存

---

## 第二步：下载两个仓库到桌面（只做一次）

打开 CMD（Win+R 输入 cmd），逐条粘贴回车：

```
git clone https://github.com/ouzhidao/Cy-knowledge-base.git %USERPROFILE%\Desktop\Cy-knowledge-base
git clone https://github.com/ouzhidao/-baidu-ocr-mcp.git %USERPROFILE%\Desktop\baidu-ocr-mcp
```

---

## 第三步：装 Python 依赖 + 放密钥（只做一次）

CMD 里跑：

```
pip install Pillow requests mcp
```

然后微信接收曹益发的 `secrets.json` 文件，放到桌面 `baidu-ocr-mcp` 文件夹里。

---

## 第四步：每次审核流程（1分钟）

1. 开 Trae CN →「打开文件夹」→ 选桌面 `Cy-knowledge-base`
2. 左侧找到 `标签审核` → `启动指令.md` → 双击 → Ctrl+A → Ctrl+C
3. 右侧对话框 Ctrl+V 粘贴 → 回车
4. 把标签图片（JPG/PNG）放到桌面，然后对 AI 说：`用 OCR 扫描 C:\Users\你的用户名\Desktop\图片名.jpg`
5. AI 自动调 OCR → 提取文字 → 按规则审核 → 出结果

---

## 知识库更新

曹益说知识库更新后，开 CMD 跑：

```
cd %USERPROFILE%\Desktop\Cy-knowledge-base && git pull
```

---

## 注意

- 每次新开 Trae CN 窗口要重新粘贴启动指令
- 发现新错字截图发曹益
- 不要自己改知识库文件
- 不要问 AI 审核标签以外的问题
