import streamlit as st
from analysis import (
    get_number_frequencies,
    top_n,
    bottom_n,
    estimate_probability,
    find_duplicate_draws,
)
from data_loader import load_powerball_data

st.title("🎯 Lottery Trend Analyzer")

df = load_powerball_data()
freqs = get_number_frequencies(df, ['num1','num2','num3','num4','num5'])

st.subheader("⚠️ Duplicate Winning Combinations")
dups = find_duplicate_draws(df)
if dups.empty:
    st.write("No full duplicate combinations detected.")
else:
    st.write("The following combinations occurred more than once:")
    st.dataframe(dups)

st.subheader("🔥 Hot and ❄️ Cold Numbers")
hot = top_n(freqs, 5)
cold = bottom_n(freqs, 5)
st.write(f"🔥 Hot Numbers: {hot}")
st.write(f"❄️ Cold Numbers: {cold}")

st.subheader("📊 Your Numbers Probability Estimate")
user_input = st.text_input("Enter your 5 numbers (comma-separated):", "5, 8, 15, 22, 30")
if user_input:
    try:
        numbers = list(map(int, user_input.split(",")))
        prob = estimate_probability(numbers, freqs)
        st.write(f"📈 Estimated Trend Score: {prob:.2%}")
    except ValueError:
        st.error("Please enter valid numbers.")
