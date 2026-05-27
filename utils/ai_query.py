import anthropic
import streamlit as st

def get_ai_answer(question: str, context: str) -> str:
    client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="""You are a food economics analyst specializing in Nigeria. 
        You answer questions about food price inflation using NBS data provided to you.
        Be concise, factual, and cite specific numbers where possible.""",
        messages=[
            {"role": "user", "content": f"Here is the data:\n{context}\n\nQuestion: {question}"}
        ]
    )
    return message.content[0].text