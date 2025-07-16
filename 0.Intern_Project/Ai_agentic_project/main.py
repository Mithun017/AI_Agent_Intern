from tavily import TavilyClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()

# API keys
gemini_api_key = os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Validate API keys
if not gemini_api_key or not tavily_api_key or not groq_api_key:
    raise ValueError("❌ Missing API keys in .env file")

# Initialize LLMs
gemini_llm = ChatGoogleGenerativeAI(api_key=gemini_api_key, model="gemini-2.0-flash")
groq_llm = ChatGroq(api_key=groq_api_key, model="llama-3.1-8b-instant")

# Tavily search function
def tavily_search(query: str) -> str:
    client = TavilyClient(api_key=tavily_api_key)
    results = client.search(query=query, search_depth="advanced")
    return "\n".join([r['content'] for r in results.get('results', [])[:3]])

# Clean HTML tags from output (optional)
def clean_output(text):
    text = re.sub(r'<sub>(.*?)</sub>', r'_\1_', text)
    text = re.sub(r'<sup>(.*?)</sup>', r'^\1^', text)
    text = re.sub(r'<[^>]+>', '', text)  # remove any other HTML tags
    return text.strip()

# Prompt templates
gemini_prompt_template = PromptTemplate.from_template("""
You are a knowledgeable assistant. Based on the following search results, write a comprehensive and informative answer to the user's query.

Search Results:
{search_results}

User Query:
{user_query}
""")

groq_prompt_template = PromptTemplate.from_template("""
You are a skilled language expert. Polish and refine the following draft into a final high-quality answer:

Draft:
{draft}
""")

# Main logic
def main():
    user_query = input("💬 Enter your query: ")

    print("\n🔍 Searching the web...\n")
    search_results = tavily_search(user_query)

    print("🧠 Generating detailed answer with Gemini...\n")
    gemini_prompt = gemini_prompt_template.format(search_results=search_results, user_query=user_query)
    gemini_output = gemini_llm.invoke(gemini_prompt)

    print("✨ Refining answer with Mistral...\n")
    groq_prompt = groq_prompt_template.format(draft=gemini_output.content)
    final_output = groq_llm.invoke(groq_prompt)

    print("\n✅ FINAL OUTPUT:\nHere is a polished and refined version of your response:\n")
    print(clean_output(final_output.content))

if __name__ == "__main__":
    main()
