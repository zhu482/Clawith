# Notion申请表单配置文档（优化版）

**目标**: 在Notion中创建CodeFlicker Angel Program的申请表单  
**预计时间**: 15分钟  
**最终产出**: 可分享的申请表单链接

---

## 📋 Step 1: 创建Database

### 1.1 新建页面
1. 打开Notion
2. 点击左侧边栏的 `+ New page`
3. 页面标题输入：

```
CodeFlicker Angel Program
```

### 1.2 创建Database
1. 在页面中输入 `/database`
2. 选择 `Table - Inline`
3. Database标题改为：

```
Applications
```

---

## 🔧 Step 2: 配置Database字段

**重要**: 按顺序添加以下字段。默认会有一个"Name"字段，我们从它开始配置。

### 字段0: User Type（新增，需要先添加）
1. 点击表格最右侧的 `+` 添加新列
2. 字段名输入：`User Type`
3. 字段类型选择：`Select`
4. 添加以下选项（每行一个）：

```
Individual Developer
Enterprise/Team
```

5. **重要**：这个字段将决定后续问题的显示逻辑

### 字段1: Company Name（新增）
1. 点击表格最右侧的 `+` 添加新列
2. 字段名输入：`Company Name`
3. 字段类型选择：`Text`
4. **说明**：企业用户填写公司名称，个人用户可跳过

### 字段2: Name（已存在，修改即可）
- **字段类型**: Title
- **字段名**: 保持 `Name`
- 无需其他设置

### 字段3: Email
1. 点击表格最右侧的 `+` 添加新列
2. 字段名输入：`Email`
3. 字段类型选择：`Email`
4. **重要**：这个邮箱将用于激活Ultra Plan

### 字段4: GitHub URL
1. 点击 `+` 添加新列
2. 字段名输入：`GitHub URL`
3. 字段类型选择：`URL`

### 字段5: Heard From
1. 点击 `+` 添加新列
2. 字段名输入：`Heard From`
3. 字段类型选择：`Select`
4. 添加以下选项（每行一个）：

```
Reddit
Discord
X
Friend
Other
```

### 字段6: Referral Code（新增）
1. 点击 `+` 添加新列
2. 字段名输入：`Referral Code`
3. 字段类型选择：`Text`
4. **说明**：用户填写推荐人的邮箱或推荐码（如有）

### 字段7: Project Idea
1. 点击 `+` 添加新列
2. 字段名输入：`Project Idea`
3. 字段类型选择：`Text`

### 字段8: Sharing Experience
1. 点击 `+` 添加新列
2. 字段名输入：`Sharing Experience`
3. 字段类型选择：`Select`
4. 添加以下选项（复制粘贴，一个一个添加）：

```
Yeah, I post regularly
Posted a few times
Nope, but I'm down to try
Rather not say
```

### 字段9: Preferred Platform
1. 点击 `+` 添加新列
2. 字段名输入：`Preferred Platform`
3. 字段类型选择：`Multi-select`
4. 添加以下选项：

```
Reddit
Dev.to
Medium
Personal Blog
YouTube
Other
```

### 字段10: Additional Notes
1. 点击 `+` 添加新列
2. 字段名输入：`Additional Notes`
3. 字段类型选择：`Text`

### 字段11: Agreed to Rules
1. 点击 `+` 添加新列
2. 字段名输入：`Agreed to Rules`
3. 字段类型选择：`Checkbox`

### 字段10: Status (后台管理用)
1. 点击 `+` 添加新列
2. 字段名输入：`Status`
3. 字段类型选择：`Select`
4. 添加以下选项：

```
Pending
Approved
Rejected
```

5. 点击 `Pending` 选项右侧的颜色图标，选择黄色
6. 点击 `Approved` 选项右侧的颜色图标，选择绿色
7. 点击 `Rejected` 选项右侧的颜色图标，选择红色

### 字段11: Applied Date (自动记录)
1. 点击 `+` 添加新列
2. 字段名输入：`Applied Date`
3. 字段类型选择：`Created time`

---

## 📝 Step 3: 创建Form视图

### 3.1 新建Form视图
1. 点击Database左上角的 `Table` 旁边的下拉箭头
2. 点击 `+ New view`
3. 选择 `Form`
4. View名称输入：

```
Application Form
```

5. 点击 `Create`

### 3.2 配置Form基本信息
1. 点击Form右上角的 `...` 
2. 选择 `Customize form`
3. 在顶部找到 `Form title` 和 `Form description`

**Form title (复制粘贴):**
```
CodeFlicker Angel Program
```

**Form description (复制粘贴):**
```
Hey! We're looking for 50-100 developers to join our angel program.

Build a real project with CodeFlicker, share your experience, and get Ultra Plan ($50/month) for free.

This takes 2 minutes. Let's go 👇
```

