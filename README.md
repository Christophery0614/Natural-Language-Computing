# 🎓 Academic Assistant Chatbot  学术助手聊天机器人

TP2633 Finla Project — Natural Language Computing

A hybrid rule-based + generative model chatbot for students, researchers, and self-learners.

一个面向学生、研究者与自学者的学术问答聊天机器人，采用「规则匹配+生成式模型」混合架构

---

## 📖 Overview

This project addresses the challenges of information access and high communication costs in academic settings. Students often struggle to understand complex theories, solve assignments, or find research materials, and traditional solutions (books, literature, consulting teachers) are time-consuming. This chatbot offers a convenient, efficient way to get academic guidance anytime, anywhere through simple conversation.

**Domain:** Natural sciences, social sciences, engineering technology  
**Target users:** Undergraduates, graduates, researchers, self-learners

---

## 🏗️ Architecture

A hybrid architecture combining rule-based systems with machine learning models. Highly regular questions (basic concept explanations, common questions) are answered quickly and accurately via preset rules; complex, variable questions (specific research topics, in-depth theoretical analysis) are handled by a generative language model.

### Pipeline

1. **Data Preprocessing**: `download_data.py` downloads conversation data from Hugging Face, filters for academic relevance via keyword matching, limits turn count, and saves the result as `academic_persona_chat.json`.

2. **Intent Classification**: The `get_intent` method in the `Bot` class matches user input against preset intent examples via keyword/phrase matching (e.g., "ask_question").

3. **Response Generation**:
   - Matched intent → randomly select from preset reply templates (adds variety)
   - No match → fall back to DialoGPT generation, then clean/format the output

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| ML Model | DialoGPT (`microsoft/DialoGPT-small`), via Transformers `AutoModelForCausalLM` / `AutoTokenizer` |
| Data | Hugging Face `datasets` library |
| Intent Config | `intents.yaml` |

---

## 📁 Directory Structure

```
.
├── index.html                    # Frontend UI
├── routes.py                     # Flask routes
├── download_data.py              # Data download & filtering
├── model.py                      # DialoGPT loading & inference
├── train.py                      # Training script
├── run.py                        # App entry point
├── intents.yaml                  # Preset intents & rules
└── academic_persona_chat.json    # Preprocessed dataset
```

---

## ✨ Key Features

- Hybrid response strategy — rule matching first (`get_intent` / `get_reply`), DialoGPT fallback
- Custom `ChatData` dataset class for conversation handling
- Text cleaning and preprocessing (`clean_text`)
- Configurable training and generation parameters

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install flask transformers datasets torch

# Download & preprocess data
python download_data.py

# (Optional) Train / fine-tune the model
python train.py

# Run the app
python run.py
```

After startup, visit the local server address to chat with the bot via the web interface.

---

## 📊 Evaluation

| Metric | Result |
|---|---|
| Preset intent accuracy | >90% |
| Model-generated accuracy | ~70% |
| User satisfaction | High for common questions; less precise on complex ones |

---

## 🔭 Limitations & Future Work

- Limited intent coverage → plan to expand intents and preset responses
- Generation quality → plan larger datasets, transfer/reinforcement learning
- Single-language support → plan multilingual support
- No feedback loop → plan a user feedback mechanism
- Weak context handling → plan improved multi-turn context understanding

---

## 🙏 Acknowledgements

- [microsoft/DialoGPT](https://github.com/microsoft/DialoGPT) — Dialogue generation pretrained model
- [huggingface/transformers](https://github.com/huggingface/transformers) — Model loading & usage

---

---

## 🇨🇳 中文版本

## 📖 项目简介

本项目旨在解决学术领域信息获取难、沟通成本高的问题。用户在学习与研究过程中常需要理解复杂理论、解决作业问题或查找研究资料，传统方式往往耗时费力。本聊天机器人通过简单对话，随时随地为用户提供便捷高效的学术解答。

**应用领域：** 自然科学、社会科学、工程技术  
**目标用户：** 本科生、研究生、研究人员及学术自学者

---

## 🏗️ 系统架构

采用**规则系统 + 机器学习模型**的混合架构。常规性问题（基础概念解释、常见问答）通过预设规则快速准确地回答；复杂多变的问题（特定研究话题讨论、复杂理论深入分析）借助生成式语言模型处理。

### 处理流程

1. **数据预处理**：使用 `download_data.py` 从 Hugging Face 数据集库下载对话数据，通过预定义学术关键词筛选出学术相关内容，并限制对话轮数以保证简洁聚焦，最终保存为 `academic_persona_chat.json`。

2. **意图分类**：`Bot` 类中的 `get_intent` 方法通过关键词/短语匹配，将用户输入归类到预设意图（如 `ask_question`）。

3. **响应生成**：
   - 若命中预设意图 → 从对应模板中随机选取回复（增加多样性）
   - 若未命中 → 调用 DialoGPT 模型生成回复，并进行清洗与格式化

---

## 🛠️ 技术栈

| 类别 | 技术/工具 |
|---|---|
| 前端 | HTML, CSS, JavaScript |
| 后端 | Python, Flask |
| 机器学习模型 | DialoGPT (`microsoft/DialoGPT-small`)，通过 Transformers `AutoModelForCausalLM` / `AutoTokenizer` |
| 数据处理 | Hugging Face `datasets` 库 |
| 意图配置 | `intents.yaml` |

---

## 📁 目录结构

```
.
├── index.html                    # 前端页面（用户输入与展示回复界面）
├── routes.py                     # Flask 路由，处理用户请求与响应
├── download_data.py              # 从 Hugging Face 下载并筛选学术对话数据
├── model.py                      # 模型加载与推理逻辑
├── train.py                      # 模型训练脚本
├── run.py                        # 应用启动入口
├── intents.yaml                  # 预设意图与规则配置
└── academic_persona_chat.json    # 预处理后的学术对话数据集
```

---

## ✨ 主要功能特性

- 混合式响应策略：优先规则匹配，未命中时回退至 DialoGPT 生成
- 自定义 `ChatData` 数据集类，用于处理对话数据
- 文本清洗与预处理（`clean_text`）
- 可配置的训练参数与生成参数

---

## 🚀 快速开始

```bash
# 安装依赖
pip install flask transformers datasets torch

# 下载并预处理数据
python download_data.py

# （可选）训练/微调模型
python train.py

# 启动应用
python run.py
```

启动后访问本地服务地址，即可在网页界面中与聊天机器人对话。

---

## 📊 评估结果

| 指标 | 结果 |
|---|---|
| 预设意图响应准确率 | >90% |
| 模型生成响应准确率 | ~70% |
| 用户满意度 | 对常见学术问题满意度高；复杂问题回答有时不够精确详尽 |

---

## 🔭 已知局限与未来工作

- 意图覆盖有限 → 计划扩展意图与预设回复，覆盖更多学术场景
- 模型生成质量 → 计划采用更大规模数据集及迁移学习、强化学习等技术改进训练
- 语言支持单一 → 计划扩展多语言支持
- 缺少反馈机制 → 计划加入用户反馈功能，根据反馈自动优化回复
- 上下文理解不足 → 计划改进多轮对话与复杂情境下的上下文理解能力

---

## 🙏 致谢与参考

- [microsoft/DialoGPT](https://github.com/microsoft/DialoGPT) — 对话生成预训练模型
- [huggingface/transformers](https://github.com/huggingface/transformers) — 模型加载与使用

---
*This README is based on the TP2633 course project report.*
*本 README 基于 TP2633 课程项目报告整理而成。*
