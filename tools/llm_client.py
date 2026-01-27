
import urllib.request
import json
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "codellama"

def query_ollama(prompt, system_prompt=""):
    """
    Sends a prompt to the local Ollama instance and returns the response text.
    """
    full_prompt = f"{system_prompt}\n\nUser Code:\n{prompt}"
    
    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.2, # Low temperature for deterministic code
            "num_predict": 2048
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        start_time = time.time()
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                body = response.read().decode('utf-8')
                result = json.loads(body)
                duration = time.time() - start_time
                # print(f"DEBUG: Ollama took {duration:.2f}s")
                return result.get("response", "").strip()
            else:
                return f"ERROR: HTTP {response.status}"
    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == "__main__":
    # Test
    print(query_ollama("System.out.println('Hello');", "Convert Java to JS"))
