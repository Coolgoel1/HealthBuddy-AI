from google import genai

api= input("Enter your Google API key(for testing purposes): ")
print("Initializing Gemini client...")
client = genai.Client(api_key=api)

def consult_gemini(prompt):
    try:
        resp = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
        return resp.text
    except Exception as e:
        print("Error contacting Gemini API")
        return ""

def maps_link(query: str, city: str, country: str):
    base = "https://www.google.com/maps/search/"
    search = f"{query} near {city}, {country}"
    return base + search.replace(" ", "+")

def show_menu():
    print("="*44)
    print("===== HEALTHBUDDY OPTIONS =====")
    print("1. SIMPLE HOME REMEDIES")
    print("2. SIMPLE MEDICINE GUIDANCE")
    print("3. NEAREST DOCTOR/HOSPITAL REFERRAL")
    print("4. EXIT")

def maps_directions(destination: str, city: str, country: str):
    base = "https://www.google.com/maps/dir/?api=1"
    dest = f"{destination} near {city}, {country}"
    return f"{base}&destination={dest.replace(' ', '+')}"

def log_session(name, age, gender, country, city, problem, choice, severe_flag):
    with open("session_log.txt", "a") as f:
        f.write(f"{name}, {age}, {gender}, {country}, {city}, Issue: {problem}, Choice: {choice}, Severe: {severe_flag}")

def classify_issue(problem: str):

    prompt = (f"Decide the severity of the health issue '{problem}'.Classify it strictly as one word: Mild, Severe, or Extreme.Do not explain, just return the category. If {problem} is not a valid problem/ailment- Give an error and terminate the program")
    return consult_gemini(prompt).lower()

def main():
    print("="*44)
    print("========== WELCOME TO HEALTHBUDDY ========== ")
    print("⚠️  ⚠️  DISCLAIMER : HEALTHBUDDY IS NOT A SUBSTITUTE FOR A DOCTOR. FOR SERIOUS OR PERSISTANT ISSUES, CONSULT A PROFESSIONAL.  ⚠️  ⚠️")
    print("="*44)
    name = input("PLEASE ENTER YOUR NAME: ")
    age = input("PLEASE ENTER YOUR AGE: ")
    gender = input("PLEASE ENTER YOUR GENDER: ")
    country = input("PLEASE ENTER YOUR COUNTRY: ")
    city = input("PLEASE ENTER YOUR CITY/REGION: ")

    print(f"Hello {name}. Your entered Data is: Age: {age}, Gender: {gender}, Location: {country}, {city}")
    print("="*44)
    problem = input("Describe your health issue(s): ")
    print(f"==> Summary: {name}, Age {age}, Gender {gender}, Location {country}/{city}, Issue(s): {problem}")

    classification = classify_issue(problem)
    print(f"Type of Problem: {classification.upper()}")

    if classification == "extreme":
        severe_flag = True
        print("=> Extreme emergency detected!")
        print("=> You must go to a hospital immediately!")
        print("=> Nearest hospital search link:")
        print(maps_link("hospital", city, country))
        log_session(name, age, gender, country, city, problem, "Emergency Hospital Referral", severe_flag)
        return 

    # For severe cases, ask user override
    if classification == "severe":
        override = input("=> Do you have severe warning signs (e.g., difficulty breathing, chest pain, fainting, blood, etc.)? (yes/no): ").lower()
        user_reports_severe = (override == "yes")
    else:
        user_reports_severe = False

    severe_flag = user_reports_severe or (classification == "severe")

    if classification == "error":
        print("==> ERROR: The described issue does not appear to be a valid health problem/ailment. TERMINATING PROGRAM.")
        log_session(name, age, gender, country, city, problem, "Error - Invalid Problem", severe_flag)
        return 

    while True:
        show_menu()
        print("="*44)
        choice = input("Select an option (1-4): ")

        if choice == "1":
            print("===== REMEDIES =====")
            if severe_flag or classification == "severe":
                prompt = (f"User issue: {problem}. Provide 3–4 general comfort measures (rest, hydration, steam inhalation, etc.) in max 2 lines each. Do not include medicines. End with a reminder to seek a doctor ASAP. If {problem} is not a valid problem/ailment- Give an error and terminate the program")
            else:
                prompt = (f"Suggest 3–4 safe Indian home remedies (nuskhe) for {problem}. Each remedy must be max 2 lines. Avoid unsafe practices; include general caution. If {problem} is not a valid problem/ailment- Give an error and terminate the program")
            print(consult_gemini(prompt))
            log_session(name, age, gender, country, city, problem, "Remedies", severe_flag)

        elif choice == "2":
            print("=== MEDICINES (SIMPLE GUIDANCE) ===")
            if severe_flag or classification == "severe":
                print("==> SEVERITY DETECTED! I WON'T BE ADVISING ANY MEDICINES. YOU MAY TRY THE REMEDIES. CONSULT A PROFESSIONAL DOCTOR ASAP.")
                log_session(name, age, gender, country, city, problem, "Medicines Blocked – Severity", severe_flag)
                continue
            else:
                confirm = input("Do you want simple, general guidance only? (yes/no): ").lower()
                if confirm == "no":
                    print("==> HealthBuddy recommends consulting a qualified doctor instead of self‑medicating.")
                    log_session(name, age, gender, country, city, problem, "Medicines Declined – Doctor Referral", severe_flag)
                    continue
                else:
                    prompt = (f"For mild issues like {problem}, suggest in plain language a general type of medicine someone might ask for at a local chemist/druggist in {country}, {city}. Keep it simple, like 'general cough syrup', 'basic cold tablets', or 'simple nasal drops'. Do not give brand names or doses. End with a reminder to consult a doctor/pharmacist. If {problem} is not a valid problem/ailment- Give an error and terminate the program")
                    print(consult_gemini(prompt))
                    log_session(name, age, gender, country, city, problem, "Simple OTC Guidance", severe_flag)

        elif choice == "3":
            print("=== Doctor Referral ===")
            print("==> HealthBuddy recommends consulting a qualified doctor for proper diagnosis and treatment.")
            print("==> You can search for nearby doctors or hospitals here:")
            print(maps_link("doctor clinic", city, country))
            print(maps_link("hospital", city, country))

            print("==> Direct directions to the nearest hospital:")
            print(maps_directions("hospital", city, country))

            log_session(name, age, gender, country, city, problem, "Doctor Referral", severe_flag)

        elif choice == "4":
            print(f"GOODBYE {name}! STAY SAFE AND HEALTHY :) ")
            log_session(name, age, gender, country, city, problem, "Exit", severe_flag)
            break

        else:
            print("==> INVALID CHOICE. PLEASE INPUT 1/2/3/4.")

if __name__ == "__main__":
    main()
