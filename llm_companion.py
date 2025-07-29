import json
import os
import time
from llama_cpp import Llama

# === File paths ===
MODEL_PATH = "models/phi-2/phi-2.Q4_K_M.gguf"
MEMORY_PATH = "memory.json"
KNOWLEDGE_PATH = "game_knowledge.txt"

# === Load player memory ===
def load_memory():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"player_name": None, "facts": []}

# === Save memory ===
def save_memory(memory):
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

# === Load game lore/knowledge ===
def load_knowledge():
    if os.path.exists(KNOWLEDGE_PATH):
        with open(KNOWLEDGE_PATH, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

# === Print gradually like an NPC ===
def type_out(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# === Setup LLM ===
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=6,
    verbose=False,
)

# === Assistant Persona ===
PERSONA = (
    "You are 'Hex', a cryptic, clever dungeon guide who speaks with sharp wit, sarcasm, and dark wisdom. "
    "You never break character. Speak like you're from another realm. Use strange metaphors or dungeon slang.\n"
)

def ask_hex(memory, player_prompt):
    name = memory.get("player_name", "Stranger")
    facts = "\n".join(memory.get("facts", []))
    lore = load_knowledge()

    system_prompt = (
        f"{PERSONA}"
        f"Player Name: {name}\n"
        f"Known Facts:\n{facts}\n"
        f"Game Lore:\n{lore}\n"
        f"Never say you are AI or assistant.\n"
        f"Keep your responses immersive and helpful.\n"
    )

    full_prompt = (
        f"{system_prompt}\n"
        f"Player: {player_prompt}\n"
        f"Hex:"
    )

    try:
        result = llm(
            prompt=full_prompt,
            max_tokens=256,
            stop=["Player:", "Hex:"],
            echo=False,
            temperature=0.7,
            top_p=0.9,
        )
        return result["choices"][0]["text"].strip()
    except Exception as e:
        return f"[Hex encountered a dark error: {e}]"

# === Start conversation ===
if __name__ == "__main__":
    memory = load_memory()
    type_out("💀 Hex: Awakened from shadows... Who summons me?", 0.03)

    if not memory.get("player_name"):
        name = input("Hex: What do they call you in the light, mortal? 🧙‍♂️\nYou: ").strip()
        memory["player_name"] = name
        memory["facts"].append(f"The player is named {name}.")
        save_memory(memory)
        type_out(f"Hex: Very well, {name}. I shall remember that. 🕯️", 0.03)

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            type_out("Hex: May the shadows cradle you once more... 🕳️", 0.03)
            break

        # Track known facts (example: "My favorite weapon is the dagger.")
        if "my name is" in user_input.lower():
            new_name = user_input.split("is")[-1].strip()
            memory["player_name"] = new_name
            memory["facts"].append(f"The player is named {new_name}.")
            save_memory(memory)

        elif any(x in user_input.lower() for x in ["i like", "i hate", "i use", "my favorite"]):
            memory["facts"].append(user_input)
            save_memory(memory)

        reply = ask_hex(memory, user_input)
        type_out(f"Hex: {reply}", 0.02)
