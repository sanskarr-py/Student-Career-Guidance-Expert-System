import tkinter as tk
from tkinter import ttk, messagebox

INTEREST_LEVELS = {
    "No Interest": 0,
    "Low Interest": 1,
    "Medium Interest": 2,
    "High Interest": 3
}


CAREERS = {
    "Computer Science": {
        "description": "A strong match for students interested in programming, technology, mathematics, and problem solving.",
        "courses": "BSc CSIT, BIT, Computer Engineering, Software Engineering",
        "weights": {
            "programming": 5,
            "math": 4,
            "technology": 5,
            "problem_solving": 5,
            "creativity": 2
        }
    },

    "Medicine & Healthcare": {
        "description": "Suitable for students interested in biology, chemistry, helping people, and healthcare.",
        "courses": "MBBS, BDS, BPharm, BSc Nursing, Public Health",
        "weights": {
            "biology": 5,
            "chemistry": 4,
            "helping": 5,
            "communication": 2,
            "teaching": 1
        }
    },

    "Engineering": {
        "description": "A good match for students who enjoy mathematics, physics, machines, technology, and problem solving.",
        "courses": "BE/BTech Civil, Computer, Electrical, Electronics, Mechanical Engineering",
        "weights": {
            "physics": 5,
            "math": 5,
            "machines": 4,
            "problem_solving": 5,
            "technology": 3
        }
    },

    "Business & Management": {
        "description": "Suitable for students interested in business, leadership, communication, and entrepreneurship.",
        "courses": "BBA, BBM, BBS, BIM, MBA",
        "weights": {
            "business": 5,
            "leadership": 5,
            "communication": 4,
            "accounting": 4,
            "creativity": 2
        }
    },

    "Graphic & UI/UX Design": {
        "description": "A strong match for creative students interested in drawing, design, visual communication, and creativity.",
        "courses": "Graphic Design, Multimedia, UI/UX Design, Fine Arts, Digital Media",
        "weights": {
            "drawing": 5,
            "creativity": 5,
            "designing": 5,
            "communication": 2,
            "writing": 1
        }
    },

    "Writing & Media": {
        "description": "Suitable for students who enjoy writing, communication, creativity, and expressing ideas.",
        "courses": "Journalism, Mass Communication, English, Media Studies, Content Creation",
        "weights": {
            "writing": 5,
            "communication": 5,
            "creativity": 4,
            "teaching": 1
        }
    },

    "Teaching & Education": {
        "description": "A good match for students who enjoy teaching, communication, and helping others learn.",
        "courses": "B.Ed, M.Ed, Education, Subject-specific Bachelor's degrees",
        "weights": {
            "teaching": 5,
            "communication": 5,
            "helping": 4,
            "writing": 2,
            "leadership": 2
        }
    },

    "Agriculture & Life Science": {
        "description": "Suitable for students interested in biology, agriculture, science, and working with plants or natural systems.",
        "courses": "BSc Agriculture, Forestry, Horticulture, Animal Science, Biotechnology",
        "weights": {
            "agriculture": 5,
            "biology": 5,
            "chemistry": 2,
            "helping": 2
        }
    },

    "Sports & Fitness": {
        "description": "Suitable for students with strong interest in sports, physical activity, coaching, and fitness.",
        "courses": "Sports Management, Physical Education, Sports Science, Fitness Training",
        "weights": {
            "sports": 5,
            "teaching": 2,
            "leadership": 3,
            "helping": 2
        }
    },

    "Accounting & Finance": {
        "description": "A good match for students interested in accounting, mathematics, business, and financial decision-making.",
        "courses": "BBA, BBS, CA, ACCA, Finance, Economics",
        "weights": {
            "accounting": 5,
            "math": 4,
            "business": 4,
            "problem_solving": 3,
            "communication": 2
        }
    }
}


