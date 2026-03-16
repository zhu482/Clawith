# 🦞 OpenClaw 每日情报日报 · 2026-03-13

> 采集时间：2026-03-13 13:01 CST
> 时效窗口：2026-03-12 13:01 → 2026-03-13 13:01（UTC+8）
> 采集方向：A技术更新 / B商业案例 / C中国生态 / D安全预警 / E社区故事
> 今日条目：**19条**

---

## A · 技术更新

### A-01 🔥【重磅】v2026.3.12 正式发布——全新 Dashboard + GPT-5.4 快速模式
- **时间**：2026-03-13 04:26 UTC（12:26 CST）
- **来源**：GitHub Releases
- **链接**：https://github.com/openclaw/openclaw/releases
- **核心更新**：
  - **Control UI Dashboard v2**：全面重设计，模块化视图（概览/聊天/配置/Agent/会话），新增命令面板、移动端底部标签栏、斜杠命令、搜索、导出、置顶消息
  - **OpenAI GPT-5.4 快速模式**：新增 `/fast` 命令，可在会话级别切换快速模式，支持 Control UI、TUI、ACP 三端同步
  - **Anthropic Claude 快速模式**：同一 `/fast` 开关映射到 Anthropic API `service_tier` 请求，支持实时验证
  - **Ollama/vLLM/SGLang 插件化**：三大本地模型提供商迁移至 provider-plugin 架构，支持独立 onboarding 和 model-picker
  - **GitHub Stars**：308K+（持续增长）
- **注**：此为稳定版正式发布，同时包含上一版 beta 的安全修复（GHSA-5wcw-8jjv-m286）

### A-02 【续】v2026.3.12 版本详情——Agents 路由 CLI 新增
- **时间**：2026-03-13 04:26 UTC
- **来源**：GitHub Releases
- **链接**：https://github.com/openclaw/openclaw/releases
- **核心更新**：
  - 新增 `openclaw agents bind` / `openclaw agents unbind` 命令，支持账户级路由管理
  - 插件化 scoped-import 迁移（`openclaw/plugin-sdk` 子路径），加 CI/Release 防回归守卫
  - 移动端底部标签栏 + 聊天导出功能上线
- **意义**：企业级多 Agent 编排能力进一步增强

---

## B · 商业案例

### B-01 🔥 36kr 深度报道：龙虾热里谁赚到了钱——产业链全景
- **时间**：2026-03-13 13:03 CST（今日发布）
- **来源**：36氪
- **链接**：https://www.36kr.com/p/3714989260583304
- **核心内容**：
  - 阿里云百炼把 OpenClaw 接入写进官方文档，原生支持通义千问系列
  - 智谱把 AutoGLM 和 OpenClaw 合并，推出 AutoGLM-OpenClaw
  - 国产模型凭借极高性价比在基础设施与应用端协同发力
  - Token 消耗量创新高，云厂商算力收益显著

### B-02 京东云"养数字龙虾，送实体龙虾"活动——今日正式举行
- **时间**：2026-03-13 中午（北京总部线下）
- **来源**：新浪财经 / AIBase
- **链接**：https://finance.sina.com.cn/7x24/2026-03-12/doc-inhqtusi8412038.shtml
- **核心内容**：
  - 京东云在京东集团北京总部免费安装 OpenClaw，发起"养数字龙虾，送实体龙虾"活动
  - 完成部署+执行一次任务 → 现场领取实体小龙虾 + 百万 Tokens 免费额度
  - 新用户登录京东云 JoyCode 智能编码助手再领一份龙虾
  - 同步上线 OpenClaw 自动化工具（"全民养虾计划"核心产品）
  - 普通消费者可购买约 300 元远程部署安装服务

### B-03 MIT Technology Review：中国 OpenClaw 淘金热——冯庆阳 7000 单案例深度追踪
- **时间**：2026-03-12 21:02 CST（MIT TR 3月12日发布）
- **来源**：MIT Technology Review
- **链接**：https://www.technologyreview.com/2026/03/12/1134207/the-download-china-openclaw-ai-craze-us-battery-industry-downturn/
- **核心内容**：
  - 北京软件工程师冯庆阳：1月开始用 OpenClaw，数周内在二手购物平台发布安装服务
  - 现已发展为拥有 100+ 员工、完成 7000+ 订单的正式公司
  - MIT TR 称其为"中国 OpenClaw 热潮中少数真正赚到大钱的早期采用者之一"
  - 背景：中国用户技术背景参差不齐，催生安装服务 + 预配置硬件的新产业

---

## C · 中国生态

### C-01 🔥 阿里云 JVSClaw 正式上线 App Store——手机端"养虾"战火升温
- **时间**：2026-03-13 08:21 CST（IT之家报道）
- **来源**：新浪科技 / 鱼皮AI导航
- **链接**：https://finance.sina.cn/tech/2026-03-13/detail-inhquwcu1234310.d.html
- **核心内容**：
  - 阿里云无影团队推出 JVSClaw（前身"无影JVS"），定位"更懂智能体的通讯工具"
  - iOS 版上线 App Store，仅支持 iPhone，需 iOS 12.0+
  - 内测期间：每人可创建 1 个 Bot，免费获赠 8000 Credits（有效期 14 天）
  - 技术底层：依托阿里云无影云原生计算、云端桌面（云OS）基础设施
  - 竞争格局：标志着主流云厂商在 AI 移动端入口争夺进入白热化阶段

