#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${STYLEFLOW_DIR:-external/StyleFlow}"
REPO_URL="https://github.com/RameenAbdal/StyleFlow.git"

mkdir -p "$(dirname "$TARGET_DIR")"

if [ -d "$TARGET_DIR/.git" ]; then
  echo "[INFO] StyleFlow 已存在于 $TARGET_DIR，尝试更新..."
  git -C "$TARGET_DIR" pull --ff-only
else
  echo "[INFO] 正在克隆 $REPO_URL -> $TARGET_DIR"
  git clone "$REPO_URL" "$TARGET_DIR"
fi

echo "[OK] StyleFlow 导入完成: $TARGET_DIR"
