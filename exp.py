class ExpertSystem:
    def __init__(self):
        # Knowledge Base: Rules mapping conditions to outcomes
        self.rules = [
            # --- GAMING & HEAVY 3D ---
            {
                "condition": lambda f: f.get("use_case") == "gaming" and f.get("budget") == "high",
                "tier": "Enthusiast Gaming / Heavy 3D",
                "recommended_specs": "Intel Core Ultra 9 / Ryzen AI Max, RTX 5070 Ti / 5080, 32GB DDR5 RAM, 1TB+ Gen4 SSD, 240Hz OLED/QHD Display",
                "laptop_examples": "ASUS ROG Zephyrus G16, Razer Blade 16, Lenovo Legion Pro 7i",
                "reason": "High-budget gaming demands high TGP dedicated graphics, high refresh rate displays, and advanced thermal management."
            },
            {
                "condition": lambda f: f.get("use_case") == "gaming" and f.get("budget") in ["medium", "low"],
                "tier": "Budget / Mid-Range Gaming",
                "recommended_specs": "Intel Core i5 / Ryzen 5/7, RTX 4050 / RTX 3050, 16GB DDR5 RAM, 512GB SSD, 144Hz FHD Display",
                "laptop_examples": "ASUS TUF Gaming A15, Acer Nitro V 15, Lenovo LOQ",
                "reason": "Entry-to-mid level budget prioritizes GPU raw power per dollar while retaining an upgradeable RAM/storage slot."
            },

            # --- CREATIVE / VIDEO EDITING / 3D RENDERING ---
            {
                "condition": lambda f: f.get("use_case") == "creative" and f.get("os") == "mac",
                "tier": "Professional Creative (macOS)",
                "recommended_specs": "Apple M-Series Pro/Max Chip, 18GB–36GB Unified Memory, 512GB/1TB SSD, Liquid Retina XDR",
                "laptop_examples": "MacBook Pro 14 / 16 (M-Series Pro/Max)",
                "reason": "macOS applications (Final Cut, DaVinci, Logic) benefit heavily from Apple Silicon unified memory bandwidth and color-accurate displays."
            },
            {
                "condition": lambda f: f.get("use_case") == "creative" and f.get("os") != "mac",
                "tier": "Professional Creative (Windows)",
                "recommended_specs": "Intel Core Ultra 7/9 or AMD Ryzen 9, Dedicated RTX 4060/5060, 32GB RAM, 100% DCI-P3 / OLED Screen",
                "laptop_examples": "ASUS ROG Zephyrus G16 (OLED), Dell XPS 16, HP Envy x360",
                "reason": "Creative workloads on Windows require a color-accurate display paired with CUDA acceleration for rendering engines."
            },

            # --- PRODUCTIVITY / EVERYDAY / SCHOOL ---
            {
                "condition": lambda f: f.get("use_case") == "productivity" and f.get("portability") == "high" and f.get("os") == "mac",
                "tier": "Ultraportable Productivity (Mac)",
                "recommended_specs": "Apple M-Series Chip, 16GB Unified Memory, 256GB/512GB SSD, 13.6-inch Liquid Retina",
                "laptop_examples": "MacBook Air 13 / 15",
                "reason": "MacBook Air offers class-leading battery life (>15 hrs), silent fanless design, and high portability."
            },
            {
                "condition": lambda f: f.get("use_case") == "productivity" and f.get("portability") == "high" and f.get("os") != "mac",
                "tier": "Ultraportable Windows / Copilot+ PC",
                "recommended_specs": "Snapdragon X Elite / Intel Core Ultra 5 / Ryzen 7, 16GB RAM, 512GB SSD, <1.3kg Weight",
                "laptop_examples": "ASUS Zenbook 14 OLED, Lenovo Slim 5, HP OmniBook Ultra",
                "reason": "Prioritizes low weight, long battery life, high-efficiency processors, and crisp OLED/IPS displays."
            },

            # --- BUDGET / GENERAL BROWSING ---
            {
                "condition": lambda f: f.get("budget") == "low" and f.get("use_case") == "productivity",
                "tier": "Budget Everyday Computing",
                "recommended_specs": "AMD Ryzen 5 / Intel Core i3 or i5, 8GB–16GB RAM, 512GB SSD, 1080p FHD Display",
                "laptop_examples": "Acer Aspire 3 / Lite, Lenovo IdeaPad Slim 3, ASUS Vivobook 15",
                "reason": "Maximizes core performance for web, office applications, and streaming while keeping component costs down."
            }
        ]

    def ask_user(self, question):
        """Helper function to collect boolean facts from the user."""
        response = input(f"{question} (y/n): ").strip().lower()
        return response == 'y'

    def run(self):
        print("=== Laptop Recommendation Expert System ===")
        print("Answer the questions below to match your needs with optimal specs.\n")

        # Fact Acquisition
        print("1. What is your primary use case?")
        print("   a) Gaming / Heavy 3D Graphics")
        print("   b) Video Editing / Content Creation / Graphic Design")
        print("   c) Office Work / School / General Browsing")
        use_choice = input("Choice (a/b/c): ").strip().lower()
        use_map = {'a': 'gaming', 'b': 'creative', 'c': 'productivity'}

        print("\n2. What is your budget category?")
        print("   a) Under $700 / Budget")
        print("   b) $700 – $1,400 / Mid-Range")
        print("   c) Above $1,400 / High-End")
        budget_choice = input("Choice (a/b/c): ").strip().lower()
        budget_map = {'a': 'low', 'b': 'medium', 'c': 'high'}

        print("\n3. Do you prefer macOS or Windows/Linux?")
        print("   a) macOS (Apple)")
        print("   b) Windows / No Preference")
        os_choice = input("Choice (a/b): ").strip().lower()
        os_map = {'a': 'mac', 'b': 'windows'}

        print("\n4. Is battery life and light weight (<1.4 kg) your top priority?")
        port_choice = input("   (y/n): ").strip().lower() == 'y'

        # Working Memory
        facts = {
            "use_case": use_map.get(use_choice, "productivity"),
            "budget": budget_map.get(budget_choice, "medium"),
            "os": os_map.get(os_choice, "windows"),
            "portability": "high" if port_choice else "normal"
        }

        print("\n--- Diagnostic Results ---")

        # Inference Engine: Matching working memory (facts) against rules
        matched = False
        for rule in self.rules:
            if rule["condition"](facts):
                print(f"\nDiagnosis: {rule['tier']}")
                print(f"Recommended Specs: {rule['recommended_specs']}")
                print(f"Examples: {rule['laptop_examples']}")
                print(f"Reasoning: {rule['reason']}")
                matched = True
                break

        if not matched:
            print("\nDiagnosis: Undetermined")
            print("Advice:    Your choices do not match any known recommendation profile.")
            print("Reasoning: No logical IF-THEN rules were satisfied by the provided inputs.")

# Run the expert system
if __name__ == "__main__":
    system = ExpertSystem()
    system.run()