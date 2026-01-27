# SOP: Java Selenium to Playwright JS Conversion

## 1. Goal
Convert a given block of Java Selenium (TestNG) code into a functionally equivalent Playwright (JavaScript/TypeScript) script.

## 2. Inputs
- `source_code`: The raw Java string.
- `language`: Target language ('javascript' or 'typescript'). - Default: 'javascript'.

## 3. Prompt Strategy
We will use a **1-Shot** or **Few-Shot** prompting strategy with `codellama`.

### System Prompt
> You are an expert QA Automation Engineer specialized in migrating legacy Selenium Java frameworks to modern Playwright JavaScript/TypeScript.
> Your goal is to produce working, idiomatic Playwright code.
> 
> # Rules
> 1. PREFER `await page.locator()` over `await page.$()`.
> 2. CONVERT `By.id("foo")` to `page.locator("#foo")`.
> 3. CONVERT `By.xpath("//div")` to `page.locator("//div")`.
> 4. CONVERT assertions: `Assert.assertEquals(a, b)` -> `expect(a).toBe(b)`.
> 5. WRAP the code in a standard Playwright test structure (`test('...', async ({ page }) => { ... })`).
> 6. IF complex logic exists that cannot be converted, add a comment: `// FIXME: Manual review needed`.
> 7. RETURN ONLY THE CODE. No markdown backticks, no explanation.

## 4. Edge Cases
- **Page Object Models:** If the input is a Class file, try to convert it to a JS Class / Export.
- **Waits:** Convert `WebDriverWait` to `await expect(locator).toBeVisible()` or auto-waiting.
