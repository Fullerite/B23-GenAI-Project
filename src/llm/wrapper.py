import requests
from textwrap import dedent
from typing import Optional, List


class LLMClient:
    def __init__(self, base_url: str, model: str = "qwen3:8b"):
        self.base_url = base_url.rstrip("/")
        self.model = model

    def generate_response(
        self,
        messages: List,
        context_chunks: Optional[List] = None
    ) -> str:
        if context_chunks:
            formatted_context = "\n\n".join(context_chunks)
            system_instruction = dedent(f"""
            # Role
            You are a helpful documentation assistant for the V4Fire Core library.

            # Context
            Use the following documentation chunks to answer the user's question:
            <formatted_context>
            {formatted_context}
            </formatted_context>

            # Instructions
            1. Answer clearly and concisely based ONLY on the context above.
            2. If the answer is not in the context, strictly state that you don't know.
            3. You MUST cite the most relevant filename (in very rare cases — filenames) at the end of your answer in 'Source: full_filename.md' format. You must use **the exact same full filename** provided in the 'Source' header of the context chunks.
            4. Do NOT generate new relative markdown links (e.g. [Link](#section)). Do NOT use any external web or github URLs. You are only allowed to mention the markdown source file name.
            """).strip()
        else:
            system_instruction = dedent("""
            # Role
            You are a helpful documentation assistant for the V4Fire Core library.

            # Mode
            You are currently in 'General Chat' mode.

            # Instructions
            1. Be polite and helpful.
            2. Answer general questions or guide the user to ask specific technical questions about the documentation.
            """).strip()

        final_messages = [{"role": "system", "content": system_instruction}] + messages

        payload = {
            "model": self.model,
            "messages": final_messages,
            "stream": False,
            "think": False,
            "options": {
                "temperature": 0.3,
                "seed": 42,
                "num_ctx": 8192,
                "num_predict": 1024
            }
        }

        try:
            response = requests.post(f"{self.base_url}/api/chat", json=payload, timeout=60)
            response.raise_for_status()
            return response.json()["message"]["content"]
        except Exception as e:
            return f"Error communicating with LLM: {str(e)}"
