import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_community.utilities import SQLDatabase
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import csv
from datetime import datetime

load_dotenv()

# -------------------------------------
# 🔁 Self-Learning Logger
# -------------------------------------
def log_unknown_input(question: str, reason: str = "Unclear/Invalid"):
    with open("chotu_logs.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), question, reason])

# -------------------------------------
# 🔗 Setup
# -------------------------------------
llm = Ollama(model="llama3.2", temperature=0.3)

db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}",
    sample_rows_in_table_info=3
)

# -------------------------------------
# 🔍 Intent Classifier
# -------------------------------------
intent_prompt = ChatPromptTemplate.from_messages([
    ("system", "Classify the user's input into one of these categories:\n"
               "- inventory\n- joke\n- math\n- casual\n- web\n\n"
               "Respond with only the category name."),
    ("human", "{question}")
])
intent_chain = intent_prompt | llm | StrOutputParser()

# -------------------------------------
# 📦 Inventory Handler (SQL + Answer + Follow-up)
# -------------------------------------
sql_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a PostgreSQL expert. Only return a valid SQL query for the question, no explanations."),
    ("human", "Schema:\n{schema}\n\nQuestion:\n{question}")
])
sql_chain = sql_prompt | llm | StrOutputParser()

answer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You're Chotu the assistant. Provide a clear, friendly, and short answer based on SQL result. If the query is about a missing column or data, say so kindly and explain how the user could add such data or what estimate can be made. Always add a short follow-up suggestion like a business consultant, only when the query is inventory-related."),
    ("human", "Question: {question}\nSQL Result: {sql_result}\nAnswer:")
])
answer_chain = answer_prompt | llm | StrOutputParser()

def run_inventory_chain(question):
    schema = db.get_table_info()
    sql_query = sql_chain.invoke({"schema": schema, "question": question})

    if not sql_query.lower().strip().startswith("select"):
        raise ValueError("Invalid SQL generated.")

    try:
        result = db.run(sql_query)
    except Exception as e:
        log_unknown_input(question, str(e))
        return f"Hmm... I checked our system, but it seems we're missing data for that like sales history or such. Maybe we can track it going forward? 📊\n\nError: {e}"

    return answer_chain.invoke({"question": question, "sql_result": result})

# -------------------------------------
# 🤣 Joke + Gossip (With One-Liner Tweak)
# -------------------------------------
joke_prompt = ChatPromptTemplate.from_messages([
    ("system", "You're Chotu, the cheeky store assistant. Tell sharp one-liner jokes or roast brands. Keep it short and witty."),
    ("human", "{question}")
])
joke_chain = joke_prompt | llm | StrOutputParser()

# -------------------------------------
# 🧮 Math Chain
# -------------------------------------
math_prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a calculator. Do math and return just the answer without any explanation."),
    ("human", "{question}")
])
math_chain = math_prompt | llm | StrOutputParser()

# -------------------------------------
# 🌐 Web Assist Chain (No true browsing yet, just simulates)
# -------------------------------------
web_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Chotu with internet access. Try to answer based on what you know online. If inappropriate, gently refuse."),
    ("human", "{question}")
])
web_chain = web_prompt | llm | StrOutputParser()

# -------------------------------------
# 🤖 Unified Chotu 2.0 Chain
# -------------------------------------
def chotu_chain(question: str):
    try:
        intent = intent_chain.invoke({"question": question}).strip().lower()

        if intent == "inventory":
            return run_inventory_chain(question)
        elif intent in ["joke", "casual"]:
            return joke_chain.invoke({"question": question})
        elif intent == "math":
            return math_chain.invoke({"question": question})
        elif intent == "web":
            return web_chain.invoke({"question": question})
        else:
            log_unknown_input(question, reason="Unclassified")
            return "Not sure what you meant. Try asking something about stock, math, or gossip."

    except Exception as e:
        log_unknown_input(question, str(e))
        return f"Chotu couldn't answer that right now. But I'm learning! 🧠\n\nError: {e}"
