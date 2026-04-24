"""Main entry point for MCP-RAG service."""

import logging
import asyncio
from pathlib import Path
from logging.handlers import RotatingFileHandler
import uvicorn

from .config import config_manager
from .http_server import app as default_http_app

LOGS_DIR = Path("/data/logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(
    LOGS_DIR / "mcp-rag.log",
    maxBytes=10 * 1024 * 1024,
    backupCount=5,
    encoding="utf-8"
)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

root_logger.addHandler(file_handler)
root_logger.addHandler(console_handler)

logger = logging.getLogger(__name__)


def _resolve_settings(app) -> object:
    shell_context = getattr(getattr(app, "state", None), "shell_context", None)
    if shell_context is not None:
        return shell_context.settings
    return config_manager.settings


async def run_http_server(app=default_http_app):
    """Run the HTTP server only."""
    logger.info("启动MCP-RAG Streamable HTTP服务器...")
    config_manager.ensure_config_file()
    settings = _resolve_settings(app)
    logging.getLogger().setLevel(logging.DEBUG if getattr(settings, "debug", False) else logging.INFO)

    # 确保数据目录存在
    data_dir = Path(settings.chroma_persist_directory)
    data_dir.mkdir(parents=True, exist_ok=True)

    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=settings.http_port if hasattr(settings, 'http_port') else 8060,
        log_level="info"
    )
    
    port = settings.http_port if hasattr(settings, 'http_port') else 8060
    print(f"\n访问地址: http://127.0.0.1:{port} (Streamable MCP endpoint: http://127.0.0.1:{port}/mcp)\n")
    
    server = uvicorn.Server(config)
    await server.serve()


def run_http_server_sync(app=default_http_app):
    """同步包装器 for HTTP server."""
    asyncio.run(run_http_server(app=app))


async def main():
    """主应用入口点。"""
    logger.info("启动MCP-RAG服务...")

    try:
        await run_http_server(app=default_http_app)

    except KeyboardInterrupt:
        logger.info("正在关闭MCP-RAG服务...")
    except Exception as e:
        logger.error(f"启动MCP-RAG服务失败: {e}")
        raise


def run_server():
    """运行MCP-RAG服务器（同步包装器）。"""
    asyncio.run(main())


if __name__ == "__main__":
    run_server()
