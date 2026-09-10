import os
from huggingface_hub import InferenceClient
import streamlit as st

st.set_page_config(
    page_title="Kas AI App",
    page_icon="🤖"
)

st.title("🤖 Kas AI - Question & Answer")
st.write("Ask a question and get an AI-generated answer!")

question = st.text_area(
    "❓ Enter your question:",
    placeholder="Example: What is photosynthesis?"
)

client = InferenceClient(
    api_key=os.environ["token"]
)

if st.button("✨ Ask Kas AI"):

    if question:

        with st.spinner("🤖 Thinking..."):

            response = client.chat.completions.create(
                model="meta-llama/Llama-3.1-8B-Instruct",
                messages=[
                    {
                        "role": "system",
                        "content": "You are Kas AI, a helpful educational AI assistant. Answer the user's questions clearly, accurately, and in a simple way."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                max_tokens=500
            )

        answer = response.choices[0].message.content

        st.subheader("📝 AI Answer")
        st.write(answer)

    else:
        st.warning("⚠️ Please enter a question.")