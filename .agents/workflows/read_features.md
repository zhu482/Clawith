---
description: Read the Clawith feature specification at the start of every session
---

# Read Feature Spec

At the start of every conversation about Clawith, always read the full feature specification document first before doing any work. This ensures you are aware of all existing functionality and won't break or duplicate it when adding new features.

// turbo
1. Read the feature specification:
```
cat /Users/ray/Documents/antigravity/Clawith/FEATURES.md
```

2. Confirm you have read and understood the full feature spec, then ask the user what they would like to work on.

## After Implementing New Features

After completing any feature addition or modification, **always update FEATURES.md**:
- Add/modify the relevant section describing the new feature
- Add a row to the "更新记录" table at the bottom with today's date and a brief summary
- Keep descriptions concise but complete enough to understand what was built and why
