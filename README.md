# StyleFlow 集成仓库

该仓库已准备好用于导入 [RameenAbdal/StyleFlow](https://github.com/RameenAbdal/StyleFlow.git) 并通过一个更易操作的 Web 界面进行调用。

> 由于当前执行环境无法直接访问 GitHub（403），我提供了自动导入脚本。你只需要在可联网环境执行一次脚本即可完成原项目导入。

## 1) 导入原始项目

```bash
bash scripts/import_styleflow.sh
```

默认会将项目拉取到：

- `external/StyleFlow`

## 2) 启动便于操作的界面

```bash
pip install -r requirements.txt
streamlit run app.py
```

启动后界面提供：

- 环境与项目状态检测
- 参数化命令生成
- 一键执行 StyleFlow 推理脚本（在本地环境可用时）
- 实时日志展示

## 3) 可自定义环境变量

- `STYLEFLOW_DIR`: 指定 StyleFlow 项目路径（默认 `external/StyleFlow`）
