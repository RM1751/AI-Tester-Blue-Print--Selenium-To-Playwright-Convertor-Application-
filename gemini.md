# Project Constitution (gemini.md)

## Data Schemas

### Input Payload (UI -> Backend)
```json
{
  "source_code": "String (The raw Selenium Java code)",
  "target_language": "String (javascript | typescript)",
  "output_dir": "String (Optional: Path to save converted files, defaults to ./output)"
}
```

### Output Payload (Backend -> UI)
```json
{
  "status": "String (success | error)",
  "converted_code": "String (The converted Playwright code)",
  "file_path": "String (Absolute path where file was saved)",
  "logs": ["String (Conversion steps or warnings)"]
}
```

## Behavioral Rules
1. **Readability First:** Output code should be idiomatic Playwright, not a line-by-line translation of Java patterns.
2. **Complete Conversion:** Attempt to convert all logic, including assertions (TestNG -> Playwright/Jest/Expect).
3. **Safe Fallback:** If a specific Selenium method has no direct equivalent, leave a comment `// TODO: Manual intervention required for [Method]` and continue.

## Architectural Invariants
- **Core Logic Decoupling:** Conversion logic must be essentially a pure function (String -> String) wrapped in file I/O.
- **UI/Logic Separation:** The UI only sends the payload; the backend handles the AST parsing/LLM conversion logic.
- **Local Intelligence:** Use Ollama (`codellama`) for all AI processing. No external API calls for conversion.

## Maintenance Log
