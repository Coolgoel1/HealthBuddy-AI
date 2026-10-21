# Healthbuddy
HealthBuddy is a healthcare consultation agent built in Python using Gemini API. It blends cultural knowledge of Indian home remedies with safety‑first logic, ensuring every suggestion is factual, non‑prescriptive, and accompanied by disclaimers. This project is the *Terminal Version*, means it will run on the terminal of your local code editor.

## Features
- **Safety-first logic**: Every output includes disclaimers and blocks unsafe queries.  
- **Cultural remedies knowledge base**: Structured, factual references to Indian home remedies.  
- **Menu-driven consultation flow**: Symptom → disclaimer → safe suggestion → escalation.  
- **Terminal-based agent**: Works seamlessly in your local code editor’s terminal.  
- **Reproducible setup**: Minimal dependencies, clear onboarding, and environment instructions.  

---

## Project Structure
```
healthbuddy/
├── README.md
├── requirements.txt
├── main.py                     #The main code file
├── check_gemini_status.py      #Confirm if your Gemini client is working or not
```

## Disclaimer
HealthBuddy is **not a medical professional**.  
It does **not** provide diagnoses, prescriptions, or emergency guidance.  
Always consult a qualified healthcare provider for medical concerns.  

---


## Documentation
- `docs/architecture.md`: Consultation flow & decision trees  
- `docs/onboarding.md`: Environment setup, Gemini API quota notes  

---

## Contributing
Pull requests are welcome! Please ensure:  
- Safety disclaimers remain intact.  
- Remedies are factual, non-prescriptive.  
- Code follows minimal, reproducible standards.

---

## Future Scope
-Add a working Web UI to make it look user friendly.

-Adding memory to the bot, so it recognises your previous ailments and allergies to give you precautions accordingly.
