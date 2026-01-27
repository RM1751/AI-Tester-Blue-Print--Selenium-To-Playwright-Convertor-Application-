
import urllib.request
import json
import sys

def check_ollama():
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "codellama",
        "prompt": "Hello world, reply with just 'Hello'",
        "stream": False
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        print(f"Connecting to {url}...")
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                body = response.read().decode('utf-8')
                response_data = json.loads(body)
                print("Response received:")
                print(json.dumps(response_data, indent=2))
                
                if "response" in response_data:
                    print("SUCCESS: Ollama (codellama) is responding.")
                    sys.exit(0)
                else:
                    print("FAILURE: Unexpected response format.")
                    sys.exit(1)
            else:
                print(f"FAILURE: HTTP {response.status}")
                sys.exit(1)
            
    except urllib.error.URLError as e:
        print(f"FAILURE: Connection error: {e}")
        print("Ensure Ollama is running on port 11434.")
        sys.exit(1)
    except Exception as e:
        print(f"FAILURE: {e}")
        print("It is possible the model 'codellama' is not pulled. Run 'ollama pull codellama'.")
        sys.exit(1)

if __name__ == "__main__":
    check_ollama()