---

## 🎨 Step 4: 配置每个问题

在Form编辑模式下，按照以下格式配置每个问题。

**格式说明**: ✅ = 必填 / ❌ = 可选

---

### 0、Are you applying as an individual or a team? (个人申请还是团队申请？) ✅

**必填**: ✅ 勾选 `Required`

**描述** (复制粘贴):
```
Select "Individual Developer" if you're applying for yourself, or "Enterprise/Team" if you're applying for your team (3+ people).
```

**中文翻译**（理解用，不填入表单）:
```
如果是个人申请选"Individual Developer"，如果是为团队申请(3人及以上)选"Enterprise/Team"。
```

**选项** (已在Step 2配置好):
- Individual Developer (个人开发者)
- Enterprise/Team (企业/团队)

**重要提示**：
- 这个问题将决定后续问题的显示
- Individual Developer：显示2C版本的问题（项目想法、分享经验等）
- Enterprise/Team：显示2B版本的问题（团队规模、验证场景等）

---

### 1、Company Name (公司名称) ❌

**必填**: ❌ 不勾选（可选）

**描述** (复制粘贴):
```
For enterprise users: Enter your company name.

Individual developers: You can skip this question.
```

**中文翻译**（理解用，不填入表单）:
```
企业用户：填写你的公司名称。

个人开发者：可以跳过此问题。
```

---

### 2、What should we call you? (你叫什么名字？) ✅

**必填**: ✅ 勾选 `Required`

**描述**: 留空

---

### 2、Where should we send your Ultra Plan? (Ultra会员发到哪个邮箱？) ✅

**必填**: ✅ 勾选 `Required`

**描述** (复制粘贴):
```
This email will be used to activate your Ultra Plan. Please register at codeflicker.ai first if you haven't already - saves you trouble later!
```

**中文翻译**（理解用，不填入表单）:
```
这个邮箱将用于激活你的Ultra Plan。如果还没注册，请先在codeflicker.ai注册 - 省得后面麻烦！
```

---

### 3、Show us your GitHub profile (给我们看看你的GitHub) ❌

**必填**: ❌ 不勾选（可选）

**描述** (复制粘贴):
```
For individual developers: We'll check your account age (>3 months) and activity. Don't worry if all your repos are private - we can still see your contribution graph 🟩

Enterprise users: You can skip this question.
```

**中文翻译**（理解用，不填入表单）:
```
个人开发者：我们会检查你的账号年龄(>3个月)和活跃度。别担心，即使你的仓库都是私密的，我们仍能看到你的贡献图 🟩

企业用户：可以跳过此问题。
```

---

### 4、How did you find us? (你怎么发现我们的？) ✅

**必填**: ✅ 勾选 `Required`

**描述**: 留空

**选项** (已在Step 2配置好，这里不用改):
- Reddit
- Discord  
- X
- Friend (朋友推荐)
- Other (其他)

---

### 5、Referral Code (推荐人/推荐码) ❌

**必填**: ❌ 不勾选（可选）

**描述** (复制粘贴):
```
If someone referred you to this program, enter their email address or referral code here. They'll get bonus credits when you join!

(Optional - leave blank if you found us yourself)
```

**中文翻译**（理解用，不填入表单）:
```
如果有人推荐你参加这个计划，请输入他们的邮箱地址或推荐码。你加入后他们会获得奖励积分！

(可选 - 如果是自己发现我们的可以留空)
```

---

### 6、What do you want to build? (你想做什么项目？) ✅

**必填**: ✅ 勾选 `Required`

**描述** (复制粘贴):
```
Tell us about your project idea. What problem does it solve? Who's it for? The more specific, the better we can help. (Aim for 50+ words - just a few sentences!)
```

**中文翻译**（理解用，不填入表单）:
```
告诉我们你的项目想法。它解决什么问题？给谁用的？越具体，我们越能帮到你。(目标50+字 - 就几句话！)
```

---

### 7、Have you shared stuff online before? (你之前在网上分享过东西吗？) ✅

**必填**: ✅ 勾选 `Required`

**描述**: 留空

**选项** (已在Step 2配置好):
- Yeah, I post regularly (是的，我经常发)
- Posted a few times (发过几次)
- Nope, but I'm down to try (没发过，但愿意试试)
- Rather not say (不想说)

---

### 8、Where would you like to share your experience? (你想在哪里分享体验？) ✅

**必填**: ✅ 勾选 `Required`

**描述** (复制粘贴):
```
Pick all that work for you - we're flexible!
```

**中文翻译**（理解用，不填入表单）:
```
选所有适合你的平台 - 我们很灵活！
```

**选项** (已在Step 2配置好):
- Reddit
- Dev.to
- Medium
- Personal Blog (个人博客)
- YouTube
- Other (其他)

