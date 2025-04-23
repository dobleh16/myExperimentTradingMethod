# 📈 Binary Options Trading Guide GUI

This project is a **Python desktop application** built with **Tkinter**, designed to assist traders in identifying optimal entry points for binary options trading, either in upward (buy) or downward (sell) market conditions. The app provides clear guidelines and a LED-style teleprompter for continuous trading tips.

## 🧠 Features

- 💡 **Trading Guidance**: Learn when to enter a buy or sell trade based on technical indicators and market behavior.
- 🖥️ **GUI Interface**: Simple and user-friendly graphical interface to guide decision-making.
- 🕹️ **LED-style Message Display**: Displays rotating trading tips every 10 seconds.
- 📊 **Strategy Configuration**: Explains which indicators to use and how to configure them for best results.

---

## 🚀 How to Use

1. Run the application using Python.
2. Choose an option:
   - **"When to Buy?"** – Displays instructions for identifying an upward trend.
   - **"When to Sell?"** – Displays instructions for identifying a downward trend.
3. Click **"Show Information"** to view detailed strategy guidance.
4. Read continuous trading tips at the bottom of the interface.

---

## 📌 Strategy Rules

### For Buying:
- Candles must be **above** the moving average and **blue** (Heiken Ashi).
- Use the **second screen** (15-minute chart) for executing the trade.
- Enter when the **stochastic oscillator** moves from below to the top line.

### For Selling:
- Candles must be **below** the moving average and **red** (Heiken Ashi).
- Use the **second screen** (15-minute chart) for executing the trade.
- Enter when the **stochastic oscillator** moves from the top to the bottom line.

---

## ⚙️ Indicator Configuration

- **Candlestick Type**: Heiken Ashi  
- **Stochastic Oscillator**: 14,3,3  
- **Moving Averages**: 9, 14, 21 (Recommended: 21)

---

## 🔁 LED Message Tips

- Max 5 trades per day.
- Ideal timeframes: 1H and 15M.
- 15M screen is your execution chart.
- Stop after 2 consecutive losses.
- Avoid trading around news events.
- Don't trade in highly volatile markets.

---

## 🛠 Requirements

- Python 3.x  
- Tkinter (standard with Python)

To install dependencies (if needed):
```bash
pip install tk
```

---

## 🧑‍💻 Author

**Heiner Herrera**  
Contributions and feedback are welcome!
