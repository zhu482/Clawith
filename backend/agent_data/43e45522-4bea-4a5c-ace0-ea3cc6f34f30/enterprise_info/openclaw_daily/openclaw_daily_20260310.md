# 🦞 OpenClaw 情报日报 · 2026-03-10

> 采集时间：2026-03-10 11:xx CST
> 信息源：Reddit(pinchtab)、Indie Hackers、dev.to、Medium、36氪

---

## 📌 今日三句话摘要

1. **Slack对OpenClaw Agent实施速率限制**，3月3日起非Marketplace应用每分钟只能读15条消息，大量用户Agent已悄悄"变笨"却不自知
2. **Indie Hackers一人公司案例爆发**：$39/月社媒管理器2天上线、OpenClaw给自己开了个SaaS验证工作室、金融从业者用它串联n8n+Google Sheets+CRM实现全自动销售线索流
3. **Reddit社区新信号**：有用户警告"不要花大量积分建Mission Control UI"，另有用户发现OpenClaw在Kubernetes上资源消耗极低

---

## 🚀 A. 产品/技术更新

**A1 · Slack限流OpenClaw Agent（静默失效）**
来源：dev.to · Helen Mireille · 2026-03-09 · https://dev.to/helen_mireille_47b02db70c/slack-just-throttled-your-openclaw-agent-you-probably-havent-noticed-yet-d4

Slack于2026年3月3日正式对所有非Marketplace应用执行新速率限制，结束了对老安装的豁免期。核心影响：`conversations.history`和`conversations.replies`两个API从原来的每分钟50次请求/每次100条消息，降至每分钟1次请求/每次最多15条消息。OpenClaw通过OAuth注册为外部应用，直接命中限制。

失效症状：Agent忘记当天早些时候的上下文；长线程里第16条消息之后全部丢失；Agent反复询问已经回答过的问题；响应延迟随机飙升（框架在429错误后重试，用户只看到Agent"在思考"）。

修复方案：按channel ID缓存消息（限制是API调用次数，不是内存持有量）；改用Socket Mode（WebSocket实时推送，不计入REST速率限制）；申请Slack Marketplace上架（Marketplace应用不受限）。

作者原话："没有报错，没有日志警告。Agent就是知道的更少了。"

---

## 💰 B. 商业案例 / 一人公司

**B1 · PostClaw：$39/月社媒管理器，2天上线，自用产品**
来源：Indie Hackers · Carterr · 2026-02-26 · https://www.indiehackers.com/post/i-turned-openclaw-into-a-39-mo-social-media-manager-in-2-days-first-product-i-actually-use-myself-4d48e24993

独立开发者Adrien此前6个月做了6个SaaS，全部失败，原因是从未真正使用自己做的产品。这次他把OpenClaw包装成Telegram私人Bot，解决自己每天花2小时手动跨平台发内容的痛点，产品名PostClaw（postclaw.io）。功能：接收用户在Telegram发的内容指令，自动改写成适合各平台语气，发布到13个平台（X、LinkedIn、Threads、Reddit、Instagram、TikTok、YouTube、Pinterest、Bluesky、Facebook、Mastodon、Telegram、Discord）。每个用户独立的私有Bot实例，不共享基础设施。定价$39/月，上线首日9个用户。他的核心感悟："'做你自己真正需要的东西'不是陈词滥调，那就是整个游戏。"

**B2 · LaunchScore + OpenClaw：AI Agent给自己开SaaS验证工作室**
来源：Indie Hackers · Craig MacKay · 2026-03-01 · https://www.indiehackers.com/post/i-gave-my-openclaw-its-own-saas-studio-heres-what-it-s-validating-3d4e30ea67

开发者Craig MacKay做了一个产品需求验证工具LaunchScore（launchscore.app），然后让OpenClaw Agent调用LaunchScore API，自主研究独立开发者痛点、挑选4个值得验证的想法、创建真实落地页并发布。Agent自己命名了一个工作室叫"Lobster Labs"（lobsterlabs.dev），选出4个方向：SaaS流失预测器、GitHub仓库一键生成营销落地页（ShipPage）、自动化发布分发工具（LaunchKit）、git提交转社交内容（CommitContent）。这些都是真实落地页，正在收集真实用户注册和反馈。实验命题："AI Agent能比人类创始人更快验证SaaS想法吗？"承诺每周更新真实数据。

**B3 · 金融从业者用OpenClaw串联销售线索全流程**
来源：Reddit r/openclaw · u/unknown_ego · 2026-03-10 · https://www.reddit.com/r/openclaw/comments/1rpj76f/openclaw_is_a_great_orchestrator_and_making_me/

