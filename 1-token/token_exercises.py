"""
Token Exercises - Interactive Practice
=======================================
Test your understanding of tokenization through hands-on exercises.

Complete these exercises to solidify your knowledge:
1. Token counting predictions
2. Cost calculations
3. Prompt optimization
4. Language comparisons
5. Context window management

Run this file and follow the prompts!
"""

import tiktoken
from typing import List, Tuple

class TokenExercises:
    def __init__(self):
        self.encoding = tiktoken.get_encoding("cl100k_base")
        self.score = 0
        self.total_questions = 0
    
    def print_header(self, title: str):
        """Print exercise header"""
        print("\n" + "=" * 70)
        print(f"🎯 {title}")
        print("=" * 70 + "\n")
    
    def check_answer(self, user_answer: int, correct_answer: int, text: str):
        """Check user's answer and provide feedback"""
        self.total_questions += 1
        difference = abs(user_answer - correct_answer)
        percentage_error = (difference / correct_answer) * 100 if correct_answer > 0 else 0
        
        if user_answer == correct_answer:
            print("✅ Correct!")
            self.score += 1
        elif percentage_error <= 10:
            print(f"🟡 Close! Actual: {correct_answer} tokens (you were off by {difference})")
            self.score += 0.5
        else:
            print(f"❌ Not quite. Actual: {correct_answer} tokens (you guessed {user_answer})")
        
        # Show the actual tokenization
        tokens = self.encoding.encode(text)
        decoded_tokens = [self.encoding.decode([t]) for t in tokens]
        print(f"   Breakdown: {decoded_tokens}\n")
    
    def exercise_1_token_counting(self):
        """Exercise 1: Predict token counts"""
        self.print_header("Exercise 1: Token Count Prediction")
        
        print("Predict how many tokens each text will produce.")
        print("Remember: 1 token ≈ 4 characters or ¾ of a word\n")
        
        test_cases = [
            "Hello, world!",
            "GPT-4 is amazing",
            "I love programming in Python",
            "The quick brown fox jumps over the lazy dog",
            "tokenization",
            "supercalifragilisticexpialidocious",
            "def calculate_sum(numbers):",
            "¿Cómo estás hoy?",
            "12345",
            "🚀 Let's go!"
        ]
        
        for i, text in enumerate(test_cases, 1):
            print(f"Question {i}: '{text}'")
            try:
                user_answer = int(input("Your prediction (number of tokens): "))
                actual_tokens = len(self.encoding.encode(text))
                self.check_answer(user_answer, actual_tokens, text)
            except ValueError:
                print("❌ Invalid input. Please enter a number.\n")
            except KeyboardInterrupt:
                print("\n\nExercise interrupted. Moving to next section...\n")
                break
    
    def exercise_2_cost_calculator(self):
        """Exercise 2: Calculate API costs"""
        self.print_header("Exercise 2: API Cost Calculator")
        
        print("Build a cost calculator for API usage.")
        print("\nPricing (example):")
        print("  - GPT-4 Input: $0.03 per 1K tokens")
        print("  - GPT-4 Output: $0.06 per 1K tokens")
        print("  - GPT-3.5 Input: $0.001 per 1K tokens")
        print("  - GPT-3.5 Output: $0.002 per 1K tokens\n")
        
        scenarios = [
            {
                "model": "GPT-4",
                "prompt": "Write a detailed explanation of machine learning in 500 words.",
                "expected_output_tokens": 700,
                "input_rate": 0.03,
                "output_rate": 0.06
            },
            {
                "model": "GPT-3.5",
                "prompt": "Summarize this article: " + ("AI is transforming industries. " * 50),
                "expected_output_tokens": 100,
                "input_rate": 0.001,
                "output_rate": 0.002
            }
        ]
        
        for i, scenario in enumerate(scenarios, 1):
            print(f"\nScenario {i} ({scenario['model']}):")
            print(f"Prompt: '{scenario['prompt'][:60]}...'")
            print(f"Expected output: {scenario['expected_output_tokens']} tokens")
            
            input_tokens = len(self.encoding.encode(scenario['prompt']))
            print(f"\nInput tokens: {input_tokens}")
            
            total_cost = (
                (input_tokens / 1000) * scenario['input_rate'] +
                (scenario['expected_output_tokens'] / 1000) * scenario['output_rate']
            )
            
            print(f"Total cost: ${total_cost:.4f}")
            
            try:
                user_cost = float(input("What's your calculated cost? $"))
                if abs(user_cost - total_cost) < 0.0001:
                    print("✅ Correct!")
                    self.score += 1
                else:
                    print(f"❌ Not quite. Correct answer: ${total_cost:.4f}")
                self.total_questions += 1
            except ValueError:
                print("❌ Invalid input.\n")
            except KeyboardInterrupt:
                print("\n\nExercise interrupted. Moving to next section...\n")
                break
    
    def exercise_3_prompt_optimization(self):
        """Exercise 3: Optimize prompts for fewer tokens"""
        self.print_header("Exercise 3: Prompt Optimization")
        
        print("Rewrite these prompts to use fewer tokens while keeping the meaning.")
        print("Goal: Reduce token count by at least 20%\n")
        
        prompts = [
            "Could you please, please help me understand how to solve this mathematical problem?",
            "I would really appreciate it if you could explain to me the concept of machine learning.",
            "Can you tell me what the weather is like today in New York City?"
        ]
        
        for i, prompt in enumerate(prompts, 1):
            original_tokens = len(self.encoding.encode(prompt))
            print(f"\nPrompt {i}:")
            print(f"Original: '{prompt}'")
            print(f"Original tokens: {original_tokens}")
            print(f"Target: {int(original_tokens * 0.8)} tokens or less")
            
            try:
                optimized = input("\nYour optimized version: ")
                optimized_tokens = len(self.encoding.encode(optimized))
                reduction = ((original_tokens - optimized_tokens) / original_tokens) * 100
                
                print(f"Your version: {optimized_tokens} tokens")
                print(f"Reduction: {reduction:.1f}%")
                
                if optimized_tokens < original_tokens * 0.8:
                    print("✅ Great optimization!")
                    self.score += 1
                elif optimized_tokens < original_tokens:
                    print("🟡 Good, but can you reduce it more?")
                    self.score += 0.5
                else:
                    print("❌ No improvement. Try to be more concise.")
                
                self.total_questions += 1
            except KeyboardInterrupt:
                print("\n\nExercise interrupted. Moving to next section...\n")
                break
    
    def exercise_4_language_comparison(self):
        """Exercise 4: Compare tokenization across languages"""
        self.print_header("Exercise 4: Multilingual Tokenization")
        
        print("Compare how the same phrase tokenizes in different languages.\n")
        
        phrase = "Hello, how are you?"
        translations = {
            "English": "Hello, how are you?",
            "Spanish": "Hola, ¿cómo estás?",
            "French": "Bonjour, comment allez-vous?",
            "Chinese": "你好，你好吗？",
            "Japanese": "こんにちは、お元気ですか？"
        }
        
        print("Which language will use the MOST tokens?")
        print("Which will use the LEAST?\n")
        
        for lang, text in translations.items():
            tokens = len(self.encoding.encode(text))
            print(f"{lang:<10}: {tokens} tokens - '{text}'")
        
        print()
        try:
            most_tokens = input("Language with MOST tokens: ").strip()
            least_tokens = input("Language with LEAST tokens: ").strip()
            
            token_counts = {lang: len(self.encoding.encode(text)) 
                          for lang, text in translations.items()}
            actual_most = max(token_counts, key=token_counts.get)
            actual_least = min(token_counts, key=token_counts.get)
            
            correct = 0
            if most_tokens.lower() == actual_most.lower():
                print(f"✅ Correct! {actual_most} has the most ({token_counts[actual_most]} tokens)")
                correct += 1
            else:
                print(f"❌ Not quite. {actual_most} has the most ({token_counts[actual_most]} tokens)")
            
            if least_tokens.lower() == actual_least.lower():
                print(f"✅ Correct! {actual_least} has the least ({token_counts[actual_least]} tokens)")
                correct += 1
            else:
                print(f"❌ Not quite. {actual_least} has the least ({token_counts[actual_least]} tokens)")
            
            self.score += correct / 2
            self.total_questions += 1
            
        except KeyboardInterrupt:
            print("\n\nExercise interrupted. Moving to next section...\n")
    
    def exercise_5_context_window(self):
        """Exercise 5: Manage context windows"""
        self.print_header("Exercise 5: Context Window Management")
        
        print("You have a 1000-token context window.")
        print("You need to fit a system message, user prompt, and response.\n")
        
        system_message = "You are a helpful AI assistant specialized in explaining complex topics simply."
        user_prompt = "Explain quantum computing in simple terms that a high school student can understand."
        
        system_tokens = len(self.encoding.encode(system_message))
        prompt_tokens = len(self.encoding.encode(user_prompt))
        
        print(f"System message: {system_tokens} tokens")
        print(f"User prompt: {prompt_tokens} tokens")
        print(f"Used so far: {system_tokens + prompt_tokens} tokens")
        print(f"Remaining for response: ? tokens")
        
        try:
            user_answer = int(input("\nHow many tokens remain for the response? "))
            correct_answer = 1000 - system_tokens - prompt_tokens
            
            if user_answer == correct_answer:
                print(f"✅ Correct! {correct_answer} tokens available")
                self.score += 1
            else:
                print(f"❌ Not quite. Correct answer: {correct_answer} tokens")
                print(f"   Calculation: 1000 - {system_tokens} - {prompt_tokens} = {correct_answer}")
            
            self.total_questions += 1
            
            # Bonus question
            print("\n🎁 Bonus: If the average response uses 3 tokens per word,")
            print("   approximately how many words can fit in the response?")
            
            user_words = int(input("Estimated words: "))
            correct_words = correct_answer // 3
            
            if abs(user_words - correct_words) <= 10:
                print(f"✅ Correct (or very close)! Approximately {correct_words} words")
                self.score += 0.5
            else:
                print(f"❌ Not quite. Approximately {correct_words} words")
            
            self.total_questions += 0.5
            
        except ValueError:
            print("❌ Invalid input.\n")
        except KeyboardInterrupt:
            print("\n\nExercise interrupted.\n")
    
    def show_final_score(self):
        """Display final score and feedback"""
        self.print_header("Final Score")
        
        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        
        print(f"Your Score: {self.score:.1f} / {self.total_questions}")
        print(f"Percentage: {percentage:.1f}%\n")
        
        if percentage >= 90:
            print("🏆 Excellent! You have a strong understanding of tokenization!")
            print("   You're ready to move on to Phase 2: Embeddings")
        elif percentage >= 75:
            print("🎉 Great job! You understand most tokenization concepts.")
            print("   Review the areas you missed, then move to Phase 2")
        elif percentage >= 60:
            print("👍 Good start! You grasp the basics.")
            print("   Review intro.md and run token_exploration.py again")
        else:
            print("📚 Keep learning! Tokenization takes practice.")
            print("   Review the materials and try these exercises again")
        
        print("\n" + "=" * 70)
        print("Next steps:")
        print("  1. Review any concepts you found challenging")
        print("  2. Experiment with token_exploration.py")
        print("  3. Try the OpenAI tokenizer tool online")
        print("  4. Move to Phase 2: Embeddings when ready")
        print("=" * 70 + "\n")

def main():
    """Run all exercises"""
    print("\n" + "=" * 70)
    print("🎓 TOKEN EXERCISES - Interactive Learning")
    print("=" * 70)
    print("\nWelcome! Complete these exercises to test your understanding.")
    print("You can skip any exercise by pressing Ctrl+C during input.\n")
    input("Press Enter to begin...")
    
    exercises = TokenExercises()
    
    try:
        exercises.exercise_1_token_counting()
        exercises.exercise_2_cost_calculator()
        exercises.exercise_3_prompt_optimization()
        exercises.exercise_4_language_comparison()
        exercises.exercise_5_context_window()
    except KeyboardInterrupt:
        print("\n\nExercises interrupted by user.")
    finally:
        exercises.show_final_score()

if __name__ == "__main__":
    main()
