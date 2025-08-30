import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("DOGE Investment Profit/Loss Predictor")

# Inputs
investment = st.number_input("Enter your investment amount (USD):", min_value=1.0, step=1.0)
buy_price = st.number_input("Enter your DOGE buy price (USD):", min_value=0.01, step=0.01)

future_prices = st.text_input("Enter possible DOGE prices for 2025 (comma-separated)", "0.60,1.00,0.25,0.40,0.15,0.07")

if st.button("Predict"):
    scenarios = [float(p.strip()) for p in future_prices.split(",") if p.strip() != ""]
    coins = investment / buy_price

    results = []
    for price in scenarios:
        value = coins * price
        profit_loss = value - investment
        results.append({
            "Price (USD)": price,
            "Value (USD)": round(value, 2),
            "Profit/Loss (USD)": round(profit_loss, 2)
        })

    df = pd.DataFrame(results)
    st.write("### Results", df)

    # Visualization
    fig, ax = plt.subplots()
    ax.bar([str(p) for p in df["Price (USD)"]],
           df["Profit/Loss (USD)"],
           color=['red' if x < 0 else 'green' for x in df["Profit/Loss (USD)"]])
    ax.axhline(0, color='black', linewidth=0.8)
    ax.set_title("Profit/Loss at Different DOGE Prices")
    ax.set_xlabel("DOGE Price (USD)")
    ax.set_ylabel("Profit/Loss (USD)")
    st.pyplot(fig)
