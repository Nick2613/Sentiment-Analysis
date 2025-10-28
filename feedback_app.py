import streamlit as st
import pandas as pd
from datetime import datetime
import io

# Page config
st.set_page_config(page_title="Feedback Form", layout="wide")

st.title("Feedback Collection Form")
st.markdown("Share your reviews below. Each submission will be added to the list, and you can download the entire collection as a CSV file.")

# Initialize session state
if 'feedbacks' not in st.session_state:
    st.session_state.feedbacks = []

# Feedback form
with st.form(key="feedback_form", clear_on_submit=True):
    st.subheader("Submit New Feedback")
    reviewer_name = st.text_input("Your Name (optional):")
    feedback_text = st.text_area("Your Review:", height=100, placeholder="Write your feedback here...")
    submitted = st.form_submit_button("Submit Feedback")

    if submitted and feedback_text.strip():
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_feedback = {
            'Timestamp': timestamp,
            'Reviewer Name': reviewer_name or 'Anonymous',
            'Feedback': feedback_text.strip()
        }
        st.session_state.feedbacks.append(new_feedback)
        st.success("Feedback submitted successfully!")

# Display feedbacks
if st.session_state.feedbacks:
    st.subheader("Submitted Feedbacks")
    df = pd.DataFrame(st.session_state.feedbacks)
    st.dataframe(df, use_container_width=True)

    # Download CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="Download Feedbacks as CSV",
        data=csv_buffer.getvalue(),
        file_name=f"feedbacks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )

    # Stats
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Submissions", len(st.session_state.feedbacks))
    with col2:
        avg_length = df['Feedback'].str.len().mean()
        st.metric("Avg Feedback Length", f"{avg_length:.0f} chars")
else:
    st.info("No feedbacks yet. Submit one above!")

# Instructions
with st.expander("How to Use"):
    st.markdown("""
    ### Setup
    1. Save this file as `feedback_app.py`
    2. Run: `streamlit run feedback_app.py`
    3. Open in browser (usually http://localhost:8501)

    ### Features
    - Submit feedback
    - See all entries
    - Download as CSV
    """)