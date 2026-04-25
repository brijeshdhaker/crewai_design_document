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
        config=dict(model_name="nomic-embed-text:latest", task_type="RETRIEVAL_DOCUMENT")
    ),
    embedding_model= dict(
        provider="ollama",
        config=dict(model= "nomic-embed-text:latest", api_key="", platform_url="http://localhost:11434/v1")
    ),
    vectordb=dict(
        provider="chromadb",
        config={
            #"collection_name": "rag_documents",
            #"persist_directory":"/home/brijeshdhaker/IdeaProjects/crewai_design_document/vectorstore/chroma", 
            #"allow_reset": "true", 
            #"is_persistent": "true"
        }
    )
)

#
_rag_tool_config = dict(
    llm=dict(
        provider="openai",
        config=dict(
            model="llama3.2:1b-instruct-q8_0",
            max_tokens=4096
            # temperature=0.7,
            # top_p=1,
            # stream=true,
        ),
    ),
    embedder=dict(
        provider="openai", # or openai, ollama, ...
        config=dict(model_name="nomic-embed-text:latest", task_type="RETRIEVAL_DOCUMENT")
    ),
    embedding_model= dict(
        provider="openai",
        config=dict(
            model_name= "nomic-embed-text:latest", 
            api_key="ollama",
            organization_id="sandbox",
            api_base="http://localhost:11434/v1",
            api_version="v1",
            default_headers={"X-Custom-Header": "ollama"}
        )
    ),
    vectordb=dict(
        provider="chromadb",
        config={
            #"collection_name": "sandbox_documents",
            #"persist_directory":"/home/brijeshdhaker/IdeaProjects/crewai_design_document/vectorstore/chroma", 
            #"allow_reset": "true", 
            #"is_persistent": "true"
        }
    )
)

# Embedders
_embedder_config_ollama={"provider": "ollama", "config": {"model_name": "nomic-embed-text", "url":"http://localhost:11434/api/embeddings"}}
_embedder_config_openai={"provider": "openai", "config": {"model_name": "nomic-embed-text", "api_key":"", "api_base":"http://localhost:11434/v1", "api_version":"v1"}}
_embedder_config_hf={"provider": "huggingface", "config": {"model_name": "sentence-transformers/all-MiniLM-L6-v2"}}

from crewai.rag.embeddings.providers.openai.types import OpenAIProviderSpec
from crewai.rag.embeddings.providers.ollama.types import OllamaProviderSpec
from crewai.rag.embeddings.providers.huggingface.types import HuggingFaceProviderSpec


_embedding_model_openai: OpenAIProviderSpec = {
    "provider": "openai",
    "config": {
        "api_key": "ollama",
        "model_name": "nomic-embed-text:latest",
        "dimensions": 768,
        "organization_id": "sandbox",
        "api_base": "http://localhost:11434/v1/",
        "api_version": "v1",
        "api_type": "ollama",
        "default_headers": {"X-Custom-Header": "ollama"}
    }
}

_embedding_model_ollama: OllamaProviderSpec = {
    "provider": "ollama",
    "config": {
        "model_name": "nomic-embed-text:latest",
        "url": "http://localhost:11434/api/embeddings"
    }
}

_embedding_model_hf: HuggingFaceProviderSpec = {
    "provider": "huggingface",
    "config": {
        "model": "sentence-transformers/all-MiniLM-L6-v2"
    }
}

## Memory
from crewai import Memory

memory_ollama = Memory(embedder={
    "provider": "ollama",
    "config": {
        "model_name": "nomic-embed-text",
        "url": "http://localhost:11434/api/embeddings",
    },
})

memory_openai = Memory(embedder={
    "provider": "openai",
    "config": {
        "model_name": "nomic-embed-text",
        "dimensions": 768,
        # "api_key": "sk-...",  # or set OPENAI_API_KEY env var
    },
})

memory_hf = Memory(embedder={
    "provider": "huggingface",
    "config": {
        "model_name": "sentence-transformers/all-MiniLM-L6-v2",
    },
})