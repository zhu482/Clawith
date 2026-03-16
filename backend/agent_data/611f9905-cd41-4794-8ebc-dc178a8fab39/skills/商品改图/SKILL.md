---
name: product-restyle
description: 得物/小红书商品改图专家。将专业影棚商品图转换为素人生图风格，支持多角度分析和AI生成。
version: 2.0.0
trigger_keywords: ["商品改图", "改图", "商品图", "得物", "素人图", "生图", "商品拍摄"]
---

# 得物/小红书商品改图 (Product Restyle)

此技能专注于将高度精致、影棚感的商品图转换为极具真实感、符合国内小红书/得物社区审美（素人感、生图感）的生活化照片。**支持各类非标品与标品（如：鞋靴、箱包、服饰、香水、数码配件等）。**

## 核心原则

1. **绝对真实感**：模仿普通人使用 iPhone 直出的样片，拒绝单反感、拒绝影棚感、拒绝刻意的虚化，拒绝刻意的构图。
2. **自然亮堂光效**：**严禁低矮暗光或阴沉氛围**。模拟明亮的室内自然光（窗光）或均匀的家庭照明，确保商品细节清晰可见，色调通透自然。
3. **场景国产化**：环境必须限定在中国（国内）家庭室内或城市户外。
4. **细节一致性**：必须精准分析商品的纹理、Logo、配色及核心特征，确保改图后的实物细节与原图完全一致。
5. **宏观与微观兼顾**：全套图中必须包含至少一张“细节放大图”，展示材质微观质感（如走线、皮纹）。
6. **去技术化构图**：模仿非专业人士的视角，支持俯拍、随手的倾斜构图。

## 标准作业流程 (Standard Operating Procedure - SOP)

无论是 CLI 还是对话模式，必须严格执行以下 **3步核心法则**。严禁跳过分析直接生成！

### 第一步：输入图原子级分析 (Reference Analysis)
**你必须“看懂”每一张图，才能“改好”每一张图。**

对用户提供的每一张输入图片，进行原子级拆解：
1.  **视觉内容识别**：这是什么？（例如：银色手提包/复古跑鞋/透明香水瓶）。
2.  **角度判定**：这是什么视角？（正面/侧面/45度/背部/俯拍/内部）。
3.  **细节提取**：有哪些不可丢失的关键特征？（金属扣件、皮料纹理、丝印Logo、拼接缝线）。
4.  **文件映射**：给每张图打上标签（如 `Ref_A: Front`, `Ref_B: Side`）。

**💻 CLI 模式推荐流程**：
使用 `analyze.py` 进行交互式分析，自动生成分析报告：
```bash
python3 .agent/skills/06-工作辅助/商品改图/scripts/analyze.py \
  --project "项目名称" \
  --input 参考图1.jpg 参考图2.jpg 参考图3.jpg
```
执行后会：
- 在 `~/Desktop/文章/商品图/[项目名称]/` 创建项目目录
- 生成 `analysis_report.md` 记录所有分析结果
- 后续生成时使用 `--project` 参数，图片自动保存到项目目录

### 第二步：视觉策略与参考分配 (Visual Strategy & Allocation)
**思考是生成的灵魂。细节的准确性取决于此步骤的分配逻辑。**

基于第一步的分析，制定生成方案：
1.  **场景逻辑构建**：
    *   根据商品属性，确定最合理的“素人拍摄场景”。
        *   **鞋靴/大件** -> 地毯、木地板、水泥地。
        *   **包袋/配饰/香水** -> 桌面、床单、窗台、手持(Hand-held)。
    *   设定光影氛围（冷白光/暖黄光/闪光灯）。
    *   **⚠️ 场景一致性铁律**：**同一组图片（5张）必须使用完全相同的场景设定**。
        *   如果第1张选择了"深灰色地毯 + 冷白光"，那么第2-5张必须全部使用"深灰色地毯 + 冷白光"。
        *   **严禁出现**：第1张地毯、第2张木地板、第3张桌面这种场景跳跃。
        *   在 Prompt 中必须明确标注 `SAME [surface] background` 或 `on the SAME grey carpet`。
