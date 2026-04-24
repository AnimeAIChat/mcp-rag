# 项目功能结构与使用流程分析

**Session ID:** ses_2bccac14cffedPkZ6GqGO6030F
**Created:** 2026/3/31 17:24:16
**Updated:** 2026/3/31 21:59:33

---

## User

分析一下该项目功能，结构及使用流程

---

## Assistant (Build · qwen3-max-2026-01-23 · 2.2s)

**Tool: glob**

**Input:**
```json
{
  "pattern": "**/*"
}
```

**Output:**
```
D:\xfwork\mcprag\mcp-rag\.git\opencode
D:\xfwork\mcprag\mcp-rag\.git\config
D:\xfwork\mcprag\mcp-rag\uv.toml
D:\xfwork\mcprag\mcp-rag\.git\index
D:\xfwork\mcprag\mcp-rag\uv.lock
D:\xfwork\mcprag\mcp-rag\tests\test_service_facade.py
D:\xfwork\mcprag\mcp-rag\tests\test_security.py
D:\xfwork\mcprag\mcp-rag\tests\test_packaging_metadata.py
D:\xfwork\mcprag\mcp-rag\tests\test_observability.py
D:\xfwork\mcprag\mcp-rag\tests\test_mcp_server.py
D:\xfwork\mcprag\mcp-rag\tests\test_http_server.py
D:\xfwork\mcprag\mcp-rag\tests\test_context.py
D:\xfwork\mcprag\mcp-rag\tests\test_config.py
D:\xfwork\mcprag\mcp-rag\tests\services\test_service_layers.py
D:\xfwork\mcprag\mcp-rag\tests\services\test_retrieval_cache.py
D:\xfwork\mcprag\mcp-rag\tests\services\test_provider_budget.py
D:\xfwork\mcprag\mcp-rag\tests\retrieval\test_query_classifier.py
D:\xfwork\mcprag\mcp-rag\tests\retrieval\test_hybrid_service.py
D:\xfwork\mcprag\mcp-rag\tests\retrieval\test_collection_index.py
D:\xfwork\mcprag\mcp-rag\tests\e2e\__init__.py
D:\xfwork\mcprag\mcp-rag\tests\e2e\test_shell_integration.py
D:\xfwork\mcprag\mcp-rag\tests\core\indexing\test_indexing.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\static\app\index.html
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\static\app\assets\index-DQAj2c0D.js
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\spa_assets.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\shell_factory.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\static\app\assets\index-BuextOge.css
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\runtime.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\retrieval_service.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\retrieval_cache.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\__init__.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\indexing_service.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\chat_service.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\observability.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\mcp_server.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\main.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\llm.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\security.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\retrieval\__init__.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\retrieval\query_classifier.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\retrieval\hybrid_service.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\service_facade.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\retrieval\collection_index.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\knowledge_bases.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\http_server.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\contracts.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\core\indexing\__init__.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\core\indexing\vector_store.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\core\indexing\text_splitter.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\core\indexing\tenancy.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\core\indexing\models.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\core\indexing\embeddings.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\core\indexing\document_processor.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\__init__.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\context.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\config.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\cli.py
D:\xfwork\mcprag\mcp-rag\src\mcp_rag\app_factory.py
D:\xfwork\mcprag\mcp-rag\pyproject.toml
D:\xfwork\mcprag\mcp-rag\frontend\vite.config.js
D:\xfwork\mcprag\mcp-rag\frontend\svelte.config.js
D:\xfwork\mcprag\mcp-rag\frontend\src\main.js
D:\xfwork\mcprag\mcp-rag\frontend\src\lib\components\SelectField.svelte
D:\xfwork\mcprag\mcp-rag\frontend\src\lib\components\PanelCard.svelte
D:\xfwork\mcprag\mcp-rag\frontend\src\lib\components\PageTabs.svelte
D:\xfwork\mcprag\mcp-rag\frontend\src\lib\components\PageShell.svelte
D:\xfwork\mcprag\mcp-rag\frontend\src\lib\api.js
D:\xfwork\mcprag\mcp-rag\frontend\src\App.svelte
D:\xfwork\mcprag\mcp-rag\frontend\src\app.css
D:\xfwork\mcprag\mcp-rag\frontend\index.html
D:\xfwork\mcprag\mcp-rag\frontend\.gitignore
D:\xfwork\mcprag\mcp-rag\frontend\package.json
D:\xfwork\mcprag\mcp-rag\frontend\pnpm-lock.yaml
D:\xfwork\mcprag\mcp-rag\MANIFEST.in
D:\xfwork\mcprag\mcp-rag\README.md
D:\xfwork\mcprag\mcp-rag\.gitattributes
D:\xfwork\mcprag\mcp-rag\.gitignore
D:\xfwork\mcprag\mcp-rag\.python-version
D:\xfwork\mcprag\mcp-rag\.git\refs\heads\main
D:\xfwork\mcprag\mcp-rag\.git\HEAD
D:\xfwork\mcprag\mcp-rag\.git\refs\remotes\origin\HEAD
D:\xfwork\mcprag\mcp-rag\.git\packed-refs
D:\xfwork\mcprag\mcp-rag\.git\objects\pack\pack-b214d5a1834da6d99dc1309c6e91a1afb9a6964d.rev
D:\xfwork\mcprag\mcp-rag\.git\objects\pack\pack-b214d5a1834da6d99dc1309c6e91a1afb9a6964d.idx
D:\xfwork\mcprag\mcp-rag\.git\objects\pack\pack-b214d5a1834da6d99dc1309c6e91a1afb9a6964d.pack
D:\xfwork\mcprag\mcp-rag\.git\hooks\update.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\sendemail-validate.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\push-to-checkout.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\prepare-commit-msg.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\pre-receive.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\pre-rebase.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\pre-push.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\pre-merge-commit.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\pre-commit.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\pre-applypatch.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\post-update.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\fsmonitor-watchman.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\commit-msg.sample
D:\xfwork\mcprag\mcp-rag\.git\hooks\applypatch-msg.sample
D:\xfwork\mcprag\mcp-rag\.git\description

(Results are truncated: showing first 100 results. Consider using a more specific path or pattern.)
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag</path>
<type>directory</type>
<entries>
.git/
.gitattributes
.gitignore
.python-version
frontend/
MANIFEST.in
pyproject.toml
README.md
src/
tests/
uv.lock
uv.toml

(12 entries)
</entries>
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 4.5s)

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag\\README.md"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag\README.md</path>
<type>file</type>
<content>1: # MCP-RAG
2: 
3: > ✨100% 由 AI 编写
4: 
5: <table>
6:   <tr>
7:     <td><img src="https://github.com/user-attachments/assets/3103638f-38cc-47fe-8314-97a08c7c73e9" width="100%"></td>
8:     <td><img src="https://github.com/user-attachments/assets/5f36a470-fd9d-42cd-bdd0-24f3bb0efa1e" width="100%"></td>
9:   </tr>
10:   <tr>
11:     <td><img src="https://github.com/user-attachments/assets/e8cccdaa-e6c3-4c5c-a4f9-31bf11f98b6e" width="100%"></td>
12:     <td><img src="https://github.com/user-attachments/assets/d387d5f6-9ca2-455a-a63c-091736850da6" width="100%"></td>
13:   </tr>
14: </table>
15: 
16: 面向 AI 客户端的服务优先 RAG 服务，当前以 FastAPI HTTP 服务和 Streamable HTTP MCP 端点为主。
17: 
18: 代码当前提供的是一个统一后端壳层：
19: - FastAPI HTTP 服务
20: - Streamable HTTP MCP
21: - 共享运行时、配置热更新、鉴权、限流、配额、观测
22: - 基于知识库注册表的检索与文档管理
23: 
24: ## 当前能力
25: 
26: - 文档导入：支持直接添加文本，以及上传 `txt`、`md`、`pdf`、`docx`
27: - 检索：向量检索 + 关键词检索融合
28: - 问答：`/search`、`/chat`、MCP `rag_ask`
29: - 多知识库：支持单知识库和 `kb_ids` 多知识库聚合检索/对话
30: - 知识库作用域：`public` 和 `agent_private`
31: - 租户上下文：`base_collection + user_id + agent_id`
32: - 运行时治理：API key、内存限流、上传/索引配额、request-level retrieval cache
33: - provider 治理：provider budget、熔断、fallback
34: - 可观测性：`/health`、`/ready`、`/metrics`
35: - 前端：内置单页管理面板 `/app`
36: 
37: ## 架构
38: 
39: 主链路：
40: 
41: ```text
42: HTTP / MCP
43:   -> app_factory.py
44:   -> http_server.py / mcp_server.py
45:   -> context.py
46:   -> service_facade.py
47:   -> services/
48:        - runtime.py
49:        - indexing_service.py
50:        - retrieval_service.py
51:        - chat_service.py
52:   -> knowledge_bases.py
53:   -> core/indexing/
54:   -> retrieval/
55: ```
56: 
57: 关键文件：
58: - `src/mcp_rag/cli.py`: CLI 入口，提供 `serve` 和 `init`
59: - `src/mcp_rag/main.py`: HTTP 服务启动入口
60: - `src/mcp_rag/http_server.py`: HTTP API、SPA 入口、Streamable HTTP MCP 挂载
61: - `src/mcp_rag/mcp_server.py`: MCP 工具定义与 `rag_ask`
62: - `src/mcp_rag/app_factory.py`: 统一装配 app context、runtime、guardrails
63: - `src/mcp_rag/knowledge_bases.py`: 知识库注册表与默认知识库解析
64: - `src/mcp_rag/config.py`: 配置模型、JSON/SQLite 持久化、热更新
65: 
66: ## 环境要求
67: 
68: - Python `>= 3.13`
69: - `uv`
70: 
71: ## 安装
72: 
73: 安装 CLI：
74: 
75: ```bash
76: uv tool install mcp-rag
77: ```
78: 
79: 安装后直接运行：
80: 
81: ```bash
82: mcp-rag serve
83: ```
84: 
85: 在仓库里开发：
86: 
87: ```bash
88: uv sync
89: ```
90: 
91: 如果需要本地 embedding：
92: 
93: ```bash
94: uv sync --extra local-embeddings
95: ```
96: 
97: 边界说明：
98: - 使用 `uv tool install mcp-rag` 的安装用户不需要 Node.js，也不需要 `pnpm`
99: - `pnpm` 只用于维护前端构建，不是服务运行时依赖
100: 
101: ## 启动与初始化
102: 
103: 启动服务：
104: 
105: ```bash
106: uv run mcp-rag serve
107: ```
108: 
109: 初始化数据目录：
110: 
111: ```bash
112: uv run mcp-rag init --data-dir ./data
113: ```
114: 
115: 默认端口是 `8060`，服务默认监听 `0.0.0.0:8060`。
116: 
117: 常用入口：
118: - 管理面板：`http://127.0.0.1:8060/app`
119: - API 文档：`http://127.0.0.1:8060/docs`
120: - MCP 端点：`http://127.0.0.1:8060/mcp`
121: 
122: 兼容入口：
123: - `/` 会重定向到 `/app`
124: - `/doc` 会重定向到 `/docs`
125: - `/documents-page` 会重定向到 `/app/documents`
126: - `/config-page` 会重定向到 `/app/config`
127: 
128: 首次启动行为：
129: - 如果 `./data/config.json` 不存在，读取配置时会先使用默认值
130: - 服务启动时会调用 `ensure_config_file()`，把默认配置写入磁盘
131: - 数据目录中的 `./data/chroma` 和相关 SQLite 文件会按需创建
132: 
133: ## 前端与静态资源
134: 
135: 发布包会把 `src/mcp_rag/static/` 一并打进 wheel / sdist。
136: 
137: 这意味着：
138: - 安装用户运行 `uv tool install mcp-rag` 后可以直接访问 `/app`
139: - 不需要单独构建前端，也不需要 Node.js
140: - 前端维护者需要在发版前生成最新静态资源
141: 
142: 前端源码在 `frontend/`，构建输出到 `src/mcp_rag/static/app`。
143: 
144: 典型流程：
145: 
146: ```bash
147: cd frontend
148: pnpm install
149: pnpm build
150: ```
151: 
152: ## 知识库模型
153: 
154: 当前项目不再只靠裸 `collection` 组织数据，而是以知识库注册表为主。
155: 
156: 知识库特性：
157: - 持久化注册表在 `knowledge_base_db_path` 指向的 SQLite 文件中
158: - 默认会确保存在一个公共知识库
159: - 当传入 `user_id + agent_id` 时，会确保存在对应的默认 `agent_private` 知识库
160: - 新建知识库后会分配稳定的内部集合名，例如 `kb_<id>`
161: 
162: 接口层仍然保留 `collection` 参数，原因是需要兼容旧调用方式。当前实际行为是：
163: - 可以显式传 `kb_id`
164: - 也可以继续传旧 `collection`
165: - 服务会把请求解析到具体知识库和实际集合名
166: 
167: ## HTTP 接口
168: 
169: 系统接口：
170: - `GET /health`
171: - `GET /ready`
172: - `GET /metrics`
173: 
174: 配置接口：
175: - `GET /config`
176: - `POST /config`
177: - `POST /config/bulk`
178: - `POST /config/reset`
179: - `POST /config/reload`
180: 
181: 服务商接口：
182: - `GET /providers/{provider}/models`
183: 
184: 知识库接口：
185: - `GET /collections`
186: - `GET /knowledge-bases`
187: - `POST /knowledge-bases`
188: 
189: 文档接口：
190: - `POST /add-document`
191: - `POST /upload-files`
192: - `GET /list-documents`
193: - `DELETE /delete-document`
194: - `GET /list-files`
195: - `DELETE /delete-file`
196: 
197: 检索与问答：
198: - `GET /search`
199: - `POST /chat`
200: 
201: MCP 调试接口：
202: - `GET /debug/mcp/tools`
203: - `POST /debug/mcp/call`
204: 
205: 几点需要明确：
206: - `/search` 和 `/chat` 支持 `kb_id`
207: - `/search` 和 `/chat` 也支持 `kb_ids` 做多知识库聚合
208: - `/upload-files` 使用 `multipart/form-data`
209: - `/delete-document` 和 `/delete-file` 通过请求体传删除参数
210: 
211: 如果启用了安全策略，API key 可以通过以下方式传入：
212: - HTTP Header: `x-api-key`
213: - Header: `Authorization: Bearer <token>`
214: - 查询参数、JSON body 或 form 中的 `api_key`
215: 
216: ## MCP
217: 
218: 当前主形态是 Streamable HTTP MCP：
219: 
220: ```json
221: {
222:   "mcpServers": {
223:     "rag": {
224:       "url": "http://127.0.0.1:8060/mcp"
225:     }
226:   }
227: }
228: ```
229: 
230: 已实现的 MCP 工具：
231: - `rag_ask`
232: 
233: `rag_ask` 主要参数：
234: - `query`
235: - `mode`: `raw` 或 `summary`
236: - `collection`
237: - `kb_id`
238: - `scope`
239: - `limit`
240: - `threshold`
241: - `tenant`
242: - `user_id` / `agent_id`
243: - `_user_id` / `_agent_id`
244: - `api_key`
245: - `request_id`
246: - `trace_id`
247: 
248: 示例：
249: 
250: ```json
251: {
252:   "name": "rag_ask",
253:   "arguments": {
254:     "query": "FastAPI 是什么",
255:     "kb_id": 1,
256:     "mode": "summary",
257:     "limit": 5
258:   }
259: }
260: ```
261: 
262: ## 配置
263: 
264: 默认配置文件：
265: 
266: ```text
267: ./data/config.json
268: ```
269: 
270: 默认知识库数据库：
271: 
272: ```text
273: ./data/knowledge_bases.sqlite3
274: ```
275: 
276: 当前配置有一个重要变化：
277: - 普通运行配置保存在 `config.json`
278: - provider 相关配置会持久化到 SQLite，而不是继续完整写回 `config.json`
279: 
280: 也就是说，这些字段会存到 SQLite 中的 `service_provider_settings`：
281: - `embedding_provider`
282: - `embedding_fallback_provider`
283: - `provider_configs`
284: - `llm_provider`
285: - `llm_fallback_provider`
286: - `llm_model`
287: - `llm_base_url`
288: - `llm_api_key`
289: 
290: 其余配置仍然保存在 `config.json`，例如：
291: 
292: ```json
293: {
294:   "http_port": 8060,
295:   "chroma_persist_directory": "./data/chroma",
296:   "knowledge_base_db_path": "./data/knowledge_bases.sqlite3",
297:   "enable_llm_summary": false,
298:   "security": {
299:     "enabled": false,
300:     "allow_anonymous": true,
301:     "api_keys": [],
302:     "tenant_api_keys": {}
303:   },
304:   "rate_limit": {
305:     "requests_per_window": 120,
306:     "window_seconds": 60,
307:     "burst": 30
308:   },
309:   "quotas": {
310:     "max_upload_files": 20,
311:     "max_upload_bytes": 52428800,
312:     "max_upload_file_bytes": 10485760,
313:     "max_index_documents": 500,
314:     "max_index_chunks": 2000,
315:     "max_index_chars": 500000
316:   },
317:   "cache": {
318:     "enabled": false,
319:     "max_entries": 256,
320:     "ttl_seconds": 300
321:   },
322:   "provider_budget": {
323:     "enabled": true
324:   }
325: }
326: ```
327: 
328: 当前内置 provider 相关能力：
329: - embedding provider 默认值是 `zhipu`
330: - LLM provider 默认值是 `doubao`
331: - 内置 provider 配置包含 `doubao`、`zhipu`、`aliyun`
332: - `qwen` / `dashscope` 会规范化为 `aliyun`
333: - `/providers/{provider}/models` 支持从兼容 OpenAI 的模型服务拉取模型列表
334: - 本地 embedding 支持 `m3e-small` 和 `e5-small`
335: - LLM 额外支持 `ollama`
336: 
337: ## 热更新与运行时刷新
338: 
339: 热更新行为：
340: - 通过 `/config`、`/config/bulk`、`/config/reset`、`/config/reload` 修改后，运行时会立即刷新
341: - 请求进入时会通过 `reload_if_changed()` 检测磁盘配置是否变化
342: - provider 设置或检索配置变化后，会重建相关运行时依赖并清理检索缓存
343: 
344: ## Readiness 与 Metrics
345: 
346: - `/health` 返回健康摘要、运行时快照和 `config_revision`
347: - `/ready` 在未完成 bootstrap 或关键依赖未就绪时返回 `503`
348: - `/metrics` 返回按 operation / provider 聚合的观测指标
349: 
350: 当前 readiness 快照会包含：
351: - `document_processor`
352: - `embedding_model`
353: - `vector_store`
354: - `hybrid_service`
355: - `llm_model`
356: - `retrieval_cache`
357: - `provider_budget`
358: 
359: ## 测试
360: 
361: 运行全量测试：
362: 
363: ```bash
364: uv run python -m unittest discover -s tests
365: ```
366: 
367: 编译检查：
368: 
369: ```bash
370: uv run python -m compileall src
371: ```
372: 
373: 当前测试覆盖：
374: - 配置默认值、磁盘重载与 provider 配置迁移
375: - HTTP 壳层与 MCP 壳层行为
376: - request context / tenant 解析
377: - request-level retrieval cache
378: - provider budget / fallback
379: - readiness / health / metrics
380: - 打包元数据与静态资源
381: 
382: ## 许可证
383: 
384: MIT

(End of file - total 384 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag\\pyproject.toml"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag\pyproject.toml</path>
<type>file</type>
<content>1: [project]
2: name = "mcp-rag"
3: version = "0.6.2"
4: description = "基于mcp的rag服务"
5: readme = "README.md"
6: requires-python = ">=3.13"
7: dependencies = [
8:     "fastapi>=0.104.0",
9:     "uvicorn[standard]>=0.24.0",
10:     "pydantic>=2.5.0",
11:     "pydantic-settings>=2.1.0",
12:     "chromadb>=0.4.18",
13:     "numpy>=1.24.0",
14:     "scikit-learn>=1.3.0",
15:     "httpx>=0.25.0",
16:     "python-multipart>=0.0.6",
17:     "mcp>=0.1.0",
18:     "typer>=0.9.0",
19:     "PyPDF2>=3.0.0",
20:     "python-docx>=1.1.0",
21:     "scalar-fastapi>=1.8.1",
22: ]
23: 
24: [project.optional-dependencies]
25: local-embeddings = [
26:     "sentence-transformers>=2.2.2",
27: ]
28: 
29: [project.scripts]
30: # CLI entrypoint: `mcp-rag` will invoke mcp_rag.cli:main
31: mcp-rag = "mcp_rag.cli:main"
32: 
33: [tool.setuptools]
34: include-package-data = true
35: 
36: [tool.setuptools.package-dir]
37: "" = "src"
38: 
39: [tool.setuptools.packages.find]
40: where = ["src"]
41: 
42: [tool.setuptools.package-data]
43: mcp_rag = [
44:     "static/*",
45:     "static/**/*",
46: ]
47: 
48: [build-system]
49: requires = ["setuptools>=65.0", "wheel"]
50: build-backend = "setuptools.build_meta"

(End of file - total 50 lines)
</content>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag\\src\\mcp_rag\\main.py"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag\src\mcp_rag\main.py</path>
<type>file</type>
<content>1: """Main entry point for MCP-RAG service."""
2: 
3: import logging
4: import asyncio
5: from pathlib import Path
6: import uvicorn
7: 
8: from .config import config_manager
9: from .http_server import app as default_http_app
10: 
11: logging.basicConfig(
12:     level=logging.INFO,
13:     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
14: )
15: 
16: logger = logging.getLogger(__name__)
17: 
18: 
19: def _resolve_settings(app) -> object:
20:     shell_context = getattr(getattr(app, "state", None), "shell_context", None)
21:     if shell_context is not None:
22:         return shell_context.settings
23:     return config_manager.settings
24: 
25: 
26: async def run_http_server(app=default_http_app):
27:     """Run the HTTP server only."""
28:     logger.info("启动MCP-RAG Streamable HTTP服务器...")
29:     config_manager.ensure_config_file()
30:     settings = _resolve_settings(app)
31:     logging.getLogger().setLevel(logging.DEBUG if getattr(settings, "debug", False) else logging.INFO)
32: 
33:     # 确保数据目录存在
34:     data_dir = Path(settings.chroma_persist_directory)
35:     data_dir.mkdir(parents=True, exist_ok=True)
36: 
37:     config = uvicorn.Config(
38:         app,
39:         host="0.0.0.0",
40:         port=settings.http_port if hasattr(settings, 'http_port') else 8060,
41:         log_level="info"
42:     )
43:     
44:     port = settings.http_port if hasattr(settings, 'http_port') else 8060
45:     print(f"\n访问地址: http://127.0.0.1:{port} (Streamable MCP endpoint: http://127.0.0.1:{port}/mcp)\n")
46:     
47:     server = uvicorn.Server(config)
48:     await server.serve()
49: 
50: 
51: def run_http_server_sync(app=default_http_app):
52:     """同步包装器 for HTTP server."""
53:     asyncio.run(run_http_server(app=app))
54: 
55: 
56: async def main():
57:     """主应用入口点。"""
58:     logger.info("启动MCP-RAG服务...")
59: 
60:     try:
61:         await run_http_server(app=default_http_app)
62: 
63:     except KeyboardInterrupt:
64:         logger.info("正在关闭MCP-RAG服务...")
65:     except Exception as e:
66:         logger.error(f"启动MCP-RAG服务失败: {e}")
67:         raise
68: 
69: 
70: def run_server():
71:     """运行MCP-RAG服务器（同步包装器）。"""
72:     asyncio.run(main())
73: 
74: 
75: if __name__ == "__main__":
76:     run_server()

(End of file - total 76 lines)
</content>
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 7.0s)

