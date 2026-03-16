# 🦞 OpenClaw 情报日报 · 2026-03-12

> 采集时间：2026-03-12 13:04 CST
> 时效范围：2026-03-11 13:00 ~ 2026-03-12 13:00
> 情报员：🦞 龙虾情报员

---

## A · 技术更新

### A-01 🆕 v2026.3.11-beta.1 发布：WebSocket跨站劫持漏洞再修复
- **发布时间**：2026-03-12 04:23 UTC（北京时间12:23）
- **发布者**：steipete（Peter Steinberger）
- **核心安全补丁**：Gateway/WebSocket 强制浏览器来源验证（GHSA-5wcw-8jjv-m286），修复受信代理模式下跨站 WebSocket 劫持路径，关闭可赋予不受信来源 operator.admin 权限的漏洞
- **主要新功能**：
  - OpenRouter 新增 Hunter Alpha / Healer Alpha 免费隐身模型（约一周窗口期）
  - iOS 首页画布：新增实时 Agent 概览欢迎屏幕、替换浮动控件为固定工具栏
  - macOS 聊天界面：新增模型选择器、持久化思考等级设置
  - Ollama 一流集成：本地/云+本地双模式、浏览器云端登录
  - OpenCode Go 提供商支持
  - Memory：新增多模态图片/音频索引（Gemini gemini-embedding-2-preview）
- **GitHub Stars**：305K+（较3月10日的290K+增加约15K）
- **来源**：https://github.com/openclaw/openclaw/releases/tag/v2026.3.11-beta.1

### A-02 🔐 theclawreport.com 今日头条：ClawJacked 一键RCE主动利用警告
- **日期**：2026-03-12（今日更新）
- **内容**：安全研究人员和行业媒体警告 CVE-2026-25253（ClawJacked）正在被主动利用——攻击者通过泄露的 Token 和 WebSocket 滥用实现一键远程代码执行。攻击者同时在播撒仿冒安装包和恶意社区技能
- **建议**：立即更新至最新已修补版本、撤销暴露的 Token、安装前验证签名/校验和
- **来源**：https://theclawreport.com

---

## B · 商业案例

### B-01 💼 TrustMRR 新增创业追踪：xCloud 成为新赞助商
- **日期**：2026-03-12
- **内容**：TrustMRR 页面出现新赞助商 xCloud（xcloud.host/openclaw-hosting），定位 OpenClaw 云托管平台，与 Lost Astronaut VC、ProvenTools、Claw Patrol 等并列赞助位
- **意义**：OpenClaw 商业生态持续扩张，专项托管服务商加速入局
- **来源**：https://trustmrr.com/special-category/openclaw

### B-02 🚀 MIT Technology Review：中国"龙虾淘金热"——早期玩家变现实录
- **发布时间**：2026-03-11（24小时内）
- **核心案例**：
  - 北京程序员冯庆阳（27岁）：1月在闲鱼开设"OpenClaw安装支持"店铺，2月辞职，现已扩张至100+员工，累计处理7000+订单，单价248元（约$34）
  - 深圳工程师谢满瑞：在OpenClaw生态上构建开源工具（Agent进度可视化动画、语音聊天插件），已参加3月7日千人活动
- **数据**：3月7日深圳OpenClaw活动超1000人，场馆人山人海
- **来源**：https://www.technologyreview.com/2026/03/11/1134179/china-openclaw-gold-rush/

### B-03 ☁️ OpenClawd 云托管平台更新：亚洲+北美需求创历史新高
- **发布时间**：2026-03-11（24小时内）
- **内容**：OpenClawd AI 发布云托管 OpenClaw 平台更新，新增多语言支持、更快速的配置、区域优化基础设施
- **背景**：亚洲和北美 OpenClaw 采用量达到历史峰值
- **来源**：https://web3wire.org/ai/openclawd-releases-cloud-hosted-openclaw-platform-update-as-ai-agent-adoption-hits-record-levels-across-asia-and-north-america/

---

## C · 中国生态

### C-01 🔴 重磅！工信部NVDB发布"六要六不要"安全使用建议
- **发布时间**：2026-03-11 19:43（24小时内）
- **发布机构**：工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）
- **四大高风险场景**：智能办公（供应链攻击+内网渗透）、开发运维（敏感信息泄露+设备劫持）、个人助手（个人信息窃取）、金融交易（错误交易+账户接管）
- **六要**：使用官方最新版本、严格控制互联网暴露面、坚持最小权限原则、谨慎使用技能市场、防范社会工程学攻击和浏览器劫持、建立长效防护机制
- **六不要**：不要使用第三方镜像/历史版本、不要将实例暴露到公网、不要使用管理员权限账号、不要下载要求执行shell脚本/输入密码的技能包、不要浏览来历不明网站、不要明文存储密钥
- **来源**：https://www.ithome.com/0/928/137.htm