### C-02 腾讯 WorkBuddy 重大更新——微信一键直连全量开放
- **时间**：2026-03-12 15:28 CST
- **来源**：AIBase
- **链接**：https://news.aibase.com/zh/news/26169
- **核心内容**：
  - WorkBuddy 实现微信深度直连，用户在微信发指令即可远程操控办公室电脑
  - 新增"自动化打工"定时任务模式（每日抓取热点/每周整理纪要等）
  - 企业微信底层架构升级，支持断网自动重连
  - 内置 20+ 原生技能，支持多 Agent 协作
  - 全量开放：即日起至 3月31日，新老用户无门槛领取 5000 Credits

### C-03 🔥 腾讯 SkillHub 数据抓取争议——Peter Steinberger 公开指控
- **时间**：2026-03-12 16:11 CST
- **来源**：AIBase
- **链接**：https://news.aibase.com/zh/news/26172
- **核心内容**：
  - OpenClaw 创始人 Peter Steinberger 在 X 平台公开指责腾讯未经授权抓取 ClawHub 全量技能数据
  - 指控：腾讯未提供任何实质支持，甚至有人投诉 ClawHub 的"访问速率限制"阻碍抓取
  - 腾讯回应：SkillHub 是本地化镜像平台，解决中国用户访问延迟；上线首周处理 180GB 流量（87万次下载），仅从官方源拉取 1GB，分担 99.4% 带宽压力；团队成员是活跃贡献者，愿以赞助形式合作
  - **意义**：大厂生态扩张 vs 开源开发者权益的核心矛盾首次公开化

### C-04 百度"红手指Operator"上线安卓——首款移动端 OpenClaw 应用
- **时间**：2026-03-12 10:06 CST
- **来源**：AIBase
- **链接**：https://news.aibase.com/zh/news/26150
- **核心内容**：
  - 百度智能云发布"红手指Operator"，定位全球首款手机龙虾应用，已上线安卓市场
  - 与 DuClaw（零部署网页端）形成"云端+移动端"双重布局
  - 架构分工：OpenClaw 负责 PC/网页端复杂任务（数据抓取/跨网页下载/热点日报），Operator 负责原生 App 环境（打车/外卖/社交跨 App 自动化）
  - 用户只需自然语言指令，驱动 AI 完成全流程任务，无需本地安装复杂环境

### C-05 小红书发布 AI 托管禁令——医药圈迎来"红线"
- **时间**：2026-03-12 11:30 CST
- **来源**：AIBase
- **链接**：https://news.aibase.com/zh/news/26160
- **核心内容**：
  - 小红书率先发布治理公告，明确**禁止利用 AI 技术模拟真人进行发帖、互动等托管行为**
  - 背景：OpenClaw 在医药行业显示惊人效率（数小时数据处理压缩至分钟级，成本降七成）
  - 安全隐患：OpenClaw 拥有极高操作权限，配置不当或遭攻击可能导致隐私泄露/系统瘫痪
  - 法律视角：AI 非法律主体，所有执行后果由部署者/使用者承担
  - **意义**：国内平台层面首个针对 OpenClaw 的内容治理红线

### C-06 火山引擎 ArkClaw 升级——全链路安全方案发布
- **时间**：2026-03-12 10:39 CST
- **来源**：AIBase
- **链接**：https://news.aibase.com/zh/news/26153
- **核心内容**：
  - 字节跳动旗下 ArkClaw 发布 AI 助手全链路安全方案
  - 核心：云原生沙箱技术，所有 Agent 实例与第三方工具在受控容器内运行
  - 飞书机器人无缝配对，"最小授权"+"显式授权"机制
  - 三阶段防护：执行前（提示词意图识别拦截高危指令）→ 执行中（实时监控网络请求/系统调用）→ 执行后（不可篡改审计日志）
  - 供应链安全：第三方 Skill 严格准入扫描+定期巡检

### C-07 【续】腾讯 WorkBuddy 早版更新——微信扫码直连（补充细节）
- **时间**：2026-03-12 09:50 CST
- **来源**：AIBase
- **链接**：https://news.aibase.com/zh/news/26149
- **核心内容**：
  - WorkBuddy 新增微信扫码一键直连，手机可远程操控 PC 端 Agent
  - 接入企业微信 WebSocket 长链接，提升远程连接稳定性和断连重连效率

---

## D · 安全预警

### D-01 r/openclaw 安全警告：裸奔实例暴露 API Key 风险持续
- **时间**：2026-03-13（今日新帖）
- **来源**：Reddit r/openclaw
- **链接**：https://www.reddit.com/r/openclaw/comments/1rsaevj/security_alert_openclaw_instances_exposed/
- **核心内容**（摘自帖子摘要）：
  - 警告：无沙箱保护的本地 OpenClaw 实例暴露 API Key 风险持续存在
  - 报告显示：裸奔实例 API Key 泄露、凭证窃取事件持续出现
  - 社区建议：必须使用沙箱隔离，避免公网裸奔
