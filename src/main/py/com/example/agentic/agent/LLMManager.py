#
import os
import getpass
from dotenv import load_dotenv
from emoji import config
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from crewai import LLM

#
# "groq:llama3–8b-8192"
# "groq:llama3-70b-8192" 
# "groq:openai/gpt-oss-20b"
# "groq:llama-3.1-70b-versatile"

class LLMManager:
    """
    """
    __agent = None
    __model = None

    @classmethod
    def get_agent(cls):
        load_dotenv()
        #
        if not os.environ.get("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key : ")

        # Initialize models
        if not cls.__agent :
            cls.__agent = create_agent(
                model="groq:openai/gpt-oss-20b",
                system_prompt="You are a helpful assistant."
            )

        return cls.__agent
    
    @classmethod
    def get_model(cls):
        # Initialize models
        if not cls.__model :
            cls.__model = init_chat_model("groq:openai/gpt-oss-20b")
            #self.llm = ChatOpenAI(
            #    model="openai/gpt-oss-20b", 
            #    api_key=os.getenv("OPENAI_API_KEY"),
            #    base_url="https://api.groq.com/openai/v1",
            #    temperature=0
            #)
        return cls.__model
    
    #
    @classmethod
    def create_llm(cls, type: str = 'openai') -> LLM :
        load_dotenv()
        # Ollama llm client
        if type == 'ollama' :
            # LLM setup using litellm additional_params={"num_ctx":16384},
            return LLM(
                model="ollama/llama3.2:latest", 
                base_url="http://localhost:11434", 
                temperature=0.4,     # Controls randomness
                #seed=21,             # Ensures consistent outputs
                #max_tokens=4096,     # Limits response length
                #top_p=0.9            # Controls the diversity of the response
            )
        # Groq llm client
        if type == 'groq' :
            return LLM(
                model="groq/openai/gpt-oss-20b", 
                base_url="https://api.groq.com/openai/v1"
            )
        # OpenAI llm client
        if type == 'openai' or type == 'hf':
            #
            if not os.environ.get("OPENAI_API_KEY"):
                os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
            return LLM(
                model="openai/llama3.2:latest", 
                base_url="http://localhost:11434/v1",
                temperature=0.2,     # Controls randomness
                seed=42,             # Ensures consistent outputs
                max_tokens=4096,     # Limits response length
                top_p=0.9            # Controls the diversity of the response
            )