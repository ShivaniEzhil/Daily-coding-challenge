# 🚀 Daily Coding Challenge Generator

An automated system that picks a fresh programming challenge every day and displays it on a sleek, modern dashboard. Perfect for maintaining your GitHub contribution streak while sharpening your coding skills!

## 🌟 Features

- **Automated Daily Commits**: Uses GitHub Actions to pick a new challenge at midnight (UTC) every day.
- **Curated Dataset**: Pulled from a high-quality list of challenges with direct links to LeetCode for solving.
- **Premium Dashboard**: A minimalist, dark-themed responsive frontend to view today's task.
- **Zero Maintenance**: Once set up, it runs entirely on GitHub's servers—no local hosting required.

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript
- **Backend**: Python (Challenge selection logic)
- **Automation**: GitHub Actions (Cron scheduler)
- **Data**: JSON-based curated challenge pool

## 🚀 How it Works

1. **The Scheduler**: A GitHub Action runs every 24 hours.
2. **The Logic**: A Python script selects a random problem from `data/challenges_pool.json`.
3. **The Update**: The script updates `data/challenge.json`, creating a new commit in your repository.
4. **The Display**: The frontend fetches and displays the latest challenge automatically.

## 🖥️ Viewing the Dashboard

You can view your live dashboard at:
[https://shivaniezhil.github.io/Daily-coding-challenge/frontend/](https://shivaniezhil.github.io/Daily-coding-challenge/frontend/)

## 📝 How to Add More Challenges

Simply add a new entry to `data/challenges_pool.json` in this format:
```json
{
    "title": "Problem Name",
    "difficulty": "Easy",
    "description": "Short description of the task.",
    "link": "https://leetcode.com/link-to-problem"
}
```

---
Happy Coding! 💻
