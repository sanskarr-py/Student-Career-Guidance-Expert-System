Student Career Guidance Expert System

A Python-based career guidance application that asks students about their interests and uses a weighted rule-based expert system to suggest suitable career paths.

The project was built as a practical way to understand how an expert system can use a knowledge base, user input, and scoring rules to make recommendations.

Features

Simple desktop GUI built with Tkinter

20 interest-based questions

Four interest levels:

No Interest

Low Interest

Medium Interest

High Interest

Weighted career matching

Match percentage for each career

Top 3 career recommendations

Suggested courses for the best match

Short explanation of the recommended career

Scrollable interface

Clear/reset button

Windows and Linux mouse-wheel support

No external Python packages required

Career Areas

The current knowledge base includes:

Computer Science

Medicine & Healthcare

Engineering

Business & Management

Graphic & UI/UX Design

Writing & Media

Teaching & Education

Agriculture & Life Science

Sports & Fitness

Accounting & Finance

How It Works

The system follows a simple expert-system workflow:

Student Input
     ↓
Interest Levels
     ↓
Knowledge Base
     ↓
Weighted Score Calculation
     ↓
Career Ranking
     ↓
Top Career Recommendations

Each career has a group of related interests with different weights.

For example, Computer Science gives more importance to:

Programming

Technology

Problem Solving

Mathematics

The selected interest level is converted into a score:

No Interest     = 0
Low Interest    = 1
Medium Interest = 2
High Interest   = 3

The system combines these values with the career weights and calculates a match percentage.

Technologies Used

Python

Tkinter

ttk

Rule-based expert system

Weighted scoring

Requirements

You only need Python installed on your computer.

Tkinter is included with most standard Python installations on Windows. On some Linux distributions, Tkinter may need to be installed separately.

How to Run

Clone the repository:

git clone https://github.com/your-username/student-career-guidance-expert-system.git

Open the project folder:

cd student-career-guidance-expert-system

Run the program:

python "Pasted code(1).py"

If you rename the Python file, use the new filename instead.

For systems where python3 is used:

python3 "Pasted code(1).py"

Project Structure

student-career-guidance-expert-system/
│
├── Pasted code(1).py
└── README.md

You can rename Pasted code(1).py to something cleaner such as career_expert_system.py before publishing the repository.

Example

Suppose a student selects high interest in:

Programming

Mathematics

Technology

Problem Solving

The system will likely give Computer Science a high match score and show related courses such as BSc CSIT, BIT, Computer Engineering, and Software Engineering.

The system can also show other career options when their match scores are strong enough.

Why I Built This

I built this project to learn how Artificial Intelligence and Expert Systems work in a practical way.

Instead of using machine learning, I used a knowledge base and weighted rules so that the recommendation process stays simple and easy to understand.

This also makes the project useful for learning concepts such as:

Knowledge representation

Rule-based reasoning

User input processing

Inference

Decision making

Limitations

This is an educational project, so the recommendations should not be treated as professional career advice.

The current system mainly considers interests. Real career decisions can also depend on academic performance, skills, personality, financial factors, available opportunities, and personal goals.

Future Improvements

Some improvements I would like to add:

More career options

More detailed career information

Academic performance as an input

Skills and personality-based questions

Better explanations for each recommendation

Saving user results

A more modern interface

Web-based version of the expert system

Author

Sanskar Acharya