该项目是一个基于MCP（Model Context Protocol）的RAG（检索增强生成）服务，主要功能包括：

**核心功能**：
- 提供FastAPI HTTP服务和Streamable HTTP MCP端点
- 支持文档导入（txt/md/pdf/docx）、向量+关键词混合检索
- 多知识库管理（public和agent_private作用域）
- 完整的运行时治理（API key鉴权、限流、配额、缓存）
- 内置Web管理面板（/app）

**项目结构**：
- `src/mcp_rag/`：核心Python代码
  - `http_server.py`/`mcp_server.py`：双协议入口
  - `service_facade.py`：统一服务门面
  - `services/`：运行时、索引、检索、聊天等服务
  - `core/indexing/`：底层索引实现
  - `retrieval/`：检索逻辑
- `frontend/`：Svelte前端源码
- `tests/`：完整的测试套件

**使用流程**：
1. 安装：`uv tool install mcp-rag` 或 `uv sync`（开发）
2. 启动：`mcp-rag serve`（默认端口8060）
3. 访问：
   - 管理面板：http://localhost:8060/app
   - API文档：http://localhost:8060/docs  
   - MCP端点：http://localhost:8060/mcp
4. 通过HTTP API或MCP工具`rag_ask`进行检索和问答

---

## User

知识库添加和生成流程是?

---

## Assistant (Build · qwen3-max-2026-01-23 · 2.8s)

**Tool: grep**

**Input:**
```json
{
  "pattern": "add-document|upload-files|POST /knowledge-bases"
}
```

