import time
import re
import random
import keyboard
import hashlib

def animate_text(text, color='\033[94m'):  # Default color is blue
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.1)
    print('\033[0m')  # Reset color

def generate_suggestions(password):
    # Use APIs or other methods to generate password suggestions
    # For demonstration, generate three random suggestions
    suggestions = []
    for _ in range(3):
        suggested_password = list(password)
        random.shuffle(suggested_password)
        suggestions.append("".join(suggested_password))
    return suggestions

def analyze_password(password):
    # Analyze password strength based on some criteria (e.g., length, complexity)
    length_score = min(2, len(password) // 4)
    complexity_score = min(2, len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) // 2)

    total_score = length_score + complexity_score
    rating = min(5, max(1, total_score * 5 // 4))  # Adjusted the rating calculation
    
    return rating, length_score, complexity_score

def analyze_hash(hash_value):
    # Check the length of the hash to determine the hash algorithm
    if len(hash_value) == 32:
        return "MD5"
    elif len(hash_value) == 40:
        return "SHA-1"
    elif len(hash_value) == 64:
        return "SHA-256"
    elif len(hash_value) == 128:
        return "SHA-512"
    else:
        return "Unknown Hash Algorithm"

def main():
    animate_text("Welcome to The HashLock Sentinel")
    animate_text("Created By: Yunus S N")
    animate_text("If You Want to Exit Press Ctrl+C", '\033[92m')  # Change color to green

    try:
        while True:
            print("\nOptions:")
            print("1. Password Analysis")
            print("2. Hash Analysis")
            print("3. Exit")

            choice = input("\nEnter your choice (1, 2, or 3): ")

            if choice == '1':
                password = input("\033[94mEnter your password: \033[0m")  # Change color to blue
                rating, length_score, complexity_score = analyze_password(password)

                print("\n\033[94mPassword Report:")
                print(f"Password Strength: {rating}/5")

                if length_score == 2:
                    print("  - Good length")
                elif length_score == 1:
                    print("  - Decent length")
                else:
                    print("  - Short length, consider adding more characters")

                if complexity_score == 2:
                    print("  - Strong complexity")
                elif complexity_score == 1:
                    print("  - Moderate complexity")
                else:
                    print("  - Weak complexity, consider adding special characters")

                suggestions = generate_suggestions(password)
                print("\n\033[94mSuggestions:")
                for suggestion in suggestions:
                    print(f"  - {suggestion}")

            elif choice == '2':
                hash_value = input("\033[94mEnter the hash value: \033[0m")  # Change color to blue
                hash_algorithm = analyze_hash(hash_value)
                print(f"\n\033[94mHash Analysis:")
                print(f"Hash Algorithm: {hash_algorithm}")

            elif choice == '3':
                print("\n\033[94mGood Bye!\033[0m")
                break

            else:
                print("\033[91mInvalid choice. Please enter 1, 2, or 3.\033[0m")

    except KeyboardInterrupt:
        print("\n\033[94mGood Bye!\033[0m")

if __name__ == "__main__":
    main()
