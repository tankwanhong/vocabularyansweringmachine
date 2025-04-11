# app.py

import streamlit as st
import subprocess

st.set_page_config(page_title="Vocabulary Spelling Bot", layout="centered")

st.title("🧠 Vocabulary Spelling Bee Bot")
st.markdown("This app launches a local bot that listens to the spelling word, transcribes it using Whisper, and submits the answer.")

if st.button("🚀 Start Bot"):
    st.success("Bot started! Watch your local browser.")
    subprocess.Popen(["python", "spelling_bot.py"])

if st.button("❌ Stop Bot"):
    st.warning("To stop the bot, please press CTRL+C in your terminal window or close the Chrome window manually.")