**Output:**
```
Found 13 matches
D:\xfwork\mcprag\mcp-rag\tests\test_http_server.py:
  Line 129:                 "/upload-files",
  Line 148:                 "/add-document",

D:\xfwork\mcprag\mcp-rag\tests\e2e\test_shell_integration.py:
  Line 100:             "/upload-files",
  Line 190:                 "/upload-files",

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\static\app\assets\index-DQAj2c0D.js:
  Line 425:  */const n=[["path",{d:"M10 11v6"}],["path",{d:"M14 11v6"}],["path",{d:"M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"}],["path",{d:"M3 6h18"}],["path",{d:"M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"}]];ya(e,wa({name:"trash-2"},()=>i,{get iconNode(){return n},children:(o,c)=>{var f=Yt(),_=Ce(f);ar(_,r,"default",{}),k(o,f)},$$slots:{default:!0}}))}const Rv="".trim(),oo=Rv.replace(/\/+$/,"");function Sn(e={}){return!e||typeof e!="object"||Array.isArray(e)||e.kb_id!==void 0&&e.kb_id!==null||e.kbId===void 0||e.kbId===null?e:{...e,kb_id:e.kbId}}class zv extends Error{constructor(r,i,n){super(i),this.name="ApiError",this.status=r,this.payload=n}}function jv(e,r={}){const i=oo?`${oo}${e}`:e,n=new URL(i,window.location.origin);for(const[o,c]of Object.entries(r))if(!(c==null||c==="")){if(Array.isArray(c)){if(!c.length)continue;n.searchParams.set(o,c.join(","));continue}n.searchParams.set(o,String(c))}return n.toString()}function mt(e={}){const r={},i=e.apiKey||e.api_key;return i&&(r["x-api-key"]=i),r}async function bt(e,{method:r="GET",query:i={},body:n,formData:o,headers:c={}}={}){const f={...c},_={method:r,headers:f};o?_.body=o:n!==void 0&&(_.body=JSON.stringify(n),f["Content-Type"]||(f["Content-Type"]="application/json"));const b=await fetch(jv(e,i),_),h=await b.text();let y=null;if(h)try{y=JSON.parse(h)}catch{y=h}if(!b.ok){const M=typeof y=="object"&&y?y.detail||y.message||b.statusText:h||b.statusText;throw new zv(b.status,M,y)}return y}function vi(e={}){const r={};return e.userId&&(r.user_id=e.userId),e.agentId&&(r.agent_id=e.agentId),e.kbId&&(r.kb_id=e.kbId),e.scope&&(r.scope=e.scope),(e.apiKey||e.api_key)&&(r.api_key=e.apiKey||e.api_key),r}const at={health:(e={})=>bt("/health",{headers:mt(e)}),ready:(e={})=>bt("/ready",{headers:mt(e)}),metrics:(e={})=>bt("/metrics",{headers:mt(e)}),config:(e={})=>bt("/config",{query:vi(e),headers:mt(e)}),updateConfig:(e,r={})=>bt("/config/bulk",{method:"POST",body:{updates:e},headers:mt(r)}),resetConfig:(e={})=>bt("/config/reset",{method:"POST...

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\http_server.py:
  Line 685: @app.post("/add-document", tags=["文档"], summary="新增单条文档")
  Line 720: @app.post("/upload-files", tags=["文档"], summary="上传文件")

D:\xfwork\mcprag\mcp-rag\frontend\src\lib\api.js:
  Line 127:     return request('/upload-files', { method: 'POST', formData, headers: identityHeaders(identity) });
  Line 131:     return request('/add-document', { method: 'POST', body, headers: identityHeaders(body) });

D:\xfwork\mcprag\mcp-rag\README.md:
  Line 187: - `POST /knowledge-bases`
  Line 190: - `POST /add-document`
  Line 191: - `POST /upload-files`
  Line 208: - `/upload-files` 使用 `multipart/form-data`
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag\\src\\mcp_rag\\http_server.py"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag\src\mcp_rag\http_server.py</path>
<type>file</type>
<content>1: """HTTP server for MCP-RAG configuration and document management."""
2: 
3: import asyncio
4: from contextlib import asynccontextmanager
5: import logging
6: from pathlib import Path
7: from typing import Dict, Any, List, Optional
8: from uuid import uuid4
9: from fastapi import HTTPException, UploadFile, File, Form, Request
10: from fastapi.staticfiles import StaticFiles
11: from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse
12: from pydantic import BaseModel, Field
13: from starlette.responses import PlainTextResponse
14: 
15: try:
16:     import httpx
17: except ImportError:  # pragma: no cover - optional dependency guard
18:     httpx = None
19: 
20: from .config import canonical_provider_name, config_manager
21: from .contracts import ChatRequest, ChatResponse, DocumentRequest, SearchRequest, SearchResponse, SearchResultView, normalize_tenant
22: from .knowledge_bases import KnowledgeBaseAccessError
23: from .shell_factory import (
24:     build_http_request_context,
25:     create_http_app,
26:     ensure_app_context_current,
27:     enforce_http_guardrails,
28:     get_default_shell_context,
29:     health_payload,
30:     metrics_payload,
31:     ready_payload,
32:     reload_shell_context,
33:     request_subject,
34:     resolve_shell_service,
35: )
36: from .mcp_server import mcp_server
37: from .security import QuotaExceededError
38: from .spa_assets import render_missing_spa_html, resolve_spa_entry
39: from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
40: 
41: logger = logging.getLogger(__name__)
42: 
43: _RETRIEVAL_CONFIG_KEYS = {
44:     "cache",
45:     "embedding_provider",
46:     "embedding_fallback_provider",
47:     "enable_cache",
48:     "enable_llm_summary",
49:     "enable_reranker",
50:     "llm_model",
51:     "llm_provider",
52:     "llm_fallback_provider",
53:     "max_retrieval_results",
54:     "provider_budget",
55:     "provider_configs",
56:     "similarity_threshold",
57: }
58: 
59: def _build_streamable_http_manager(*, shell_context=None) -> StreamableHTTPSessionManager:
60:     if shell_context is not None:
61:         mcp_server.shell_context = shell_context
62:     return StreamableHTTPSessionManager(
63:         app=mcp_server.server,
64:         json_response=True,
65:         stateless=True,
66:     )
67: 
68: 
69: def _get_streamable_http_manager() -> StreamableHTTPSessionManager:
70:     manager = getattr(app.state, "streamable_http_manager", None)
71:     if manager is None:
72:         raise RuntimeError("Streamable HTTP transport is not running")
73:     return manager
74: 
75: 
76: @asynccontextmanager
77: async def _app_lifespan(lifespan_app):
78:     await reload_shell_context(lifespan_app.state.shell_context)
79:     lifespan_app.state.shell_context.bootstrapped = True
80: 
81:     manager = _build_streamable_http_manager(shell_context=lifespan_app.state.shell_context)
82:     lifespan_app.state.streamable_http_manager = manager
83:     async with manager.run():
84:         try:
85:             yield
86:         finally:
87:             lifespan_app.state.streamable_http_manager = None
88: 
89: 
90: app = create_http_app(context=get_default_shell_context(), lifespan=_app_lifespan)
91: 
92: # Mount static files
93: static_path = Path(__file__).parent / "static"
94: static_path.mkdir(exist_ok=True)
95: app.mount("/static", StaticFiles(directory=str(static_path)), name="static")
96: 
97: 
98: async def _streamable_http_asgi(scope, receive, send):
99:     if scope.get("type") != "http":
100:         response = PlainTextResponse("Streamable HTTP supports only HTTP requests", status_code=405)
101:         await response(scope, receive, send)
102:         return
103: 
104:     try:
105:         await _get_streamable_http_manager().handle_request(scope, receive, send)
106:     except RuntimeError as err:  # pragma: no cover - defensive
107:         logger.error("Streamable HTTP transport unavailable: %s", err)
108:         response = PlainTextResponse("MCP transport unavailable", status_code=503)
109:         await response(scope, receive, send)
110: 
111: 
112: app.mount("/mcp", _streamable_http_asgi, name="streamable-mcp")
113: app.mount("/mcp/", _streamable_http_asgi, name="streamable-mcp-slash")
114: app.mount("/sse", _streamable_http_asgi, name="sse")
115: 
116: 
117: @app.middleware("http")
118: async def _request_identity_middleware(request: Request, call_next):
119:     await ensure_app_context_current(request)
120:     request_id = (request.headers.get("x-request-id") or "").strip() or uuid4().hex
121:     trace_id = (request.headers.get("x-trace-id") or "").strip()
122:     if not trace_id:
123:         traceparent = (request.headers.get("traceparent") or "").strip()
124:         trace_id = traceparent.split("-")[1] if traceparent.count("-") >= 3 else traceparent or request_id
125: 
126:     request.state.request_id = request_id
127:     request.state.trace_id = trace_id or request_id
128: 
129:     response = await call_next(request)
130:     response.headers.setdefault("X-Request-Id", request_id)
131:     response.headers.setdefault("X-Trace-Id", trace_id or request_id)
132:     return response
133: 
134: 
135: async def get_rag_service(request: Request):
136:     """Compatibility wrapper used by unit tests and the shell routes."""
137: 
138:     return await resolve_shell_service(request)
139: 
140: 
141: def _config_affects_retrieval(*keys: str) -> bool:
142:     normalized = {str(key).split(".", 1)[0] for key in keys if key}
143:     return bool(normalized & _RETRIEVAL_CONFIG_KEYS)
144: 
145: 
146: class ConfigUpdate(BaseModel):
147:     """Configuration update model."""
148:     key: str
149:     value: Any
150: 
151: 
152: class BulkConfigUpdate(BaseModel):
153:     """Bulk configuration update model."""
154:     updates: Dict[str, Any]
155: 
156: 
157: class DocumentAdd(BaseModel):
158:     """Document addition model."""
159:     content: str
160:     collection: str = "default"
161:     kb_id: Optional[int] = None
162:     scope: Optional[str] = None
163:     metadata: Dict[str, Any] = Field(default_factory=dict)
164:     user_id: Optional[int] = None
165:     agent_id: Optional[int] = None
166:     api_key: Optional[str] = None
167: 
168: 
169: class DeleteDocumentRequest(BaseModel):
170:     """Delete document request model."""
171:     document_id: str
172:     collection: str = "default"
173:     kb_id: Optional[int] = None
174:     scope: Optional[str] = None
175:     user_id: Optional[int] = None
176:     agent_id: Optional[int] = None
177:     api_key: Optional[str] = None
178: 
179: 
180: class DeleteFileRequest(BaseModel):
181:     """Delete file request model."""
182:     filename: str
183:     collection: str = "default"
184:     kb_id: Optional[int] = None
185:     scope: Optional[str] = None
186:     user_id: Optional[int] = None
187:     agent_id: Optional[int] = None
188:     api_key: Optional[str] = None
189: 
190: 
191: class KnowledgeBaseCreate(BaseModel):
192:     """Create knowledge base request."""
193: 
194:     name: str
195:     scope: str = "public"
196:     owner_user_id: Optional[int] = None
197:     owner_agent_id: Optional[int] = None
198:     api_key: Optional[str] = None
199: 
200: 
201: class MCPDebugCall(BaseModel):
202:     """Debug MCP tool invocation request."""
203: 
204:     tool: str
205:     arguments: Dict[str, Any] = Field(default_factory=dict)
206:     api_key: Optional[str] = None
207: 
208: 
209: def _provider_config_entry(provider: str) -> Any | None:
210:     provider_name = canonical_provider_name(provider)
211:     provider_configs = getattr(config_manager.settings, "provider_configs", {}) or {}
212:     return provider_configs.get(provider_name)
213: 
214: 
215: def _infer_openai_model_family(model_id: str) -> str:
216:     model_name = str(model_id or "").strip().lower()
217:     embedding_markers = ("embedding", "bge-", "m3e", "e5", "rerank", "text-embedding")
218:     if any(marker in model_name for marker in embedding_markers):
219:         return "embedding"
220:     return "chat"
221: 
222: 
223: async def _fetch_openai_compatible_models(base_url: str, api_key: str) -> list[dict[str, str]]:
224:     if httpx is None:
225:         raise RuntimeError("httpx is not installed")
226: 
227:     async with httpx.AsyncClient(
228:         base_url=base_url.rstrip("/"),
229:         headers={
230:             "Authorization": f"Bearer {api_key}",
231:             "Content-Type": "application/json",
232:         },
233:         timeout=20.0,
234:     ) as client:
235:         response = await client.get("/models")
236:         if response.status_code != 200:
237:             raise RuntimeError(f"Model API error: {response.status_code} - {response.text}")
238: 
239:         payload = response.json()
240:         items = payload.get("data") if isinstance(payload, dict) else None
241:         if not isinstance(items, list):
242:             return []
243: 
244:         models = []
245:         for item in items:
246:             model_id = str((item or {}).get("id") or "").strip()
247:             if not model_id:
248:                 continue
249:             models.append(
250:                 {
251:                     "id": model_id,
252:                     "label": model_id,
253:                     "family": _infer_openai_model_family(model_id),
254:                     "source": "remote",
255:                 }
256:             )
257:         return models
258: 
259: 
260: async def _fetch_ollama_models(base_url: str) -> list[dict[str, str]]:
261:     if httpx is None:
262:         raise RuntimeError("httpx is not installed")
263: 
264:     async with httpx.AsyncClient(base_url=base_url.rstrip("/"), timeout=20.0) as client:
265:         response = await client.get("/api/tags")
266:         if response.status_code != 200:
267:             raise RuntimeError(f"Ollama API error: {response.status_code} - {response.text}")
268: 
269:         payload = response.json()
270:         items = payload.get("models") if isinstance(payload, dict) else None
271:         if not isinstance(items, list):
272:             return []
273: 
274:         models = []
275:         for item in items:
276:             model_id = str((item or {}).get("name") or "").strip()
277:             if not model_id:
278:                 continue
279:             models.append(
280:                 {
281:                     "id": model_id,
282:                     "label": model_id,
283:                     "family": "chat",
284:                     "source": "remote",
285:                 }
286:             )
287:         return models
288: 
289: 
290: def _legacy_collection_key(collection: str, *, scope: str, user_id: int | None, agent_id: int | None) -> str:
291:     if scope == "public":
292:         return f"legacy:public:{collection or 'default'}"
293:     return f"legacy:agent_private:{user_id}:{agent_id}:{collection or 'default'}"
294: 
295: 
296: def _resolve_request_knowledge_base(
297:     request: Request,
298:     *,
299:     kb_id: int | None = None,
300:     scope: str | None = None,
301:     collection: str = "default",
302:     user_id: int | None = None,
303:     agent_id: int | None = None,
304:     api_key: str | None = None,
305:     operation: str = "request",
306: ) -> tuple:
307:     shell_context = request.app.state.shell_context
308:     resolved_scope = shell_context.knowledge_bases.normalize_scope(scope, user_id=user_id, agent_id=agent_id)
309:     try:
310:         resolution = shell_context.knowledge_bases.resolve(
311:             kb_id=kb_id,
312:             scope=resolved_scope,
313:             user_id=user_id,
314:             agent_id=agent_id,
315:             legacy_collection=collection,
316:             legacy_collection_key=_legacy_collection_key(
317:                 collection,
318:                 scope=resolved_scope,
319:                 user_id=user_id,
320:                 agent_id=agent_id,
321:             ),
322:         )
323:     except KnowledgeBaseAccessError as exc:
324:         raise HTTPException(status_code=403, detail=str(exc)) from exc
325:     effective_user_id = resolution.knowledge_base.owner_user_id if resolution.scope == "agent_private" else None
326:     effective_agent_id = resolution.knowledge_base.owner_agent_id if resolution.scope == "agent_private" else None
327:     tenant = normalize_tenant(
328:         base_collection=resolution.name,
329:         user_id=effective_user_id,
330:         agent_id=effective_agent_id,
331:     )
332:     request_context = build_http_request_context(
333:         request,
334:         tenant=tenant,
335:         base_collection=resolution.name,
336:         user_id=effective_user_id,
337:         agent_id=effective_agent_id,
338:         api_key=api_key,
339:         kb_id=resolution.kb_id,
340:         kb_scope=resolution.scope,
341:         kb_name=resolution.name,
342:         resolved_collection=resolution.collection_name,
343:         operation=operation,
344:         subject=request_subject(request, tenant, fallback=f"{operation}:{resolution.collection_name}"),
345:     )
346:     return resolution, request_context
347: 
348: 
349: def _parse_kb_ids(raw_value: Any) -> list[int]:
350:     if raw_value is None or raw_value == "":
351:         return []
352:     if isinstance(raw_value, list):
353:         values = raw_value
354:     else:
355:         values = str(raw_value).split(",")
356:     parsed: list[int] = []
357:     for item in values:
358:         try:
359:             value = int(str(item).strip())
360:         except (TypeError, ValueError):
361:             continue
362:         if value not in parsed:
363:             parsed.append(value)
364:     return parsed
365: 
366: 
367: async def _search_across_knowledge_bases(
368:     *,
369:     request: Request,
370:     service,
371:     query: str,
372:     collection: str,
373:     kb_ids: list[int],
374:     scope: str | None,
375:     limit: int,
376:     user_id: int | None,
377:     agent_id: int | None,
378:     api_key: str | None,
379:     operation: str,
380: ) -> tuple[list[Any], SearchResponse]:
381:     contexts = [
382:         _resolve_request_knowledge_base(
383:             request,
384:             kb_id=kb_id,
385:             scope=scope,
386:             collection=collection,
387:             user_id=user_id,
388:             agent_id=agent_id,
389:             api_key=api_key,
390:             operation=operation,
391:         )[1]
392:         for kb_id in kb_ids
393:     ]
394:     if contexts:
395:         enforce_http_guardrails(request, request_context=contexts[0])
396:     responses = await asyncio.gather(
397:         *[
398:             service.search(
399:                 SearchRequest(
400:                     query=query,
401:                     collection=request_context.kb_name or collection,
402:                     limit=limit,
403:                     kb_id=request_context.kb_id,
404:                     scope=request_context.kb_scope,
405:                     tenant=request_context.tenant,
406:                     context=request_context,
407:                 )
408:             )
409:             for request_context in contexts
410:         ]
411:     )
412: 
413:     merged_results: list[SearchResultView] = []
414:     for response, request_context in zip(responses, contexts):
415:         for item in response.results:
416:             metadata = dict(item.metadata or {})
417:             metadata.setdefault("knowledge_base_id", request_context.kb_id)
418:             metadata.setdefault("knowledge_base_name", request_context.kb_name)
419:             metadata.setdefault("knowledge_base_scope", request_context.kb_scope)
420:             metadata.setdefault("owner_user_id", request_context.tenant.user_id)
421:             metadata.setdefault("owner_agent_id", request_context.tenant.agent_id)
422:             merged_results.append(
423:                 SearchResultView(
424:                     content=item.content,
425:                     score=item.score,
426:                     vector_score=item.vector_score,
427:                     keyword_score=item.keyword_score,
428:                     metadata=metadata,
429:                     source=item.source,
430:                     filename=item.filename,
431:                     retrieval_method=item.retrieval_method,
432:                 )
433:             )
434:     merged_results.sort(key=lambda item: item.score, reverse=True)
435:     merged_results = merged_results[:limit]
436: 
437:     summary = None
438:     if merged_results and getattr(service.runtime.settings, "enable_llm_summary", False):
439:         try:
440:             llm_model = await service.runtime.ensure_llm_model()
441:             summary_context = "\n\n".join(
442:                 f"知识库 {item.metadata.get('knowledge_base_name', '未知')} · 文档 {index + 1} (相似度: {item.score:.3f}):\n{item.content}"
443:                 for index, item in enumerate(merged_results)
444:             )
445:             summary = await llm_model.summarize(summary_context, query)
446:         except Exception as exc:
447:             logger.warning("LLM summary failed for multi-kb search, falling back to raw results: %s", exc)
448: 
449:     return contexts, SearchResponse(
450:         query=query,
451:         collection="multi_kb",
452:         results=merged_results,
453:         summary=summary,
454:     )
455: 
456: 
457: def _format_chat_context(results: list[SearchResultView]) -> str:
458:     return "\n\n".join(
459:         f"知识库 {item.metadata.get('knowledge_base_name', '未知')} / 文档 {index + 1} ({item.filename or item.source}):\n{item.content}"
460:         for index, item in enumerate(results)
461:     )
462: 
463: 
464: def _build_chat_prompt(query: str, context: str) -> str:
465:     return (
466:         "基于以下知识库内容回答用户的问题。如果知识库内容不足以回答问题，请说明无法找到相关信息。\n\n"
467:         f"知识库内容:\n{context}\n\n"
468:         f"用户问题: {query}\n\n"
469:         "请提供准确、简洁的回答:"
470:     )
471: 
472: 
473: def _format_llm_fallback_response(context: str, error: Exception) -> str:
474:     detail = str(error).strip() or error.__class__.__name__
475:     return (
476:         "### Retrieved Context\n\n"
477:         f"{context}\n\n"
478:         "### Note\n"
479:         "LLM is not available. The above context was retrieved for your query.\n\n"
480:         f"LLM error: {detail}"
481:     )
482: 
483: 
484: @app.get("/", tags=["系统"], summary="根入口")
485: async def root():
486:     """Root endpoint - redirect to the SPA shell."""
487:     return RedirectResponse(url="/app")
488: 
489: 
490: @app.get("/doc", tags=["系统"], summary="文档入口重定向")
491: async def doc_redirect():
492:     """Redirect to API documentation."""
493:     return RedirectResponse(url="/docs")
494: 
495: 
496: @app.get("/health", tags=["系统"], summary="健康检查")
497: async def health(request: Request):
498:     """Lightweight health summary without warming the runtime."""
499:     return health_payload(request.app.state.shell_context)
500: 
501: 
502: @app.get("/ready", tags=["系统"], summary="就绪检查")
503: async def ready(request: Request):
504:     """Readiness signal for shell wiring."""
505:     payload = ready_payload(request.app.state.shell_context)
506:     return JSONResponse(status_code=200 if payload["ready"] else 503, content=payload)
507: 
508: 
509: @app.get("/metrics", tags=["系统"], summary="运行指标")
510: async def metrics(request: Request):
511:     """Observability snapshot."""
512:     return metrics_payload(request.app.state.shell_context)
513: 
514: 
515: def _spa_redirect_target(view: str | None = None) -> str:
516:     """Build a stable SPA redirect target for legacy page routes."""
517: 
518:     if not view:
519:         return "/app"
520:     return f"/app/{view}"
521: 
522: 
523: def _serve_spa_entry(*, request_path: str):
524:     """Serve the prebuilt SPA entry file or a clear fallback page."""
525: 
526:     entry = resolve_spa_entry(static_path)
527:     if entry is None:
528:         return HTMLResponse(
529:             content=render_missing_spa_html(static_dir=static_path, request_path=request_path),
530:             status_code=503,
531:         )
532:     return FileResponse(entry, media_type="text/html")
533: 
534: 
535: @app.get("/app", response_class=HTMLResponse, tags=["应用"], summary="前端应用入口")
536: @app.get("/app/{spa_path:path}", response_class=HTMLResponse, tags=["应用"], summary="前端应用子路径")
537: async def spa_entry(spa_path: str = ""):
538:     """Serve the SPA shell for browser clients."""
539: 
540:     request_path = "/app" if not spa_path else f"/app/{spa_path}"
541:     return _serve_spa_entry(request_path=request_path)
542: 
543: 
544: @app.get("/documents-page", tags=["应用"], summary="文档页兼容入口")
545: async def documents_page():
546:     """Backward-compatible redirect to the SPA documents view."""
547: 
548:     return RedirectResponse(url=_spa_redirect_target("documents"))
549: 
550: 
551: @app.get("/config-page", tags=["应用"], summary="配置页兼容入口")
552: async def config_page():
553:     """Backward-compatible redirect to the SPA config view."""
554: 
555:     return RedirectResponse(url=_spa_redirect_target("config"))
556: 
557: 
558: @app.get("/config", tags=["配置"], summary="读取配置")
559: async def get_config(request: Request, api_key: Optional[str] = None):
560:     """Get current configuration."""
561:     context = request.app.state.shell_context
562:     async with context.observability.timer("config.get"):
563:         request_context = build_http_request_context(request, api_key=api_key, subject="config")
564:         enforce_http_guardrails(request, request_context=request_context)
565:         return config_manager.get_all_settings()
566: 
567: 
568: @app.post("/config", tags=["配置"], summary="更新单个配置项")
569: async def update_config(config: ConfigUpdate, request: Request):
570:     """Update a single configuration setting."""
571:     context = request.app.state.shell_context
572:     async with context.observability.timer("config.update"):
573:         request_context = build_http_request_context(request, subject="config")
574:         enforce_http_guardrails(request, request_context=request_context)
575:         success = config_manager.update_setting(config.key, config.value)
576:         if not success:
577:             raise HTTPException(status_code=400, detail=f"Failed to update config {config.key}")
578:         await reload_shell_context(context, settings_obj=config_manager.settings)
579:         if _config_affects_retrieval(config.key):
580:             await context.runtime.invalidate_all_retrieval_cache()
581:         return {"message": f"Config {config.key} updated successfully", "reloaded": True}
582: 
583: 
584: @app.post("/config/bulk", tags=["配置"], summary="批量更新配置")
585: async def update_config_bulk(config: BulkConfigUpdate, request: Request):
586:     """Update multiple configuration settings."""
587:     context = request.app.state.shell_context
588:     async with context.observability.timer("config.bulk_update"):
589:         request_context = build_http_request_context(request, subject="config")
590:         enforce_http_guardrails(request, request_context=request_context)
591:         success = config_manager.update_settings(config.updates)
592:         if not success:
593:             raise HTTPException(status_code=400, detail="Failed to update config")
594:         await reload_shell_context(context, settings_obj=config_manager.settings)
595:         if _config_affects_retrieval(*config.updates.keys()):
596:             await context.runtime.invalidate_all_retrieval_cache()
597:         return {"message": "Config updated successfully", "reloaded": True}
598: 
599: 
600: @app.post("/config/reset", tags=["配置"], summary="重置默认配置")
601: async def reset_config(request: Request):
602:     """Reset configuration to defaults."""
603:     context = request.app.state.shell_context
604:     async with context.observability.timer("config.reset"):
605:         request_context = build_http_request_context(request, subject="config")
606:         enforce_http_guardrails(request, request_context=request_context)
607:         success = config_manager.reset_to_defaults()
608:         if not success:
609:             raise HTTPException(status_code=400, detail="Failed to reset config")
610:         await reload_shell_context(context, settings_obj=config_manager.settings)
611:         await context.runtime.invalidate_all_retrieval_cache()
612:         return {"message": "Config reset to defaults successfully", "reloaded": True}
613: 
614: 
615: @app.post("/config/reload", tags=["配置"], summary="从磁盘重载配置")
616: async def reload_config(request: Request):
617:     """Reload configuration from disk and rebuild the live runtime."""
618:     context = request.app.state.shell_context
619:     async with context.observability.timer("config.reload"):
620:         request_context = build_http_request_context(request, subject="config")
621:         enforce_http_guardrails(request, request_context=request_context)
622:         settings_obj = config_manager.reload()
623:         await reload_shell_context(context, settings_obj=settings_obj)
624:         await context.runtime.invalidate_all_retrieval_cache()
625:         return {"message": "Config reloaded successfully", "reloaded": True}
626: 
627: 
628: @app.get("/providers/{provider}/models", tags=["服务商"], summary="获取服务商模型列表")
629: async def get_provider_models(
630:     provider: str,
631:     request: Request,
632:     family: Optional[str] = None,
633: ):
634:     """Fetch provider model list from remote service when supported."""
635:     context = request.app.state.shell_context
636:     async with context.observability.timer("provider_models.get"):
637:         request_context = build_http_request_context(request, subject=f"provider_models:{provider}")
638:         enforce_http_guardrails(request, request_context=request_context)
639: 
640:         provider_name = canonical_provider_name(provider)
641:         provider_config = _provider_config_entry(provider_name)
642:         requested_family = str(family or "").strip().lower() or None
643: 
644:         try:
645:             if provider_name in {"m3e-small", "e5-small"}:
646:                 local_model = provider_name
647:                 model_family = "embedding"
648:                 if requested_family and requested_family != model_family:
649:                     return {"provider": provider_name, "family": requested_family, "models": []}
650:                 return {
651:                     "provider": provider_name,
652:                     "family": model_family,
653:                     "models": [{"id": local_model, "label": local_model, "family": model_family, "source": "local"}],
654:                 }
655: 
656:             if provider_name == "ollama":
657:                 base_url = str(getattr(provider_config, "base_url", "") or "http://localhost:11434")
658:                 models = await _fetch_ollama_models(base_url)
659:             else:
660:                 if provider_config is None:
661:                     raise HTTPException(status_code=404, detail=f"Unknown provider: {provider_name}")
662:                 api_key = getattr(provider_config, "api_key", None)
663:                 base_url = str(getattr(provider_config, "base_url", "") or "")
664:                 if not base_url:
665:                     raise HTTPException(status_code=400, detail="Provider base_url is missing")
666:                 if not api_key:
667:                     raise HTTPException(status_code=400, detail="Provider api_key is missing")
668:                 models = await _fetch_openai_compatible_models(base_url, api_key)
669:         except HTTPException:
670:             raise
671:         except Exception as exc:
672:             logger.warning("Failed to fetch models for provider %s: %s", provider_name, exc)
673:             raise HTTPException(status_code=502, detail=str(exc)) from exc
674: 
675:         if requested_family:
676:             models = [item for item in models if item.get("family") == requested_family]
677: 
678:         return {
679:             "provider": provider_name,
680:             "family": requested_family,
681:             "models": models,
682:         }
683: 
684: 
685: @app.post("/add-document", tags=["文档"], summary="新增单条文档")
686: async def add_document(doc: DocumentAdd, request: Request):
687:     """Add a single document."""
688:     try:
689:         _, request_context = _resolve_request_knowledge_base(
690:             request,
691:             kb_id=doc.kb_id,
692:             scope=doc.scope,
693:             collection=doc.collection,
694:             user_id=doc.user_id,
695:             agent_id=doc.agent_id,
696:             api_key=doc.api_key,
697:             operation="add_document",
698:         )
699:         context = request.app.state.shell_context
700:         async with context.observability.timer("add_document"):
701:             enforce_http_guardrails(request, request_context=request_context)
702:             service = await get_rag_service(request)
703:             return await service.add_document(
704:                 DocumentRequest(
705:                     content=doc.content,
706:                     collection=request_context.kb_name or doc.collection,
707:                     metadata=doc.metadata,
708:                     kb_id=request_context.kb_id,
709:                     scope=request_context.kb_scope,
710:                     tenant=request_context.tenant,
711:                     context=request_context,
712:                 )
713:             )
714:     except QuotaExceededError as exc:
715:         raise HTTPException(status_code=413, detail=str(exc)) from exc
716:     except KnowledgeBaseAccessError as exc:
717:         raise HTTPException(status_code=403, detail=str(exc)) from exc
718: 
719: 
720: @app.post("/upload-files", tags=["文档"], summary="上传文件")
721: async def upload_files(
722:     request: Request,
723:     files: List[UploadFile] = File(...),
724:     collection: str = Form("default"),
725:     kb_id: Optional[int] = Form(None),
726:     scope: Optional[str] = Form(None),
727:     user_id: Optional[int] = Form(None),
728:     agent_id: Optional[int] = Form(None),
729:     api_key: Optional[str] = Form(None),
730: ):
731:     """Upload and process multiple files."""
732:     if not files:
733:         raise HTTPException(status_code=400, detail="No files provided")
734: 
735:     _, request_context = _resolve_request_knowledge_base(
736:         request,
737:         kb_id=kb_id,
738:         scope=scope,
739:         collection=collection,
740:         user_id=user_id,
741:         agent_id=agent_id,
742:         api_key=api_key,
743:         operation="upload_files",
744:     )
745:     context = request.app.state.shell_context
746:     async with context.observability.timer("upload_files"):
747:         enforce_http_guardrails(request, request_context=request_context)
748:         service = await get_rag_service(request)
749:         return await service.upload_files(
750:             files,
751:             collection=collection,
752:             request_context=request_context,
753:         )
754: 
755: 
756: @app.get("/collections", tags=["知识库"], summary="列出历史集合")
757: async def list_collections(
758:     request: Request,
759:     user_id: Optional[int] = None,
760:     agent_id: Optional[int] = None,
761:     api_key: Optional[str] = None,
762: ):
763:     """List all collections."""
764:     request_context = build_http_request_context(
765:         request,
766:         tenant=normalize_tenant(base_collection="collections", user_id=user_id, agent_id=agent_id),
767:         base_collection="collections",
768:         user_id=user_id,
769:         agent_id=agent_id,
770:         api_key=api_key,
771:         operation="list_collections",
772:         subject=request_subject(
773:             request,
774:             normalize_tenant(base_collection="collections", user_id=user_id, agent_id=agent_id),
775:             fallback="collections",
776:         ),
777:     )
778:     context = request.app.state.shell_context
779:     async with context.observability.timer("list_collections"):
780:         enforce_http_guardrails(request, request_context=request_context)
781:         collections = [item.collection_name for item in context.knowledge_bases.list_accessible(user_id=user_id, agent_id=agent_id)]
782:     return {"collections": collections}
783: 
784: 
785: @app.get("/knowledge-bases", tags=["知识库"], summary="列出知识库")
786: async def list_knowledge_bases(
787:     request: Request,
788:     user_id: Optional[int] = None,
789:     agent_id: Optional[int] = None,
790:     api_key: Optional[str] = None,
791: ):
792:     """List accessible knowledge bases."""
793: 
794:     tenant = normalize_tenant(base_collection="knowledge_bases", user_id=user_id, agent_id=agent_id)
795:     request_context = build_http_request_context(
796:         request,
797:         tenant=tenant,
798:         base_collection="knowledge_bases",
799:         user_id=user_id,
800:         agent_id=agent_id,
801:         api_key=api_key,
802:         operation="list_knowledge_bases",
803:         subject=request_subject(request, tenant, fallback="knowledge_bases"),
804:     )
805:     context = request.app.state.shell_context
806:     async with context.observability.timer("list_knowledge_bases"):
807:         enforce_http_guardrails(request, request_context=request_context)
808:         items = context.knowledge_bases.list_accessible(user_id=user_id, agent_id=agent_id)
809:     return {"knowledge_bases": [item.to_dict() for item in items]}
810: 
811: 
812: @app.post("/knowledge-bases", tags=["知识库"], summary="创建知识库")
813: async def create_knowledge_base(payload: KnowledgeBaseCreate, request: Request):
814:     """Create a public or agent-private knowledge base."""
815: 
816:     tenant = normalize_tenant(
817:         base_collection="knowledge_bases",
818:         user_id=payload.owner_user_id,
819:         agent_id=payload.owner_agent_id,
820:     )
821:     request_context = build_http_request_context(
822:         request,
823:         tenant=tenant,
824:         base_collection="knowledge_bases",
825:         user_id=payload.owner_user_id,
826:         agent_id=payload.owner_agent_id,
827:         api_key=payload.api_key,
828:         operation="create_knowledge_base",
829:         subject=request_subject(request, tenant, fallback="knowledge_bases:create"),
830:     )
831:     context = request.app.state.shell_context
832:     async with context.observability.timer("create_knowledge_base"):
833:         enforce_http_guardrails(request, request_context=request_context)
834:         knowledge_base = context.knowledge_bases.create_knowledge_base(
835:             name=payload.name,
836:             scope=payload.scope,
837:             owner_user_id=payload.owner_user_id,
838:             owner_agent_id=payload.owner_agent_id,
839:         )
840:     return knowledge_base.to_dict()
841: 
842: 
843: @app.get("/debug/mcp/tools", tags=["MCP 调试"], summary="列出 MCP 工具")
844: async def debug_mcp_tools(request: Request, api_key: Optional[str] = None):
845:     """List MCP tools for the debug UI."""
846: 
847:     tenant = normalize_tenant(base_collection="mcp_debug")
848:     request_context = build_http_request_context(
849:         request,
850:         tenant=tenant,
851:         base_collection="mcp_debug",
852:         api_key=api_key,
853:         operation="debug_mcp_tools",
854:         subject="mcp_debug",
855:     )
856:     context = request.app.state.shell_context
857:     async with context.observability.timer("debug_mcp_tools"):
858:         enforce_http_guardrails(request, request_context=request_context)
859:         return {"tools": mcp_server.debug_tools()}
860: 
861: 
862: @app.post("/debug/mcp/call", tags=["MCP 调试"], summary="调试调用 MCP 工具")
863: async def debug_mcp_call(payload: MCPDebugCall, request: Request):
864:     """Call one MCP tool through an HTTP debug facade."""
865: 
866:     tenant = normalize_tenant(base_collection="mcp_debug")
867:     request_context = build_http_request_context(
868:         request,
869:         tenant=tenant,
870:         base_collection="mcp_debug",
871:         api_key=payload.api_key,
872:         operation="debug_mcp_call",
873:         subject="mcp_debug",
874:     )
875:     context = request.app.state.shell_context
876:     async with context.observability.timer("debug_mcp_call"):
877:         enforce_http_guardrails(request, request_context=request_context)
878:         result = await mcp_server.debug_call_tool(payload.tool, payload.arguments)
879:     return result
880: 
881: 
882: @app.post("/chat", tags=["对话与检索"], summary="对话问答")
883: async def chat_with_knowledge_base(chat_request: dict, request: Request):
884:     """Chat with knowledge base using LLM."""
885:     query = chat_request.get("query", "")
886:     collection = chat_request.get("collection", "default")
887:     kb_id = chat_request.get("kb_id")
888:     kb_ids = _parse_kb_ids(chat_request.get("kb_ids"))
889:     scope = chat_request.get("scope")
890:     limit = int(chat_request.get("limit", 5) or 5)
891:     user_id = chat_request.get("user_id")
892:     agent_id = chat_request.get("agent_id")
893:     api_key = chat_request.get("api_key")
894: 
895:     if not query:
896:         raise HTTPException(status_code=400, detail="Query is required")
897: 
898:     context = request.app.state.shell_context
899:     async with context.observability.timer("chat"):
900:         service = await get_rag_service(request)
901:         if kb_ids:
902:             contexts, search_response = await _search_across_knowledge_bases(
903:                 request=request,
904:                 service=service,
905:                 query=query,
906:                 collection=collection,
907:                 kb_ids=kb_ids,
908:                 scope=scope,
909:                 limit=limit,
910:                 user_id=user_id,
911:                 agent_id=agent_id,
912:                 api_key=api_key,
913:                 operation="chat",
914:             )
915:             context_text = _format_chat_context(search_response.results)
916:             prompt = _build_chat_prompt(query, context_text)
917:             try:
918:                 llm_model = await service.runtime.ensure_llm_model()
919:                 answer = await llm_model.generate(prompt)
920:             except Exception as exc:
921:                 logger.warning("LLM generation failed for multi-kb chat, using retrieval context fallback: %s", exc)
922:                 answer = _format_llm_fallback_response(context_text, exc)
923:             response = ChatResponse(
924:                 query=query,
925:                 collection="multi_kb",
926:                 response=answer,
927:                 sources=search_response.results,
928:             )
929:         else:
930:             _, request_context = _resolve_request_knowledge_base(
931:                 request,
932:                 kb_id=kb_id,
933:                 scope=scope,
934:                 collection=collection,
935:                 user_id=user_id,
936:                 agent_id=agent_id,
937:                 api_key=api_key,
938:                 operation="chat",
939:             )
940:             enforce_http_guardrails(request, request_context=request_context)
941:             response = await service.chat(
942:                 ChatRequest(
943:                     query=query,
944:                     collection=request_context.kb_name or collection,
945:                     limit=limit,
946:                     kb_id=request_context.kb_id,
947:                     scope=request_context.kb_scope,
948:                     tenant=request_context.tenant,
949:                     context=request_context,
950:                 )
951:             )
952:     return response.to_dict()
953: 
954: @app.get("/search", tags=["对话与检索"], summary="检索知识库")
955: async def search_documents(
956:     request: Request,
957:     query: str,
958:     collection: str = "default",
959:     kb_id: Optional[int] = None,
960:     kb_ids: Optional[str] = None,
961:     scope: Optional[str] = None,
962:     limit: int = 5,
963:     user_id: Optional[int] = None,
964:     agent_id: Optional[int] = None,
965:     api_key: Optional[str] = None,
966: ):
967:     """Search documents."""
968:     logger.info("Searching for '%s' in collection '%s'", query, collection)
969:     parsed_kb_ids = _parse_kb_ids(kb_ids)
970:     context = request.app.state.shell_context
971:     async with context.observability.timer("search"):
972:         service = await get_rag_service(request)
973:         if parsed_kb_ids:
974:             contexts, response = await _search_across_knowledge_bases(
975:                 request=request,
976:                 service=service,
977:                 query=query,
978:                 collection=collection,
979:                 kb_ids=parsed_kb_ids,
980:                 scope=scope,
981:                 limit=limit,
982:                 user_id=user_id,
983:                 agent_id=agent_id,
984:                 api_key=api_key,
985:                 operation="search",
986:             )
987:         else:
988:             _, request_context = _resolve_request_knowledge_base(
989:                 request,
990:                 kb_id=kb_id,
991:                 scope=scope,
992:                 collection=collection,
993:                 user_id=user_id,
994:                 agent_id=agent_id,
995:                 api_key=api_key,
996:                 operation="search",
997:             )
998:             enforce_http_guardrails(request, request_context=request_context)
999:             response = await service.search(
1000:                 SearchRequest(
1001:                     query=query,
1002:                     collection=request_context.kb_name or collection,
1003:                     limit=limit,
1004:                     kb_id=request_context.kb_id,
1005:                     scope=request_context.kb_scope,
1006:                     tenant=request_context.tenant,
1007:                     context=request_context,
1008:                 )
1009:             )
1010:     return response.to_dict()
1011: 
1012: @app.get("/list-documents", tags=["文档"], summary="列出文档记录")
1013: async def list_documents(
1014:     request: Request,
1015:     collection: str = "default",
1016:     kb_id: Optional[int] = None,
1017:     scope: Optional[str] = None,
1018:     limit: int = 100,
1019:     offset: int = 0,
1020:     filename: str = None,
1021:     user_id: Optional[int] = None,
1022:     agent_id: Optional[int] = None,
1023:     api_key: Optional[str] = None,
1024: ):
1025:     """List documents in a collection."""
1026:     _, request_context = _resolve_request_knowledge_base(
1027:         request,
1028:         kb_id=kb_id,
1029:         scope=scope,
1030:         collection=collection,
1031:         user_id=user_id,
1032:         agent_id=agent_id,
1033:         api_key=api_key,
1034:         operation="list_documents",
1035:     )
1036:     context = request.app.state.shell_context
1037:     async with context.observability.timer("list_documents"):
1038:         enforce_http_guardrails(request, request_context=request_context)
1039:         service = await get_rag_service(request)
1040:         result = await service.list_documents(
1041:             collection=request_context.kb_name or collection,
1042:             limit=limit,
1043:             offset=offset,
1044:             filename=filename,
1045:             request_context=request_context,
1046:         )
1047:     return result
1048: 
1049: 
1050: @app.delete("/delete-document", tags=["文档"], summary="删除文档记录")
1051: async def delete_document(document_request: DeleteDocumentRequest, request: Request):
1052:     """Delete a document."""
1053:     try:
1054:         _, request_context = _resolve_request_knowledge_base(
1055:             request,
1056:             kb_id=document_request.kb_id,
1057:             scope=document_request.scope,
1058:             collection=document_request.collection,
1059:             user_id=document_request.user_id,
1060:             agent_id=document_request.agent_id,
1061:             api_key=document_request.api_key,
1062:             operation="delete_document",
1063:         )
1064:         context = request.app.state.shell_context
1065:         async with context.observability.timer("delete_document"):
1066:             enforce_http_guardrails(request, request_context=request_context)
1067:             service = await get_rag_service(request)
1068:             success = await service.delete_document(
1069:                 document_id=document_request.document_id,
1070:                 collection=request_context.kb_name or document_request.collection,
1071:                 request_context=request_context,
1072:             )
1073:         if success:
1074:             return {"message": "Document deleted successfully"}
1075:         else:
1076:             raise HTTPException(status_code=404, detail="Document not found or failed to delete")
1077:     except HTTPException:
1078:         raise
1079:     except Exception as e:
1080:         logger.error(f"Error deleting document: {e}")
1081:         raise HTTPException(status_code=500, detail=str(e))
1082: 
1083: 
1084: @app.get("/list-files", tags=["文档"], summary="列出文件")
1085: async def list_files(
1086:     request: Request,
1087:     collection: str = "default",
1088:     kb_id: Optional[int] = None,
1089:     scope: Optional[str] = None,
1090:     user_id: Optional[int] = None,
1091:     agent_id: Optional[int] = None,
1092:     api_key: Optional[str] = None,
1093: ):
1094:     """List files in a collection."""
1095:     try:
1096:         _, request_context = _resolve_request_knowledge_base(
1097:             request,
1098:             kb_id=kb_id,
1099:             scope=scope,
1100:             collection=collection,
1101:             user_id=user_id,
1102:             agent_id=agent_id,
1103:             api_key=api_key,
1104:             operation="list_files",
1105:         )
1106:         context = request.app.state.shell_context
1107:         async with context.observability.timer("list_files"):
1108:             enforce_http_guardrails(request, request_context=request_context)
1109:             service = await get_rag_service(request)
1110:             result = await service.list_files(
1111:                 collection=request_context.kb_name or collection,
1112:                 request_context=request_context,
1113:             )
1114:         return {"files": result}
1115:     except HTTPException:
1116:         raise
1117:     except Exception as e:
1118:         logger.error(f"Error listing files: {e}")
1119:         raise HTTPException(status_code=500, detail=str(e))
1120: 
1121: 
1122: @app.delete("/delete-file", tags=["文档"], summary="删除文件")
1123: async def delete_file(file_request: DeleteFileRequest, request: Request):
1124:     """Delete a file."""
1125:     try:
1126:         _, request_context = _resolve_request_knowledge_base(
1127:             request,
1128:             kb_id=file_request.kb_id,
1129:             scope=file_request.scope,
1130:             collection=file_request.collection,
1131:             user_id=file_request.user_id,
1132:             agent_id=file_request.agent_id,
1133:             api_key=file_request.api_key,
1134:             operation="delete_file",
1135:         )
1136:         context = request.app.state.shell_context
1137:         async with context.observability.timer("delete_file"):
1138:             enforce_http_guardrails(request, request_context=request_context)
1139:             service = await get_rag_service(request)
1140:             success = await service.delete_file(
1141:                 filename=file_request.filename,
1142:                 collection=request_context.kb_name or file_request.collection,
1143:                 request_context=request_context,
1144:             )
1145:         if success:
1146:             return {"message": "File deleted successfully"}
1147:         else:
1148:             raise HTTPException(status_code=404, detail="File not found or failed to delete")
1149:     except HTTPException:
1150:         raise
1151:     except Exception as e:
1152:         logger.error(f"Error deleting file: {e}")
1153:         raise HTTPException(status_code=500, detail=str(e))

(End of file - total 1153 lines)
</content>
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 3.8s)

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag\\src\\mcp_rag\\services\\indexing_service.py"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\indexing_service.py</path>
<type>file</type>
<content>1: """Indexing service for document ingestion and management."""
2: 
3: from __future__ import annotations
4: 
5: import logging
6: import re
7: import shutil
8: import tempfile
9: from pathlib import Path
10: from typing import Any, Dict, List, Sequence
11: 
12: from fastapi import UploadFile
13: 
14: from ..context import RequestContext, normalize_request_context
15: from ..contracts import BatchUploadResponse, DocumentRequest, TenantSpec, UploadFileResult
16: from ..core.indexing.models import TenantContext as CoreTenantContext
17: from ..security import IndexQuotaPolicy, QuotaExceededError, UploadQuotaPolicy
18: from .runtime import ServiceRuntime
19: 
20: logger = logging.getLogger(__name__)
21: 
22: _FILE_NAME_RE = re.compile(r"[/\\:*?\"<>|]+")
23: 
24: 
25: class IndexingService:
26:     """Document ingestion, listing, and deletion operations."""
27: 
28:     def __init__(self, runtime: ServiceRuntime):
29:         self.runtime = runtime
30: 
31:     @staticmethod
32:     def _is_expected_upload_failure(exc: Exception) -> bool:
33:         if isinstance(exc, QuotaExceededError):
34:             return True
35:         message = str(exc)
36:         return any(
37:             token in message
38:             for token in (
39:                 "Embedding API error:",
40:                 "429",
41:                 "余额不足",
42:                 "无可用资源包",
43:                 "cooldown",
44:                 "rate limit",
45:             )
46:         )
47: 
48:     def _log_upload_failure(self, *, filename: str, collection_name: str, exc: Exception) -> None:
49:         provider = getattr(self.runtime.settings, "embedding_provider", "unknown")
50:         if self._is_expected_upload_failure(exc):
51:             logger.warning(
52:                 "Upload failed for %s in %s via embedding provider %s: %s",
53:                 filename,
54:                 collection_name,
55:                 provider,
56:                 exc,
57:             )
58:             return
59:         logger.exception("Failed to process upload %s in %s", filename, collection_name)
60: 
61:     async def add_document(self, request: DocumentRequest) -> Dict[str, Any]:
62:         request_context = normalize_request_context(
63:             request.context,
64:             tenant=request.tenant,
65:             base_collection=request.collection,
66:             kb_id=request.kb_id,
67:             kb_scope=request.scope,
68:         )
69:         tenant = request_context.tenant.to_core()
70:         collection_name = request_context.resolved_collection or request.collection
71:         processor = await self.runtime.ensure_document_processor()
72:         vector_store = await self.runtime.ensure_vector_store()
73:         embedding_model = await self.runtime.ensure_embedding_model()
74:         self.runtime.attach_embedding_model(vector_store, embedding_model)
75: 
76:         filename = self._resolve_filename(request.metadata, fallback="manual_input")
77:         processed = processor.process_text(
78:             request.content,
79:             source=request.metadata.get("source", "manual_input"),
80:             filename=filename,
81:             file_type=request.metadata.get("file_type", "text"),
82:             metadata=request.metadata,
83:         )
84:         chunks = processor.chunk_document(processed)
85:         if not chunks:
86:             raise ValueError("No content extracted from document")
87:         self._enforce_index_quota(document_count=1, chunks=chunks)
88: 
89:         await vector_store.upsert_chunks(
90:             chunks,
91:             tenant=tenant,
92:             collection_name=collection_name,
93:         )
94:         await self.runtime.refresh_keywords(collection_name, tenant)
95:         self.runtime.invalidate_retrieval_scope(collection_name, tenant)
96: 
97:         return {
98:             "message": "Document added successfully",
99:             "document_id": processed.document_id,
100:             "chunk_count": len(chunks),
101:         }
102: 
103:     async def upload_files(
104:         self,
105:         files: Sequence[UploadFile],
106:         *,
107:         collection: str = "default",
108:         tenant: TenantSpec | Dict[str, Any] | None = None,
109:         request_context: RequestContext | None = None,
110:     ) -> Dict[str, Any]:
111:         resolved_context = normalize_request_context(
112:             request_context,
113:             tenant=tenant,
114:             base_collection=collection,
115:         )
116:         tenant_spec = resolved_context.tenant
117:         collection_name = resolved_context.resolved_collection or collection
118:         processor = await self.runtime.ensure_document_processor()
119:         vector_store = await self.runtime.ensure_vector_store()
120:         embedding_model = await self.runtime.ensure_embedding_model()
121:         self.runtime.attach_embedding_model(vector_store, embedding_model)
122: 
123:         upload_policy = UploadQuotaPolicy.from_settings(self.runtime.settings)
124:         file_sizes = [self._measure_upload_size(upload) for upload in files]
125:         try:
126:             upload_policy.require(file_sizes)
127:         except QuotaExceededError as exc:
128:             return BatchUploadResponse(
129:                 total_files=len(files),
130:                 successful=0,
131:                 failed=len(files),
132:                 results=[
133:                     UploadFileResult(
134:                         filename=getattr(upload, "filename", "unknown"),
135:                         file_type="unknown",
136:                         content_length=file_sizes[index],
137:                         processed=False,
138:                         error=str(exc),
139:                         preview="",
140:                     )
141:                     for index, upload in enumerate(files)
142:                 ],
143:             ).to_dict()
144: 
145:         results: list[UploadFileResult] = []
146:         indexed_documents = 0
147:         indexed_chunks = 0
148:         indexed_chars = 0
149:         cache_dirty = False
150:         for upload in files:
151:             temp_path: Path | None = None
152:             try:
153:                 visible_source = Path(upload.filename).name if upload.filename else "upload"
154:                 temp_path = await self._write_upload_to_tempfile(upload)
155:                 processed_doc = processor.process_file(
156:                     temp_path,
157:                     metadata={"source": visible_source, "filename": visible_source},
158:                     filename=visible_source,
159:                 )
160:                 processed_doc.source = visible_source
161:                 processed_doc.filename = visible_source
162:                 processed_doc.metadata["source"] = visible_source
163:                 processed_doc.metadata["filename"] = visible_source
164:                 if processed_doc.error or not processed_doc.content.strip():
165:                     results.append(
166:                         UploadFileResult(
167:                             filename=visible_source,
168:                             file_type=processed_doc.file_type,
169:                             content_length=len(processed_doc.content),
170:                             processed=False,
171:                             error=processed_doc.error or "No content extracted",
172:                             preview="",
173:                         )
174:                     )
175:                     continue
176: 
177:                 chunks = processor.chunk_document(processed_doc)
178:                 next_document_count = indexed_documents + 1
179:                 next_chunk_count = indexed_chunks + len(chunks)
180:                 next_total_chars = indexed_chars + sum(len(chunk.content) for chunk in chunks)
181:                 self._enforce_index_quota(
182:                     document_count=next_document_count,
183:                     chunk_count=next_chunk_count,
184:                     total_chars=next_total_chars,
185:                 )
186:                 await vector_store.upsert_chunks(
187:                     chunks,
188:                     tenant=tenant_spec.to_core(),
189:                     collection_name=collection_name,
190:                 )
191:                 await self.runtime.refresh_keywords(collection_name, tenant_spec.to_core())
192:                 cache_dirty = True
193:                 indexed_documents = next_document_count
194:                 indexed_chunks = next_chunk_count
195:                 indexed_chars = next_total_chars
196: 
197:                 preview = processed_doc.content[:500]
198:                 if len(processed_doc.content) > 500:
199:                     preview += "..."
200: 
201:                 results.append(
202:                     UploadFileResult(
203:                         filename=visible_source,
204:                         file_type=processed_doc.file_type,
205:                         content_length=len(processed_doc.content),
206:                         processed=True,
207:                         error="",
208:                         preview=preview,
209:                     )
210:                 )
211:             except Exception as exc:
212:                 failed_filename = Path(getattr(upload, "filename", "unknown")).name
213:                 self._log_upload_failure(
214:                     filename=failed_filename,
215:                     collection_name=collection_name,
216:                     exc=exc,
217:                 )
218:                 results.append(
219:                     UploadFileResult(
220:                         filename=failed_filename,
221:                         file_type="unknown",
222:                         content_length=0,
223:                         processed=False,
224:                         error=str(exc),
225:                         preview="",
226:                     )
227:                 )
228:             finally:
229:                 if temp_path is not None and temp_path.exists():
230:                     temp_path.unlink(missing_ok=True)
231: 
232:         if indexed_documents > 0:
233:             self.runtime.invalidate_retrieval_scope(collection_name, tenant_spec.to_core())
234: 
235:         return BatchUploadResponse(
236:             total_files=len(files),
237:             successful=len([item for item in results if item.processed]),
238:             failed=len([item for item in results if not item.processed]),
239:             results=results,
240:         ).to_dict()
241: 
242:     async def list_documents(
243:         self,
244:         *,
245:         collection: str = "default",
246:         limit: int = 100,
247:         offset: int = 0,
248:         filename: str | None = None,
249:         tenant: TenantSpec | Dict[str, Any] | None = None,
250:         request_context: RequestContext | None = None,
251:     ) -> Dict[str, Any]:
252:         vector_store = await self.runtime.ensure_vector_store()
253:         tenant_spec = normalize_request_context(
254:             request_context,
255:             tenant=tenant,
256:             base_collection=collection,
257:         ).tenant
258:         resolved_collection = normalize_request_context(
259:             request_context,
260:             tenant=tenant,
261:             base_collection=collection,
262:         ).resolved_collection or collection
263:         return await vector_store.list_documents(
264:             collection_name=resolved_collection,
265:             limit=limit,
266:             offset=offset,
267:             filename=filename,
268:             tenant=tenant_spec.to_core(),
269:         )
270: 
271:     async def list_files(
272:         self,
273:         *,
274:         collection: str = "default",
275:         tenant: TenantSpec | Dict[str, Any] | None = None,
276:         request_context: RequestContext | None = None,
277:     ) -> List[Dict[str, Any]]:
278:         vector_store = await self.runtime.ensure_vector_store()
279:         tenant_spec = normalize_request_context(
280:             request_context,
281:             tenant=tenant,
282:             base_collection=collection,
283:         ).tenant
284:         resolved_collection = normalize_request_context(
285:             request_context,
286:             tenant=tenant,
287:             base_collection=collection,
288:         ).resolved_collection or collection
289:         return await vector_store.list_files(
290:             collection_name=resolved_collection,
291:             tenant=tenant_spec.to_core(),
292:         )
293: 
294:     async def list_collections(
295:         self,
296:         *,
297:         tenant: TenantSpec | Dict[str, Any] | None = None,
298:         request_context: RequestContext | None = None,
299:     ) -> List[str]:
300:         vector_store = await self.runtime.ensure_vector_store()
301:         collections = await vector_store.list_collections()
302:         names = [entry["name"] for entry in collections]
303: 
304:         tenant_spec = None
305:         if tenant is not None or request_context is not None:
306:             tenant_spec = normalize_request_context(request_context, tenant=tenant).tenant
307:         if tenant_spec is None:
308:             return sorted(names)
309: 
310:         filtered: list[str] = []
311:         for item in collections:
312:             if tenant_spec.user_id is not None and item.get("user_id") != tenant_spec.user_id:
313:                 continue
314:             if tenant_spec.agent_id is not None and item.get("agent_id") != tenant_spec.agent_id:
315:                 continue
316:             filtered.append(str(item["name"]))
317:         return sorted(filtered)
318: 
319:     async def delete_document(
320:         self,
321:         *,
322:         document_id: str,
323:         collection: str = "default",
324:         tenant: TenantSpec | Dict[str, Any] | None = None,
325:         request_context: RequestContext | None = None,
326:     ) -> bool:
327:         vector_store = await self.runtime.ensure_vector_store()
328:         tenant_spec = normalize_request_context(
329:             request_context,
330:             tenant=tenant,
331:             base_collection=collection,
332:         )
333:         deleted = await self._delete_document_identifier(
334:             vector_store,
335:             identifier=document_id,
336:             collection=tenant_spec.resolved_collection or collection,
337:             tenant=tenant_spec.tenant.to_core(),
338:         )
339:         if deleted:
340:             await self.runtime.refresh_keywords(tenant_spec.resolved_collection or collection, tenant_spec.tenant.to_core())
341:             self.runtime.invalidate_retrieval_scope(
342:                 tenant_spec.resolved_collection or collection,
343:                 tenant_spec.tenant.to_core(),
344:             )
345:         return deleted
346: 
347:     async def delete_file(
348:         self,
349:         *,
350:         filename: str,
351:         collection: str = "default",
352:         tenant: TenantSpec | Dict[str, Any] | None = None,
353:         request_context: RequestContext | None = None,
354:     ) -> bool:
355:         vector_store = await self.runtime.ensure_vector_store()
356:         tenant_spec = normalize_request_context(
357:             request_context,
358:             tenant=tenant,
359:             base_collection=collection,
360:         )
361:         result = await vector_store.delete_file(
362:             filename,
363:             collection_name=tenant_spec.resolved_collection or collection,
364:             tenant=tenant_spec.tenant.to_core(),
365:         )
366:         await self.runtime.refresh_keywords(tenant_spec.resolved_collection or collection, tenant_spec.tenant.to_core())
367:         if result:
368:             self.runtime.invalidate_retrieval_scope(
369:                 tenant_spec.resolved_collection or collection,
370:                 tenant_spec.tenant.to_core(),
371:             )
372:         return result
373: 
374:     async def _delete_document_identifier(
375:         self,
376:         vector_store,
377:         *,
378:         identifier: str,
379:         collection: str,
380:         tenant: CoreTenantContext,
381:     ) -> bool:
382:         get_collection = getattr(vector_store, "_get_collection", None)
383:         if not callable(get_collection):
384:             return await vector_store.delete_document(
385:                 identifier,
386:                 collection_name=collection,
387:                 tenant=tenant,
388:             )
389: 
390:         collection_handle = await get_collection(collection, tenant)
391:         deleted = False
392: 
393:         try:
394:             exact_chunk = collection_handle.get(ids=[identifier], include=["metadatas"])
395:             if exact_chunk.get("ids"):
396:                 collection_handle.delete(ids=[identifier])
397:                 deleted = True
398:         except Exception as exc:
399:             logger.debug("Exact chunk delete probe failed for %s: %s", identifier, exc)
400: 
401:         try:
402:             document_matches = collection_handle.get(where={"document_id": identifier}, include=["metadatas"])
403:             if document_matches.get("ids"):
404:                 collection_handle.delete(where={"document_id": identifier})
405:                 deleted = True
406:         except Exception as exc:
407:             logger.debug("Document-id delete probe failed for %s: %s", identifier, exc)
408: 
409:         return deleted
410: 
411:     async def _write_upload_to_tempfile(self, upload: UploadFile) -> Path:
412:         suffix = Path(upload.filename or "").suffix
413:         with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
414:             shutil.copyfileobj(upload.file, temp_file)
415:             return Path(temp_file.name)
416: 
417:     def _enforce_index_quota(
418:         self,
419:         *,
420:         document_count: int,
421:         chunks: Sequence[Any] | None = None,
422:         chunk_count: int | None = None,
423:         total_chars: int | None = None,
424:     ) -> None:
425:         policy = IndexQuotaPolicy.from_settings(self.runtime.settings)
426:         effective_chunk_count = chunk_count if chunk_count is not None else len(list(chunks or ()))
427:         effective_total_chars = total_chars if total_chars is not None else sum(
428:             len(getattr(chunk, "content", "")) for chunk in (chunks or ())
429:         )
430:         policy.require(
431:             document_count=document_count,
432:             chunk_count=effective_chunk_count,
433:             total_chars=effective_total_chars,
434:         )
435: 
436:     def _measure_upload_size(self, upload: UploadFile) -> int:
437:         current_position = upload.file.tell()
438:         upload.file.seek(0, 2)
439:         size = int(upload.file.tell())
440:         upload.file.seek(current_position)
441:         return size
442: 
443:     def _resolve_filename(self, metadata: Dict[str, Any], fallback: str = "manual_input") -> str:
444:         raw = str(metadata.get("filename") or metadata.get("title") or fallback or "manual_input").strip()
445:         raw = _FILE_NAME_RE.sub("_", raw)
446:         return raw[:80] or "manual_input"

(End of file - total 446 lines)
</content>
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 15.3s)

知识库添加和生成流程如下：

## 知识库创建流程
1. **创建知识库**：通过 `POST /knowledge-bases` 接口创建，指定名称、作用域（public/agent_private）和所有者信息
2. **自动分配ID**：系统为新知识库分配唯一 `kb_id` 和内部集合名 `kb_<id>`
3. **持久化存储**：知识库元数据保存到 `knowledge_bases.sqlite3` SQLite数据库

## 文档添加流程
有两种方式添加文档到知识库：

### 1. 单文档添加 (`POST /add-document`)
- **参数**：content（文本内容）、kb_id（知识库ID）、metadata（元数据）
- **处理流程**：
  - 验证配额限制（文档数/字符数）
  - 文本分块（使用text_splitter）
  - 向量化（调用embedding模型）
  - 存入Chroma向量数据库
  - 更新关键词索引
  - 清理检索缓存

### 2. 文件上传 (`POST /upload-files`)
- **支持格式**：txt、md、pdf、docx
- **处理流程**：
  - 文件大小和数量配额检查
  - 临时文件写入
  - 文件解析提取文本（使用PyPDF2/python-docx等）
  - 文本分块和向量化
  - 批量存入向量数据库
  - 更新关键词索引和缓存

## 核心组件交互
```
HTTP API → service_facade.py → indexing_service.py 
    → document_processor.py（文件解析/分块）
    → embeddings.py（向量化）
    → vector_store.py（Chroma存储）
    → knowledge_bases.py（知识库管理）
