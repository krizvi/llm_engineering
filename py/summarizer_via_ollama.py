from py.web_scraper import Website

MODEL = "llama3.2:1b"


# calling the api using python
def useLlamaViaCurlStyle(model, messages):
    OLLAMA_API = "http://localhost:11434/api/chat"
    HEADERS = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": messages,
        "stream": False
    }
    import requests
    response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
    return response.json()['message']['content']


def useLlamaViaOllamaLib(model, messages):
    import ollama
    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']


def useLlammaViaOpenAILib(MODEL, messages):
    from openai import OpenAI
    openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
    response = openai.chat.completions.create(model=MODEL, messages=messages)
    return response.choices[0].message.content


def messages_for(website):
    system_prompt = "You are an assistant that analyzes the contents of a website and provides a short summary, ignoring text that might be navigation related. Respond in markdown."

    user_prompt = (f"You are looking at a website titled '{website.title}'. "
                   f"Please provide a short summary of this website in 50 words max. "
                   f"Stay focused and to the point. "
                   f"If it includes news or announcements, then summarize these too.")
    user_prompt += "\n```\n"+website.text+"\n```"

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]


print("importRequest=>", useLlamaViaCurlStyle(MODEL, messages_for(Website("http://edu.khalidrizvi.com"))))
print("importOllama=>", useLlamaViaOllamaLib(MODEL, messages_for(Website("http://edu.khalidrizvi.com"))))
print("importOpenAI=>", useLlammaViaOpenAILib(MODEL, messages_for(Website("http://edu.khalidrizvi.com"))))