2.  **参考图精准分配 (Key Reference Mapping) ⚠️重要**：
    *   **强制要求**：**每张生成图必须使用至少 3 张参考图**。严禁单图参考！
        *   即使生成"正面图"，也必须同时输入正面、侧面、细节等多角度参考，让 AI 综合理解产品结构。
        *   单图参考会导致细节丢失、结构变形。
    *   **映射表制定**：
        *   生成 **正面/主视图** -> 使用 **正面 + 侧面 + 细节** (Ref_A + Ref_B + Ref_C)。
        *   生成 **侧面/结构图** -> 使用 **侧面 + 正面 + 后跟** (Ref_B + Ref_A + Ref_C)。
        *   生成 **细节/材质图** -> 使用 **细节 + 正面 + 侧面** (Ref_C + Ref_A + Ref_B)。
        *   生成 **全景图** -> 使用 **所有参考图** (Ref_A + Ref_B + Ref_C + ...)。

### 第三步：高精度执行 (High-Precision Execution)
根据策略表，分批次、精准调用工具生成。
- 确保 Prompt 准确描述了第二步设定的场景和光影。
- 确保 `--input` 参数严格遵循“参考图这一分配”。
- **强制场景一致性**：在每一张图的 Prompt 中明确使用 `on the SAME [surface]` 或 `consistent scene`。
- 确保风格词 (`raw photo`, `amateur shot`) 始终在线。

- **可选网感升级**：如需提升"网感"，加入 `white shoebox`, `natural window light`, `blurred background` 等关键词。
---

## 技术细节参考 (Technical Reference)

### 1. 场景库 (Scenario Library)

#### A. 居家地面 (Authentic Floor) - *适用于鞋靴、大包、电器*
- **素色地毯 (Plain Carpet)**：深灰、米白或浅驼色地毯。纹理可以是圈绒或短毛。
- **木地板/瓷砖 (Wood/Tile)**：国内常见的暖色木地板或米白瓷砖。
- **核心要义**：**不要放垃圾**。依靠材质本身的纹理和自然的光影来体现真实感。

#### B. 生活桌面 (Lifestyle Desk) - *适用于香水、首饰、小包、3C*
- **书桌/化妆台**：白色或木纹桌面。
- **床品 (Embed)**：随手放在略带褶皱的床单或沙发上（营造慵懒感）。
- **光线**：更倾向于自然光（窗边）或台灯下的聚焦光。

### 2. “去构图化”的视觉逻辑
- **拒绝“摆拍感”**：位置不要太整齐，允许微歪。
- **角度选择**：
    - **俯视 (Top-Down)**：适合展示整体轮廓。
    - **平视 (Eye-Level)**：适合展示侧面结构。
    - **手持 (In-Hand)**：适合展示大小比例（注意手部尽量虚化或只露局部，避免恐怖谷）。

### 3. "网感真实"升级指南 (Internet Vibe Upgrade) ⭐ 新增
基于小红书/得物高赞晒单的视觉特征，以下元素可以让图片更具"网感"同时保持真实：

#### 3.1 开箱仪式感 (Unboxing Ritual)
- **核心道具**：**白色鞋盒 + 薄纸 (Tissue Paper)**。
- **摆放逻辑**：
    - 鞋子不是直接放地上，而是**放在鞋盒上**或**斜靠鞋盒**。
    - 薄纸呈**半展开、随意揉皱**状态（不是整齐叠放）。
- **心理暗示**："我刚拿到货，迫不及待拍给你看"。
- **Prompt 关键词**：`white shoebox`, `crumpled tissue paper`, `unboxing moment`, `product placed on box`.

#### 3.2 自然光 + 暖色调 (Natural Warm Light)
- **光源**：**自然窗光 + 室内暖白光混合**。严禁偏暗、阴冷或对比度过高的暗调风格。
- **亮度和色调**：画面背景要明亮、干净，色温 4000K 左右（中性偏微暖），像是在采光良好的卧室或客厅拍摄。
- **阴影**：**极淡、扩散性强的柔和阴影**。
- **拍摄时间感**：模拟上午 10 点或下午 2 点的充沛自然光。
- **Prompt 关键词**：`bright natural window light`, `well-lit room`, `airy atmosphere`, `soft natural shadows`.