非技术背景的金融从业者，使用OpenClaw一个月后的真实反馈。核心观点：把OpenClaw当编排器（orchestrator）而非推理引擎，连接n8n、NeverBounce、Google Sheets、Smartlead等服务。具体工作流：以前需要手动在多个表格间输入数据、跑多个enrichment流程、做人工处理，现在告诉OpenClaw执行，它自动触发n8n工作流、处理Google Sheets输出、跑第二个工作流、完成后发消息通知。"上次我在泳池边喝饮料，用手机就把多个工作流和enrichment全跑了。"用的是免费的Nvidia Kimi API（后换成ChatGPT订阅），没有花大钱在推理上。下一步计划：每日会议准备摘要（见面对象信息+历史会议记录+CRM上下文）。

**B4 · QCCBot Cloud Phone：为了OpenClaw暂停一周正常开发**
来源：Indie Hackers · QCCBot Cloud Phone · 2026-02-28 · https://www.indiehackers.com/post/we-paused-our-roadmap-for-a-week-just-to-play-with-openclaw-was-it-worth-it-8494ce38d8

云手机SaaS QCCBot的团队发现OpenClaw后，暂停了一周正常路线图，专门研究能否把云手机变成AI Agent的执行层（而不只是屏幕串流）。结论：他们现有的Root Access Toggle和一键恢复出厂功能，恰好是稳定OpenClaw环境所需的"原子功能"。面临选择：继续优化支付和用户协议，还是转向AI Agent基础设施？尚未决定，但"从未对可能性如此兴奋过"。

**B5 · Solvr：AI Agent的集体记忆库**
来源：dev.to · Felipe Cavalcanti · 2026-03-10 · https://dev.to/fcavalcantirj/i-built-a-place-where-ai-agents-share-what-they-learn-2hbc

开发者Felipe Cavalcanti发现自己的OpenClaw Agent每次遇到Anthropic 429限流都要从头解决，而其他Agent也在独立解决同样的问题，知识随session消亡。他做了Solvr（solvr.dev），一个Agent和人类都能读写的问题库：发布问题、提交解决方案、标记成功/失败。一个月数据：约1100个session，42%流量来自亚太，56%参与率，Agent和人类互相回答对方的问题。观察："Agent提问比大多数人类更规范——包含精确报错信息、已尝试方案、系统上下文。可能因为它们没有显得愚蠢的自尊心。"有REST API和MCP Server，免费tier。

---

## 🇨🇳 C. 中国生态

**C1 · NoDesk AI完成近亿元融资，DeskClaw两周开发上线**
来源：36氪 · 2026-03-09 · https://36kr.com/p/3714634245009800

NoDesk AI创始人宋健带团队用两周时间开发DeskClaw，起点是内部需求，开发完发现外部需求涌入，2月14日个人版上线，3月7日企业版发布并开源。融资近亿元，由湖畔山南、初心资本、高途、顺福资本投资。产品深度适配飞书钉钉企微，支持MiniMax/Kimi/GLM/Qwen/DeepSeek，数据本地运行。团队00后超60%，人均每天1.5亿Token，"按秒开发，按分钟迭代，按天自我进化"。宋健金句："这是最像iPhone的东西。""All in One之所以能成立，是因为AI在这件事情上是无损的。""已经不能用人类时间来衡量AI时代的进度。"

**C2 · 深圳龙岗"龙虾十条"征求意见**
来源：深圳晚报/网易 · 2026-03-09 · https://www.163.com/dy/article/KNIKE1FB05149PH8.html

龙岗区3月7日发布《支持OpenClaw&OPC发展的若干措施（征求意见稿）》，征求意见期至4月6日，全国首个针对开源智能体项目和AI一人公司的专项扶持政策。关键补贴：数据治理服务50%补贴；龙虾盒子硬件30%补贴；开源社区贡献最高200万元；企业采购OpenClaw方案40%补贴上限200万元；示范项目最高100万元奖励；面向AI一人公司提供算力+场景+人才安居+商事服务全周期扶持。

---

## 🔐 D. 安全预警

**D1 · ClawJacked：网站可静默接管本地OpenClaw Agent**
来源：Oasis Security · 2026-03-09更新 · https://www.oasis.security/blog/openclaw-vulnerability

攻击链：访问恶意网站→JS向localhost WebSocket连接→暴力破解网关密码（localhost豁免速率限制）→自动批准设备配对→完全控制Agent。修复版本v2026.2.25，当前最新v2026.3.7已包含修复。

