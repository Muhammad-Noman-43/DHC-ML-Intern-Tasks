import requests
from rich.markdown import Markdown
from rich.console import Console
import os
from dotenv import load_dotenv

def query(prompt):
    prompt = {
        "messages":[
            {
                "role":"user",
                "content":f"{prompt}"
            }
        ],
        "model":"mistralai/Mistral-7B-Instruct-v0.2:together"
    }
    try:
        response = requests.post(url = API_URL, headers = HEADERS, json = prompt)
    except:
        print("There was an issue in reaching the model...")
        return None
    return response.json()

load_dotenv() # Yaha .env file wale vars (hugginface model token) nikale hain hum ne

HF_TOKEN = os.getenv("HF_TOKEN") # Huggingface token ko variable me store kar liya

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization":f"Bearer {HF_TOKEN}" # HF token ko authoenticate krne k liye token de diya
}


systemPrompt = """
Act as a helpful and friendly medical assistant.
Provide 2 lines descrition of the problem first, then suggest possible causes, then suggest possible solutions.
Provided explanation and solutions should be at most 50 lines (only if deep explanation is necessary), simple, easy to understand for a non-medical user.
Never provide medications or their dosages.
Always suggest consulting a licensed doctor for serious concerns.
Keep answers simple and clear.
Don't ask for personal information.
Don't ask any follow-up questions. 
"""

# These are just my own instructions. I wouldn't apply this in real life tbh :)

userPrompt = input("Ask your question: ")

def isPromptSafe(prompt):
    dangerousWords = ["suicide", "overdose", "poison", "cyanide", "arsenic", "heroin", "cocaine", "methamphetamine", "fentanyl", "lsd", "ecstasy", "ketamine", "pcp", "bomb", "explosive", "gun", "knife", "stab", "shoot", "kill", "murder", "assassinate", "torture", "harm", "self-harm", "cut", "slash", "bleed", "die", "death", "euthanasia", "abort", "miscarry", "sterilize", "castrate", "amputate", "inject", "snort", "smoke", "ingest", "swallow", "choke", "strangle", "drown", "burn", "electrocute", "radiation", "nuclear", "biological", "chemical", "weapon", "virus", "bacteria", "plague", "anthrax", "ricin", "botulism", "sarin", "mustard", "phosgene", "hack", "phish", "forge", "steal", "traffick", "exploit", "sextort", "pedophile", "child", "minor", "rape", "assault", "molest", "incest", "porn", "csam", "terror", "bombing", "jihad", "isis", "alqaeda", "ransomware", "ddos", "cyberattack", "disrupt", "sabotage", "infrastructure", "grid", "hospital", "airport", "train", "poisonous", "lethal", "fatal", "deadly", "prescribe", "diagnose", "cure", "operate", "surgery", "anesthetize"]
    
    # ye words chatgpt se generate karwae hain mene
    
    for word in dangerousWords:
        if word in prompt:
            return False
    return True

if isPromptSafe(userPrompt):
    finalPrompt = f"{systemPrompt}\n\n User's Question is as follows: {userPrompt}" # mine cutomized prompt

    output = query(finalPrompt)

    if output is not None:
        outputText = output["choices"][0]["message"]["content"]
        console = Console() # thore extra steps, not important
        console.print(Markdown(outputText)) # sirf output acha dikhega thora
    else:
        print("Failed to get a response from the model.")
        
else:
    print("Sorry! Couldn't help in matters related to self-harm. (We suspected some danger words)")
