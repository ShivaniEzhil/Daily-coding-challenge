import json
import random
from datetime import datetime
import os

CHALLENGES = [
    {"title": "Hello World", "difficulty": "Easy", "description": "Write a program that prints 'Hello, World!' to the console."},
    {"title": "Simple Calculator", "difficulty": "Easy", "description": "Take two numbers from the user and output their sum, difference, product, and quotient."},
    {"title": "Odd or Even Checker", "difficulty": "Easy", "description": "Ask the user for a number and determine if it is odd or even."},
    {"title": "Number Guessing Game", "difficulty": "Medium", "description": "The program selects a random number, and the user must guess it. Provide feedback until they guess correctly."},
    {"title": "Palindrome Checker", "difficulty": "Medium", "description": "Write a function that checks if a given string reads the same forward and backward."},
    {"title": "FizzBuzz", "difficulty": "Easy", "description": "Print numbers from 1 to 100. Replace multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and both with 'FizzBuzz'."},
    {"title": "Reverse a String", "difficulty": "Easy", "description": "Take a string input and return the string in reverse order."},
    {"title": "Multiplication Table", "difficulty": "Easy", "description": "Ask for a number and print its multiplication table up to 12."},
    {"title": "Fibonacci Sequence", "difficulty": "Medium", "description": "Generate the first n numbers of the Fibonacci sequence."},
    {"title": "Word Counter", "difficulty": "Easy", "description": "Take a sentence input and count the number of words in it."},
    {"title": "Factorial Calculator", "difficulty": "Easy", "description": "Calculate the factorial of a given number."},
    {"title": "Prime Number Checker", "difficulty": "Medium", "description": "Check if a given number is prime."},
    {"title": "Anagram Checker", "difficulty": "Medium", "description": "Determine if two strings are anagrams of each other."},
    {"title": "Array Sum", "difficulty": "Easy", "description": "Summarize all elements in an array of integers."},
    {"title": "Find the Largest Element", "difficulty": "Easy", "description": "Find the maximum value in an array of numbers."}
]

def generate_daily_challenge():
    # Pick a random challenge
    challenge = random.choice(CHALLENGES)
    challenge["date"] = datetime.now().strftime("%Y-%m-%d")
    
    # Save to data/challenge.json
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'challenge.json')
    with open(output_path, 'w') as f:
        json.dump(challenge, f, indent=4)
    
    print(f"Daily challenge generated: {challenge['title']}")

if __name__ == "__main__":
    generate_daily_challenge()