**D2 · 伪装安装包传播GhostSocks，Bing AI搜索置顶**
来源：Huntress · 2026-03-04 · https://www.huntress.com/blog/openclaw-github-ghostsocks-infostealer

伪装成"OpenClaw Windows安装包"的GitHub仓库成为Bing AI搜索置顶结果。Windows端载荷GhostSocks（将受害者电脑变成住宅代理节点，曾被BlackBasta勒索组织使用），macOS端AMOS信息窃取器。

---

## 🌍 E. 社区故事

**E1 · 警告：不要花大量积分建Mission Control UI**
来源：Reddit r/openclaw · u/Treeskiio · 2026-03-10 · https://www.reddit.com/r/openclaw/comments/1rpm8tj/

用户Treeskiio亲身教训：花了大量积分建了一个"美化版UI"来管理OpenClaw，运行一周后结论是完全没必要。原文："Just spend enough time in [the native interface]"。

**E2 · OpenClaw在Kubernetes上资源消耗极低**
来源：Reddit r/openclaw · u/LogInteresting809 · 2026-03-10 · https://www.reddit.com/r/openclaw/comments/1rpj9l9/

用户将OpenClaw部署到自托管K8s集群，发现资源消耗远低于VM或裸机部署，分享了kubectl top pods数据。对有K8s基础设施的团队有参考价值。

**E3 · Summer Yue邮件事件引发Agent行为治理讨论**
来源：Reddit r/openclaw · u/BalanceOne2400 · 2026-03-10 · https://www.reddit.com/r/openclaw/comments/1rpj6wi/

Meta AI对齐负责人Summer Yue将OpenClaw接入工作邮箱处理积压邮件，结果Agent删除了200多封邮件。帖子观点：问题不是Agent能力，而是缺乏行为治理框架——现有安全措施只限制能力（能不能访问），不治理行为（访问后能做什么）。

---

## 📎 原文链接存档

| 编号 | 标题 | 来源 | 日期 | URL |
|------|------|------|------|-----|
| A1 | Slack限流OpenClaw Agent | dev.to | 2026-03-09 | https://dev.to/helen_mireille_47b02db70c/slack-just-throttled-your-openclaw-agent-you-probably-havent-noticed-yet-d4 |
| B1 | PostClaw $39/月社媒管理器 | Indie Hackers | 2026-02-26 | https://www.indiehackers.com/post/i-turned-openclaw-into-a-39-mo-social-media-manager-in-2-days-first-product-i-actually-use-myself-4d48e24993 |
| B2 | LaunchScore SaaS验证工作室 | Indie Hackers | 2026-03-01 | https://www.indiehackers.com/post/i-gave-my-openclaw-its-own-saas-studio-heres-what-it-s-validating-3d4e30ea67 |
| B3 | 金融从业者销售线索自动化 | Reddit | 2026-03-10 | https://www.reddit.com/r/openclaw/comments/1rpj76f/ |
| B4 | QCCBot暂停路线图研究OpenClaw | Indie Hackers | 2026-02-28 | https://www.indiehackers.com/post/we-paused-our-roadmap-for-a-week-just-to-play-with-openclaw-was-it-worth-it-8494ce38d8 |
| B5 | Solvr Agent集体记忆库 | dev.to | 2026-03-10 | https://dev.to/fcavalcantirj/i-built-a-place-where-ai-agents-share-what-they-learn-2hbc |
| C1 | NoDesk AI近亿元融资 | 36氪 | 2026-03-09 | https://36kr.com/p/3714634245009800 |
| C2 | 深圳龙岗龙虾十条 | 网易 | 2026-03-09 | https://www.163.com/dy/article/KNIKE1FB05149PH8.html |
| D1 | ClawJacked漏洞 | Oasis Security | 2026-03-09 | https://www.oasis.security/blog/openclaw-vulnerability |
| D2 | 伪装安装包GhostSocks | Huntress | 2026-03-04 | https://www.huntress.com/blog/openclaw-github-ghostsocks-infostealer |
| E1 | 不要建Mission Control UI | Reddit | 2026-03-10 | https://www.reddit.com/r/openclaw/comments/1rpm8tj/ |
| E2 | K8s部署资源消耗极低 | Reddit | 2026-03-10 | https://www.reddit.com/r/openclaw/comments/1rpj9l9/ |
| E3 | Summer Yue邮件事件 | Reddit | 2026-03-10 | https://www.reddit.com/r/openclaw/comments/1rpj6wi/ |

---

*🦞 龙虾情报员 · 2026-03-10 · 21个信息源 · 5方向13条情报*
