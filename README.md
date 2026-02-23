# 🇮🇳 Autonomous PLI Alpha Generator

[![CI](https://github.com/harshi1111/pli-alpha-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/harshi1111/pli-alpha-generator/actions/workflows/ci.yml)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A quant analysis system that identifies **information asymmetry** in Indian manufacturing stocks by combining live market data with LLM-powered supply chain intelligence.

## 🎯 What It Does

- **Live Data Fetching**: Real-time prices from Yahoo Finance
- **News Analysis**: Latest PLI scheme updates from NewsAPI
- **Expert Intelligence**: Incorporates Gemini/Claude analysis
- **Risk Detection**: Flags hidden risks (Chinese JVs, high debt)
- **Stealth Ranking**: Identifies institutional accumulation
- **Buy Triggers**: Dynamic levels based on 52-week technicals

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/pli-alpha-generator.git
cd pli-alpha-generator

# Install dependencies
pip install -r requirements.txt

# Set up API keys
cp .env.example .env
# Edit .env with your NewsAPI key

# Run analysis
python src/dynamic_pli_analyzer.py
```
## 📊 Sample Output (Feb 23, 2026)

🎯 HIGHEST ASYMMETRY OPPORTUNITY
TCI Express Limited (TCIEXP)
Price: ₹554.20
Buy Trigger: ₹487.56
Target: ₹848.00
Risk/Reward: 6.96:1

## Architecture

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Yahoo      │    │  NewsAPI    │    │  Gemini     │
│  Finance    │    │             │    │  (Manual)   │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │
       └──────────────────┼──────────────────┘
                          ▼
              ┌─────────────────────┐
              │  PLI Alpha Engine   │
              │  (Python + pandas)  │
              └─────────────────────┘
                          │
                          ▼
              ┌─────────────────────┐
              │  Analysis Reports   │
              │  + Buy Triggers     │
              └─────────────────────┘

## 🔄 CI/CD Pipeline
- Automated testing on every push
- Weekly scheduled runs via GitHub Actions
- Artifact storage for historical tracking
- Code quality checks (black, flake8)

## 📈 Track Record

| Date | Pick | Entry | Target | Status |
|------|------|-------|--------|--------|
| 2026-02-23 | TCIEXP | ₹554 | ₹848 | Active |




## 🎯 Current Top Pick (February 23, 2026)

**TCI Express Limited (TCIEXP)**
- Price: ₹554.20
- Buy Trigger: ₹487.56
- Target: ₹848.00
- Asymmetry Score: 7/10

## 📊 Latest Analysis

<!-- TIMESTAMP_START -->
Last Updated: February 23, 2026 at 12:09 IST
<!-- TIMESTAMP_END -->

## 🚀  Test It Locally
powershell
# Run analysis and save JSON
python src/dynamic_pli_analyzer.py

# Update README with results
python scripts/update_readme.py

# Check the updated README
cat README.md

## 🤝 Contributing
Contributions welcome! Please read CONTRIBUTING.md

## 📄 License
MIT License - use for learning, modify for your needs!

## ⚠️ Disclaimer
For educational purposes only. Not investment advice.

" " 
