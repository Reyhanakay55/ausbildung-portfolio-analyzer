# Ausbildung Portfolio Analyzer

A Python command-line tool that evaluates Ausbildung application readiness based on language skills, academic background, application preparation, technical portfolio, and GitHub activity.

## Features

- Calculates a Language Readiness Score
- Calculates an Academic Profile Score
- Calculates an Application Readiness Score
- Calculates a Technical Portfolio Score
- Calculates an Overall Ausbildung Readiness Score out of 100
- Connects to the GitHub API
- Reads public repository count from a GitHub profile
- Gives strong points
- Identifies weak points
- Suggests recommended next steps
- Handles invalid numeric input
- Accepts flexible language input such as A2, a2, or A2 with spaces

## Technologies

- Python
- Git and GitHub
- GitHub REST API
- requests
- JSON
- Conditional logic
- Functions
- Input validation

## How to Run

1. Install the required dependency:

```bash
pip install -r requirements.txt
```

2. Run the program:

```bash
python3 main.py
```

3. Answer the questions shown in the terminal.

## Scoring Categories

- Technical Portfolio: 35 points
- Language Readiness: 25 points
- Academic Profile: 20 points
- Application Readiness: 20 points

Total: 100 points

## GitHub Analysis

The program asks for a GitHub username and retrieves the number of public repositories using the GitHub API.

The repository count is converted into a GitHub repository score and included in the Technical Portfolio Score.

## Example Output

```text
Technical portfolio score: 19
Overall Ausbildung readiness score: 68 /100

Strong points:
- Strong academic profile
- Good application preparation

Weak points:
- Language readiness should be improved
- Technical portfolio needs more development

Recommended next steps:
- Improve German and English language skills
- Build more diverse software projects
- Gain database experience
- Continue interview preparation
```

## What I Learned

During this project I practiced:

- Working with Python functions
- Using if / elif / else conditions
- Validating numeric user input
- Working with the GitHub REST API
- Reading JSON data from an API response
- Using the requests library
- Creating a weighted scoring system
- Handling invalid input without crashing the program
- Using Git and GitHub during project development

## Future Improvements

- Analyze individual GitHub repositories in more detail
- Check README quality automatically
- Analyze programming language diversity
- Add database support
- Save previous analysis results
- Add a graphical user interface
- Provide more detailed scoring explanations

## Disclaimer

This score measures application readiness based on the entered profile data and GitHub activity.

It is not a real hiring probability.