```

## 关键特性
- **多租户支持**：基于 `user_id + agent_id` 的租户隔离
- **配额控制**：上传文件大小、文档数量、字符总数限制
- **混合检索**：同时维护向量索引和关键词索引
- **缓存失效**：文档变更后自动清理相关检索缓存

---

## User

@src\mcp_rag\service_facade.py 模块作用和工作流程？

---

## Assistant (Build · qwen3-max-2026-01-23 · 14.2s)

`service_facade.py` 模块是**统一服务门面**，作用和工作流程如下：

## 核心作用
- **统一入口**：为HTTP和MCP协议提供一致的服务接口
- **租户上下文标准化**：通过 `normalize_request_context` 统一处理多租户信息
- **服务协调**：协调索引、检索、聊天三大核心服务

## 工作流程
1. **初始化**：创建 `RagService` 实例，包含：
   - `ServiceRuntime`（运行时依赖管理）
   - `IndexingService`（文档管理）
   - `RetrievalService`（检索服务）  
   - `ChatService`（对话服务）

2. **请求处理**：
   - 接收来自HTTP/MCP的请求
   - 标准化租户上下文（用户/代理/知识库信息）
   - 路由到对应的服务组件执行具体逻辑

3. **单例模式**：通过 `get_rag_service()` 提供全局唯一的 `RagService` 实例

## 关键特性
- **协议无关**：HTTP和MCP调用相同的业务逻辑
- **上下文隔离**：每个请求都有独立的租户上下文
- **服务解耦**：门面层不包含业务逻辑，只负责协调



---

## User

知识库生成后有哪些使用方法及如何被使用

---

## Assistant (Build · qwen3-max-2026-01-23 · 4.3s)

**Tool: grep**

**Input:**
```json
{
  "pattern": "kb_id|knowledge.*base|rag_ask"
}
```

**Output:**
```
Found 271 matches (showing first 100)
D:\xfwork\mcprag\mcp-rag\tests\test_config.py:
  Line 219:             db_path = Path(tmpdir) / "knowledge_bases.sqlite3"
  Line 225:                         "knowledge_base_db_path": str(db_path),
  Line 258:             db_path = Path(tmpdir) / "knowledge_bases.sqlite3"
  Line 262:                         "knowledge_base_db_path": str(db_path),