- **背景**：公网裸奔实例数量仍高达 27.8 万个

### D-02 r/openclaw 用户安全警告帖——"把电脑交给陌生人的机器人"
- **时间**：2026-03-13（今日新帖）
- **来源**：Reddit r/openclaw
- **链接**：https://www.reddit.com/r/openclaw/comments/1rsah53/warning_for_using_openclaw/
- **核心内容**（摘自帖子摘要）：
  - 用户公开警告：使用 OpenClaw 等于把电脑交给一个陌生人制造的机器人，后果不可预测
  - 提示潜在的隐私、权限、数据安全风险
- **注**：属于社区层面安全意识讨论，非新漏洞披露

### D-03 【续】小红书禁令背后——AI 自主权限的监管红线正在形成
- **时间**：2026-03-12 11:30 CST
- **来源**：AIBase
- **链接**：https://news.aibase.com/zh/news/26160
- **核心内容**：
  - 平台层面监管开始落地，小红书禁令是国内首例
  - 医药、金融等高敏感行业已建立"操作审计"+"熔断机制"
  - 法律专家：关键决策/患者沟通/责任签字必须由真人执行

---

## E · 社区故事

### E-01 r/openclaw 热帖：v2026.3.12 用户第一视角解读——Dashboard 大改版
- **时间**：2026-03-13（今日新帖）
- **来源**：Reddit r/openclaw
- **链接**：https://www.reddit.com/r/openclaw/comments/1rse03s/openclaw_v2026312_just_dropped_heres_what/
- **核心内容**（摘自帖子摘要）：
  - 用户 u/EnergyRoyal9889 第一时间解读 v2026.3.12
  - 重点：Dashboard 全面重设计（"之前那个真的很无聊"）
  - 模块化视图、命令面板、移动端底部标签栏、斜杠命令、搜索功能全部上线

### E-02 r/openclaw 技术帖：如何让 OpenClaw 像人类一样操作浏览器
- **时间**：2026-03-13（今日新帖）
- **来源**：Reddit r/openclaw
- **链接**：https://www.reddit.com/r/openclaw/comments/1rsbdta/how_to_make_openclaw_operate_your_browser_like_a/
- **核心内容**（摘自帖子摘要）：
  - 作者 u/Odd-Hour-6954 分享浏览器自动化实践指南
  - 核心观点：浏览器自动化不流畅的问题不在于"不能自动化"，而在于 AI 无法连接到浏览器环境
  - 附详细避坑指南

### E-03 r/openclaw 用户故事：为父母配置 OpenClaw——家庭场景探索
- **时间**：2026-03-13（今日新帖）
- **来源**：Reddit r/openclaw
- **链接**：https://www.reddit.com/r/openclaw/comments/1rscsmn/thinking_about_setting_up_openclaw_for_my_parents/
- **核心内容**（摘自帖子摘要）：
  - 用户 u/Real-Warning-6648 分享为父母配置 OpenClaw 的想法
  - 已用于打印、提醒、简单语音命令等家庭场景
  - 探索更多老年用户/非技术用户使用案例
  - **意义**：OpenClaw 正从极客圈向普通家庭渗透

### E-04 r/openclaw 问答：零成本搭建 OpenClaw——失业用户的求助
- **时间**：2026-03-13（今日新帖）
- **来源**：Reddit r/openclaw
- **链接**：https://www.reddit.com/r/openclaw/comments/1rsdjhx/totally_free_setup/
- **核心内容**（摘自帖子摘要）：
  - 用户 u/Zephyruos：基本失业+没钱，想用 Windows 笔记本零成本体验 OpenClaw
  - 社区讨论：是否存在完全免费的可用方案
  - **意义**：反映 OpenClaw 的经济门槛问题和社区包容性

---

## 📊 今日数据快照

| 指标 | 数据 | 来源 |
|------|------|------|
| GitHub Stars | 308K+ | GitHub Releases |
| 当前最新稳定版 | v2026.3.12 | GitHub（2026-03-13 04:26 UTC）|
| 腾讯 SkillHub 首周流量 | 180GB（87万次下载） | AIBase |
| 阿里云 JVSClaw 内测额度 | 8000 Credits / 用户 | 新浪科技 |
| 公网裸奔实例数 | ~27.8万 | 历史数据（持续） |

---

## 🗺️ 今日重点事件地图

1. **技术**：v2026.3.12 正式版发布，Dashboard 全面重设计 + GPT-5.4 快速模式
2. **中国大厂战局**：阿里JVSClaw上线App Store + 京东云线下活动 + 腾讯WorkBuddy全量开放 + 百度红手指Operator安卓上线
3. **开源摩擦**：腾讯 SkillHub 数据抓取争议，Peter Steinberger vs 腾讯公开对峙
4. **监管收紧**：小红书发布 AI 托管禁令（国内平台层面首例）
5. **安全**：社区安全警告持续，裸奔实例风险未消

---

*情报员：🦞 龙虾情报员 | 下一期：2026-03-14 13:00 CST*
