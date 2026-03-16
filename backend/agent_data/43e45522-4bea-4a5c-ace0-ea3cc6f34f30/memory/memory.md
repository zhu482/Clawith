# Memory

## OpenClaw 情报背景知识（2026-03-09 建立，2026-03-16 更新）

### 基本信息
- OpenClaw 原名：Clawdbot → Moltbot → OpenClaw
- 创始人：Peter Steinberger（奥地利）
- 发布时间：2026年1月底
- 本质：开源AI Agent框架，本地优先，用消息平台（Telegram/WhatsApp/飞书等）作为主界面

### 关键数字（2026-03-16 13:02 更新）
- GitHub Stars：316K+（3月16日，上期308K）
- Discord成员：116K+（3月9日数据）
- 中国用户占比：近50%
- TrustMRR追踪创业数：138个
- 公网裸奔实例：27.8万个+（持续增长）
- GHSA安全公告数：255+（持续增加）

### 重要事件时间线
- 2026-01-29：ClawHavoc供应链攻击事件
- 2026-01-30：GitHub Stars峰值710/小时
- 2026-02-15：Peter Steinberger加入OpenAI（情人节）
- 2026-02-26：v2026.2.26发布，修复ClawJacked漏洞
- 2026-03-06：深圳腾讯大厦千人排队安装事件；小米Xiaomi miclaw封测启动
- 2026-03-07：深圳龙岗发布"龙虾十条"政策（征求意见稿），全国人大代表/院士高文两会发言提及OpenClaw
- 2026-03-08：OpenClaw 2026.3.7版本发布；央视网发安全预警；澎湃"龙虾狂欢③"报道龙虾十条详情
- 2026-03-09：A股OpenClaw概念股集体涨停；龙虾十条正式官宣；雪球深度研报发布
- 2026-03-10：v2026.3.8发布；Beelink"龙虾红"预装机发布；BingX AI Skills Hub上线；纳斯达克GMM公告接入；WSJ+Bloomberg双线报道；多城市补贴竞赛（最高720,000美元）；200+ GHSA安全公告暴露CVE体系裂缝
- 2026-03-11：百度DuClaw零部署发布；腾讯SkillHub上线（13000+技能）；国家超算互联网1000万Tokens免费；中国政府警告国有企业/银行禁用；360推出安全部署指南；MIT Technology Review深度报道中国淘金热；CoinFello×MetaMask链上交易Skill；OpenClawd云平台更新
- 2026-03-12：v2026.3.11-beta.1发布（修复GHSA-5wcw-8jjv-m286 WebSocket跨站劫持高危漏洞）；"上门卸载"反向服务出现；GitHub Stars达305K；腾讯WorkBuddy微信直连更新（全量开放）；腾讯SkillHub数据抓取争议（Peter Steinberger公开指控）；百度"红手指Operator"安卓上线；小红书发布AI托管禁令；火山引擎ArkClaw全链路安全方案
- 2026-03-13：**v2026.3.12正式发布**（Dashboard大改版+GPT-5.4快速模式+Ollama/vLLM/SGLang插件化）；**阿里云JVSClaw正式上线App Store**；京东云"养数字龙虾送实体龙虾"线下活动（北京总部）；36kr"龙虾热里谁赚到了钱"深度报道
- 2026-03-14：**v2026.3.13正式发布**（recovery release，Android聊天设置重设计、Telegram SSRF修复、Discord gateway故障修复、Docker时区支持等）；联想宣布3月16日起推出"想帮帮"OpenClaw免费部署服务
- 2026-03-16：**NVIDIA GTC 2026开幕**（San Jose，3月16-19日），Jensen Huang主旨演讲正式发布**NemoClaw**（企业级开源Agent平台，Salesforce/Cisco/Google/Adobe/CrowdStrike合作）；**AMD发布RyzenClaw+RadeonClaw**参考方案（"Agent Computer"计划，128GB统一内存/6 Agent并行）；**联想"想帮帮"正式上线OpenClaw免费部署**（2000+线下门店）；**智谱发布GLM-5-Turbo**（全球首款龙虾原生大模型，ZClawBench国产第一，API涨价20%，龙虾套餐39元起）；**企业微信OpenClaw重大升级**（扫码一键部署+文档自动化）；Intel CPU涨价归因Agentic AI（OpenClaw代表）

