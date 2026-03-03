import os
import shlex
import subprocess
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="StyleFlow 控制台", page_icon="🎨", layout="wide")

st.title("🎨 StyleFlow 便捷控制界面")
st.caption("用于快速检查环境、构建命令并调用 StyleFlow 推理脚本。")

styleflow_dir = Path(os.getenv("STYLEFLOW_DIR", "external/StyleFlow")).resolve()

with st.sidebar:
    st.header("项目设置")
    st.write(f"当前 StyleFlow 路径: `{styleflow_dir}`")
    refresh = st.button("刷新状态")

if refresh:
    st.rerun()

col1, col2 = st.columns(2)

with col1:
    st.subheader("1) 环境状态")
    exists = styleflow_dir.exists()
    git_exists = (styleflow_dir / ".git").exists()

    st.write("- 项目目录存在:", "✅" if exists else "❌")
    st.write("- Git 仓库存在:", "✅" if git_exists else "❌")

    if not exists:
        st.warning("未检测到 StyleFlow 项目。请先执行: `bash scripts/import_styleflow.sh`")

with col2:
    st.subheader("2) 快速导入命令")
    st.code("bash scripts/import_styleflow.sh", language="bash")

st.divider()

st.subheader("3) 推理命令构建")

script_name = st.text_input("脚本名", value="main.py", help="StyleFlow 仓库内要执行的 Python 脚本")

arg_col1, arg_col2, arg_col3 = st.columns(3)
with arg_col1:
    image_path = st.text_input("输入图片路径", value="data/example.jpg")
with arg_col2:
    output_dir = st.text_input("输出目录", value="outputs")
with arg_col3:
    extra_args = st.text_input("额外参数", value="")

base_cmd = ["python", script_name, "--input", image_path, "--output", output_dir]
if extra_args.strip():
    base_cmd.extend(shlex.split(extra_args))

cmd_preview = " ".join(shlex.quote(x) for x in base_cmd)
st.code(f"cd {shlex.quote(str(styleflow_dir))} && {cmd_preview}", language="bash")

run_btn = st.button("运行命令", type="primary")

if run_btn:
    if not styleflow_dir.exists():
        st.error("StyleFlow 项目不存在，请先导入。")
    else:
        try:
            result = subprocess.run(
                base_cmd,
                cwd=styleflow_dir,
                capture_output=True,
                text=True,
                check=False,
            )
            st.write(f"退出码: `{result.returncode}`")
            st.text_area("STDOUT", result.stdout or "(empty)", height=250)
            st.text_area("STDERR", result.stderr or "(empty)", height=250)
            if result.returncode == 0:
                st.success("执行完成。")
            else:
                st.warning("执行失败，请根据日志检查参数与依赖。")
        except FileNotFoundError as exc:
            st.error(f"执行失败: {exc}")
