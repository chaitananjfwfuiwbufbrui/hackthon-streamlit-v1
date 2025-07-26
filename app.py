import streamlit as st

st.set_page_config(page_title="AI Content Generator", layout="wide")
st.title("AI Content Generator")
st.markdown("""
<style>
.bg-box {
    background: #f9fafb;
    box-shadow: 0 1px 6px rgba(30,41,59,0.08);
    border-radius: 14px;
    padding: 32px 28px 24px 28px;
    margin-bottom: 14px;
    display: flex;
    flex-direction: column;
}
.grid-2 {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 28px;
}
@media (max-width: 900px) {
  .grid-2 { grid-template-columns: 1fr; }
}
.section-title {
    font-weight: 700;
    font-size: 22px;
    margin-bottom: 10px;
}
.label {
    font-size: 15px;
    color: #718096;
    margin-bottom: 3px;
}
.protips, .features {
    background: #eaf2fb;
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 10px;
}
.features-title { font-weight:700; font-size:17px; margin-bottom: 7px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="grid-2">', unsafe_allow_html=True)
# -- LEFT COLUMN --
st.markdown('<div>', unsafe_allow_html=True)
s1, s2 = st.columns([0.6, 0.4])
with s1:
    with st.container():
        st.markdown('<div class="section-title">Generate Content</div>', unsafe_allow_html=True)

        # Streamlit form for input and submit
        with st.form("content_form"):
            topic = st.text_input("Topic", placeholder="e.g., Introduction to Calculus")
            description = st.text_area("Description (Optional)", placeholder="Provide more context...")
            col1, col2 = st.columns(2)
            with col1:
                diff = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
            with col2:
                duration = st.selectbox("Duration", ["10 min", "20 min", "30 min"])
            content_type = st.radio(
                "Content Type",
                ["Interactive Lesson", "Video Content", "Study Notes", "Practice Quiz"],
                horizontal=True
            )
            submitted = st.form_submit_button("Generate Content")
        st.markdown('</div>', unsafe_allow_html=True)

        # Print submitted data
        if submitted:
            st.success("Form submitted!")
            st.write("**Form Data:**")
            st.write({
                "Topic": topic,
                "Description": description,
                "Difficulty Level": diff,
                "Duration": duration,
                "Content Type": content_type
            })

    st.markdown('</div>', unsafe_allow_html=True)

# -- RIGHT COLUMN --
with s2:
    st.markdown('<div>', unsafe_allow_html=True)
    with st.container():
        st.markdown(
            """
            <div class="features">
            <div class="features-title">AI Features</div>
            <ul>
                <li><b>Adaptive Content</b><br>Content adapts to student level and learning style</li>
                <li><b>Interactive Media</b><br>Generates animations, diagrams, and interactive elements</li>
                <li><b>Smart Assessment</b><br>Automatically creates quizzes and practice exercises</li>
            </ul>
            </div>
            <div class="protips">
            <div class="features-title">Pro Tips</div>
            <ul>
                <li>Be specific with your topic for better results</li>
                <li>Include learning objectives in the description</li>
                <li>Choose the right difficulty level for your students</li>
                <li>Combine different content types for engaging lessons</li>
            </ul>
            </div>
            """, unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # Close grid-2

# Example callback for triggering custom logic on button click
if submitted:
    # Place your custom function here
    st.info("Triggering your custom logic with the form inputs above!")