D:\xfwork\mcprag\mcp-rag\tests\test_http_server.py:
  Line 124:             knowledge_bases = self.client.get("/knowledge-bases", params={"user_id": 7, "agent_id": 2})
  Line 125:             self.assertEqual(knowledge_bases.status_code, 200)
  Line 126:             self.assertTrue(knowledge_bases.json()["knowledge_bases"])
  Line 197:             search = self.client.get("/search", params={"query": "fastapi", "kb_ids": "1,2", "user_id": 7, "agent_id": 2})
  Line 205:                 json={"query": "What is FastAPI?", "kb_ids": [1, 2], "user_id": 7, "agent_id": 2},
  Line 220:         self.assertEqual(payload[0]["name"], "rag_ask")
  Line 222:         with patch.object(http_server_module.mcp_server, "debug_call_tool", AsyncMock(return_value={"tool": "rag_ask", "contents": [{"type": "text", "text": "ok"}]})):
  Line 225:                 json={"tool": "rag_ask", "arguments": {"query": "fastapi", "scope": "public"}},
  Line 228:             self.assertEqual(result.json()["tool"], "rag_ask")
  Line 477:             self.assertTrue(any(tool["name"] == "rag_ask" for tool in tools_payload))
  Line 487:                         "name": "rag_ask",

