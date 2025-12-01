## 🚀 Job Daily Agent  
**自动化求职岗位筛选系统（All-in-One Job Application Assistant）**

> 自动把今日推送到邮箱的招聘平台邮件筛选后
> 打分 + 增加简历修改建议，
> 生成岗位推荐邮件 + 每日9 p.m. 发送至邮箱。

🔗 **项目仓库**：`https://github.com/AAholdingACES-zhou/job-daily-agent-cron`  
🔗 **Workflow**：`https://www.coze.cn/work_flow?workflow_id=7578184743356874761&space_id=7578173564516696110`

---

### ⭐ 项目简介  

Job Daily Agent 是一个全自动求职助手，会在每天固定时间：

1. 从邮箱中抓取最近 24 小时的岗位推荐邮件（如智联、前程无忧等）
2. 用 LLM 解析邮件 HTML 文本，抽取结构化岗位信息(如岗位内容、地点、薪酬等）
3. 结合个人画像为每个岗位评估匹配度并打分
4. 生成一封包含「岗位列表 + 匹配度 + 推荐理由 + 简历修改建议」的日报邮件
5. 每日晚9点通过 SMTP 自动发送到我的个人邮箱

### 🔧 Workflow 重要结束节点

- **Coze Workflow**
  - 邮件抓取节点（IMAP）
  - 内容解析与清洗节点（代码块）
  - 岗位识别与结构化抽取（LLM）
  - 岗位匹配与打分（LLM + 规则）
  - 文本生成与邮件发送
    
- **GitHub Actions 定时触发**
  - 使用 `cron` 表达式实现每天定时调用 Coze Workflow
  - Action 日志与运行状态通过徽章展示

---

### 📈 系统结构
```
Job Daily Agent/
│
├── workflows/
│   └── job_daily_agent_main.json       # Coze Workflow 工作流
│
├── .github/
│   └── workflows/
│       └── cron.yml                    # GitHub Actions 定时任务
│
└── Overview_workflow.md

```

---

## Workflow展示


---

## 邮件输出结果（Sample-12-01手动触发）

<img width="842" height="372" alt="image" src="https://github.com/user-attachments/assets/307d3500-339c-4483-b1f0-12c712f7192b" />

<img width="1105" height="744" alt="image" src="https://github.com/user-attachments/assets/5a187894-9853-4e26-b410-4aead7572f74" />