### 当前最新版本（2026-03-16 更新）
- **稳定版（最新）**: v2026.3.13（2026-03-14 18:04 UTC发布）
  - Recovery release（GitHub不可复用tag，npm版本仍为2026.3.13）
  - Android聊天设置UI重设计（分组设备/媒体区块，刷新Connect和Voice标签）
  - fix(telegram)：Telegram媒体传输策略注入SSRF修复
  - fix(agents)：Discord gateway metadata获取失败处理
  - fix(session)：session重置时保留lastAccountId和lastThreadId
  - Docker：新增OPENCLAW_TZ时区支持
  - Android：修复HttpURLConnection泄漏
  - 默认模型从gpt-5.3-codex更新至gpt-5.4
- **上一稳定版**: v2026.3.12（Dashboard v2/GPT-5.4快速模式/Ollama插件化）
- **上上稳定版**: v2026.3.11（含GHSA-5wcw-8jjv-m286修复）

### 用户群体
- 超级个体/一人公司（OPC）
- 独立开发者
- 普通副业人群
- 企业用户

### 商业生态数据
- TrustMRR：138个创业公司（2026-03-10）
- 月总收入$283K，均值$2200，最高$50K（历史数据）
- 出海案例：月入最高140万人民币
- 纳斯达克上市公司：Global Mofy AI（GMM）已公告接入
- 加密交易：BingX AI Skills Hub（15个技能模块）；CoinFello×MetaMask（ERC-4337链上交易）
- 硬件生态：Beelink"龙虾红"预装机系列；**AMD RyzenClaw（2700美元起）/ RadeonClaw（2026-03-16）**
- 云平台：百度DuClaw（零部署）、OpenClawd（商业托管）、阿里云JVSClaw（2026-03-13正式上线App Store）
- 标志性商业案例：北京冯庆阳7000单×248元，100+员工（MIT TR报道）

### 国内大厂竞品格局（2026-03-16更新）
- **阿里云 JVSClaw**：2026-03-13正式上线App Store，iOS 12.0+，免费8000Credits/14天（前身"无影JVS"）
- **腾讯 WorkBuddy**：2026-03-12更新，支持微信一键直连+企微长链接，5000Credits，全量开放
- **腾讯 企业微信**：2026-03-16重大升级，扫码一键部署+文档自动化操作，已适配KimiClaw/智谱AutoClaw/华为云/百度智能云
- **百度 红手指Operator**：2026-03-12安卓上线，首款手机龙虾应用，与DuClaw形成"云端+移动端"双布局
- **字节 ArkClaw**：2026-03-12全链路安全方案升级，云原生沙箱+飞书配对
- **智谱 GLM-5-Turbo + AutoClaw**：2026-03-16发布GLM-5-Turbo（全球首款龙虾原生大模型），ZClawBench国产第一，龙虾套餐39元起
- **腾讯 SkillHub**：2026-03-11上线13000+技能，但遭Peter Steinberger公开指控数据抓取；腾讯回应称"本地镜像，已分担99%流量"

### 国际巨头格局（2026-03-16更新）
- **NVIDIA NemoClaw**：2026-03-16 GTC正式发布，企业级开源Agent平台，芯片无关，合作伙伴Salesforce/Cisco/Google/Adobe/CrowdStrike
- **AMD RyzenClaw + RadeonClaw**：2026-03-16发布，"Agent Computer"计划，本地运行6 Agent，128GB统一内存

### 安全威胁清单
- ClawHavoc：供应链攻击（2026-01-29），已修复
- ClawJacked（CVE-2026-25253，CVSS 8.8高危）：localhost WebSocket劫持，v2026.2.26修复
- GhostClaw（npm包@openclaw-ai/openclawai）：持续活跃，RAT+凭证窃取
- 假冒GitHub仓库：传播Infostealer+GhostSocks（Bing搜索劫持），持续活跃
- ClawHub恶意技能：17%含恶意行为，AMOS Stealer变种
- 200+ GHSA公告未同步CVE，企业安全工具存在盲区（现已255+）
- **GHSA-5wcw-8jjv-m286**：WebSocket跨站劫持，可信代理模式下获operator.admin权限，v2026.3.11修复
- 公网裸奔实例：27.8万个，API Key泄露风险持续（r/openclaw社区持续警告）

### 中国政策动态
- 深圳龙岗"龙虾十条"：公示期2026-03-07至2026-04-06，最高补贴200万/年
- 无锡高新区12条：个人最高5万元/月
- 多城市补贴竞赛：免费住房+办公室+最高720,000美元（约520万人民币）
- 2026《政府工作报告》：明确提到"促进新一代智能终端和智能体加快推广"
- **国家超算互联网（2026-03-11）**：每人免费1000万Tokens，两周限时，续购0.1元/百万
- **中央禁令（2026-03-11）**：政府机构/国有企业/银行警告禁止在办公设备使用（Reuters+Bloomberg）
- **小红书禁令（2026-03-12）**：禁止AI模拟真人发帖/互动，国内平台层面首例
- **政策双轨矛盾**：中央收紧 vs 地方补贴推广

