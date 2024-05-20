import os
from dotenv import load_dotenv
from openai import OpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt



# @retry(wait=wait_random_exponential(multiplier=0.5, max=20), stop=stop_after_attempt(6))
def openai_chat(question, 
                system_message="You are a helpful assistant.", 
                model="gpt-3.5-turbo",
                api_key: str = None,
                base_url: str = None,
                organization: str = None,
                **kwargs) -> str:
    """
    Function to interact with OpenAI chat API.
    
    Args:
        question (str): The user's question.
        system_message (str): The system's message (default is "You are a helpful assistant.").
        model (str): The model to use (default is "gpt-3.5-turbo").
        api_key (str): The API key for authentication.
        base_url (str): The base URL for the API.
    
    Returns:
        str: The response message from the chat.
    """

    if api_key is None:

        try:
            api_key = os.getenv("openai_key")
        except Exception as e:
            raise ValueError(f"Please set the OPENAI_API_KEY environment variable. Error: {str(e)}")
        
    if base_url is None:
        base_url = "https://api.groq.com/openai/v1"
        try:
            base_url = os.getenv("base_url")
        except Exception as e:
            base_url = None
    client = OpenAI(api_key=api_key, 
                    base_url=base_url,
                    organization=organization)
    completion = client.chat.completions.create(
        model=model,
        seed=42,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": question+"\nAnswer in bahasa Indonesia"}
        ],
        **kwargs
    )

    return completion.choices[0].message.content