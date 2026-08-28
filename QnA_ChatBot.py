from dotenv import load_dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)

st.title("🤖 ASK BUDDY - IT'S AI QnA BOT")
st.markdown(
    "My QnA BOT with LangChain and Google Gemini!"
)

if "message" not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:

    role = message["role"]
    content = message["content"]

    st.chat_message(role).markdown(content)



query = st.chat_input(
    "Ask Anything ?"
)


if query:


    st.session_state.message.append(
        {
            "role": "user",
            "content": query
        }
    )


    st.chat_message("user").markdown(query)


    chat_history = []


    for msg in st.session_state.message:


        if msg["role"] == "user":

            chat_history.append(
                HumanMessage(
                    content=msg["content"]
                )
            )


        else:

            chat_history.append(
                AIMessage(
                    content=msg["content"]
                )
            )


    response = llm.invoke(chat_history)



    if isinstance(response.content, list):

        answer = response.content[0]["text"]

    else:

        answer = response.content



    st.chat_message("ai").markdown(answer)


    st.session_state.message.append(
        {
            "role": "ai",
            "content": answer
        }
    )