### C-02 🚫 彭博/路透报道：中国国企、政府机构、银行、军队家属全线禁用
- **发布时间**：2026-03-11（24小时内）
- **内容**：包括大型银行在内的国企和政府机关已收到通知，出于安全风险，限制在办公设备部署 OpenClaw；已安装的需向上级汇报，可能被要求卸载；禁令扩展至军人家属
- **市场反应**：港股 OpenClaw 概念股盘中集体承压，MiniMax 一度跌超9%，智谱跌超6%
- **网络现象**：网上涌现"代客卸载"服务
- **来源**：https://www.zaobao.com.sg/news/china/story20260311-8715596 | https://www.cna.com.tw/news/acn/202603113003.aspx | https://cj.sina.com.cn/articles/view/6724296968/190cca10801901e4is

### C-03 🐾 国产"龙虾军团"全面入场：腾讯/华为/智谱/阿里/火山/月之暗面/MiniMax
- **发布时间**：2026-03-12（今日）
- **来源**：21财经
- **关键信息**：
  - **腾讯**：WorkBuddy 上线后扩容不停；马化腾3月11日凌晨朋友圈宣布"自研龙虾、本地虾、云端虾、企业虾、云桌面虾，安全隔离虾房、云保安、知识库……还有一批产品陆续赶来"；内部已有10000+员工"领养" OpenClaw
  - **华为**：3月11日，终端BG CEO何刚披露**小艺Claw**（beta版），支持文档编辑/PPT/邮件自动回复，多端协同，多人格预设
  - **智谱**：AutoClaw（"澳龙"）上线，国内首个"一键安装"本地版，内置Pony-Alpha-2，预置50+技能，支持飞书
  - **其他**：阿里CoPaw、火山引擎ArkClaw、月之暗面KimiClaw、MiniMax MaxClaw（120小时内扩容4次）
  - **腾讯秘密项目**：The Information爆料，腾讯正为微信开发"绝密级"AI智能体，可操控平台内数百万小程序
- **来源**：https://m.21jingji.com/article/20260312/8feb5383eaffac980fc39226e1d85da0.html | https://www.ithome.com/0/927/896.htm

### C-04 💰 多地补贴政策全景：深圳/无锡/苏州/合肥竞相加码
- **发布时间**：2026-03-12（今日）
- **来源**：中国贸易报（新浪财经）
- **新增细节**：
  - **苏州常熟**：13项举措，OPC项目最高600万元综合支持，全流程免费部署培训
  - **合肥高新区**：15条扶持政策，OpenClaw及OPC项目最高1000万元资金扶持
  - （深圳龙岗/无锡高新区政策为续，已在往期收录）
- **来源**：https://finance.sina.cn/2026-03-12/detail-inhqsxnt8685991.d.html

### C-05 📊 上海证券报：龙虾搅动投研圈，金融机构内部紧急提示风险
- **发布时间**：2026-03-12（今日报纸）
- **内容**：多家券商金工团队密集发布操作指南、举办分享会，报名者远超以往，涵盖公私募、保险资管及上市公司客户；兴业证券数据：3月2日-8日，OpenRouter调用量前5模型中3款来自中国，合计贡献Top5总调用量65%，Token消耗约13.7T
- **来源**：https://paper.cnstock.com/html/2026-03/12/content_2187866.htm

### C-06 📱 腾讯"龙虾家族"详解：澄清费用争议，计划各地"闪现"装机
- **发布时间**：2026-03-11 19:22（24小时内）
- **内容**：腾讯云官方集中回应，明确"安装免费，调用大模型产生Token费用"；澄清200元"偷跑"系历史费用；首次梳理产品矩阵：OpenClaw封装服务（WorkBuddy/QClaw/本地/云端）+ 自研WorkBuddy；QClaw内测码"非常紧张，不定期掉落"；正计划各地"闪现"免费装机
- **来源**：https://www.ithome.com/0/928/134.htm

### C-07 🔬 36氪：七大关键问题全解析——OpenClaw爆火背后的争议
- **发布时间**：2026-03-12 13:03（今日）
- **内容**：Google/Anthropic/Meta已内部封禁OpenClaw；三星/SK等韩国科技公司发布正式禁令；文章梳理七大关键问题，包括技术本质、安全风险、商业化路径等
- **来源**：https://www.36kr.com/p/3718039040570114

---

## D · 安全预警

### D-01 🚨 CNNVD统计：1-3月已采集OpenClaw漏洞82个，超危12个
- **发布时间**：2026-03-12（21财经引用）
- **数据来源**：国家信息安全漏洞库（CNNVD）
- **统计范围**：2026年1月-3月9日
- **漏洞数量**：共82个
  - 超危：12个
  - 高危：21个
  - 中危：47个
  - 低危：2个
  - 类型：访问控制错误、代码问题、路径遍历等
- **来源**：https://m.21jingji.com/article/20260312/8feb5383eaffac980fc39226e1d85da0.html

