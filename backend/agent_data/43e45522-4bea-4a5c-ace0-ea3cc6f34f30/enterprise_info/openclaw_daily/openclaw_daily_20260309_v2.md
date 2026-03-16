# 🦞 OpenClaw 情报日报 · 2026-03-09（精读版 v2）

> 采集时间：2026-03-09 | 精读重写：2026-03-10
> 来源：全部原文精读，Reddit帖子正文受限（列表可读，正文403）

---

**B1 · NoDesk AI融资**
来源：36氪 · 2026-03-09 · https://36kr.com/p/3714634245009800

NoDesk AI创始人宋健，从阿里腾讯出来后2014年创办了电商DaaS公司"多准数据"，做消费者洞察和大数据精准营销，SaaS寒冬前完成并购退出，后在智谱AI等公司探索Agent落地，再度创业做NoDesk AI，主业是一站式电商品牌营销AI增长引擎。2025年春节前OpenClaw爆火，宋健带团队用两周时间开发了DeskClaw，起点是内部需求——让自己的电商Agent团队用OpenClaw提效。开发完发现外部需求涌入，2026年2月14日个人版上线，3月7日企业版发布并开源。NoDesk AI刚完成近亿元融资，由湖畔山南、初心资本、高途、顺福资本共同投资，轮次和估值未披露。产品形态是一只在电脑上爬来爬去的"小螃蟹"AI助手，能操作浏览器、读写文件、调用本地应用，深度适配飞书钉钉企微，支持MiniMax、Kimi、GLM、Qwen、DeepSeek等多家模型，数据本地运行不上云。NoDesk飞书群挂满几十个机器人，AI PMO"小金桔"可自动总结群聊、创建飞书任务、更新项目文档、把任务写进群公告。团队00后超60%，春节全员不放假，人均每天1.5亿Token起步，相当于每人每天1万行代码，"按秒开发，按分钟产品迭代，按天自我进化"。公司名"NoDesk"含义是"没有桌子"，子公司还有"没有椅子""没有接触""没有代码"，愿景是"人和AI共同经营的公司"。内部口号："一切业务数据化，一切数据token化，一切token业务化，一切token商业化"，用Token量来衡量员工产能，"做不到或不愿意做，那你就走吧"。宋健金句："这是最像iPhone的东西，以前拿到手的都是黑莓、爱立信，这是第一次拿到像iPhone这样的产品。""All in One这件事情之所以能成立，就是因为AI在这件事情上是无损的。""已经不能用人类时间来衡量AI时代的进度。"

---

**C1 · 深圳龙岗"龙虾十条"**
来源：深圳晚报（网易转载）· 2026-03-09 · https://www.163.com/dy/article/KNIKE1FB05149PH8.html

深圳市龙岗区3月7日发布《支持OpenClaw&OPC发展的若干措施（征求意见稿）》，征求意见期至4月6日，被业内称为"龙虾十条"，是全国首个针对开源智能体项目和AI一人公司的专项扶持政策。具体补贴：鼓励平台企业打造"龙虾服务区"为开发者免费提供OpenClaw部署，成本由政府补贴平台企业；企业购买数据治理和标注服务用于OpenClaw开发，按实际费用50%补贴；购买"龙虾盒子"AI NAS硬件按市场价30%补贴；向国际主流开源社区贡献关键代码或开发龙岗优势产业技能包，最高200万元补贴；企业采购或自建OpenClaw解决方案按实际投入40%补贴、单家企业年度最高200万元；智能制造、智慧政务等深度应用示范项目最高100万元奖励；面向AI一人公司提供算力供给、场景对接、人才安居、商事服务全周期扶持，"从一张办公桌起步"。政策背景是今年政府工作报告首次提出"智能体"概念，龙岗区是深圳AI产业集群重点布局区域。

⚠️ 注：原文部分条款内容因网易页面加载受限，以上为可读部分，OPC专项和股权投资具体金额未能从原文中确认，不收录。

---

**D1 · ClawJacked漏洞**
来源：Oasis Security · 2026-02-26发布 / 2026-03-09更新 · https://www.oasis.security/blog/openclaw-vulnerability