D:\xfwork\mcprag\mcp-rag\tests\test_mcp_server.py:
  Line 14:     async def test_rag_ask_formats_results_and_summary(self):
  Line 37:             content = await server.handle_rag_ask(
  Line 56:     async def test_rag_ask_accepts_legacy_tenant_fields(self):
  Line 70:             content = await server.handle_rag_ask(
  Line 86:     async def test_rag_ask_enforces_api_key_and_rate_limit(self):
  Line 112:         denied = await server.handle_rag_ask({"query": "fastapi", "collection": "docs"})
  Line 115:         allowed = await server.handle_rag_ask(
  Line 120:         throttled = await server.handle_rag_ask(

D:\xfwork\mcprag\mcp-rag\tests\e2e\test_shell_integration.py:
  Line 151:         mcp_result = await server.handle_rag_ask(
  Line 185:         self.assertGreaterEqual(self.context.observability.snapshot().operations["mcp.rag_ask"].count, 1)
  Line 234:             self.assertTrue(any(tool["name"] == "rag_ask" for tool in tools_response.json()["result"]["tools"]))
  Line 244:                         "name": "rag_ask",

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\static\app\assets\index-DQAj2c0D.js:
  Line 425:  */const n=[["path",{d:"M10 11v6"}],["path",{d:"M14 11v6"}],["path",{d:"M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"}],["path",{d:"M3 6h18"}],["path",{d:"M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"}]];ya(e,wa({name:"trash-2"},()=>i,{get iconNode(){return n},children:(o,c)=>{var f=Yt(),_=Ce(f);ar(_,r,"default",{}),k(o,f)},$$slots:{default:!0}}))}const Rv="".trim(),oo=Rv.replace(/\/+$/,"");function Sn(e={}){return!e||typeof e!="object"||Array.isArray(e)||e.kb_id!==void 0&&e.kb_id!==null||e.kbId===void 0||e.kbId===null?e:{...e,kb_id:e.kbId}}class zv extends Error{constructor(r,i,n){super(i),this.name="ApiError",this.status=r,this.payload=n}}function jv(e,r={}){const i=oo?`${oo}${e}`:e,n=new URL(i,window.location.origin);for(const[o,c]of Object.entries(r))if(!(c==null||c==="")){if(Array.isArray(c)){if(!c.length)continue;n.searchParams.set(o,c.join(","));continue}n.searchParams.set(o,String(c))}return n.toString()}function mt(e={}){const r={},i=e.apiKey||e.api_key;return i&&(r["x-api-key"]=i),r}async function bt(e,{method:r="GET",query:i={},body:n,formData:o,headers:c={}}={}){const f={...c},_={method:r,headers:f};o?_.body=o:n!==void 0&&(_.body=JSON.stringify(n),f["Content-Type"]||(f["Content-Type"]="application/json"));const b=await fetch(jv(e,i),_),h=await b.text();let y=null;if(h)try{y=JSON.parse(h)}catch{y=h}if(!b.ok){const M=typeof y=="object"&&y?y.detail||y.message||b.statusText:h||b.statusText;throw new zv(b.status,M,y)}return y}function vi(e={}){const r={};return e.userId&&(r.user_id=e.userId),e.agentId&&(r.agent_id=e.agentId),e.kbId&&(r.kb_id=e.kbId),e.scope&&(r.scope=e.scope),(e.apiKey||e.api_key)&&(r.api_key=e.apiKey||e.api_key),r}const at={health:(e={})=>bt("/health",{headers:mt(e)}),ready:(e={})=>bt("/ready",{headers:mt(e)}),metrics:(e={})=>bt("/metrics",{headers:mt(e)}),config:(e={})=>bt("/config",{query:vi(e),headers:mt(e)}),updateConfig:(e,r={})=>bt("/config/bulk",{method:"POST",body:{updates:e},headers:mt(r)}),resetConfig:(e={})=>bt("/config/reset",{method:"POST...
  Line 426: `).map(s=>s.trim()).filter(Boolean)}function Be(a){const s=Number(a||0);if(!Number.isFinite(s)||s<=0)return"0 B";const u=["B","KB","MB","GB"];let g=s,w=0;for(;g>=1024&&w<u.length-1;)g/=1024,w+=1;return`${g.toFixed(g>=10?0:1)} ${u[w]}`}function De(a){if(!a)return"未采样";const s=new Date(a*1e3||a);return Number.isNaN(s.getTime())?"未采样":s.toLocaleString()}function U(a){return a==null||Number.isNaN(Number(a))?"0%":`${(Number(a)*100).toFixed(1)}%`}function pe(a,s=180){const u=String(a??"");return u.length>s?`${u.slice(0,s)}...`:u}function $e(a){const s=String(a).toLowerCase();return["ready","healthy","configured","enabled","ok","success"].includes(s)?"good":["warn","warning","degraded","partial","limited"].includes(s)?"warn":["error","failed","misconfigured","unhealthy","cooldown"].includes(s)?"bad":"info"}function Se(a,s="未知"){return a==null||a===""?s:String(a)}function Re(a){return`${Number(a||0).toFixed(3)} / 1.000`}function Pe(a){const s=String(a||"").trim().toLowerCase();return h[s]||s}function qe(a={}){const s={};for(const[u,g]of Object.entries(a||{}))s[Pe(u)]=g;return s}function $t(a){if(!a)return a;const s=qe(a.provider_configs||{});return{...a,embedding_provider:Pe(a.embedding_provider),embedding_fallback_provider:Pe(a.embedding_fallback_provider),llm_provider:Pe(a.llm_provider),llm_fallback_provider:Pe(a.llm_fallback_provider),provider_configs:s}}function Xe(a){const u={...$t(a)||{}};for(const g of y)delete u[g];return u}function fe(a){const s=Array.isArray(a==null?void 0:a.results)?a.results.filter(u=>!(u!=null&&u.processed)):[];return s.length?s.slice(0,3).map(u=>`${Se(u.filename,"unknown")}: ${Se(u.error,"上传失败")}`).join("；"):""}function Te(a){const s=Pe(a);return _.find(u=>u.id===s)||null}function Kr(a){return _.filter(s=>s.families.includes(a))}function Rr(a){return Kr(a).map(s=>({value:s.id,label:s.title}))}function ei(a){return a==="chat"?"llm_model":"embedding_model"}function Rt(a,s,u=""){var Y,K;const g=Pe(a),w=qe(q({},t(v).provider_configs_text));let S=(...
  Line 427: `):"",tenant_api_keys_text:JSON.stringify(((S=a.security)==null?void 0:S.tenant_api_keys)??{},null,2)},s.rate_limit={...s.rate_limit,...a.rate_limit||{}},s.quotas={...s.quotas,...a.quotas||{}},s.observability={...s.observability,...a.observability||{}},s.provider_budget={...s.provider_budget,...a.provider_budget||{},embeddings:{...s.provider_budget.embeddings,...((ge=a.provider_budget)==null?void 0:ge.embeddings)||{}},llm:{...s.provider_budget.llm,...((Y=a.provider_budget)==null?void 0:Y.llm)||{}}},s.provider_configs_text=JSON.stringify(a.provider_configs??{},null,2);const u=((K=a.provider_configs)==null?void 0:K[s.embedding_provider])??{};s.embedding_base_url=u.base_url??"",s.embedding_model=u.embedding_model??"",s.embedding_api_key=u.api_key??"";const g=((V=a.provider_configs)==null?void 0:V[s.llm_provider])??{};s.llm_model=g.llm_model??"",s.llm_base_url=a.llm_base_url??g.base_url??s.llm_base_url,s.llm_api_key=a.llm_api_key??g.api_key??s.llm_api_key,s.full_config_text=JSON.stringify(Xe(a),null,2),p(v,s),Id()}function rl(){const a=qe(q({},t(v).provider_configs_text)),s=Pe(t(v).llm_provider),u=Pe(t(v).embedding_provider),g=a[s]||{},w=a[u]||{},S={...a};return u&&(S[u]={...S[u]||{},...w,embedding_model:t(v).embedding_model||w.embedding_model||"",model:""}),s&&(S[s]={...S[s]||{},...g,llm_model:t(v).llm_model||g.llm_model||"",model:"",base_url:g.base_url??t(v).llm_base_url,api_key:g.api_key??t(v).llm_api_key??null}),{host:t(v).host,port:Number(t(v).port),http_port:Number(t(v).http_port),debug:!!t(v).debug,vector_db_type:t(v).vector_db_type,chroma_persist_directory:t(v).chroma_persist_directory,knowledge_base_db_path:t(v).knowledge_base_db_path,qdrant_url:t(v).qdrant_url,embedding_provider:u,embedding_fallback_provider:Pe(t(v).embedding_fallback_provider)||null,embedding_device:t(v).embedding_device,embedding_cache_dir:t(v).embedding_cache_dir||null,llm_provider:s,llm_fallback_provider:Pe(t(v).llm_fallback_provider)||null,llm_model:t(v).llm_model||g.llm_model||"",llm_bas...
  Line 431: `),S=g[0];p(Wr,{...S,id:`${Nr}`,content:w||S.content||"该文件暂无可预览内容。",metadata:{...S.metadata,filename:Nr}})}async function ec({silent:a=!1,refresh:s=!0}={}){try{let u=rl();if(t(Pr)==="advanced"&&(u=q(null,t(v).full_config_text),!u||typeof u!="object"||Array.isArray(u)))throw new Error("高级配置必须是 JSON 对象");await at.updateConfig(u,t(B)),a||me("配置已保存","后台已重新加载运行时。","success"),s&&await hn()}catch(u){throw a||me("保存失败",u.message,"error"),u}finally{}}async function Mi(){if(t(Ee)==="config"&&(Xn=!0,!es)){es=!0;try{for(;Xn;){Xn=!1;try{await ec({silent:!0,refresh:!1})}catch(a){me("自动保存失败",a.message,"error")}}}finally{es=!1}}}function tc(a){const s=a.target;(s instanceof HTMLInputElement||s instanceof HTMLTextAreaElement)&&(s.type==="checkbox"||s.type==="radio"||Mi())}function rc(a){const s=a.target;s instanceof HTMLInputElement&&(s.type!=="checkbox"&&s.type!=="radio"||Mi())}function yl(a){return s=>{a(s),Mi()}}function ic(){return`${t(gt).length} 个知识库`}function kl(){var a;return!!((a=t(jr))!=null&&a.ready)}function xl(){var a,s;return!!(((a=t(br))==null?void 0:a.healthy)??((s=t(br))==null?void 0:s.ready))}function ac(){var g,w,S;const a=((g=t(Ut))==null?void 0:g.total_requests)??0,s=((w=t(Ut))==null?void 0:w.error_count)??((S=t(Ut))==null?void 0:S.errors)??0,u=a?s/a:0;return`${a} 次请求，错误率 ${U(u)}`}function Ba(){return t(Ee)==="workspace"?(async()=>{await Ii({silent:!0}),(t(Ue)==="detail"||t(Ue)==="detail-preview")&&(await ta(),t(Ue)==="detail-preview"&&Nr&&await wl({silent:!0}))})():t(Ee)==="overview"?hn():t(Ee)==="documents"?dl():t(Ee)==="mcp"?ol({silent:!0}):ll()}function nc(){var s;const a=((s=t(Ut))==null?void 0:s.operations)||{};return Object.entries(a).map(([u,g])=>({name:u,stats:g})).sort((u,g)=>g.stats.count-u.stats.count)}function sc(){var s;const a=((s=t(Ut))==null?void 0:s.providers)||{};return Object.entries(a).map(([u,g])=>({name:u,stats:g})).sort((u,g)=>g.stats.count-u.stats.count)}function lc(){var s,u;const a=((s=t(jr))==null?void 0:s.runtime)||((u=t(br))==null?v...

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\retrieval_service.py:
  Line 1: """Retrieval service for search and rag_ask flows."""
  Line 28:             kb_id=request.kb_id,
  Line 45:             kb_id=request.kb_id,
  Line 99:         """Compatibility wrapper for rag_ask."""
  Line 105:             kb_id=request.kb_id,

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\chat_service.py:
  Line 25:     """Generate chat responses from retrieved knowledge base context."""
  Line 36:             kb_id=request.kb_id,
  Line 45:                 kb_id=request.kb_id,

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\indexing_service.py:
  Line 66:             kb_id=request.kb_id,

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\mcp_server.py:
  Line 13: from .knowledge_bases import KnowledgeBaseAccessError
  Line 50:                     name="rag_ask",
  Line 70:                             "kb_id": {
  Line 139:             if name == "rag_ask":
  Line 140:                 return await self.handle_rag_ask(arguments)
  Line 148:                 "name": "rag_ask",
  Line 156:                         "kb_id": {"type": "integer"},
  Line 177:         if name == "rag_ask":
  Line 178:             payload = await self.handle_rag_ask(arguments)
  Line 193:     async def handle_rag_ask(self, arguments: Dict[str, Any]) -> Sequence[types.TextContent]:
  Line 194:         """Handle rag_ask tool call with shell-level formatting."""
  Line 203:             kb_id = arguments.get("kb_id")
  Line 209:             resolved_scope = self.shell_context.knowledge_bases.normalize_scope(scope, user_id=user_id, agent_id=agent_id)
  Line 210:             resolution = self.shell_context.knowledge_bases.resolve(
  Line 211:                 kb_id=kb_id,
  Line 235:                 kb_id=resolution.kb_id,
  Line 239:                 operation="rag_ask",
  Line 246:             with self.shell_context.observability.timer("mcp.rag_ask"):
  Line 259:                         kb_id=resolution.kb_id,

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\http_server.py:
  Line 22: from .knowledge_bases import KnowledgeBaseAccessError
  Line 161:     kb_id: Optional[int] = None
  Line 173:     kb_id: Optional[int] = None
  Line 184:     kb_id: Optional[int] = None
  Line 192:     """Create knowledge base request."""
  Line 296: def _resolve_request_knowledge_base(
  Line 299:     kb_id: int | None = None,
  Line 308:     resolved_scope = shell_context.knowledge_bases.normalize_scope(scope, user_id=user_id, agent_id=agent_id)
  Line 310:         resolution = shell_context.knowledge_bases.resolve(
  Line 311:             kb_id=kb_id,
  Line 325:     effective_user_id = resolution.knowledge_base.owner_user_id if resolution.scope == "agent_private" else None
  Line 326:     effective_agent_id = resolution.knowledge_base.owner_agent_id if resolution.scope == "agent_private" else None
  Line 339:         kb_id=resolution.kb_id,
  Line 349: def _parse_kb_ids(raw_value: Any) -> list[int]:
  Line 367: async def _search_across_knowledge_bases(
  Line 373:     kb_ids: list[int],
  Line 382:         _resolve_request_knowledge_base(
  Line 384:             kb_id=kb_id,
  Line 392:         for kb_id in kb_ids
  Line 403:                     kb_id=request_context.kb_id,
  Line 417:             metadata.setdefault("knowledge_base_id", request_context.kb_id)
  Line 418:             metadata.setdefault("knowledge_base_name", request_context.kb_name)
  Line 419:             metadata.setdefault("knowledge_base_scope", request_context.kb_scope)
  Line 442:                 f"知识库 {item.metadata.get('knowledge_base_name', '未知')} · 文档 {index + 1} (相似度: {item.score:.3f}):\n{item.content}"
  Line 459:         f"知识库 {item.metadata.get('knowledge_base_name', '未知')} / 文档 {index + 1} ({item.filename or item.source}):\n{item.content}"
  Line 689:         _, request_context = _resolve_request_knowledge_base(
  Line 691:             kb_id=doc.kb_id,
  Line 708:                     kb_id=request_context.kb_id,
  Line 725:     kb_id: Optional[int] = Form(None),
  Line 735:     _, request_context = _resolve_request_knowledge_base(
  Line 737:         kb_id=kb_id,
  Line 781:         collections = [item.collection_name for item in context.knowledge_bases.list_accessible(user_id=user_id, agent_id=agent_id)]
  Line 785: @app.get("/knowledge-bases", tags=["知识库"], summary="列出知识库")
  Line 786: async def list_knowledge_bases(
  Line 792:     """List accessible knowledge bases."""
  Line 794:     tenant = normalize_tenant(base_collection="knowledge_bases", user_id=user_id, agent_id=agent_id)
  Line 798:         base_collection="knowledge_bases",
  Line 802:         operation="list_knowledge_bases",
  Line 803:         subject=request_subject(request, tenant, fallback="knowledge_bases"),
  Line 806:     async with context.observability.timer("list_knowledge_bases"):
  Line 808:         items = context.knowledge_bases.list_accessible(user_id=user_id, agent_id=agent_id)

(Results truncated: showing 100 of 271 matches (171 hidden). Consider using a more specific path or pattern.)
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 22.5s)

知识库生成后的使用方法和使用场景如下：

## 使用方法

### 1. HTTP API 接口
- **检索**：`GET /search?query=xxx&kb_id=1`（单知识库）或 `kb_ids=1,2`（多知识库聚合）
- **问答**：`POST /chat` 传入 `{"query": "xxx", "kb_id": 1}`
- **管理**：
  - `GET /knowledge-bases` 列出所有可访问的知识库
  - `GET /list-documents?kb_id=1` 查看知识库中文档
  - `DELETE /delete-document` 删除文档

### 2. MCP 协议调用
- **工具调用**：通过 `rag_ask` 工具，参数包含 `kb_id`
- **示例**：
```json
{
  "name": "rag_ask",
  "arguments": {
    "query": "FastAPI 是什么",
    "kb_id": 1,
    "mode": "summary"
  }
}
```

### 3. Web 管理界面
- 访问 `http://localhost:8060/app` 进行可视化操作
- 支持文档上传、知识库管理、配置修改等

## 使用流程

### 请求解析阶段
1. **参数接收**：通过 `kb_id` 或 `kb_ids` 指定目标知识库
2. **上下文解析**：`_resolve_request_knowledge_base()` 函数解析知识库信息
3. **权限验证**：检查租户（user_id/agent_id）是否有访问权限

### 执行阶段
1. **检索服务**：`RetrievalService.search()` 执行向量+关键词混合检索
2. **结果聚合**：多知识库场景下合并结果并按相似度排序
3. **LLM 增强**（可选）：启用 `enable_llm_summary` 时生成摘要回答

### 结果返回
- **元数据增强**：每个检索结果包含 `knowledge_base_id`、`knowledge_base_name`、`knowledge_base_scope` 等元数据
- **上下文格式化**：聊天场景下自动格式化为"知识库X / 文档Y"的上下文

## 核心特性

### 多知识库支持
- **单库查询**：指定 `kb_id` 查询特定知识库
- **多库聚合**：通过 `kb_ids` 参数跨多个知识库检索，结果统一排序

### 租户隔离
- **public**：公开知识库，所有用户可访问
- **agent_private**：私有知识库，基于 `user_id + agent_id` 隔离

### 缓存优化
- **请求级缓存**：相同查询在 TTL 内直接返回缓存结果
- **自动失效**：知识库内容变更后自动清理相关缓存



---

## User

summary生成流程是?

---

## Assistant (Build · qwen3-max-2026-01-23 · 9.4s)

**Tool: grep**

**Input:**
```json
{
  "pattern": "enable_llm_summary|summarize|summary"
}
```

**Output:**
```
Found 168 matches (showing first 100)
D:\xfwork\mcprag\mcp-rag\tests\test_service_facade.py:
  Line 42:     enable_llm_summary: bool = True
  Line 268:         self.summarize_calls = []
  Line 274:     async def summarize(self, content: str, query: str) -> str:
  Line 275:         self.summarize_calls.append((content, query))
  Line 276:         return f"summary for {query}"
  Line 347:         self.assertEqual(search.summary, "summary for fastapi")

D:\xfwork\mcprag\mcp-rag\tests\test_observability.py:
  Line 20:     def test_timer_snapshot_and_health_summary(self) -> None:
  Line 49:         health = collector.health_summary()
  Line 80:         health = collector.health_summary()

D:\xfwork\mcprag\mcp-rag\tests\test_mcp_server.py:
  Line 14:     async def test_rag_ask_formats_results_and_summary(self):
  Line 29:                 summary="summary text",
  Line 41:                     "mode": "summary",
  Line 51:             self.assertIn("summary text", text)

D:\xfwork\mcprag\mcp-rag\tests\test_http_server.py:
  Line 40:         fake_llm.summarize = AsyncMock(return_value="mock multi summary")
  Line 42:         fake_runtime.settings = type("FakeSettings", (), {"enable_llm_summary": True})()
  Line 78:                 summary="summary text",
  Line 94:                 summary="summary text",
  Line 200:             self.assertEqual(search.json()["summary"], "mock multi summary")
  Line 404:                     summary_enabled=False,

D:\xfwork\mcprag\mcp-rag\tests\services\test_service_layers.py:
  Line 39:     enable_llm_summary: bool = True
  Line 281:     def __init__(self, *, fail_summarize: bool = False, fail_generate: bool = False):
  Line 282:         self.fail_summarize = fail_summarize
  Line 285:         self.summarize_calls = []
  Line 293:     async def summarize(self, content: str, query: str) -> str:
  Line 294:         self.summarize_calls.append((content, query))
  Line 295:         if self.fail_summarize:
  Line 296:             raise RuntimeError("summarize failed")
  Line 297:         return f"summary for {query}"
  Line 467:         self.settings = _FakeSettings(enable_llm_summary=True, enable_cache=True)
  Line 496:         self.assertEqual(search.summary, "summary for fastapi")
  Line 508:         self.assertEqual(cached.summary, "summary for fastapi")
  Line 510:         self.assertEqual(len(self.llm.summarize_calls), 1)
  Line 582:     async def test_ask_falls_back_when_summary_generation_fails(self):
  Line 584:             settings_obj=_FakeSettings(enable_llm_summary=False, enable_cache=True),
  Line 589:             llm_model=_FakeLLM(fail_summarize=True),
  Line 597:                 mode="summary",
  Line 602:         self.assertEqual(response.summary, "摘要生成功能暂未启用。")
  Line 604:     async def test_summary_mode_fallback_is_cached(self):
  Line 607:             settings_obj=_FakeSettings(enable_llm_summary=False, enable_cache=True),
  Line 618:             mode="summary",
  Line 625:         self.assertEqual(first.summary, "summary for fastapi")
  Line 626:         self.assertEqual(second.summary, "summary for fastapi")
  Line 628:         self.assertEqual(len(llm.summarize_calls), 1)
  Line 641:         self.assertEqual(first.summary, second.summary)
  Line 649:         self.assertEqual(third.summary, "summary for fastapi")

D:\xfwork\mcprag\mcp-rag\tests\services\test_retrieval_cache.py:
  Line 16:         "mode": "summary",
  Line 19:         "summary_enabled": True,
  Line 27: def _build_response(summary: str = "summary text") -> SearchResponse:
  Line 41:         summary=summary,

D:\xfwork\mcprag\mcp-rag\tests\services\test_provider_budget.py:
  Line 18:     async def summarize(self, content: str, query: str) -> str:
  Line 19:         return f"{self.label}:summarize"

D:\xfwork\mcprag\mcp-rag\tests\e2e\test_shell_integration.py:
  Line 49:     async def summarize(self, content: str, query: str) -> str:
  Line 50:         return f"summary for {query}"
  Line 63:                 "enable_llm_summary": True,
  Line 126:         self.assertEqual(search_payload["summary"], "summary for FastAPI")
  Line 152:             {"query": "FastAPI", "collection": "docs", "mode": "summary", "api_key": "secret"}
  Line 156:         self.assertIn("summary for FastAPI", mcp_result[0].text)
  Line 248:                             "mode": "summary",
  Line 255:             self.assertIn("summary for FastAPI", call_response.json()["result"]["content"][0]["text"])

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\static\app\assets\index-DQAj2c0D.js:
  Line 425:  */const n=[["path",{d:"M10 11v6"}],["path",{d:"M14 11v6"}],["path",{d:"M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"}],["path",{d:"M3 6h18"}],["path",{d:"M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"}]];ya(e,wa({name:"trash-2"},()=>i,{get iconNode(){return n},children:(o,c)=>{var f=Yt(),_=Ce(f);ar(_,r,"default",{}),k(o,f)},$$slots:{default:!0}}))}const Rv="".trim(),oo=Rv.replace(/\/+$/,"");function Sn(e={}){return!e||typeof e!="object"||Array.isArray(e)||e.kb_id!==void 0&&e.kb_id!==null||e.kbId===void 0||e.kbId===null?e:{...e,kb_id:e.kbId}}class zv extends Error{constructor(r,i,n){super(i),this.name="ApiError",this.status=r,this.payload=n}}function jv(e,r={}){const i=oo?`${oo}${e}`:e,n=new URL(i,window.location.origin);for(const[o,c]of Object.entries(r))if(!(c==null||c==="")){if(Array.isArray(c)){if(!c.length)continue;n.searchParams.set(o,c.join(","));continue}n.searchParams.set(o,String(c))}return n.toString()}function mt(e={}){const r={},i=e.apiKey||e.api_key;return i&&(r["x-api-key"]=i),r}async function bt(e,{method:r="GET",query:i={},body:n,formData:o,headers:c={}}={}){const f={...c},_={method:r,headers:f};o?_.body=o:n!==void 0&&(_.body=JSON.stringify(n),f["Content-Type"]||(f["Content-Type"]="application/json"));const b=await fetch(jv(e,i),_),h=await b.text();let y=null;if(h)try{y=JSON.parse(h)}catch{y=h}if(!b.ok){const M=typeof y=="object"&&y?y.detail||y.message||b.statusText:h||b.statusText;throw new zv(b.status,M,y)}return y}function vi(e={}){const r={};return e.userId&&(r.user_id=e.userId),e.agentId&&(r.agent_id=e.agentId),e.kbId&&(r.kb_id=e.kbId),e.scope&&(r.scope=e.scope),(e.apiKey||e.api_key)&&(r.api_key=e.apiKey||e.api_key),r}const at={health:(e={})=>bt("/health",{headers:mt(e)}),ready:(e={})=>bt("/ready",{headers:mt(e)}),metrics:(e={})=>bt("/metrics",{headers:mt(e)}),config:(e={})=>bt("/config",{query:vi(e),headers:mt(e)}),updateConfig:(e,r={})=>bt("/config/bulk",{method:"POST",body:{updates:e},headers:mt(r)}),resetConfig:(e={})=>bt("/config/reset",{method:"POST...
  Line 426: `).map(s=>s.trim()).filter(Boolean)}function Be(a){const s=Number(a||0);if(!Number.isFinite(s)||s<=0)return"0 B";const u=["B","KB","MB","GB"];let g=s,w=0;for(;g>=1024&&w<u.length-1;)g/=1024,w+=1;return`${g.toFixed(g>=10?0:1)} ${u[w]}`}function De(a){if(!a)return"未采样";const s=new Date(a*1e3||a);return Number.isNaN(s.getTime())?"未采样":s.toLocaleString()}function U(a){return a==null||Number.isNaN(Number(a))?"0%":`${(Number(a)*100).toFixed(1)}%`}function pe(a,s=180){const u=String(a??"");return u.length>s?`${u.slice(0,s)}...`:u}function $e(a){const s=String(a).toLowerCase();return["ready","healthy","configured","enabled","ok","success"].includes(s)?"good":["warn","warning","degraded","partial","limited"].includes(s)?"warn":["error","failed","misconfigured","unhealthy","cooldown"].includes(s)?"bad":"info"}function Se(a,s="未知"){return a==null||a===""?s:String(a)}function Re(a){return`${Number(a||0).toFixed(3)} / 1.000`}function Pe(a){const s=String(a||"").trim().toLowerCase();return h[s]||s}function qe(a={}){const s={};for(const[u,g]of Object.entries(a||{}))s[Pe(u)]=g;return s}function $t(a){if(!a)return a;const s=qe(a.provider_configs||{});return{...a,embedding_provider:Pe(a.embedding_provider),embedding_fallback_provider:Pe(a.embedding_fallback_provider),llm_provider:Pe(a.llm_provider),llm_fallback_provider:Pe(a.llm_fallback_provider),provider_configs:s}}function Xe(a){const u={...$t(a)||{}};for(const g of y)delete u[g];return u}function fe(a){const s=Array.isArray(a==null?void 0:a.results)?a.results.filter(u=>!(u!=null&&u.processed)):[];return s.length?s.slice(0,3).map(u=>`${Se(u.filename,"unknown")}: ${Se(u.error,"上传失败")}`).join("；"):""}function Te(a){const s=Pe(a);return _.find(u=>u.id===s)||null}function Kr(a){return _.filter(s=>s.families.includes(a))}function Rr(a){return Kr(a).map(s=>({value:s.id,label:s.title}))}function ei(a){return a==="chat"?"llm_model":"embedding_model"}function Rt(a,s,u=""){var Y,K;const g=Pe(a),w=qe(q({},t(v).provider_configs_text));let S=(...
  Line 427: `):"",tenant_api_keys_text:JSON.stringify(((S=a.security)==null?void 0:S.tenant_api_keys)??{},null,2)},s.rate_limit={...s.rate_limit,...a.rate_limit||{}},s.quotas={...s.quotas,...a.quotas||{}},s.observability={...s.observability,...a.observability||{}},s.provider_budget={...s.provider_budget,...a.provider_budget||{},embeddings:{...s.provider_budget.embeddings,...((ge=a.provider_budget)==null?void 0:ge.embeddings)||{}},llm:{...s.provider_budget.llm,...((Y=a.provider_budget)==null?void 0:Y.llm)||{}}},s.provider_configs_text=JSON.stringify(a.provider_configs??{},null,2);const u=((K=a.provider_configs)==null?void 0:K[s.embedding_provider])??{};s.embedding_base_url=u.base_url??"",s.embedding_model=u.embedding_model??"",s.embedding_api_key=u.api_key??"";const g=((V=a.provider_configs)==null?void 0:V[s.llm_provider])??{};s.llm_model=g.llm_model??"",s.llm_base_url=a.llm_base_url??g.base_url??s.llm_base_url,s.llm_api_key=a.llm_api_key??g.api_key??s.llm_api_key,s.full_config_text=JSON.stringify(Xe(a),null,2),p(v,s),Id()}function rl(){const a=qe(q({},t(v).provider_configs_text)),s=Pe(t(v).llm_provider),u=Pe(t(v).embedding_provider),g=a[s]||{},w=a[u]||{},S={...a};return u&&(S[u]={...S[u]||{},...w,embedding_model:t(v).embedding_model||w.embedding_model||"",model:""}),s&&(S[s]={...S[s]||{},...g,llm_model:t(v).llm_model||g.llm_model||"",model:"",base_url:g.base_url??t(v).llm_base_url,api_key:g.api_key??t(v).llm_api_key??null}),{host:t(v).host,port:Number(t(v).port),http_port:Number(t(v).http_port),debug:!!t(v).debug,vector_db_type:t(v).vector_db_type,chroma_persist_directory:t(v).chroma_persist_directory,knowledge_base_db_path:t(v).knowledge_base_db_path,qdrant_url:t(v).qdrant_url,embedding_provider:u,embedding_fallback_provider:Pe(t(v).embedding_fallback_provider)||null,embedding_device:t(v).embedding_device,embedding_cache_dir:t(v).embedding_cache_dir||null,llm_provider:s,llm_fallback_provider:Pe(t(v).llm_fallback_provider)||null,llm_model:t(v).llm_model||g.llm_model||"",llm_bas...
  Line 431: `),S=g[0];p(Wr,{...S,id:`${Nr}`,content:w||S.content||"该文件暂无可预览内容。",metadata:{...S.metadata,filename:Nr}})}async function ec({silent:a=!1,refresh:s=!0}={}){try{let u=rl();if(t(Pr)==="advanced"&&(u=q(null,t(v).full_config_text),!u||typeof u!="object"||Array.isArray(u)))throw new Error("高级配置必须是 JSON 对象");await at.updateConfig(u,t(B)),a||me("配置已保存","后台已重新加载运行时。","success"),s&&await hn()}catch(u){throw a||me("保存失败",u.message,"error"),u}finally{}}async function Mi(){if(t(Ee)==="config"&&(Xn=!0,!es)){es=!0;try{for(;Xn;){Xn=!1;try{await ec({silent:!0,refresh:!1})}catch(a){me("自动保存失败",a.message,"error")}}}finally{es=!1}}}function tc(a){const s=a.target;(s instanceof HTMLInputElement||s instanceof HTMLTextAreaElement)&&(s.type==="checkbox"||s.type==="radio"||Mi())}function rc(a){const s=a.target;s instanceof HTMLInputElement&&(s.type!=="checkbox"&&s.type!=="radio"||Mi())}function yl(a){return s=>{a(s),Mi()}}function ic(){return`${t(gt).length} 个知识库`}function kl(){var a;return!!((a=t(jr))!=null&&a.ready)}function xl(){var a,s;return!!(((a=t(br))==null?void 0:a.healthy)??((s=t(br))==null?void 0:s.ready))}function ac(){var g,w,S;const a=((g=t(Ut))==null?void 0:g.total_requests)??0,s=((w=t(Ut))==null?void 0:w.error_count)??((S=t(Ut))==null?void 0:S.errors)??0,u=a?s/a:0;return`${a} 次请求，错误率 ${U(u)}`}function Ba(){return t(Ee)==="workspace"?(async()=>{await Ii({silent:!0}),(t(Ue)==="detail"||t(Ue)==="detail-preview")&&(await ta(),t(Ue)==="detail-preview"&&Nr&&await wl({silent:!0}))})():t(Ee)==="overview"?hn():t(Ee)==="documents"?dl():t(Ee)==="mcp"?ol({silent:!0}):ll()}function nc(){var s;const a=((s=t(Ut))==null?void 0:s.operations)||{};return Object.entries(a).map(([u,g])=>({name:u,stats:g})).sort((u,g)=>g.stats.count-u.stats.count)}function sc(){var s;const a=((s=t(Ut))==null?void 0:s.providers)||{};return Object.entries(a).map(([u,g])=>({name:u,stats:g})).sort((u,g)=>g.stats.count-u.stats.count)}function lc(){var s,u;const a=((s=t(jr))==null?void 0:s.runtime)||((u=t(br))==null?v...

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\static\app\assets\index-BuextOge.css:
  Line 1: @import"https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap";:root{--bg: #f8f3ea;--bg-deep: #f0e6d8;--surface: rgba(255, 252, 246, .9);--surface-strong: #fffdf9;--surface-soft: rgba(43, 124, 114, .08);--text: #17303b;--muted: #6f8086;--border: rgba(23, 48, 59, .12);--shadow: 0 22px 48px rgba(156, 133, 96, .16);--primary: #2b7c72;--primary-strong: #205e57;--accent: #d69a2d;--danger: #cc4b37;--success: #1f8a56;--warning: #b36b16;--info: #2c6fcf;--radius-xl: 24px;--radius-lg: 18px;--radius-md: 14px;--radius-sm: 10px}html,body{margin:0;min-height:100%;color:var(--text);background:#fcfcfd;font-family:IBM Plex Sans,Segoe UI,sans-serif}body:before{content:none}*{box-sizing:border-box}button,input,textarea,select{font:inherit}button{cursor:pointer}input,textarea,select{width:100%;border:1px solid var(--border);border-radius:14px;background:#ffffffe6;color:var(--text);padding:.8rem .95rem;outline:none;transition:border-color .18s ease,box-shadow .18s ease,transform .18s ease}input:focus,textarea:focus,select:focus{border-color:#0f766e73;box-shadow:0 0 0 4px #0f766e1a}textarea{min-height:160px;resize:vertical}.code-block{margin:0;padding:1rem;min-height:220px;overflow:auto;white-space:pre-wrap;word-break:break-word;border-radius:16px;border:1px solid rgba(23,48,59,.1);background:#13232df0;color:#f5f0e6;font-family:IBM Plex Mono,monospace;font-size:.9rem;line-height:1.55}a{color:inherit;text-decoration:none}.app-shell{position:relative;z-index:1;display:grid;grid-template-columns:252px minmax(0,1fr);min-height:100vh}.sidebar{position:sticky;top:0;height:100vh;padding:14px 12px;background:#fbfbfc;color:var(--text);border-right:1px solid var(--border);display:flex;flex-direction:column;gap:14px;box-shadow:none}.brand{display:flex;gap:10px;align-items:center;padding:6px 6px 10px}.brand-mark{width:32px;height:32px;border-radius:10px;display:grid;place-items:center;f...

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\retrieval_service.py:
  Line 18:     """Hybrid retrieval and summary generation."""
  Line 80:         summary: str | None = None
  Line 81:         if hits and self.runtime.settings.enable_llm_summary:
  Line 84:                 summary = await llm_model.summarize(self._build_summary_context(hits), request.query)
  Line 86:                 logger.warning("LLM summary failed, falling back to raw results: %s", exc)
  Line 92:             summary=summary,
  Line 110:         if request.mode == "summary" and response.summary is None:
  Line 113:                 response.summary = await llm_model.summarize(
  Line 114:                     self._build_summary_context_from_views(response.results),
  Line 119:                 response.summary = "摘要生成功能暂未启用。"
  Line 159:             summary_enabled=bool(getattr(self.runtime.settings, "enable_llm_summary", False)),
  Line 164:     def _build_summary_context(self, hits) -> str:
  Line 170:     def _build_summary_context_from_views(self, results: List[SearchResultView]) -> str:

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\runtime.py:
  Line 118:     async def summarize(self, content: str, query: str) -> str:
  Line 119:         return await self._runtime._invoke_llm("summarize", self._model.summarize, content, query)
  Line 564:             bool(getattr(self.settings, "enable_llm_summary", False)),
  Line 882:         if not bool(getattr(self.settings, "enable_llm_summary", False)):

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\retrieval_cache.py:
  Line 53:         summary=response.summary,
  Line 69:     summary_enabled: bool

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\mcp_server.py:
  Line 61:                                 "enum": ["raw", "summary"],
  Line 154:                         "mode": {"type": "string", "enum": ["raw", "summary"], "default": "raw"},
  Line 268:                 if mode == "summary":
  Line 280:             if mode == "summary":
  Line 282:                 lines.append(response.summary or "摘要生成功能暂未启用。")

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\llm.py:
  Line 30:     async def summarize(self, content: str, query: str) -> str:
  Line 61:     async def summarize(self, content: str, query: str) -> str:
  Line 147:     async def summarize(self, content: str, query: str) -> str:
  Line 219:     async def summarize(self, content: str, query: str) -> str:

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\observability.py:
  Line 1: """Lightweight request metrics and health summary helpers."""
  Line 124:     """Simple health summary suitable for a `/health` handler."""
  Line 307:     def health_summary(self) -> HealthSummary:
  Line 348:         health = self.health_summary()

D:\xfwork\mcprag\mcp-rag\src\mcp_rag\http_server.py:
  Line 48:     "enable_llm_summary",
  Line 437:     summary = None
  Line 438:     if merged_results and getattr(service.runtime.settings, "enable_llm_summary", False):
  Line 441:             summary_context = "\n\n".join(

(Results truncated: showing 100 of 168 matches (68 hidden). Consider using a more specific path or pattern.)
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 14.9s)

summary生成流程如下：

## 触发条件
1. **配置启用**：`enable_llm_summary: true`（默认false）
2. **请求模式**：MCP的 `rag_ask` 工具设置 `mode: "summary"`，或HTTP接口启用摘要功能

## 生成流程

### 1. 检索阶段
- 执行向量+关键词混合检索获取原始结果
- 如果配置了 `enable_llm_summary`，立即调用LLM生成摘要：
  ```python
  summary = await llm_model.summarize(self._build_summary_context(hits), request.query)
  ```

### 2. 上下文构建
- **单知识库**：格式化为"知识库X · 文档Y (相似度: Z):\n内容"
- **多知识库**：包含知识库名称、文档序号和相似度信息

### 3. LLM调用
- 调用对应provider的 `summarize()` 方法
- 支持的provider包括：doubao（默认）、zhipu、aliyun、ollama等
- 包含熔断和fallback机制

### 4. 结果处理
- **成功**：返回摘要文本作为 `response.summary`
- **失败**：记录警告日志，回退到原始检索结果
- **未启用**：返回"摘要生成功能暂未启用。"

## 缓存机制
- 摘要结果会缓存到 `retrieval_cache` 中
- 相同查询在TTL内直接返回缓存的摘要
- 知识库内容变更后自动失效相关缓存

## 使用方式
- **HTTP API**：`GET /search?query=xxx&kb_id=1`（需配置启用）
- **MCP工具**：`rag_ask` 参数包含 `"mode": "summary"`
- **Web界面**：问答界面自动根据配置决定是否显示摘要



---

## User

检索时如何知道 kb_id信息，比如用户上传了法律，教育，旅游三个方面的知识库内容，现在要检索 南京有哪些 好玩的地方，如何指定kb_id

---

## Assistant (Build · qwen3-max-2026-01-23 · 5.1s)

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag\\src\\mcp_rag\\knowledge_bases.py"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag\src\mcp_rag\knowledge_bases.py</path>
<type>file</type>
<content>1: """Persistent knowledge base registry and request resolution helpers."""
2: 
3: from __future__ import annotations
4: 
5: import sqlite3
6: from contextlib import closing
7: from dataclasses import asdict, dataclass
8: from datetime import datetime, timezone
9: from pathlib import Path
10: from threading import RLock
11: from typing import Any
12: from uuid import uuid4
13: 
14: _ACTIVE_STATUS = "active"
15: _PUBLIC_SCOPE = "public"
16: _AGENT_PRIVATE_SCOPE = "agent_private"
17: 
18: 
19: def _utc_now() -> str:
20:     return datetime.now(timezone.utc).isoformat()
21: 
22: 
23: def _normalize_text(value: Any, default: str | None = None) -> str | None:
24:     if value is None:
25:         return default
26:     text = str(value).strip()
27:     return text or default
28: 
29: 
30: def _normalize_int(value: Any) -> int | None:
31:     if value is None or value == "":
32:         return None
33:     if isinstance(value, bool):
34:         return int(value)
35:     try:
36:         return int(str(value).strip())
37:     except (TypeError, ValueError):
38:         return None
39: 
40: 
41: @dataclass(slots=True, frozen=True)
42: class KnowledgeBase:
43:     """Business-facing knowledge base entity."""
44: 
45:     id: int
46:     name: str
47:     scope: str
48:     owner_user_id: int | None
49:     owner_agent_id: int | None
50:     collection_name: str
51:     legacy_collection_key: str | None
52:     status: str
53:     created_at: str
54:     updated_at: str
55: 
56:     def to_dict(self) -> dict[str, Any]:
57:         return asdict(self)
58: 
59:     @property
60:     def is_public(self) -> bool:
61:         return self.scope == _PUBLIC_SCOPE
62: 
63: 
64: @dataclass(slots=True, frozen=True)
65: class KnowledgeBaseResolution:
66:     """Resolved knowledge base information for one request."""
67: 
68:     knowledge_base: KnowledgeBase
69:     selected_via: str
70: 
71:     @property
72:     def kb_id(self) -> int:
73:         return self.knowledge_base.id
74: 
75:     @property
76:     def collection_name(self) -> str:
77:         return self.knowledge_base.collection_name
78: 
79:     @property
80:     def scope(self) -> str:
81:         return self.knowledge_base.scope
82: 
83:     @property
84:     def name(self) -> str:
85:         return self.knowledge_base.name
86: 
87: 
88: class KnowledgeBaseAccessError(RuntimeError):
89:     """Raised when a caller cannot access a knowledge base."""
90: 
91: 
92: class KnowledgeBaseStore:
93:     """SQLite-backed knowledge base registry."""
94: 
95:     def __init__(self, db_path: str):
96:         self.db_path = Path(db_path)
97:         self.db_path.parent.mkdir(parents=True, exist_ok=True)
98:         self._lock = RLock()
99:         self._initialize()
100: 
101:     def _connect(self) -> sqlite3.Connection:
102:         connection = sqlite3.connect(self.db_path)
103:         connection.row_factory = sqlite3.Row
104:         return connection
105: 
106:     def _initialize(self) -> None:
107:         with self._lock, closing(self._connect()) as connection:
108:             connection.executescript(
109:                 """
110:                 CREATE TABLE IF NOT EXISTS knowledge_bases (
111:                     id INTEGER PRIMARY KEY AUTOINCREMENT,
112:                     name TEXT NOT NULL,
113:                     scope TEXT NOT NULL,
114:                     owner_user_id INTEGER,
115:                     owner_agent_id INTEGER,
116:                     collection_name TEXT NOT NULL UNIQUE,
117:                     legacy_collection_key TEXT,
118:                     status TEXT NOT NULL DEFAULT 'active',
119:                     created_at TEXT NOT NULL,
120:                     updated_at TEXT NOT NULL
121:                 );
122:                 CREATE UNIQUE INDEX IF NOT EXISTS idx_knowledge_bases_legacy
123:                     ON knowledge_bases(legacy_collection_key)
124:                     WHERE legacy_collection_key IS NOT NULL;
125:                 CREATE INDEX IF NOT EXISTS idx_knowledge_bases_access
126:                     ON knowledge_bases(scope, owner_user_id, owner_agent_id, status);
127:                 """
128:             )
129: 
130:     def _row_to_model(self, row: sqlite3.Row | None) -> KnowledgeBase | None:
131:         if row is None:
132:             return None
133:         return KnowledgeBase(
134:             id=int(row["id"]),
135:             name=str(row["name"]),
136:             scope=str(row["scope"]),
137:             owner_user_id=_normalize_int(row["owner_user_id"]),
138:             owner_agent_id=_normalize_int(row["owner_agent_id"]),
139:             collection_name=str(row["collection_name"]),
140:             legacy_collection_key=_normalize_text(row["legacy_collection_key"]),
141:             status=str(row["status"]),
142:             created_at=str(row["created_at"]),
143:             updated_at=str(row["updated_at"]),
144:         )
145: 
146:     def get(self, kb_id: int) -> KnowledgeBase | None:
147:         with self._lock, closing(self._connect()) as connection:
148:             row = connection.execute(
149:                 "SELECT * FROM knowledge_bases WHERE id = ? LIMIT 1",
150:                 (int(kb_id),),
151:             ).fetchone()
152:         return self._row_to_model(row)
153: 
154:     def get_by_legacy_key(self, legacy_collection_key: str | None) -> KnowledgeBase | None:
155:         key = _normalize_text(legacy_collection_key)
156:         if key is None:
157:             return None
158:         with self._lock, closing(self._connect()) as connection:
159:             row = connection.execute(
160:                 "SELECT * FROM knowledge_bases WHERE legacy_collection_key = ? LIMIT 1",
161:                 (key,),
162:             ).fetchone()
163:         return self._row_to_model(row)
164: 
165:     def get_public_default(self) -> KnowledgeBase | None:
166:         with self._lock, closing(self._connect()) as connection:
167:             row = connection.execute(
168:                 """
169:                 SELECT * FROM knowledge_bases
170:                 WHERE scope = ? AND owner_user_id IS NULL AND owner_agent_id IS NULL AND status = ?
171:                 ORDER BY id ASC
172:                 LIMIT 1
173:                 """,
174:                 (_PUBLIC_SCOPE, _ACTIVE_STATUS),
175:             ).fetchone()
176:         return self._row_to_model(row)
177: 
178:     def get_default_agent_private(self, *, user_id: int, agent_id: int) -> KnowledgeBase | None:
179:         with self._lock, closing(self._connect()) as connection:
180:             row = connection.execute(
181:                 """
182:                 SELECT * FROM knowledge_bases
183:                 WHERE scope = ? AND owner_user_id = ? AND owner_agent_id = ? AND status = ?
184:                 ORDER BY id ASC
185:                 LIMIT 1
186:                 """,
187:                 (_AGENT_PRIVATE_SCOPE, int(user_id), int(agent_id), _ACTIVE_STATUS),
188:             ).fetchone()
189:         return self._row_to_model(row)
190: 
191:     def list_accessible(self, *, user_id: int | None = None) -> list[KnowledgeBase]:
192:         with self._lock, closing(self._connect()) as connection:
193:             rows = connection.execute(
194:                 """
195:                 SELECT * FROM knowledge_bases
196:                 WHERE status = ?
197:                   AND (
198:                     scope = ?
199:                     OR (? IS NOT NULL AND owner_user_id = ?)
200:                   )
201:                 ORDER BY CASE WHEN scope = ? THEN 0 ELSE 1 END, name COLLATE NOCASE ASC, id ASC
202:                 """,
203:                 (_ACTIVE_STATUS, _PUBLIC_SCOPE, user_id, user_id, _PUBLIC_SCOPE),
204:             ).fetchall()
205:         return [item for row in rows if (item := self._row_to_model(row)) is not None]
206: 
207:     def create(
208:         self,
209:         *,
210:         name: str,
211:         scope: str,
212:         owner_user_id: int | None = None,
213:         owner_agent_id: int | None = None,
214:         legacy_collection_key: str | None = None,
215:     ) -> KnowledgeBase:
216:         resolved_name = _normalize_text(name, default="Knowledge Base") or "Knowledge Base"
217:         resolved_scope = _normalize_text(scope, default=_PUBLIC_SCOPE) or _PUBLIC_SCOPE
218:         now = _utc_now()
219:         temporary_collection = f"pending_{uuid4().hex}"
220:         with self._lock, closing(self._connect()) as connection:
221:             cursor = connection.execute(
222:                 """
223:                 INSERT INTO knowledge_bases(
224:                     name,
225:                     scope,
226:                     owner_user_id,
227:                     owner_agent_id,
228:                     collection_name,
229:                     legacy_collection_key,
230:                     status,
231:                     created_at,
232:                     updated_at
233:                 )
234:                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
235:                 """,
236:                 (
237:                     resolved_name,
238:                     resolved_scope,
239:                     _normalize_int(owner_user_id),
240:                     _normalize_int(owner_agent_id),
241:                     temporary_collection,
242:                     _normalize_text(legacy_collection_key),
243:                     _ACTIVE_STATUS,
244:                     now,
245:                     now,
246:                 ),
247:             )
248:             kb_id = int(cursor.lastrowid)
249:             collection_name = f"kb_{kb_id}"
250:             connection.execute(
251:                 "UPDATE knowledge_bases SET collection_name = ?, updated_at = ? WHERE id = ?",
252:                 (collection_name, now, kb_id),
253:             )
254:             connection.commit()
255:         created = self.get(kb_id)
256:         if created is None:
257:             raise RuntimeError(f"Knowledge base {kb_id} was not persisted")
258:         return created
259: 
260: 
261: class KnowledgeBaseService:
262:     """Higher-level knowledge base resolution with default creation."""
263: 
264:     def __init__(self, db_path: str):
265:         self.store = KnowledgeBaseStore(db_path)
266: 
267:     def ensure_public_default(self) -> KnowledgeBase:
268:         existing = self.store.get_public_default()
269:         if existing is not None:
270:             return existing
271:         return self.store.create(
272:             name="公共知识库",
273:             scope=_PUBLIC_SCOPE,
274:             legacy_collection_key="legacy:public:default",
275:         )
276: 
277:     def ensure_agent_private_default(self, *, user_id: int, agent_id: int) -> KnowledgeBase:
278:         existing = self.store.get_default_agent_private(user_id=int(user_id), agent_id=int(agent_id))
279:         if existing is not None:
280:             return existing
281:         return self.store.create(
282:             name=f"Agent {int(agent_id)} 知识库",
283:             scope=_AGENT_PRIVATE_SCOPE,
284:             owner_user_id=int(user_id),
285:             owner_agent_id=int(agent_id),
286:             legacy_collection_key=f"legacy:agent_private:{int(user_id)}:{int(agent_id)}:default",
287:         )
288: 
289:     def create_knowledge_base(
290:         self,
291:         *,
292:         name: str,
293:         scope: str,
294:         owner_user_id: int | None = None,
295:         owner_agent_id: int | None = None,
296:         legacy_collection_key: str | None = None,
297:     ) -> KnowledgeBase:
298:         resolved_scope = self.normalize_scope(scope, user_id=owner_user_id, agent_id=owner_agent_id)
299:         if resolved_scope == _PUBLIC_SCOPE:
300:             owner_user_id = None
301:             owner_agent_id = None
302:         if resolved_scope == _AGENT_PRIVATE_SCOPE:
303:             if owner_user_id is None:
304:                 raise ValueError("agent_private knowledge bases require owner_user_id")
305:         return self.store.create(
306:             name=name,
307:             scope=resolved_scope,
308:             owner_user_id=owner_user_id,
309:             owner_agent_id=owner_agent_id,
310:             legacy_collection_key=legacy_collection_key,
311:         )
312: 
313:     def list_accessible(self, *, user_id: int | None = None, agent_id: int | None = None) -> list[KnowledgeBase]:
314:         items = self.store.list_accessible(user_id=user_id)
315:         self.ensure_public_default()
316:         if user_id is not None and agent_id is not None:
317:             default_private = self.ensure_agent_private_default(user_id=user_id, agent_id=agent_id)
318:             if all(item.id != default_private.id for item in items):
319:                 items.append(default_private)
320:         public_default = self.ensure_public_default()
321:         if all(item.id != public_default.id for item in items):
322:             items.append(public_default)
323:         return sorted(
324:             items,
325:             key=lambda item: (0 if item.scope == _PUBLIC_SCOPE else 1, item.name.lower(), item.id),
326:         )
327: 
328:     def get(self, kb_id: int) -> KnowledgeBase | None:
329:         return self.store.get(int(kb_id))
330: 
331:     def resolve(
332:         self,
333:         *,
334:         kb_id: int | None = None,
335:         scope: str | None = None,
336:         user_id: int | None = None,
337:         agent_id: int | None = None,
338:         legacy_collection: str | None = None,
339:         legacy_collection_key: str | None = None,
340:     ) -> KnowledgeBaseResolution:
341:         resolved_user_id = _normalize_int(user_id)
342:         resolved_agent_id = _normalize_int(agent_id)
343:         resolved_kb_id = _normalize_int(kb_id)
344: 
345:         if resolved_kb_id is not None:
346:             knowledge_base = self.store.get(resolved_kb_id)
347:             if knowledge_base is None:
348:                 raise KnowledgeBaseAccessError(f"knowledge base {resolved_kb_id} not found")
349:             self._ensure_access(knowledge_base, user_id=resolved_user_id)
350:             return KnowledgeBaseResolution(knowledge_base=knowledge_base, selected_via="kb_id")
351: 
352:         legacy_key = _normalize_text(legacy_collection_key)
353:         if legacy_key is not None:
354:             knowledge_base = self.store.get_by_legacy_key(legacy_key)
355:             if knowledge_base is not None:
356:                 self._ensure_access(knowledge_base, user_id=resolved_user_id)
357:                 return KnowledgeBaseResolution(knowledge_base=knowledge_base, selected_via="legacy_key")
358: 
359:         resolved_scope = self.normalize_scope(scope, user_id=resolved_user_id, agent_id=resolved_agent_id)
360:         if resolved_scope == _PUBLIC_SCOPE:
361:             collection_name = _normalize_text(legacy_collection, default="公共知识库")
362:             if collection_name and collection_name not in {"default", "knowledge", "公共知识库"}:
363:                 legacy_key = legacy_key or f"legacy:public:{collection_name}"
364:                 existing = self.store.get_by_legacy_key(legacy_key)
365:                 if existing is not None:
366:                     return KnowledgeBaseResolution(knowledge_base=existing, selected_via="legacy_public")
367:                 created = self.create_knowledge_base(
368:                     name=collection_name,
369:                     scope=_PUBLIC_SCOPE,
370:                     legacy_collection_key=legacy_key,
371:                 )
372:                 return KnowledgeBaseResolution(knowledge_base=created, selected_via="legacy_public")
373:             return KnowledgeBaseResolution(knowledge_base=self.ensure_public_default(), selected_via="scope")
374: 
375:         if resolved_user_id is None or resolved_agent_id is None:
376:             raise KnowledgeBaseAccessError("agent_private knowledge base requires user_id and agent_id")
377: 
378:         if legacy_collection and legacy_collection not in {"default", "knowledge"}:
379:             legacy_key = legacy_key or f"legacy:agent_private:{resolved_user_id}:{resolved_agent_id}:{legacy_collection}"
380:             existing = self.store.get_by_legacy_key(legacy_key)
381:             if existing is not None:
382:                 self._ensure_access(existing, user_id=resolved_user_id)
383:                 return KnowledgeBaseResolution(knowledge_base=existing, selected_via="legacy_private")
384:             created = self.create_knowledge_base(
385:                 name=legacy_collection,
386:                 scope=_AGENT_PRIVATE_SCOPE,
387:                 owner_user_id=resolved_user_id,
388:                 owner_agent_id=resolved_agent_id,
389:                 legacy_collection_key=legacy_key,
390:             )
391:             return KnowledgeBaseResolution(knowledge_base=created, selected_via="legacy_private")
392: 
393:         return KnowledgeBaseResolution(
394:             knowledge_base=self.ensure_agent_private_default(user_id=resolved_user_id, agent_id=resolved_agent_id),
395:             selected_via="scope",
396:         )
397: 
398:     def normalize_scope(self, scope: str | None, *, user_id: int | None, agent_id: int | None) -> str:
399:         resolved_scope = (_normalize_text(scope) or "").lower()
400:         if resolved_scope in {"public", _PUBLIC_SCOPE}:
401:             return _PUBLIC_SCOPE
402:         if resolved_scope in {"agent_private", "private", _AGENT_PRIVATE_SCOPE}:
403:             return _AGENT_PRIVATE_SCOPE
404:         if user_id is not None and agent_id is not None:
405:             return _AGENT_PRIVATE_SCOPE
406:         return _PUBLIC_SCOPE
407: 
408:     def _ensure_access(self, knowledge_base: KnowledgeBase, *, user_id: int | None) -> None:
409:         if knowledge_base.scope == _PUBLIC_SCOPE:
410:             return
411:         if user_id is None or knowledge_base.owner_user_id != int(user_id):
412:             raise KnowledgeBaseAccessError(f"access denied for knowledge base {knowledge_base.id}")

(End of file - total 412 lines)
</content>
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 19.5s)

要指定知识库进行检索，需要先获取 `kb_id` 信息，然后在查询时使用。具体流程如下：

## 获取 kb_id 信息

### 1. 列出所有知识库
通过 `GET /knowledge-bases` 接口获取知识库列表：
```bash
curl http://localhost:8060/knowledge-bases
```

返回示例：
```json
{
  "knowledge_bases": [
    {"id": 1, "name": "法律", "scope": "public"},
    {"id": 2, "name": "教育", "scope": "public"}, 
    {"id": 3, "name": "旅游", "scope": "public"}
  ]
}
```

### 2. Web 界面查看
访问 `http://localhost:8060/app`，在知识库管理页面可以看到每个知识库的 ID 和名称。

## 指定 kb_id 进行检索

### HTTP API 方式
```bash
# 单知识库检索（旅游知识库）
curl "http://localhost:8060/search?query=南京有哪些好玩的地方&kb_id=3"

# 多知识库聚合检索（同时查旅游和教育）
curl "http://localhost:8060/search?query=南京有哪些好玩的地方&kb_ids=3,2"
```

### MCP 工具调用方式
```json
{
  "name": "rag_ask",
  "arguments": {
    "query": "南京有哪些好玩的地方",
    "kb_id": 3,
    "mode": "summary"
  }
}
```

## 自动解析机制

如果不想手动管理 kb_id，系统也支持通过知识库名称自动解析：
- **legacy_collection 参数**：传入知识库名称（如 "旅游"）
- 系统会自动创建或查找对应的 kb_id

```bash
# 通过名称自动解析（系统会创建 kb_id 或复用已存在的）
curl "http://localhost:8060/search?query=南京有哪些好玩的地方&collection=旅游"
```

## 推荐做法

对于您的场景（法律、教育、旅游三个知识库）：
1. **先调用 `/knowledge-bases` 获取 kb_id 映射**
2. **存储 kb_id 供后续使用**（kb_id 是稳定不变的）
3. **检索时明确指定 kb_id=3（旅游知识库）**

这样可以确保精确检索到旅游相关的内容，避免跨知识库的无关结果。



---

## User

在AI聊天中如何指定呢，毕竟玩家只知道输入问题

---

## Assistant (Build · qwen3-max-2026-01-23 · 22.9s)

在AI聊天场景中，有几种方式处理知识库指定问题：

## 1. 自动路由（推荐）
在应用层实现智能路由逻辑：
- **关键词识别**：分析用户问题中的关键词自动选择知识库
  - "南京旅游"/"景点"/"好玩的地方" → 自动路由到旅游知识库(kb_id=3)
  - "法律咨询"/"合同"/"法规" → 路由到法律知识库(kb_id=1)
  - "教育"/"学习"/"考试" → 路由到教育知识库(kb_id=2)

- **实现示例**：
```python
def route_query(query: str) -> int:
    query_lower = query.lower()
    if any(word in query_lower for word in ['旅游', '景点', '好玩', '游玩', '攻略']):
        return 3  # 旅游知识库
    elif any(word in query_lower for word in ['法律', '合同', '律师', '法规', '起诉']):
        return 1  # 法律知识库
    elif any(word in query_lower for word in ['教育', '学习', '考试', '学校', '课程']):
        return 2  # 教育知识库
    else:
        return 0  # 默认查询所有或公共知识库
```

## 2. 多知识库并行检索
直接查询所有相关知识库，让系统自动聚合结果：
```json
{
  "query": "南京有哪些好玩的地方",
  "kb_ids": [1, 2, 3]  // 同时查所有知识库
}
```
系统会返回跨知识库的综合结果，并标注每个结果来自哪个知识库。

## 3. 上下文记忆
在聊天会话中记住用户当前关注的领域：
- 用户首次提问涉及旅游 → 记录当前会话上下文为"旅游"
- 后续问题自动使用 kb_id=3，直到用户切换话题

## 4. 前端界面辅助
如果是Web应用，可以在聊天界面提供知识库选择器：
- 下拉菜单让用户选择"法律/教育/旅游"
- 或者自动显示"检测到您可能想了解旅游信息，是否要专注于旅游知识库？"

## 实际调用示例
对于问题"南京有哪些好玩的地方"，应用层自动调用：
```bash
# HTTP API
POST /chat
{
  "query": "南京有哪些好玩的地方", 
  "kb_id": 3,
  "mode": "summary"
}

# MCP工具  
{
  "name": "rag_ask",
  "arguments": {
    "query": "南京有哪些好玩的地方",
    "kb_id": 3,
    "mode": "summary"
  }
}
```

这样用户只需要自然地提问，系统在后台自动处理知识库路由，提供精准的回答。

---

## User

分析@src\mcp_rag/ 目录下各文件作用，及服务启动工作流程

---

## Assistant (Build · qwen3-max-2026-01-23 · 13.3s)

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag\\src\\mcp_rag\\app_factory.py"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag\src\mcp_rag\app_factory.py</path>
<type>file</type>
<content>1: """Runtime assembly for HTTP, MCP, and CLI entry points."""
2: 
3: from __future__ import annotations
4: 
5: import asyncio
6: import inspect
7: from collections.abc import AsyncIterator, Callable
8: from dataclasses import dataclass, field
9: from typing import Any, Awaitable
10: 
11: from fastapi import FastAPI, HTTPException, Request
12: from fastapi.responses import HTMLResponse
13: from scalar_fastapi import Layout, Theme, get_scalar_api_reference
14: 
15: from .config import ConfigManager, config_manager
16: from .context import RequestContext, TenantSpec, normalize_tenant
17: from .knowledge_bases import KnowledgeBaseService
18: from .observability import ObservabilityCollector
19: from .security import (
20:     AuthenticationError,
21:     AuthorizationError,
22:     RateLimitExceededError,
23:     SecurityPolicy,
24:     TokenBucketRateLimiter,
25: )
26: from .service_facade import RagService
27: from .services import ServiceRuntime
28: 
29: ServiceProvider = Callable[[], Awaitable[Any] | Any]
30: 
31: 
32: @dataclass(slots=True)
33: class AppContext:
34:     """Runtime and transport guardrails shared by HTTP and MCP entry points."""
35: 
36:     settings: Any
37:     runtime: ServiceRuntime
38:     security_policy: SecurityPolicy
39:     rate_limiter: TokenBucketRateLimiter
40:     observability: ObservabilityCollector
41:     knowledge_bases: KnowledgeBaseService
42:     config_manager: ConfigManager | None = None
43:     service_provider: ServiceProvider | None = None
44:     service: Any | None = None
45:     service_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
46:     reload_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
47:     bootstrapped: bool = False
48:     config_revision: int = 0
49: 
50: 
51: ShellContext = AppContext
52: 
53: _default_app_context: AppContext | None = None
54: 
55: 
56: def create_app_context(
57:     *,
58:     settings_obj: Any | None = None,
59:     config_manager_obj: ConfigManager | None = None,
60:     runtime: ServiceRuntime | None = None,
61:     service_provider: ServiceProvider | None = None,
62:     security_policy: SecurityPolicy | None = None,
63:     rate_limiter: TokenBucketRateLimiter | None = None,
64:     observability: ObservabilityCollector | None = None,
65: ) -> AppContext:
66:     """Create an app context without eagerly warming heavy dependencies."""
67: 
68:     manager = config_manager_obj
69:     resolved_settings = settings_obj
70:     if resolved_settings is None:
71:         if manager is None:
72:             manager = config_manager
73:         resolved_settings = manager.ensure_config_file()
74: 
75:     resolved_observability = observability or ObservabilityCollector.from_settings(resolved_settings)
76:     resolved_runtime = runtime or ServiceRuntime(settings_obj=resolved_settings, observability=resolved_observability)
77:     if runtime is not None:
78:         resolved_runtime.observability = resolved_observability
79:     context = AppContext(
80:         settings=resolved_settings,
81:         runtime=resolved_runtime,
82:         security_policy=security_policy or SecurityPolicy.from_settings(resolved_settings),
83:         rate_limiter=rate_limiter or TokenBucketRateLimiter.from_settings(resolved_settings),
84:         observability=resolved_observability,
85:         knowledge_bases=KnowledgeBaseService(getattr(resolved_settings, "knowledge_base_db_path", "./data/knowledge_bases.sqlite3")),
86:         config_manager=manager,
87:         config_revision=manager.revision if manager is not None else 0,
88:     )
89: 
90:     if service_provider is not None:
91:         context.service_provider = service_provider
92:         return context
93: 
94:     async def _default_service_provider() -> RagService:
95:         if context.service is not None:
96:             return context.service
97: 
98:         async with context.service_lock:
99:             if context.service is None:
100:                 context.service = RagService(runtime=context.runtime)
101:             return context.service
102: 
103:     context.service_provider = _default_service_provider
104:     return context
105: 
106: 
107: create_shell_context = create_app_context
108: 
109: 
110: def get_default_app_context() -> AppContext:
111:     """Return the process-wide app context shared by default transports."""
112: 
113:     global _default_app_context
114:     if _default_app_context is None:
115:         _default_app_context = create_app_context(config_manager_obj=config_manager)
116:     return _default_app_context
117: 
118: 
119: get_default_shell_context = get_default_app_context
120: 
121: 
122: async def sync_app_context(context: AppContext, *, force: bool = False) -> bool:
123:     """Rebuild runtime-scoped dependencies when config changes."""
124: 
125:     manager = context.config_manager
126:     if manager is None:
127:         return False
128: 
129:     async with context.reload_lock:
130:         settings_obj = manager.reload() if force else (manager.reload_if_changed() or manager.settings)
131:         if not force and context.config_revision == manager.revision:
132:             return False
133: 
134:         context.settings = settings_obj
135:         context.security_policy = SecurityPolicy.from_settings(settings_obj)
136:         context.rate_limiter = TokenBucketRateLimiter.from_settings(settings_obj)
137:         context.knowledge_bases = KnowledgeBaseService(
138:             getattr(settings_obj, "knowledge_base_db_path", "./data/knowledge_bases.sqlite3")
139:         )
140: 
141:         configure = getattr(context.observability, "configure_from_settings", None)
142:         if callable(configure):
143:             configure(settings_obj)
144:         else:
145:             context.observability = ObservabilityCollector.from_settings(settings_obj)
146: 
147:         reload_runtime = getattr(context.runtime, "reload_settings", None)
148:         if callable(reload_runtime):
149:             await reload_runtime(settings_obj)
150:         else:
151:             old_runtime = context.runtime
152:             context.runtime = ServiceRuntime(settings_obj=settings_obj, observability=context.observability)
153:             context.service = None
154:             if old_runtime is not context.runtime and hasattr(old_runtime, "close"):
155:                 await old_runtime.close()
156: 
157:         context.config_revision = manager.revision
158:         return True
159: 
160: 
161: async def reload_app_context(context: AppContext, *, settings_obj: Any | None = None) -> bool:
162:     """Force a live runtime reload, optionally with an explicit settings object."""
163: 
164:     if settings_obj is None:
165:         return await sync_app_context(context, force=True)
166: 
167:     async with context.reload_lock:
168:         context.settings = settings_obj
169:         context.security_policy = SecurityPolicy.from_settings(settings_obj)
170:         context.rate_limiter = TokenBucketRateLimiter.from_settings(settings_obj)
171:         context.knowledge_bases = KnowledgeBaseService(
172:             getattr(settings_obj, "knowledge_base_db_path", "./data/knowledge_bases.sqlite3")
173:         )
174: 
175:         configure = getattr(context.observability, "configure_from_settings", None)
176:         if callable(configure):
177:             configure(settings_obj)
178:         else:
179:             context.observability = ObservabilityCollector.from_settings(settings_obj)
180: 
181:         reload_runtime = getattr(context.runtime, "reload_settings", None)
182:         if callable(reload_runtime):
183:             await reload_runtime(settings_obj)
184:         else:
185:             old_runtime = context.runtime
186:             context.runtime = ServiceRuntime(settings_obj=settings_obj, observability=context.observability)
187:             context.service = None
188:             if old_runtime is not context.runtime and hasattr(old_runtime, "close"):
189:                 await old_runtime.close()
190: 
191:         if context.config_manager is not None:
192:             context.config_revision = context.config_manager.revision
193:         return True
194: 
195: 
196: async def ensure_app_context_current(target: Request | Any, *, force: bool = False) -> AppContext:
197:     """Refresh the app context for request-driven transports."""
198: 
199:     context = get_app_context(target)
200:     await sync_app_context(context, force=force)
201:     return context
202: 
203: 
204: def create_http_app(
205:     *,
206:     context: AppContext | None = None,
207:     lifespan: Callable[[FastAPI], AsyncIterator[None]] | None = None,
208: ) -> FastAPI:
209:     """Create the default HTTP shell app."""
210: 
211:     openapi_tags = [
212:         {"name": "系统", "description": "服务入口、健康检查与运行指标。"},
213:         {"name": "应用", "description": "前端单页应用与历史兼容页面入口。"},
214:         {"name": "配置", "description": "系统配置读取、更新、重载与重置。"},
215:         {"name": "服务商", "description": "模型服务商与模型列表同步相关接口。"},
216:         {"name": "知识库", "description": "知识库集合查询、创建与权限范围解析。"},
217:         {"name": "文档", "description": "文档与文件的导入、上传、查询、删除。"},
218:         {"name": "对话与检索", "description": "检索、对话与多知识库查询能力。"},
219:         {"name": "MCP 调试", "description": "MCP 工具列表与调试调用。"},
220:     ]
221: 
222:     app = FastAPI(
223:         title="MCP-RAG 接口文档",
224:         description="MCP-RAG 的统一后端接口，涵盖配置管理、知识库、文档导入、检索、对话与 MCP 调试。",
225:         lifespan=lifespan,
226:         docs_url=None,
227:         redoc_url=None,
228:         openapi_tags=openapi_tags,
229:     )
230:     app.state.shell_context = context or get_default_app_context()
231: 
232:     @app.get("/docs", include_in_schema=False)
233:     async def scalar_docs() -> HTMLResponse:
234:         return get_scalar_api_reference(
235:             openapi_url=app.openapi_url or "/openapi.json",
236:             title="MCP-RAG 接口文档",
237:             layout=Layout.MODERN,
238:             theme=Theme.DEFAULT,
239:             show_sidebar=True,
240:             hide_dark_mode_toggle=False,
241:             scalar_proxy_url="https://proxy.scalar.com",
242:             integration="fastapi",
243:         )
244: 
245:     return app
246: 
247: 
248: def get_app_context(target: Request | Any) -> AppContext:
249:     """Fetch or attach an app context from a request-like object."""
250: 
251:     app = getattr(target, "app", None)
252:     if app is None:
253:         raise TypeError("App context target must expose an app attribute")
254: 
255:     context = getattr(app.state, "shell_context", None)
256:     if context is None:
257:         context = get_default_app_context()
258:         app.state.shell_context = context
259:     return context
260: 
261: 
262: get_shell_context = get_app_context
263: 
264: 
265: async def resolve_app_service(target: Request | Any) -> Any:
266:     """Resolve the service instance via the shared app context."""
267: 
268:     context = await ensure_app_context_current(target)
269:     provider = context.service_provider
270:     if provider is None:
271:         raise RuntimeError("App context is missing a service provider")
272: 
273:     service = provider()
274:     if inspect.isawaitable(service):
275:         return await service
276:     return service
277: 
278: 
279: resolve_shell_service = resolve_app_service
280: 
281: 
282: def runtime_snapshot(context: AppContext) -> dict[str, Any]:
283:     """Return runtime readiness signals without initializing heavy providers."""
284: 
285:     runtime = context.runtime
286:     snapshot_fn = getattr(runtime, "readiness_snapshot", None)
287:     if callable(snapshot_fn):
288:         return snapshot_fn()
289:     return {
290:         "document_processor": {"ready": getattr(runtime, "_document_processor", None) is not None, "status": "unknown"},
291:         "embedding_model": {"ready": getattr(runtime, "_embedding_model", None) is not None, "status": "unknown"},
292:         "vector_store": {"ready": getattr(runtime, "_vector_store", None) is not None, "status": "unknown"},
293:         "hybrid_service": {"ready": getattr(runtime, "_hybrid_service", None) is not None, "status": "unknown"},
294:         "llm_model": {"ready": getattr(runtime, "_llm_model", None) is not None, "status": "unknown"},
295:     }
296: 
297: 
298: def runtime_ready(snapshot: dict[str, Any]) -> bool:
299:     """Collapse structured runtime readiness into a single transport-level flag."""
300: 
301:     for name, value in snapshot.items():
302:         if name == "provider_budget":
303:             continue
304:         if isinstance(value, dict) and "ready" in value and not bool(value["ready"]):
305:             return False
306:     return True
307: 
308: 
309: def health_payload(context: AppContext) -> dict[str, Any]:
310:     """Build a lightweight health response."""
311: 
312:     collector_payload = context.observability.as_dict()
313:     health = dict(collector_payload["health"])
314:     snapshot = runtime_snapshot(context)
315:     health["bootstrapped"] = context.bootstrapped
316:     health["ready"] = bool(context.bootstrapped and runtime_ready(snapshot))
317:     health["runtime"] = snapshot
318:     health["config_revision"] = context.config_revision
319:     return health
320: 
321: 
322: def ready_payload(context: AppContext) -> dict[str, Any]:
323:     """Build a readiness response."""
324: 
325:     snapshot = runtime_snapshot(context)
326:     return {
327:         "bootstrapped": context.bootstrapped,
328:         "ready": bool(context.bootstrapped and runtime_ready(snapshot)),
329:         "runtime": snapshot,
330:         "config_revision": context.config_revision,
331:     }
332: 
333: 
334: def metrics_payload(context: AppContext) -> dict[str, Any]:
335:     """Expose the current metrics snapshot."""
336: 
337:     payload = context.observability.as_dict()
338:     payload["config_revision"] = context.config_revision
339:     return payload
340: 
341: 
342: def request_api_key(request: Request, explicit_api_key: str | None = None) -> str | None:
343:     """Read an API key from explicit args, headers, or query params."""
344: 
345:     if explicit_api_key:
346:         token = explicit_api_key.strip()
347:         if token:
348:             return token
349: 
350:     api_key = request.headers.get("x-api-key") or request.headers.get("X-API-Key")
351:     if api_key:
352:         token = api_key.strip()
353:         if token:
354:             return token
355: 
356:     authorization = request.headers.get("authorization") or request.headers.get("Authorization")
357:     if authorization:
358:         prefix = "bearer "
359:         if authorization.lower().startswith(prefix):
360:             token = authorization[len(prefix):].strip()
361:             if token:
362:                 return token
363: 
364:         token = authorization.strip()
365:         if token:
366:             return token
367: 
368:     query_token = request.query_params.get("api_key")
369:     if query_token:
370:         token = query_token.strip()
371:         if token:
372:             return token
373: 
374:     return None
375: 
376: 
377: def build_http_request_context(
378:     request: Request,
379:     *,
380:     tenant: TenantSpec | dict[str, Any] | None = None,
381:     base_collection: str = "default",
382:     user_id: int | None = None,
383:     agent_id: int | None = None,
384:         api_key: str | None = None,
385:         kb_id: int | None = None,
386:         kb_scope: str | None = None,
387:         kb_name: str | None = None,
388:         resolved_collection: str | None = None,
389:         operation: str = "request",
390:         subject: str | None = None,
391: ) -> RequestContext:
392:     """Build and attach the canonical request context for an HTTP request."""
393: 
394:     request_context = RequestContext.from_http(
395:         request,
396:         tenant=tenant,
397:         base_collection=base_collection,
398:         user_id=user_id,
399:         agent_id=agent_id,
400:         api_key=request_api_key(request, api_key),
401:         kb_id=kb_id,
402:         kb_scope=kb_scope,
403:         kb_name=kb_name,
404:         resolved_collection=resolved_collection,
405:         operation=operation,
406:         subject=subject,
407:     )
408:     request.state.request_context = request_context
409:     request.state.request_id = request_context.request_id
410:     request.state.trace_id = request_context.trace_id
411:     return request_context
412: 
413: 
414: def build_mcp_request_context(
415:     payload: dict[str, Any],
416:     *,
417:     tenant: TenantSpec | dict[str, Any] | None = None,
418:     base_collection: str = "default",
419:     user_id: int | None = None,
420:     agent_id: int | None = None,
421:     api_key: str | None = None,
422:     kb_id: int | None = None,
423:     kb_scope: str | None = None,
424:     kb_name: str | None = None,
425:     resolved_collection: str | None = None,
426:     operation: str = "mcp",
427:     subject: str | None = None,
428: ) -> RequestContext:
429:     """Build the canonical request context for an MCP tool call."""
430: 
431:     return RequestContext.from_mcp(
432:         payload,
433:         tenant=tenant,
434:         base_collection=base_collection,
435:         user_id=user_id,
436:         agent_id=agent_id,
437:         api_key=api_key,
438:         kb_id=kb_id,
439:         kb_scope=kb_scope,
440:         kb_name=kb_name,
441:         resolved_collection=resolved_collection,
442:         operation=operation,
443:         subject=subject,
444:     )
445: 
446: 
447: def tenant_subject(tenant: TenantSpec | None, *, fallback: str = "default") -> str:
448:     """Build a stable subject key from tenant scope."""
449: 
450:     if tenant is None:
451:         return fallback
452:     return normalize_tenant(tenant).canonical_key(fallback=fallback)
453: 
454: 
455: def request_subject(request: Request, tenant: TenantSpec | None, *, fallback: str = "default") -> str:
456:     """Build a rate-limit subject for an HTTP request."""
457: 
458:     client_host = request.client.host if request.client and request.client.host else fallback
459:     return tenant_subject(tenant, fallback=client_host)
460: 
461: 
462: def enforce_guardrails(
463:     context: AppContext,
464:     *,
465:     request_context: RequestContext,
466: ) -> None:
467:     """Apply auth and rate limiting with the shared app context."""
468: 
469:     auth = context.security_policy.validate(request_context.api_key, tenant=request_context.tenant)
470:     if not auth.allowed:
471:         if auth.reason == "api key required":
472:             raise AuthenticationError(auth.reason)
473:         raise AuthorizationError(auth.reason)
474: 
475:     resolved_subject = request_context.subject_key(fallback=auth.tenant_key or "default")
476:     if context.rate_limiter.limit <= 0:
477:         return
478: 
479:     decision = context.rate_limiter.allow(resolved_subject)
480:     if decision.allowed:
481:         return
482: 
483:     raise RateLimitExceededError(
484:         f"rate limit exceeded for {resolved_subject}: retry after {decision.retry_after_seconds:.2f}s"
485:     )
486: 
487: 
488: def enforce_http_guardrails(
489:     request: Request,
490:     *,
491:     request_context: RequestContext,
492: ) -> None:
493:     """Apply app guardrails and convert failures into HTTP errors."""
494: 
495:     context = get_app_context(request)
496:     try:
497:         enforce_guardrails(context, request_context=request_context)
498:     except AuthenticationError as exc:
499:         raise HTTPException(status_code=401, detail=str(exc)) from exc
500:     except AuthorizationError as exc:
501:         raise HTTPException(status_code=403, detail=str(exc)) from exc
502:     except RateLimitExceededError as exc:
503:         raise HTTPException(
504:             status_code=429,
505:             detail=str(exc),
506:             headers={"Retry-After": "1"},
507:         ) from exc

(End of file - total 507 lines)
</content>
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 18.6s)

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag\\src\\mcp_rag\\cli.py"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag\src\mcp_rag\cli.py</path>
<type>file</type>
<content>1: """CLI interface for MCP-RAG service."""
2: 
3: import typer
4: from pathlib import Path
5: 
6: from .main import run_http_server_sync
7: 
8: app = typer.Typer()
9: 
10: 
11: @app.command()
12: def serve():
13:     """启动每个客户端都可通过 Streamable HTTP 访问的 MCP-RAG 服务。"""
14:     typer.echo("启动MCP-RAG Streamable HTTP服务器...")
15:     run_http_server_sync()
16: 
17: 
18: 
19: @app.command()
20: def init(
21:     data_dir: str = typer.Option("./data", "--data-dir", help="数据目录")
22: ):
23:     """初始化MCP-RAG服务。"""
24:     data_path = Path(data_dir)
25:     chroma_dir = data_path / "chroma"
26: 
27:     # 创建目录
28:     data_path.mkdir(parents=True, exist_ok=True)
29:     chroma_dir.mkdir(parents=True, exist_ok=True)
30: 
31:     typer.echo(f"在 {data_path} 初始化了MCP-RAG数据目录")
32: 
33: 
34: @app.callback()
35: def callback():
36:     """MCP-RAG: 基于MCP协议的低延迟RAG服务。"""
37:     pass
38: 
39: 
40: def main():
41:     """CLI入口点。"""
42:     app()
43: 
44: 
45: if __name__ == "__main__":
46:     main()

(End of file - total 46 lines)
</content>
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 14.5s)

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\xfwork\\mcprag\\mcp-rag\\src\\mcp_rag\\services\\__init__.py"
}
```

**Output:**
```
<path>D:\xfwork\mcprag\mcp-rag\src\mcp_rag\services\__init__.py</path>
<type>file</type>
<content>1: """Service layer for MCP-RAG."""
2: 
3: from .chat_service import ChatService
4: from .indexing_service import IndexingService
5: from .retrieval_service import RetrievalService
6: from .runtime import RuntimeContainer, ServiceRuntime
7: 
8: __all__ = [
9:     "ChatService",
10:     "IndexingService",
11:     "RetrievalService",
12:     "RuntimeContainer",
13:     "ServiceRuntime",
14: ]
15: 

(End of file - total 15 lines)
</content>
```

---

## Assistant (Build · qwen3-max-2026-01-23 · 45.2s)

## src/mcp_rag/ 目录文件作用分析

### 核心模块
- **`main.py`**: HTTP服务主入口，启动uvicorn服务器
- **`cli.py`**: 命令行接口，提供`serve`和`init`命令
- **`app_factory.py`**: 应用上下文工厂，组装运行时依赖（配置、安全、限流、可观测性等）
- **`service_facade.py`**: 统一服务门面，协调HTTP/MCP协议与核心服务
- **`shell_factory.py`**: Shell上下文工厂，处理请求级上下文和守卫逻辑

### 协议层
- **`http_server.py`**: FastAPI HTTP服务实现，包含所有API路由和Web界面
- **`mcp_server.py`**: MCP协议服务实现，定义`rag_ask`工具

### 核心服务层 (`services/`)
- **`runtime.py`**: 服务运行时容器，管理LLM、Embedding、向量存储等依赖
- **`indexing_service.py`**: 文档索引服务，处理文件上传、解析、分块、向量化
- **`retrieval_service.py`**: 检索服务，执行混合检索和摘要生成
- **`chat_service.py`**: 聊天服务，基于检索结果生成对话回答

### 基础设施
- **`config.py`**: 配置管理，支持JSON/SQLite持久化和热更新
- **`knowledge_bases.py`**: 知识库注册表，管理多知识库元数据
- **`context.py`**: 请求上下文管理，处理租户、权限信息
- **`contracts.py`**: 数据契约定义，统一各层数据结构
- **`security.py`**: 安全策略，实现API Key鉴权、限流、配额控制
- **`observability.py`**: 可观测性，收集指标、健康检查信息
- **`llm.py`**: LLM抽象层，支持多种大模型provider

### 其他
- **`spa_assets.py`**: SPA静态资源管理
- **`static/`**: Web前端静态文件
- **`core/`**: 核心索引实现（文档处理器、文本分块、向量存储等）
- **`retrieval/`**: 检索相关逻辑（查询分类、混合检索服务等）

## 服务启动工作流程

### 1. 启动入口
```bash
mcp-rag serve  # 通过CLI
# 或
uv run mcp-rag serve
```

### 2. 初始化阶段
1. **CLI解析**: `cli.py` 解析命令参数
2. **配置加载**: `config.py` 加载默认配置，创建`config.json`文件
3. **应用上下文创建**: `app_factory.py` 创建`AppContext`，包含：
   - 配置管理器
   - 安全策略（API Key、限流）
   - 可观测性收集器
   - 知识库服务
   - 服务运行时容器

### 3. HTTP服务启动
1. **FastAPI应用创建**: `http_server.py` 创建FastAPI实例
2. **生命周期管理**: 设置lifespan，在启动时：
   - 加载shell上下文
   - 初始化MCP服务管理器
   - 挂载静态文件和MCP端点

### 4. 运行时依赖懒加载
- **首次请求触发**: 各组件（文档处理器、Embedding模型、向量存储、LLM）在首次使用时初始化
- **依赖注入**: 通过`ServiceRuntime`统一管理组件依赖关系

### 5. 请求处理流程
```
HTTP/MCP请求 → app_factory中间件 → shell_factory上下文解析 
→ service_facade路由 → 具体服务层（indexing/retrieval/chat）
→ 核心组件（core/indexing, retrieval） → 返回结果
```

### 6. 热更新支持
- 配置变更时自动重新加载运行时依赖
- 知识库内容变更时自动清理检索缓存

这种架构实现了协议无关、租户隔离、配置热更新的RAG服务，同时提供完整的治理能力（安全、限流、配额、可观测性）。





---