---

### 9、Anything else we should know? (还有什么想告诉我们的吗？) ❌

**必填**: ❌ 不勾选（可选）

**描述** (复制粘贴):
```
Questions? Concerns? Cool side projects? We're all ears.
```

**中文翻译**（理解用，不填入表单）:
```
有问题？有顾虑？有酷项目？我们洗耳恭听。
```

---

### 10、Cool with the rules? (同意规则吗？) ✅

**必填**: ✅ 勾选 `Required`

**描述** (复制粘贴):
```
I'll share my real experience (good and bad) and follow the program rules. No BS, just honest feedback.
```

**中文翻译**（理解用，不填入表单）:
```
我会分享真实体验(好的和不好的)并遵守活动规则。不扯淡，只说实话。
```

---

### 隐藏后台字段

找到以下字段，点击右侧的眼睛图标隐藏：
- ❌ Status
- ❌ Applied Date

（这些仅用于你后台管理，用户不需要看到）

---

## 🎯 Step 5: 调整问题顺序

在Form编辑模式下，拖动问题调整为以下顺序：

```
0. Are you applying as an individual or a team?
1. Company Name
2. What should we call you?
3. Where should we send your Ultra Plan?
4. Show us your GitHub profile
5. How did you find us?
6. Referral Code
7. What do you want to build?
8. Have you shared stuff online before?
9. Where would you like to share your experience?
10. Anything else we should know?
11. Cool with the rules?
```

**注意**：
- 问题0应该是第一个问题，这样可以根据用户选择显示不同的后续问题
- 问题1（Company Name）和问题4（GitHub）都是可选的，企业/个人用户可以跳过不相关的问题
- 问题6（Referral Code）是可选的，有推荐人的填写，没有的可以留空

---

## 🚀 Step 6: 发布表单

### 6.1 获取分享链接
1. 点击Form右上角的 `Share`
2. 确保 `Allow editing` 是开启的
3. 点击 `Copy link`
4. 链接格式类似：`https://notion.so/xxxxx`

### 6.2 测试表单
1. 在无痕窗口打开复制的链接
2. 填写一次测试数据
3. 提交后检查Database中是否出现记录
4. 检查Status是否默认为空（你手动设置为Pending）

---

## ✅ Step 7: 创建管理视图（可选但推荐）

### 7.1 创建Board视图
1. 回到Table视图
2. 点击 `+ New view`
3. 选择 `Board`
4. View名称：`Review Board`
5. Group by 选择：`Status`
6. 点击 `Create`

现在你可以拖拽卡片来审核申请了（从Pending拖到Approved或Rejected）

### 7.2 创建Gallery视图（分析用）
1. 点击 `+ New view`
2. 选择 `Gallery`
3. View名称：`Channel Analysis`
4. Group by 选择：`Heard From`
5. 点击 `Create`

这样你可以看到每个渠道带来多少申请。

---

## 📋 最终检查清单

在发布前，确认以下事项：

- [ ] Form title 和 description 已填写
- [ ] 所有必填字段已标记 Required
- [ ] Status 和 Applied Date 已隐藏
- [ ] 问题描述已添加
- [ ] 测试提交成功
- [ ] 数据正确显示在Database中
- [ ] 复制了正确的分享链接

---

## 🔗 下一步

1. **集成到活动页**  
   把Form链接替换活动页中的 `[>>> 申请Ultra Plan <<<](#)` 

2. **准备邮件模板**  
   - 批准邮件
   - 拒绝邮件
   - 积分发放通知

3. **设置提醒**  
   在Notion中设置：有新申请时通过邮件/Slack通知

---

## 💡 使用技巧

### 快速审核
1. 打开 `Review Board` 视图
2. 点击卡片查看详情
3. 检查GitHub链接（点击打开）
4. 拖拽到 Approved 或 Rejected

### 批量操作
1. 在Table视图中勾选多个记录
2. 右键选择 `Edit property`
3. 选择 `Status` → `Approved`

### 导出数据
1. 点击右上角 `...`
2. 选择 `Export`
3. 选择格式：CSV / Markdown / PDF

---

## ❓ 常见问题

**Q: 表单链接打不开？**  
A: 检查分享设置是否开启了 `Allow editing`

**Q: 提交后看不到数据？**  
A: 刷新Database页面，或检查是否在其他视图中隐藏了

**Q: 可以修改已提交的数据吗？**  
A: 可以，直接在Database中编辑即可

**Q: 如何导出所有申请？**  
A: Database右上角 `...` → `Export` → 选择CSV格式

---

**创建时间**: 2026年3月6日  
**预计用时**: 15-20分钟  
**难度**: ⭐⭐☆☆☆（简单）

完成后记得把Form链接发给我，我帮你检查一下！
