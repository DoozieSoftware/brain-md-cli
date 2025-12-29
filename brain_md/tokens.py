"""Token estimation using tiktoken."""

import tiktoken


def estimate_tokens(text: str, model: str = "gpt-4") -> int:
    """
    Estimate token count for a given text.
    
    Uses cl100k_base encoding (GPT-4, GPT-3.5-turbo).
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    
    return len(encoding.encode(text))
