import requests
print("Ausbildung Portfolio Analyzer")
german_level=input("german level: ").strip().lower()
english_level=input("english level: ").strip().lower()
high_school_grade=float(input("high school grade: "))
real_project_count=int(input("real project count: "))
cv_ready = input("Professional CV ready? (yes/no): ")
github_ready = input("GitHub and project links ready? (yes/no): ")
target_role_clear = input("Target Ausbildung role clear? (yes/no): ")
interview_preparation = input("Interview preparation level (0-3): ")
application_strategy = input("Company research and application strategy level (0-3): ")
relocation_plan = input("Start date and relocation plan clear? (yes/no): ")
it_education = input("IT-related education? (yes/no): ")
academic_project = input("Relevant academic/technical project? (yes/no): ")
learning_continuity = input("Actively continuing to learn? (yes/no): ")
git_usage = input("Uses Git/GitHub regularly? (yes/no): ")
project_quality = int(input("Real working projects score (0-8): "))
project_diversity = int(input("Project diversity score (0-7): "))
programming_basics = int(input("Programming fundamentals score (0-6): "))
api_experience = input("API experience? (yes/no): ")
database_experience = input("Database experience? (yes/no): ")
documentation_quality = int(input("README/documentation score (0-2): "))
if german_level == "a2":
    german_score = 6
elif german_level == "b1":
    german_score = 11
elif german_level == "a1":
    german_score = 3
elif german_level == "b2":
    german_score = 15
elif german_level == "c1":
    german_score = 18
else :
    german_score = 0
print("German_score:", german_score)
if english_level == "a1":
    english_score = 1
elif english_level == "a2":
    english_score = 1
elif english_level == "b1":
    english_score = 4 
elif english_level == "b2":
    english_score = 6
elif english_level == "c1":
    english_score = 7
else :
    english_score = 0
print("english_score:",english_score)
language_score = german_score + english_score
print("language readiness score:", language_score)
if high_school_grade >= 90:
    school_score = 8
elif high_school_grade >= 80:
    school_score = 7
elif high_school_grade >= 70:
    school_score = 5
elif high_school_grade >= 60:
    school_score = 3
elif high_school_grade >= 50:
    school_score = 1
else:
    school_score = 0
print("School score:", school_score)
if it_education == "yes":
    it_education_score = 5
else:
    it_education_score = 0

if academic_project == "yes":
    academic_project_score = 4
else:
    academic_project_score = 0

if learning_continuity == "yes":
    learning_continuity_score = 3
else:
    learning_continuity_score = 0
academic_score = school_score + it_education_score + academic_project_score + learning_continuity_score
print("Academic profile score:", academic_score)
if cv_ready == "yes":
    cv_score = 5
else:
    cv_score = 0

if github_ready == "yes":
    github_score = 4
else:
    github_score = 0

if target_role_clear == "yes":
    target_role_score = 3
else:
    target_role_score = 0

interview_score = int(interview_preparation)
if interview_score > 3:
    interview_score = 3
elif interview_score < 0:
    interview_score = 0

strategy_score = int(application_strategy)
if strategy_score > 3:
    strategy_score = 3
elif strategy_score < 0:
    strategy_score = 0

if relocation_plan == "yes":
    relocation_score = 2
else:
    relocation_score = 0

application_readiness_score = (
    cv_score
    + github_score
    + target_role_score
    + interview_score
    + strategy_score
    + relocation_score
)

print("Application readiness score:", application_readiness_score)
if git_usage == "yes":
    git_score = 5
else:
    git_score = 0

if project_quality > 8:
    project_quality = 8
elif project_quality < 0:
    project_quality = 0

if project_diversity > 7:
    project_diversity = 7
elif project_diversity < 0:
    project_diversity = 0

if programming_basics > 6:
    programming_basics = 6
elif programming_basics < 0:
    programming_basics = 0

if api_experience == "yes":
    api_score = 4
else:
    api_score = 0

if database_experience == "yes":
    database_score = 3
else:
    database_score = 0

if documentation_quality > 2:
    documentation_quality = 2
elif documentation_quality < 0:
    documentation_quality = 0


github_username = input("GitHub username: ")
github_url = f"https://api.github.com/users/{github_username}"
response = requests.get(github_url)

if response.status_code == 200:
    github_data = response.json()
    public_repos = github_data["public_repos"]

    if public_repos == 0:
        github_repo_score = 0
    elif public_repos == 1:
        github_repo_score = 2
    elif public_repos == 2:
        github_repo_score = 4
    else:
        github_repo_score = 5
    print("GitHub repo score:", github_repo_score)   
    print("Public repositories:", public_repos)
else:
    print("GitHub profile could not be found.")
    github_repo_score = 0
technical_score = (
    github_repo_score
    + project_quality
    + project_diversity
    + programming_basics
    + api_score
    + database_score
    + documentation_quality
)

print("Technical portfolio score:", technical_score)
overall_score = (
    language_score
    + academic_score
    + application_readiness_score
    + technical_score
)

print("Overall Ausbildung readiness score:", overall_score, "/100")
print("\nStrong points:")

if academic_score >= 16:
    print("- Strong academic profile")

if application_readiness_score >= 16:
    print("- Good application preparation")

if technical_score >= 25:
    print("- Strong technical portfolio")

if language_score >= 18:
    print("- Strong language readiness")
print("\nWeak points:")

if language_score < 15:
    print("- Language readiness should be improved")

if technical_score < 20:
    print("- Technical portfolio needs more development")

if academic_score < 12:
    print("- Academic profile could be strengthened")

if application_readiness_score < 14:
    print("- Application preparation needs improvement")
print("\nRecommended next steps:")

if language_score < 15:
    print("- Improve German and English language skills")

if technical_score < 20:
    print("- Build more diverse software projects")

if api_score == 0:
    print("- Gain API experience")

if database_score == 0:
    print("- Gain database experience")

if interview_score < 3:
    print("- Continue interview preparation")
print("\nNote:")
print("This score measures application readiness, not the probability of being hired.")   