QUESTIONS = [
    ("programming", "How interested are you in Programming?"),
    ("math", "How interested are you in Mathematics?"),
    ("biology", "How interested are you in Biology?"),
    ("chemistry", "How interested are you in Chemistry?"),
    ("physics", "How interested are you in Physics?"),
    ("drawing", "How interested are you in Drawing?"),
    ("creativity", "How interested are you in Creativity?"),
    ("helping", "How interested are you in Helping People?"),
    ("communication", "How interested are you in Communication?"),
    ("business", "How interested are you in Business?"),
    ("leadership", "How interested are you in Leadership?"),
    ("problem_solving", "How interested are you in Problem Solving?"),
    ("technology", "How interested are you in Technology?"),
    ("writing", "How interested are you in Writing?"),
    ("teaching", "How interested are you in Teaching?"),
    ("accounting", "How interested are you in Accounting?"),
    ("designing", "How interested are you in Designing?"),
    ("machines", "How interested are you in Machines?"),
    ("agriculture", "How interested are you in Agriculture?"),
    ("sports", "How interested are you in Sports?")
]



class CareerExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Career Guidance Expert System")
        self.root.geometry("850x750")
        self.root.minsize(700, 600)
        self.root.configure(bg="#f4f7fb")

        self.variables = {}

        self.setup_style()
        self.create_interface()

 
    def setup_style(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Title.TLabel",
            font=("Arial", 22, "bold"),
            foreground="#173b75",
            background="#ffffff"
        )

        style.configure(
            "Subtitle.TLabel",
            font=("Arial", 11),
            foreground="#555555",
            background="#ffffff"
        )

        style.configure(
            "Question.TLabel",
            font=("Arial", 11, "bold"),
            foreground="#222222",
            background="#ffffff"
        )

        style.configure(
            "TCombobox",
            padding=5,
            font=("Arial", 10)
        )

        style.configure(
            "Primary.TButton",
            font=("Arial", 11, "bold"),
            padding=(15, 8)
        )

        style.configure(
            "Secondary.TButton",
            font=("Arial", 11),
            padding=(15, 8)
        )


    def create_interface(self):
        # Header
        header = tk.Frame(self.root, bg="#ffffff")
        header.pack(fill="x")

        ttk.Label(
            header,
            text="Student Career Guidance Expert System",
            style="Title.TLabel"
        ).pack(pady=(20, 5))

        ttk.Label(
            header,
            text="Answer the questions honestly. The system will analyze your interests and suggest suitable career paths.",
            style="Subtitle.TLabel"
        ).pack(pady=(0, 20))

    
        container = tk.Frame(self.root, bg="#f4f7fb")
        container.pack(fill="both", expand=True, padx=15, pady=15)

        self.canvas = tk.Canvas(
            container,
            bg="#ffffff",
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.canvas.yview
        )

        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg="#ffffff"
        )

        self.window_id = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw"
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        self.scrollable_frame.bind(
            "<Configure>",
            lambda event: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.bind(
            "<Configure>",
            self.resize_scrollable_frame
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

  
        question_container = tk.Frame(
            self.scrollable_frame,
            bg="#ffffff"
        )
        question_container.pack(
            fill="x",
            padx=30,
            pady=20
        )

        for key, question in QUESTIONS:
            self.create_question(
                question_container,
                key,
                question
            )

 
        button_frame = tk.Frame(
            self.scrollable_frame,
            bg="#ffffff"
        )
        button_frame.pack(pady=10)

        ttk.Button(
            button_frame,
            text="Get Career Recommendation",
            style="Primary.TButton",
            command=self.recommend
        ).grid(row=0, column=0, padx=8)

        ttk.Button(
            button_frame,
            text="Clear",
            style="Secondary.TButton",
            command=self.clear
        ).grid(row=0, column=1, padx=8)

    
        self.result_frame = tk.Frame(
            self.scrollable_frame,
            bg="#eef6ff",
            bd=1,
            relief="solid"
        )
        self.result_frame.pack(
            fill="x",
            padx=30,
            pady=(15, 30)
        )

        self.result_title = tk.Label(
            self.result_frame,
            text="Career Recommendation",
            font=("Arial", 16, "bold"),
            bg="#eef6ff",
            fg="#173b75"
        )
        self.result_title.pack(pady=(15, 5))

        self.result_label = tk.Label(
            self.result_frame,
            text="Your recommendation will appear here.",
            font=("Arial", 11),
            bg="#eef6ff",
            fg="#333333",
            justify="left",
            anchor="w",
            wraplength=650
        )
        self.result_label.pack(
            padx=20,
            pady=(5, 20)
        )

    
        self.canvas.bind_all("<MouseWheel>", self.mouse_wheel)
        self.canvas.bind_all("<Button-4>", self.mouse_wheel_linux)
        self.canvas.bind_all("<Button-5>", self.mouse_wheel_linux)

    def create_question(self, parent, key, question):
        frame = tk.Frame(
            parent,
            bg="#ffffff"
        )
        frame.pack(
            fill="x",
            pady=6
        )

        ttk.Label(
            frame,
            text=question,
            style="Question.TLabel"
        ).pack(
            side="left",
            padx=(0, 20)
        )

        variable = tk.StringVar(value="No Interest")
        self.variables[key] = variable

        combo = ttk.Combobox(
            frame,
            textvariable=variable,
            values=list(INTEREST_LEVELS.keys()),
            state="readonly",
            width=18
        )
        combo.pack(side="right")

   
    def resize_scrollable_frame(self, event):
        self.canvas.itemconfig(
            self.window_id,
            width=event.width
        )

    def mouse_wheel(self, event):
        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

    def mouse_wheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

   
    def calculate_score(self, career_data):
        score = 0
        maximum_score = 0

        for interest, weight in career_data["weights"].items():
            selected_level = self.variables[interest].get()
            interest_score = INTEREST_LEVELS[selected_level]

            score += interest_score * weight
            maximum_score += 3 * weight

        if maximum_score == 0:
            return 0

        return (score / maximum_score) * 100

    def recommend(self):
        
        results = []

        for career_name, career_data in CAREERS.items():
            score = self.calculate_score(career_data)
            results.append(
                (score, career_name, career_data)
            )

        results.sort(
            key=lambda item: item[0],
            reverse=True
        )

        top_results = results[:3]

        total_interest = sum(
            INTEREST_LEVELS[var.get()]
            for var in self.variables.values()
        )

        if total_interest == 0:
            messagebox.showwarning(
                "No Interest Selected",
                "Please select at least some interests before getting a recommendation."
            )
            return

        best_score, best_career, best_data = top_results[0]

        if best_score < 30:
            result = (
                "No strong career match was found yet.\n\n"
                "Try selecting Medium or High Interest for subjects and activities "
                "you genuinely enjoy."
            )

            self.result_label.config(text=result)
            messagebox.showinfo(
                "Career Recommendation",
                result
            )
            return

        
        lines = [
            f"Best Match: {best_career}",
            f"Match Score: {best_score:.1f}%",
            "",
            best_data["description"],
            "",
            f"Possible Courses: {best_data['courses']}",
            "",
            "Other Suitable Options:"
        ]

        for score, career_name, _ in top_results[1:]:
            if score >= 30:
                lines.append(
                    f"• {career_name} — {score:.1f}% match"
                )

        lines.extend([
            "",
            "Note: This is a rule-based guidance system, not a final career decision."
        ])

        result = "\n".join(lines)

        self.result_label.config(text=result)

        messagebox.showinfo(
            "Career Recommendation",
            result
        )


    def clear(self):
        for variable in self.variables.values():
            variable.set("No Interest")

        self.result_label.config(
            text="Your recommendation will appear here."
        )

        self.canvas.yview_moveto(0)

    def on_close(self):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()

    app = CareerExpertSystem()

    root.protocol(
        "WM_DELETE_WINDOW",
        app.on_close
    )

    root.mainloop()
