
import sys
import os

# Add tools directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm_client import query_ollama

SOP_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "architecture", "sop_conversion.md")

def read_sop():
    try:
        with open(SOP_PATH, "r") as f:
            return f.read()
    except:
        return "You are a code converter."

def convert_code(source_code, target_lang="javascript"):
    sop_content = read_sop()
    
    # Extract System Prompt from SOP (Simplified extraction)
    # In a real system, we'd parse the MD properly. Here we just construct a strong prompt.
    
    system_prompt = f"""
You are an expert QA Automation Engineer.
Your task is to convert Selenium Java code to Playwright {target_lang}.

RULES:
1. Wrap snippets in a test() block if they are test methods.
2. Use 'await page.locator()' for selectors.
3. Convert Assert.assertEquals() -> expect().toBe().
4. OUTPUT ONLY THE CODE. NO EXPLANATION.
    """
    
    print(f"Converting code to {target_lang}...")
    response = query_ollama(source_code, system_prompt)
    return response

if __name__ == "__main__":
    sample_java = """
    @Test
    public void loginTest() {
        driver.get("https://example.com");
        driver.findElement(By.id("user")).sendKeys("admin");
        driver.findElement(By.id("pass")).sendKeys("1234");
        driver.findElement(By.id("loginBtn")).click();
        Assert.assertEquals(driver.getTitle(), "Dashboard");
    }
    """
    print(convert_code(sample_java))
