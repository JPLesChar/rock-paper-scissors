import random

import streamlit as st

st.title("✊✋✌ Rock Paper Scissors")

moves = ("✊ Rock", "✋ Paper", "✌ Scissors")
player_choice = st.radio("Choose your move:", moves)

if st.button("Play"):
    computer_choice = random.choice(moves)
    st.session_state["round"] = (player_choice, computer_choice)

if "round" in st.session_state:
    played_choice, computer_choice = st.session_state["round"]
    st.write(f"You chose {played_choice}")
    st.write(f"Computer chose {computer_choice}")

    if played_choice == computer_choice:
        st.write("It's a tie!")
    elif (
        (played_choice == "✊ Rock" and computer_choice == "✌ Scissors")
        or (played_choice == "✋ Paper" and computer_choice == "✊ Rock")
        or (played_choice == "✌ Scissors" and computer_choice == "✋ Paper")
    ):
        st.write("You win!")
    else:
        st.write("Computer wins!")