#### 3.3 细节放大微距 (Macro & Detail Focus) ⭐ 新增
- **目的**：通过“怼脸拍”建立极致信任。
- **拍摄手法**：镜头距离商品 5-10cm，聚焦在核心 Logo、拉链、缝线或材质纹理上。
- **构图**：商品局部占据画面 70% 以上，背景自然虚化（模拟手机微距模式的散景）。
- **Prompt 关键词**：`extreme macro shot`, `macro photography mode`, `shot on iPhone macro`, `focus on texture`, `hyper-detailed stitching`.

#### 3.3 环境层次感 (Layered Background)
- **前景**：地毯/地板（清晰）。
- **中景**：鞋盒、薄纸（半清晰）。
- **背景**：床脚、窗帘、木地板等**模糊的生活元素**（营造空间纵深）。
- **核心**：不是纯色背景，而是"能看出这是在家里拍的"。
- **Prompt 关键词**：`blurred bedroom background`, `wooden floor in distance`, `curtain visible in background`, `depth of field`.

#### 3.4 构图的"随意精致" (Casual but Composed)
- **摆放**：鞋子**略微倾斜**或**一只靠在盒子上**（不是完全对称）。
- **视觉效果**：看起来是"随手摆的"，但恰好展示了关键角度。
- **Prompt 关键词**：`casually placed`, `slightly tilted`, `leaning against box`.

### 4. 视觉诱惑点 (Visual Hooks)
- **材质锐度**：强调 `high contrast texture`, `sharp focus`.
- **光线色温**：**优先自然暖光**（网感升级），其次冷白光（硬核验货风）。
- **品质锚点**：背景越简单，越能说明商品原本就很强。

## 标准5图组合策略 (Standard 5-Image Set)

这套组合适用于绝大多数商品，确保全方位无死角展示。

1.  **图1：开箱全景 (The Arrival / Overview)**
    *   **内容**：商品全貌 + 极简环境。
    *   **目的**：第一眼吸引，展示“刚拿到手”的状态。
2.  **图2：正面定妆 (Front / Main View)**
    *   **内容**：最标志性的正面或主视角。
    *   **目的**：验证颜值，确认款式。
3.  **图3：侧面/结构 (Side / Profile)**
    *   **内容**：侧面线条、厚度、结构层次。
    *   **目的**：展示立体感和版型。
4.  **图4：材质特写 (Texture / Macro)**
    *   **内容**：把镜头怼到材质表面（皮纹、织物、金属光泽）。
    *   **目的**：建立对品质的信任。
5.  **图5：功能/背部细节 (Function / Back)**
    *   **内容**：拉链、扣件、背部设计、内部结构或底部。
    *   **目的**：补充信息，完整体验。

## 使用示例

### 完整工作流程 (Complete Workflow)

#### Step 1: 分析参考图并生成报告
```bash
# 进入项目目录
cd ~/Desktop/文章

# 运行分析工具（交互式）
python3 .agent/skills/06-工作辅助/商品改图/scripts/analyze.py \
  --project "kappa_silver_sneakers" \
  --input 图片测试/67f21bf4b39fa3e121dbb8e37d4317c0.jpg \
          图片测试/微信图片_20260208205249_23960_6.jpg \
          图片测试/微信图片_20260208205249_23957_6.jpg
```

**交互式输入示例**:
```
📸 参考图 1/3: 67f21bf4b39fa3e121dbb8e37d4317c0.jpg
  角度: 正面俯视
  关键细节: 双层鞋带系统、鞋舌Logo、银色反光材质
  标签: Ref_A, Front, Main

📸 参考图 2/3: 微信图片_20260208205249_23960_6.jpg
  角度: 侧面
  关键细节: 厚底波浪结构、侧面TPU支撑条、Kappa Logo
  标签: Ref_B, Side, Profile

📸 参考图 3/3: 微信图片_20260208205249_23957_6.jpg
  角度: 后跟
  关键细节: 后跟包裹结构、提环、后跟Logo
  标签: Ref_C, Heel, Back

🎬 场景设定
  表面: 深灰色地毯
  光线: 自然窗光+暖黄光
  氛围: 网感开箱
```

执行后会生成：
- `~/Desktop/文章/商品图/kappa_silver_sneakers/analysis_report.md`

#### Step 2: 基于分析报告生成图片

