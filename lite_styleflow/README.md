# StyleFlow 精简版（自包含）

这是一个基于现有代码**独立实现**的精简项目，保持与原项目相同的核心功能和界面流程：

- 环境与项目状态检测
- 导入命令展示（并提供本项目内置导入脚本）
- 推理命令构建与预览
- 一键执行命令并展示 STDOUT/STDERR 与退出码

## 目录结构

- `lite_styleflow/app.py`：精简版 Streamlit 页面
- `lite_styleflow/scripts/import_styleflow.sh`：导入/更新 StyleFlow 的本地脚本
- `lite_styleflow/requirements.txt`：精简版依赖

## 启动

```bash
pip install -r lite_styleflow/requirements.txt
streamlit run lite_styleflow/app.py
```

## 可选环境变量

- `STYLEFLOW_DIR`：指定 StyleFlow 路径（默认 `external/StyleFlow`）