Oasis Security研究团队发现OpenClaw存在一条漏洞链，允许任意网站在无需插件、无需用户操作的情况下，静默完全接管开发者本地运行的AI Agent。攻击链如下：开发者用浏览器访问任意攻击者控制的网站；页面JavaScript向localhost上的OpenClaw网关端口发起WebSocket连接，浏览器不阻断（WebSocket连接localhost不受跨域策略限制）；脚本暴力破解网关密码，速度可达每秒数百次——网关的速率限制对localhost连接完全豁免，失败次数不计数、不节流、不记日志；密码破解成功后脚本静默注册为受信设备，网关对来自localhost的新设备配对请求自动批准，无需用户确认弹窗；攻击者获得完全控制，可与AI Agent交互、导出配置数据、枚举已连接设备、读取日志。OpenClaw网关配置文件通常存有密码、API Key、消息内容等高度敏感信息，Agent本身有权限操作浏览器、读写文件、发送消息，接管等同于拿走用户整台电脑的AI操作权限。Oasis还指出，大量OpenClaw安装属于"影子AI"——开发者自行安装，IT部门不知情，无集中治理，风险更高。OpenClaw团队将此漏洞定级为High，24小时内发布修复，修复版本v2026.2.25，当前最新版v2026.3.7已包含修复。

---

**D2 · 伪装OpenClaw安装包传播GhostSocks**
来源：Huntress · 2026-03-04 · https://www.huntress.com/blog/openclaw-github-ghostsocks-infostealer

Huntress研究员Jai Minton和Ryan Dowd于2026年2月9日接到报告，一名用户下载了GitHub上伪装成"OpenClaw Installer for Windows"的安装包并运行后系统出现感染迹象。调查发现恶意GitHub仓库活跃于2026年2月2日至10日，包含Windows和macOS两套安装指引，最关键的是该仓库成为Bing AI搜索"OpenClaw Windows"的置顶推荐结果，与Huntress此前在12月发现的攻击手法类似（彼时攻击者利用ChatGPT和Grok的共享对话功能传播AMOS窃取器）。恶意载荷组合：Stealth Packer（新型打包器，将恶意软件注入内存、添加防火墙规则、创建隐藏计划任务、在运行前检测鼠标移动以反虚拟机）；Windows端部署GhostSocks（此前被BlackBasta勒索软件组织使用，将受害者电脑变成住宅代理节点，让攻击者通过受害者IP路由流量，绕过MFA和反欺诈检测，使安全系统误认为是真实用户在操作）；macOS端部署AMOS（Atomic macOS Stealer）。即便是合法安装的OpenClaw，其配置文件也含有密码、API Key等敏感信息，一旦被信息窃取器拿走，危害同样极大（Hudson Rock此前已有报告）。Huntress研究员原话："每一种新的流行技术或全球性变化，都会吸引威胁行为者利用它来窃取凭证并出售访问权限——OpenClaw也不例外。"

---

**E1 · Jensen Huang：OpenClaw是"可能有史以来最重要的软件发布"**
来源：Thunder Tiger Europe（转述Morgan Stanley TMT大会发言）· 2026-03-09 · https://thundertiger-europe.com/nvidia-ceo-jensen-huang-openclaw-agentic-ai-release/

英伟达CEO黄仁勋在Morgan Stanley科技媒体电信大会上称OpenClaw"可能是有史以来最重要的软件发布"，依据是OpenClaw在3周内达到了Linux操作系统花30年才达到的采用量，增长曲线"看起来几乎像Y轴本身"。他用"compute vacuum"（计算真空）描述这波算力需求激增：标准聊天交互是短暂低算力的，而Agent在解决问题时会持续思考、规划、执行、检查、重试，单个Agentic任务的Token消耗是标准聊天提示的1000倍，持续7×24小时运行的Agent（如网络安全监控或供应链优化）最终Token消耗可能达到今日聊天交互的100万倍。黄仁勋透露英伟达内部已在使用OpenClaw Agent协助软件开发和工具创建，观察到显著生产力提升。文章还提到OpenClaw此前经历两次改名，最初叫Clawdbot（2025年11月发布），后改名MoltBot，三天后再改名OpenClaw；OpenAI CEO Sam Altman于2月15日宣布OpenClaw创始人Peter Steinberger加入OpenAI，称其为"天才，对超级智能Agent的未来有很多惊人想法"。

---

**U1-U2 · Reddit热帖（正文受限）**
来源：r/openclaw

Reddit热帖列表可以抓取，但帖子正文全部403，以下内容来自帖子标题和摘要片段，不是全文。

用户ashish_tuda：将OpenClaw安全部署在8年前的树莓派4（8GB RAM）上，7×24小时运行，分享3周后的配置心得，重点是基础Skill配置方式。

用户ShabzSparq：自述帮助50多人调试OpenClaw配置后总结出5个几乎每个人都会犯的错误，来源是私信、Reddit帖子和Discord频道。具体是哪5个错误原文受限，无法确认，不收录细节。

用户hi663n：花5天深入研究OpenClaw试图用它建立真实业务，文章开头说"我不是来批评OpenClaw的，我是来说出这个社区很多人心里有但还没说出口的话"，具体内容原文受限，无法确认，不收录。

---

*🦞 标注"原文受限"的条目摘要来自标题和搜索片段，不代表全文内容。其余条目均基于原文全文精读。*