**方式A: 使用 restyle.py（推荐）**
```bash
# 图1: 开箱全景（使用 Ref_A + Ref_B）
python3 .agent/skills/06-工作辅助/商品改图/scripts/restyle.py \
  --project "kappa_silver_sneakers" \
  --input 图片测试/67f21bf4b39fa3e121dbb8e37d4317c0.jpg \
          图片测试/微信图片_20260208205249_23960_6.jpg \
  --output "01_arrival.jpg" \
  --scene indoor \
  --prompt "Top-down view of Kappa silver metallic chunky sneakers on SAME grey carpet, white shoebox visible, crumpled tissue paper, natural window light, warm afternoon sunlight"

# 图2: 正面（仅使用 Ref_A）
python3 .agent/skills/06-工作辅助/商品改图/scripts/restyle.py \
  --project "kappa_silver_sneakers" \
  --input 图片测试/67f21bf4b39fa3e121dbb8e37d4317c0.jpg \
  --output "02_front.jpg" \
  --scene indoor \
  --prompt "Front view of Kappa silver metallic sneakers, symmetrical placement, on SAME grey carpet, showing complex lacing system"

# 图3: 侧面（仅使用 Ref_B）
python3 .agent/skills/06-工作辅助/商品改图/scripts/restyle.py \
  --project "kappa_silver_sneakers" \
  --input 图片测试/微信图片_20260208205249_23960_6.jpg \
  --output "03_side.jpg" \
  --scene indoor \
  --prompt "Side profile of single silver metallic chunky sneaker on SAME grey carpet, low angle, emphasizing thick sole"

# 图4: 材质特写（使用 Ref_B）
python3 .agent/skills/06-工作辅助/商品改图/scripts/restyle.py \
  --project "kappa_silver_sneakers" \
  --input 图片测试/微信图片_20260208205249_23960_6.jpg \
  --output "04_macro.jpg" \
  --scene indoor \
  --prompt "Extreme close-up of silver metallic texture and white mesh, sharp focus on materials, on SAME grey carpet"

# 图5: 后跟细节（仅使用 Ref_C）
python3 .agent/skills/06-工作辅助/商品改图/scripts/restyle.py \
  --project "kappa_silver_sneakers" \
  --input 图片测试/微信图片_20260208205249_23957_6.jpg \
  --output "05_heel.jpg" \
  --scene indoor \
  --prompt "Close-up of heel and back, showing sole width and rear design, on SAME grey carpet"
```

所有生成的图片会自动保存到：
`~/Desktop/文章/商品图/kappa_silver_sneakers/`

并且每次生成都会自动更新 `analysis_report.md`，记录：
- 使用的参考图
- 完整的 Prompt
- 生成时间

#### Step 3: 查看分析报告
```bash
cat ~/Desktop/文章/商品图/kappa_silver_sneakers/analysis_report.md
```

报告示例：
```markdown
# 商品改图分析报告

**项目名称**: kappa_silver_sneakers
**创建时间**: 2026-02-08T23:42:00
**输出目录**: `~/Desktop/文章/商品图/kappa_silver_sneakers`

---

## 📸 参考图分析 (Reference Analysis)

### Ref_A: `67f21bf4b39fa3e121dbb8e37d4317c0.jpg`
- **角度**: 正面俯视
- **细节**: 双层鞋带系统、鞋舌Logo、银色反光材质
- **标签**: Ref_A, Front, Main

### Ref_B: `微信图片_20260208205249_23960_6.jpg`
- **角度**: 侧面
- **细节**: 厚底波浪结构、侧面TPU支撑条、Kappa Logo
- **标签**: Ref_B, Side, Profile

---

## 🎬 场景设定 (Scene Setting)
- **表面**: 深灰色地毯
- **光线**: 自然窗光+暖黄光
- **氛围**: 网感开箱

---

## 🖼️ 生成任务 (Generation Tasks)

### 1. 01_arrival
- **参考图**: 67f21bf4b39fa3e121dbb8e37d4317c0.jpg, 微信图片_20260208205249_23960_6.jpg
- **提示词**:
\`\`\`
Top-down view of Kappa silver metallic chunky sneakers on SAME grey carpet...
\`\`\`
- **输出文件**: `01_arrival.jpg`
- **生成时间**: 2026-02-08T23:45:00
```
