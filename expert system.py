class ExpertSystem:
    def __init__(self):
        # Knowledge Base: Rules mapping conditions to outcomes
        self.rules = [
            {
                "condition": lambda f: f.get("fever") and f.get("cough") and f.get("shortness_of_breath"),
                "diagnosis": "Possible Respiratory Infection (e.g., Pneumonia/COVID-19)",
                "advice": "Consult a healthcare provider immediately for an evaluation.",
                "reason": "You reported fever, cough, AND shortness of breath."
            },
            {
                "condition": lambda f: f.get("fever") and f.get("cough") and not f.get("shortness_of_breath"),
                "diagnosis": "Possible Viral Infection (e.g., Flu/Cold)",
                "advice": "Rest, stay hydrated, and monitor your temperature.",
                "reason": "You have a fever and cough, but no difficulty breathing."
            },
            {
                "condition": lambda f: f.get("sneezing") and f.get("itchy_eyes") and not f.get("fever"),
                "diagnosis": "Possible Seasonal Allergies",
                "advice": "Consider over-the-counter antihistamines and avoid triggers.",
                "reason": "You have sneezing and itchy eyes without a fever."
            },
            {
                "condition": lambda f: f.get("headache") and f.get("sensitivity_to_light"),
                "diagnosis": "Possible Migraine",
                "advice": "Rest in a dark, quiet room and stay hydrated.",
                "reason": "Headache paired with light sensitivity strongly indicates a migraine."
            }
        ]

    def ask_user(self, question):
        """Helper function to collect boolean facts from the user."""
        response = input(f"{question} (y/n): ").strip().lower()
        return response == 'y'

    def run(self):
        print("=== Medical Symptom Advisory Expert System ===")
        print("Answer the following questions with 'y' for Yes or 'n' for No.\n")

        # Fact Acquisition (User Interface / Working Memory)
        facts = {
            "fever": self.ask_user("Do you have a fever?"),
            "cough": self.ask_user("Do you have a cough?"),
            "shortness_of_breath": self.ask_user("Are you experiencing shortness of breath?"),
            "sneezing": self.ask_user("Are you sneezing frequently?"),
            "itchy_eyes": self.ask_user("Do you have itchy or watery eyes?"),
            "headache": self.ask_user("Do you have a headache?"),
            "sensitivity_to_light": self.ask_user("Are your eyes unusually sensitive to light?"),
        }

        print("\n--- Diagnostic Results ---")
        
        # Inference Engine: Matching working memory (facts) against rules
        matched = False
        for rule in self.rules:
            if rule["condition"](facts):
                print(f"\nDiagnosis: {rule['diagnosis']}")
                print(f"Advice:    {rule['advice']}")
                print(f"Reasoning: {rule['reason']}")
                matched = True
                break

        if not matched:
            print("\nDiagnosis: Undetermined")
            print("Advice:    Your symptoms do not match known patterns in this knowledge base.")
            print("Reasoning: No logical IF-THEN rules were satisfied by the provided inputs.")

# Run the expert system
if __name__ == "__main__":
    system = ExpertSystem()
    system.run()