import streamlit as st

st.title("📊 Marketing Campaign Review")
st.write("Scroll down to interact with the campaign cards...")

# Add some spacing to simulate a long webpage
for _ in range(15):
    st.write("")

# 1. Initialize our memory vault (Session State)
if "likes_count" not in st.session_state:
    st.session_state.likes_count = 0

# 2. Create an isolated fragment so clicking doesn't reload the whole page
@st.fragment
def like_button_component():
    # This layout keeps the button and the number side-by-side
    col1, col2 = st.columns([1, 4])
    
    with col1:
        # Clicking this button ONLY re-runs this specific function!
        if st.button("❤️ Like"):
            st.session_state.likes_count += 1
            
    with col2:
        st.write(f"This campaign has **{st.session_state.likes_count}** likes!")

# 3. Call the component on your page
st.subheader("Campaign Alpha Draft Copy")
like_button_component()