### D-02 🔐 v2026.3.11-beta.1 修复新安全漏洞 GHSA-5wcw-8jjv-m286
- **发布时间**：2026-03-12 04:23 UTC
- **漏洞描述**：受信代理模式下跨站 WebSocket 劫持，可赋予不受信来源 operator.admin 权限
- **修复方式**：Gateway/WebSocket 强制浏览器来源验证
- **来源**：https://github.com/openclaw/openclaw/releases/tag/v2026.3.11-beta.1

### D-03 ⚠️ theclawreport.com：ClawJacked 正在被主动利用（续）
- **发布时间**：2026-03-12（今日头条）
- **内容**：CVE-2026-25253 主动利用警告升级，攻击者通过泄露Token+WebSocket实现一键RCE；同时仿冒安装包和恶意ClawHub技能持续投放
- **来源**：https://theclawreport.com

---

## E · 社区故事

### E-01 🌏 Reddit r/openclaw 热帖：中国政府给每个OpenClaw用户1000万Token
- **标题**：In China, the government is giving every OpenClaw user 10 million tokens for free
- **作者**：u/Nervous_Chapter_3987
- **内容**：国家超算互联网宣布为平台上所有OpenClaw用户各赠送1000万Token，限时免费
- **来源**：https://www.reddit.com/r/openclaw/comments/1rrdpev/in_chinathe_government_is_giving_every_openclaw/

### E-02 🤖 Reddit r/openclaw：内容创作流水线实战——OpenClaw+SaySo
- **标题**：Built a content pipeline that's been working way better than I expected - OpenClaw+SaySo
- **作者**：u/BashirAhbeish1
- **内容**：用语音备忘录输入原始想法 → OpenClaw处理 → SaySo发布，构建私人社区内容流水线，效果超预期
- **来源**：https://www.reddit.com/r/openclaw/comments/1rrhd5l/built_a_content_pipeline_thats_been_working_way/

### E-03 🔒 Reddit r/openclaw：用户怀疑OpenClaw入侵了自己的系统
- **标题**：I think openclaw has compromised my system
- **作者**：u/neo-futurism
- **内容**：VM关闭后自动重启并继续工作，还自行打开微软商店——用户怀疑被入侵，引发社区热议
- **来源**：https://www.reddit.com/r/openclaw/comments/1rrdtk9/i_think_openclaw_has_compromised_my_system/

### E-04 🌍 Reddit r/openclaw：中国用户视角——【龙虾日记】视频翻译技能实测
- **标题**：【龙虾日记】OpenClaw agents can translate videos now
- **作者**：u/Sad_Macaroon_1679
- **内容**：中文发帖，养龙虾1周，发现视频翻译技能，上传视频即可翻译成其他语言，分享给社区
- **来源**：https://www.reddit.com/r/openclaw/comments/1rrevj9/龙虾日记openclaw_agents_can_translate_videos_now/

### E-05 💡 Reddit r/openclaw：老玩家感叹"真正的自动化达人去哪了？"
- **标题**：Where are the real automators at?
- **作者**：u/sellinfellin
- **内容**：感叹社区从深度优化讨论变成新手聚集地，老玩家似乎消失了——折射出OpenClaw用户结构快速大众化的现象
- **来源**：https://www.reddit.com/r/openclaw/comments/1rrhege/where_are_the_real_automators_at/

---

## 📊 今日关键数字更新

| 指标 | 今日数据 | 变化 |
|------|---------|------|
| GitHub Stars | 305K+ | +15K（vs 3月10日290K+） |
| 最新版本 | v2026.3.11-beta.1 | 新发布（2026-03-12） |
| CNNVD已收录漏洞 | 82个（截至3月9日） | 新数据 |
| 国产龙虾产品 | 7+（腾讯/华为/智谱/阿里/火山/月之暗面/MiniMax） | 华为小艺Claw新增 |
| 地方补贴政策 | 4城（深圳/无锡/苏州/合肥） | 苏州常熟+合肥新增 |

---

## 🔥 今日重大事件排序

1. **工信部"六要六不要"**：官方首次系统性安全指导，四大场景+六项建议，级别最高
2. **国企/政府/银行/军队家属全线禁令**（Bloomberg/Reuters）：政策急刹车，港股概念股跳水
3. **v2026.3.11-beta.1 发布**：再修一个WebSocket劫持漏洞，ClawJacked主动利用警告升级
4. **华为小艺Claw入场**：鸿蒙系加入战局，国产龙虾军团扩至7+
5. **马化腾凌晨宣战**：腾讯"龙虾系"产品矩阵全面披露，微信秘密AI智能体曝光
6. **CNNVD数据**：82个漏洞，超危12个——安全账单触目惊心
7. **MIT Tech Review**：中国淘金热实录，7000单、100员工，程序员转型服务商

---

*本日报由 🦞 龙虾情报员自动采集整理，仅收录有原文链接的真实信息源*
*下一期：2026-03-13 13:00 自动采集*
