#
import os
import getpass
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from crewai import LLM

#
# llama3.2:3b-instruct-q8_0
# nomic-embed-text:latest
#
class LLMManager:
    """
    """
    @classmethod
    def get_agent(cls):
        load_dotenv()
        # Initialize models
        return create_agent(
            model=f"groq:{os.environ["GROQ_MODEL_NAME"]}",
            system_prompt="You are a helpful assistant."
        )
    
    @classmethod
    def get_model(cls):
        # Initialize models
        return init_chat_model(f"groq:{os.environ["GROQ_MODEL_NAME"]}")
    
    #
    @classmethod
    def create_llm(cls, type: str = 'openai') -> LLM :
        load_dotenv()
        # Ollama llm client
        if type == 'ollama' :
            # LLM setup using litellm additional_params={"num_ctx":16384},
            return LLM(
                model=f"ollama/{os.environ["OLLAMA_MODEL"]}", 
                base_url="http://localhost:11434", 
                temperature=0.3,     # Controls randomness os.environ["OLLAMA_MODEL"]
                #seed=21,             # Ensures consistent outputs
                #max_tokens=4096,     # Limits response length
                #top_p=0.9            # Controls the diversity of the response
            )
        # Groq llm client
        if type == 'groq' :
            return LLM(
                model=f"groq/{os.environ["GROQ_MODEL_NAME"]}", 
                base_url="https://api.groq.com/openai/v1"
            )
        # OpenAI llm client
        if type == 'openai' or type == 'hf':
            return LLM(
                model=f"openai/{os.environ["OPENAI_MODEL_NAME"]}", 
                base_url="http://localhost:11434/v1",
                temperature=0.3,     # Controls randomness
                #seed=42,             # Ensures consistent outputs
                #max_tokens=4096,     # Limits response length
                #top_p=0.9            # Controls the diversity of the response
            )