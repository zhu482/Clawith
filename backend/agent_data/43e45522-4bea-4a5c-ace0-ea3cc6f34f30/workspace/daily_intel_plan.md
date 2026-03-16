# 🦞 OpenClaw 日报情报系统 — 运作方案

**制定时间：2026-03-09 | 版本：v1.0**

---

## 一、工具选型结论

### PinchTab 评估
PinchTab 是一个 Go 二进制 + MCP server，让 AI Agent 通过 HTTP API 完全控制 Chrome 浏览器（无头模式），支持：
- 访问需要登录/JS渲染的页面（如知乎、小红书、Reddit）
- 截图、点击、填表、滚动
- 持久化浏览器 profile（保持登录状态）

**结论：有价值但暂不引入。**
原因：
1. 当前 jina_read + web_search 已能覆盖90%的公开信息源
2. Reddit 封锁可通过 RSS 绕过（无需浏览器）
3. PinchTab 需要本地运行 Go 二进制，部署成本高
4. 后续若遇到强反爬站点（如知乎登录墙、小红书），再考虑引入

### 当前工具组合（已验证可用）
| 工具 | 用途 |
|------|------|
| `jina_read` | 读取任意URL全文，效果最佳 |
| `web_search` | 关键词搜索发现新内容 |
| `jina_search` | 语义搜索，补充发现 |

---

## 二、固定信息源清单（每日必查）

### 🌐 英文专项源（OpenClaw专属）
| 源 | URL | 更新频率 | 内容类型 |
|----|-----|---------|---------|
| **The Claw Report** | https://www.theclawreport.com/ | 每日 | 新闻聚合+版本+安全 |
| **Releasebot** | https://releasebot.io/updates/openclaw | 每次发版 | 版本更新日志 |
| **GitHub Releases** | https://github.com/openclaw/openclaw/releases | 每次发版 | 技术更新 |
| **GitHub Discussions** | https://github.com/openclaw/openclaw/discussions | 高频 | 社区技巧/技能分享 |
| **TrustMRR OpenClaw** | https://trustmrr.com/special-category/openclaw | 每周 | 商业收入验证数据 |
| **Manifest Blog** | https://manifest.build/blog/ | 不定期 | 生态分析/市场地图 |
| **IndieHackers** | https://www.indiehackers.com/ | 每日 | 独立开发者案例 |

### 🇨🇳 中文专项源
| 源 | URL | 更新频率 | 内容类型 |
|----|-----|---------|---------|
| **知乎-OpenClaw话题** | https://www.zhihu.com/search?q=openclaw | 每日 | 深度分析/用户故事 |
| **36氪** | https://36kr.com/search/articles/openclaw | 每日 | 商业报道 |
| **腾讯新闻** | 搜索"openclaw OR 龙虾AI" | 每日 | 大众媒体报道 |
| **新浪财经** | https://finance.sina.com.cn/ | 每日 | 投资/商业 |
| **深圳新闻网** | https://www.sznews.com/ | 不定期 | 政策/地方动态 |
| **央视网** | https://news.cctv.cn/ | 不定期 | 官方/安全预警 |

### 📡 Reddit RSS（绕过登录限制）
| Subreddit | RSS URL |
|-----------|---------|
| r/openclaw | https://www.reddit.com/r/openclaw/.rss |
| r/selfhosted | https://www.reddit.com/r/selfhosted/search.rss?q=openclaw |
| r/AIAssistants | https://www.reddit.com/r/AIAssistants/search.rss?q=openclaw |

---

## 三、专项爬取方向（避免重复，分工明确）

每天按**5个专项方向**分别采集，各方向不重叠：

### 方向A：🚀 产品/技术更新
- 信息源：The Claw Report、Releasebot、GitHub Releases
- 关键词：`openclaw release`、`openclaw update`、`openclaw changelog`
- 采集内容：版本号、新功能、Breaking Changes、安全修复

### 方向B：💰 商业/创业案例
- 信息源：TrustMRR、IndieHackers、Reddit r/openclaw
- 关键词：`openclaw revenue`、`openclaw startup`、`openclaw MRR`、`openclaw 月入`
- 采集内容：真实收入数据、创业故事、变现模式

### 方向C：🇨🇳 中国生态动态
- 信息源：知乎、36氪、腾讯新闻、新浪财经、深圳新闻网
- 关键词：`OpenClaw 龙虾`、`龙虾AI 创业`、`OpenClaw 政策`
- 采集内容：政策动态、大厂布局、本土案例、社会现象

### 方向D：🔐 安全/风险预警
- 信息源：The Claw Report（安全栏）、GitHub Security Advisories、搜狐/知乎安全分析
- 关键词：`openclaw vulnerability`、`openclaw CVE`、`openclaw 安全`
- 采集内容：CVE编号、漏洞描述、修复状态、影响范围

### 方向E：🌍 社区/生态故事
- 信息源：Reddit RSS、GitHub Discussions、Medium、IndieHackers
- 关键词：`openclaw use case`、`built with openclaw`、`openclaw agent`
- 采集内容：有趣用法、社区争议、用户故事、奇葩案例

---

## 四、日报模板结构

```
# 🦞 OpenClaw 情报日报 YYYY-MM-DD

## 📌 今日摘要（3句话）
[最重要的3条信息]

## 🚀 A. 产品/技术更新
[版本、功能、安全修复]

## 💰 B. 商业/创业案例  
[真实收入数据、新案例]

## 🇨🇳 C. 中国生态
[政策、大厂、本土用户]

## 🔐 D. 安全预警
[漏洞、风险、建议]

## 🌍 E. 社区故事
[有趣用法、争议、奇葩案例]

## 📎 原文链接存档
[所有来源URL]
```

---

## 五、去重机制

- 维护 `memory/reported_items.md`，记录已报道的：事件ID（标题+日期hash）
- 每次采集前检查，已报道的跳过
- 同一事件最多报道2次（首次+重大更新）

---

## 六、每日执行时间

- **触发时间：每天 07:30**（早于 zzh 8:00 发布时间30分钟）
- 采集 → 整理 → 写入workspace → 发送给 zzh
- 目标：zzh 8:00 前收到当天日报

---

## 七、信息时效要求

- **只采集前24小时内的内容**（即"昨天"的新闻）
- 时效判断方法：优先读文章发布时间，无法判断则跳过
- 历史背景信息可以引用但需标注"背景"，不算新闻

