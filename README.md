![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Blockchain](https://img.shields.io/badge/Data-On--Chain-orange?logo=bitcoin&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

# 🚀 Crypto On-Chain Data Pipeline

An automated pipeline that collects **real-time blockchain data** from the Blockchair API and analyzes on-chain activity to generate crypto market insights.

This project demonstrates how developers can build a simple **crypto analytics pipeline** using public blockchain data.

---

## ✨ Key Features

- 🐋 **Whale Tracking** — Detect large BTC transactions and exchange fund flows
- 🔥 **Mempool Analysis** — Monitor unconfirmed transactions and fee rates
- ⛏️ **Network Health** — Track hashrate, mining difficulty, blockchain stats
- 📊 **Delta Tracking** — Compare today's metrics vs. yesterday with % changes
- 🔄 **Automated** — Runs on schedule, zero manual intervention

---

## 📊 Data Source

Blockchain data is fetched directly from:

- **Blockchair API** — Bitcoin, Ethereum, and other chains: https://blockchair.com/api/docs#link_M3
- **Public blockchain datasets**

Example metrics collected:

- Transaction volume & network activity
- Mempool size & fee rates
- Hashrate & mining difficulty
- Large whale transactions

Example endpoint:

```
https://api.blockchair.com/bitcoin/stats
https://api.blockchair.com/ethereum/stats
https://api.blockchair.com/litecoin/stats
https://api.blockchair.com/bitcoin-cash/stats
https://api.blockchair.com/bitcoin/mempool/transactions
```

<details>
<summary>📋 Sample Response (click to expand)</summary>

```json
{
  "data": {
    "blocks": 888123,
    "transactions": 1025843912,
    "market_price_usd": 84250.50,
    "hashrate_24h": "725,000,000 TH/s",
    "difficulty": 113000000000000,
    "mempool_transactions": 42150,
    "average_transaction_fee_usd": 2.45
  }
}
```

</details>

---

## 🏗 System Architecture

```
Blockchair API
     ↓
Data Fetching
     ↓
Data Processing & Snapshot
     ↓
On-chain Analysis
     ↓
Insights / Reports
```

---

## 🛠 Tech Stack

- **Python 3.10+**
- `requests` — API data fetching
- `python-dotenv` — Environment config
- `pandas` — Data processing (optional)

---

## 📦 Installation

```bash
git clone https://github.com/Binhpham151412/crypto-onchain-data-pipeline.git
cd crypto-onchain-data-pipeline
pip install -r requirements.txt
```

---

## 📈 Example

```python
import requests

url = "https://api.blockchair.com/bitcoin/stats"
response = requests.get(url)
data = response.json()["data"]

print(f"BTC Price: ${data['market_price_usd']:,.2f}")
print(f"Hashrate: {data['hashrate_24h']}")
print(f"Mempool: {data['mempool_transactions']} txs")
```

---

## 📌 Project Goal

This repository demonstrates how to build an **on-chain data pipeline** using public blockchain APIs.

- ✅ Fetching real-time blockchain data
- ✅ Processing on-chain metrics
- ✅ Snapshot-based delta tracking
- ✅ Generating actionable insights

> 🔗 This is a simplified version of a larger private system that combines on-chain analysis with **AI-powered content generation**.

---

## ⚠️ Disclaimer

- This project is for **educational and research purposes only**.
- It is **not financial advice**.
- Always do your own research (DYOR) before making any investment decisions.

---

## 👨‍💻 Author

**Backend Developer** specializing in:

- 🔗 Blockchain data analytics & on-chain analysis
- 🤖 AI automation pipelines
- 📊 Crypto data engineering

> _Building tools that turn raw blockchain data into actionable insights._

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## ⭐ Support

If you find this project useful, feel free to ⭐ **star** the repository!

---

<p align="center">
  <b>Built with ❤️ for the crypto developer community</b>
</p>
