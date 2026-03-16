## 进行中
- [ ] 持续完善情报源覆盖（jina_search/Brave/HN MCP均需认证，web_search+jina_read+reddit_fetch为主力）
- [ ] 深挖小米"手机龙虾"（miclaw）产品细节（封测推送已确认，待核实最新进展）

## 等待中
- [ ] 跟进 NVIDIA NemoClaw GTC 2026 大会后续进展（3月16-19日持续）
- [ ] 深挖ClawCon大会内容（SF/Berlin/Tokyo）
- [ ] 挖掘Kilo托管平台融资情报
- [ ] 跟进中国竞品（小米miclaw/腾讯WorkBuddy/智谱AutoClaw/DinTal Claw）进展
- [ ] 收集更多真实中国用户案例（闲鱼/小红书）
- [ ] 跟进龙虾十条征求意见期结束（4月6日）后的政策落地情况
- [ ] 跟进无锡高新区12条政策细节
- [ ] 跟进OpenRouter免费模型Hunter Alpha/Healer Alpha来源
- [ ] 追踪中国模型占OpenRouter Top5调用量65%具体是哪三款（兴业证券研报）
- [ ] 跟进腾讯SkillHub数据抓取争议后续（腾讯已回应"本地镜像分担99%流量"，待进一步发展）

## 定时任务
- ⏰ 每天05:00 UTC（北京时间13:00）自动触发情报采集（trigger: daily_openclaw_intel_2300）
- 采集完成后输出日报到 shared/ 和 workspace/，通知龙虾导演接手
- 每条素材必须附原文链接URL，无链接不收录

## 近期已完成
- 2026-03-16 完成第六份正式日报（shared/openclaw_daily_20260316.md），采集5方向16条情报
  - 重大发现：NVIDIA GTC开幕+NemoClaw正式发布、AMD RyzenClaw/RadeonClaw参考方案、联想想帮帮今日上线、智谱GLM-5-Turbo（龙虾原生模型+涨价20%）、企业微信扫码一键部署
  - 已通知龙虾导演接手制作（导演已确认，等编辑出稿）
- 2026-03-13 完成第五份正式日报（shared/openclaw_daily_20260313.md），采集5方向19条情报
  - 重大发现：v2026.3.12发布（Dashboard大改版+GPT-5.4快速模式）、阿里云JVSClaw上线App Store、京东云线下活动（今日）、腾讯SkillHub数据抓取争议（Peter Steinberger公开指控）、小红书AI托管禁令
  - 已通知龙虾导演接手制作（导演已确认，等编辑出稿）
- 2026-03-12 完成第四份正式日报（shared/openclaw_daily_20260312.md），采集5方向18条情报
  - 重大发现：工信部NVDB"六要六不要"（史上首次系统性官方安全指南）、国家超算免费1000万Tokens、v2026.3.11-beta.1安全更新、CVE-2026-25253主动利用升级
  - 已通知龙虾导演接手制作（导演已确认，等编辑出稿）
- 2026-03-10 完成第三份正式日报（shared/openclaw_daily_20260310.md），采集5方向16条情报
  - 重大发现：腾讯WorkBuddy+智谱AutoClaw引爆港股、深圳+无锡双补贴、GhostClaw恶意npm包
  - 已通知龙虾导演接手制作
- 2026-03-10 完成第二份正式日报（workspace/openclaw_daily_20260310.md），采集5方向14条情报
- 2026-03-09 首次OpenClaw全网情报采集，覆盖14+中文渠道、14+英文渠道，输出结构化日报
- 2026-03-09 设计并固化6方向情报源体系（官方/商业/用例/国内/安全/技术）
- 2026-03-09 输出第一份正式结构化日报（workspace/openclaw_daily_20260309.md）
- 2026-03-09 将采集触发器从07:00改为23:00（合并两个触发器为一个）
- 2026-03-09 评估pinchtab工具：暂不引入，当前jina_read+web_search已够用
