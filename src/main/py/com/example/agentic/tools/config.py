"""
"""
_tool_config = dict(
    llm=dict(
        provider="ollama", # or google, openai, anthropic, llama2, ...
        config=dict(
            model="llama3.2:1b-instruct-q8_0",
            # num_predict=256,
            # temperature=0.7,
            # top_p=1,
            # stream=true,
        ),
    ),
    embedder=dict(
        provider="ollama", # or openai, ollama, ...
        config=dict(model_name="nomic-embed-text", task_type="RETRIEVAL_DOCUMENT")
    ),
    embedding_model= dict(
        provider="openai",
        config=dict(model= "nomic-embed-text", api_key="", platform_url="http://localhost:11434/v1")
    ),
    vectordb=dict(
        provider="chromadb",
        config={"persist_directory":"agentic-ai/chromadb", "allow_reset": "true", "is_persistent": "true"}
    )
)

#
_rag_tool_config = dict(
    llm=dict(
        provider="ollama", # or google, openai, anthropic, llama2, ...
        config=dict(
            model="llama3.2:1b-instruct-q8_0",
            # temperature=0.5,
            # top_p=1,
            # stream=true,
        ),
    ),
    embedder=dict(
        provider="ollama", # or openai, ollama, ...
        config=dict(model_name="nomic-embed-text", task_type="RETRIEVAL_DOCUMENT")
    ),
    embedding_model= dict(
        provider="openai",
        config=dict(model= "nomic-embed-text", dimensions=768, api_key="", platform_url="http://localhost:11434/v1")
    ),
    vectordb=dict(
        provider="chromadb",
        config={"persist_directory":"agentic-ai/chromadb", "allow_reset": "true", "is_persistent": "true"}
    )
)

# Embedders
_embedder_config_ollama={"provider": "ollama", "config": {"model_name": "nomic-embed-text", "url":"http://localhost:11434/api/embeddings"}}
_embedder_config_openai={"provider": "openai", "config": {"model_name": "nomic-embed-text", "api_key":"", "api_base":"http://localhost:11434/v1", "dimensions":768, "api_version":"v1"}}
_embedder_config_hf={"provider": "huggingface", "config": {"model_name": "sentence-transformers/all-MiniLM-L6-v2"}}

from crewai.rag.embeddings.providers.openai.types import OpenAIProviderSpec
from crewai.rag.embeddings.providers.ollama.types import OllamaProviderSpec
from crewai.rag.embeddings.providers.huggingface.types import HuggingFaceProviderSpec

_embedding_model_openai: OpenAIProviderSpec = {
    "provider": "openai",
    "config": {
        #"api_key": "ollama",
        "model_name": "nomic-embed-text",
        "dimensions": 4096,
        #"organization_id": "your-org-id",
        "api_base": "http://localhost:11434/v1/",
        #"api_version": "v1",
        #"default_headers": {"X-Custom-Header": "xxxxx"}
    }
}

_embedding_model_ollama: OllamaProviderSpec = {
    "provider": "ollama",
    "config": {
        "model_name": "nomic-embed-text",
        "url": "http://localhost:11434/api/embeddings"
    }
}

_embedding_model_hf: HuggingFaceProviderSpec = {
    "provider": "huggingface",
    "config": {
        "url": "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
    }
}