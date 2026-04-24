FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/usr/local \
    HF_ENDPOINT=https://hf-mirror.com

WORKDIR /app

# 安装 uv 包管理器（使用清华镜像）
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple uv

# 复制依赖文件、README 和源码（构建时需要 src 目录）
COPY pyproject.toml uv.lock uv.toml README.md ./
COPY src ./src

# 安装依赖（利用 Docker 缓存层，仅依赖变化时重新安装）
RUN uv sync --frozen

# 创建数据目录
RUN mkdir -p /data/chroma

EXPOSE 8060

# 开发模式启动：直接运行服务（无需 init，数据目录自动创建）
CMD ["sh", "-c", "mkdir -p /data/chroma && uv run uvicorn mcp_rag.main:default_http_app --host 0.0.0.0 --port 8060 --reload --reload-dir /app/src"]
