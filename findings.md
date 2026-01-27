# Findings

## Research
(To be populated)

## Discoveries
- **North Star:** Selenium Java -> Playwright JS/TS Code Converter.
- **Integrations:** TestNG Selenium Java -> Playwright JS/TS transformation logic.
- **Source of Truth:** User input via UI (Selenium Java Code).
- **Delivery Payload:** Display in UI and save to a new directory.
- **Behavioral Rules:** Convert everything. Prioritize readability over strict 1:1 mapping.

## Constraints
- Input is Java calling Selenium/TestNG.
- Output is JS/TS calling Playwright.
- Must handle file system operations (writing output).
- **LLM Provider:** Ollama (Local).
- **Model:** `codellama`.