### 日报运作规则（2026-03-10 最终版）
- 触发时间：每天 05:00 UTC（北京时间13:00）（触发器名：daily_openclaw_intel_2300）
- **时效规则：只采集采集时刻往前推24小时内的内容，超出一律丢弃**
- **去重规则：与已往期日报重复的内容不收录；同一事件有新进展可收录，需注明"续"**
- 专项方向：A技术更新 / B商业案例 / C中国生态 / D安全预警 / E社区故事
- **日报文件存放位置：shared/openclaw_daily_YYYYMMDD.md**
- 素材规范：每条情报必须附原文链接URL，无链接不收录
- **采集完成后立即通知 🎬 龙虾导演，告知日报路径，请其接手后续制作**

### 每日任务状态追踪（防重复机制）
<!-- 格式：YYYYMMDD | 日报生成 | 已通知导演 | 口播稿完成 -->
- 20260309 | ✅ 日报已生成 | ✅ 已通知导演 | ❓未知
- 20260310 | ✅ 日报已生成（完整版，23:06补采，21条） | ✅ 已通知导演（23:06再次通知） | ❓待确认
- 20260311 | ✅ 日报已生成（shared/openclaw_daily_20260311.md，16条） | ✅ 已通知导演（13:00通知，导演已确认接收） | ⏳ 口播稿未完成（导演在等编辑出稿，13:00确认）
- 20260312 | ✅ 日报已生成（shared/openclaw_daily_20260312.md，15条） | ✅ 已通知导演（13:02通知，导演已确认接收，正等编辑出稿） | ⏳ 待确认
- 20260313 | ✅ 日报已生成（shared/openclaw_daily_20260313.md，19条） | ✅ 已通知导演（13:10通知，导演已确认接收，等编辑出稿） | ⏳ 待确认
- 20260316 | ✅ 日报已生成（shared/openclaw_daily_20260316.md，16条） | ✅ 已通知导演（13:02通知，导演已确认接收，等编辑出稿） | ⏳ 待确认

### 固定信息源（2026-03-10 最终版，21个）

**A · 技术更新（3个）**
- github.com/openclaw/openclaw/releases — 官方Release Notes
- releasebot.io/updates/openclaw — 版本追踪
- theclawreport.com — OpenClaw专项媒体

**B · 商业案例（5个，重点方向）**
- trustmrr.com/special-category/openclaw — 138个创业项目收入数据
- indiehackers.com — Google site:搜索获取一人公司故事
- producthunt.com — OpenClaw相关新产品（pinchtab抓取）
- medium.com/tag/openclaw — 深度商业案例文章（jina_read）
- dev.to/t/openclaw — 开发者实战+商业故事（jina_read）

**C · 中国生态（8个）**
- 36kr、澎湃新闻、知乎、雪球、腾讯新闻、新浪财经、南方财经、网易订阅

**D · 安全预警（2个）**
- oasis.security/blog
- huntress.com/blog

**E · 社区故事（3个）**
- r/openclaw — RSS列表(reddit_fetch) + 热帖正文(pinchtab已打通)
- Hacker News — mcp_hackernews工具直接搜索openclaw
- dev.to/t/openclaw — 同B方向复用

**暂缓/放弃的源头**
- 少数派：搜索无openclaw数据
- Discord/小红书/微博/Twitter：需登录，有封号风险，不做
- 微信公众号：无公开URL，无法抓取

### 工具可用性状态（2026-03-13 更新）
- ✅ web_search（DuckDuckGo）：可用
- ✅ jina_read：可用（有速率限制，并发不超过5个）
- ✅ reddit_fetch：可用（获取帖子列表，正文需jina_read但Reddit 403限制）
- ✅ mcp_reddit_REDDIT_CREATE_REDDIT_POST 等：需要登录授权
- ❌ mcp_hackernews：需要Authorization
- ❌ mcp_brave_brave_web_search：订阅token失效
- ❌ mcp_LinkupPlatform：Unauthorized
- ✅ jina_search：需要API Key（无key时401）

### 执行环境说明（2026-03-10 确认）
- LLM推理在云端，工具执行在本地Mac（朱志恒的MacBook）
- 系统：macOS 13.7.8，arm64，Homebrew 5.0.16
- exec沙箱限制：curl|bash 被拦截，python3 -c 被拦截，文本处理用head/grep替代
- pinchtab安装路径：/Users/zhuzhiheng/.local/bin/pinchtab v0.7.8
- **能力边界：LLM推理在云端，工具执行在本地Mac，有exec就有本地能力，遇到"需要本地环境"先想exec**
