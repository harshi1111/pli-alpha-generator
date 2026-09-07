# 🇮🇳 PLI Alpha Generator

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A learning project to understand GitHub Actions, APIs, and automation. It scans Indian manufacturing companies every Monday, looks for price dislocations, and updates this README automatically. Uses PLI stocks as a dataset because they're interesting and have good data availability.

## What it tracks

- **PLI beneficiaries** - Dixon, Syrma, Amber, TCI Express, Blue Dart
- **Asymmetry signals** - Near 52-week lows + institutional stealth accumulation
- **Hidden risks** - Chinese JV exposure, high debt, extreme valuations
- **Buy triggers** - 2% above 52-week low with 6:1+ risk/reward

## How it works

Runs every Monday 9:30 AM IST via GitHub Actions. Fetches live data from Yahoo Finance, applies expert validation from Feb 2026 Gemini analysis, and spits out a JSON report + updated README.

## Running this yourself

```bash
# Clone it
git clone https://github.com/harshi1111/pli-alpha-generator.git
cd pli-alpha-generator

# Install stuff
pip install -r requirements.txt

# Add your NewsAPI key (free from newsapi.org)
cp .env.example .env
# Edit .env file

# Run
python src/dynamic_pli_analyzer.py
```
## Architecture
```
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
```


## 📈 Track Record

| Date | Pick | Entry | Target | Status |
|------|------|-------|--------|--------|
| 2026-07-06 | SYRMA | ₹1402 | ₹1518 | Active |
| 2026-07-13 | SYRMA | ₹1432 | ₹1518 | Active |
| 2026-07-20 | BLUEDART | ₹4899 | ₹7036 | Active |
| 2026-07-27 | BLUEDART | ₹5037 | ₹7036 | Active |
| 2026-08-03 | SYRMA | ₹1369 | ₹1518 | Active |
| 2026-08-10 | SYRMA | ₹1493 | ₹1518 | Active |
| 2026-08-17 | SYRMA | ₹1497 | ₹1543 | Active |
| 2026-08-24 | SYRMA | ₹1454 | ₹1543 | Active |
| 2026-08-31 | SYRMA | ₹1437 | ₹1543 | Active |
| 2026-09-07 | SYRMA | ₹1618 | ₹1626 | Active |



## Current Top Pick (February 23, 2026)

**TCI Express Limited (TCIEXP)**
- Price: ₹554.20
- Buy Trigger: ₹487.56
- Target: ₹848.00
- Asymmetry Score: 7/10

## Latest Analysis

<!-- TIMESTAMP_START -->
Last Updated: September 07, 2026 at 08:52 IST
<!-- TIMESTAMP_END -->

## Contributing
Contributions welcome! Please read CONTRIBUTING.md

## License
MIT License - use for learning, modify for your needs!

## ⚠️ Disclaimer
For educational purposes only. Not investment advice.

