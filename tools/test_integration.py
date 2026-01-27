
import urllib.request
import json
import sys
import time

def test_server():
    url = "http://localhost:8000/convert"
    payload = {
        "source_code": "driver.findElement(By.id(\"login\")).click();"
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    print("Testing server integration...")
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                body = response.read().decode('utf-8')
                result = json.loads(body)
                print("Response received from server:")
                print(json.dumps(result, indent=2))
                
                if result.get("status") == "success" and "converted_code" in result:
                    print("SUCCESS: Pipeline works (Server -> App -> Ollama).")
                    sys.exit(0)
                else:
                    print("FAILURE: Invalid response content.")
                    sys.exit(1)
            else:
                print(f"FAILURE: HTTP {response.status}")
                sys.exit(1)
    except Exception as e:
        print(f"FAILURE: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Wait for server to start
    time.sleep(2)
    test_server()
