import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Running Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(45, 755, "M.Sc. Informatics — 10 Minor Python Projects (Viva & Presentation Notes)")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.6)
            self.line(45, 748, 567, 748)
            
        # Running Footer
        self.setFont("Helvetica", 8)
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(567, 28, footer_text)
        self.drawString(45, 28, "Confidential Academic Presentation Notes • Master of Science (Informatics)")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.6)
        self.line(45, 38, 567, 38)
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=45,
        rightMargin=45,
        topMargin=50,
        bottomMargin=48
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Typography
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#1A365D"),
        alignment=1,
        spaceAfter=8
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2B6CB0"),
        alignment=1,
        spaceAfter=15
    )
    
    proj_title_style = ParagraphStyle(
        'ProjTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=17,
        textColor=colors.HexColor("#1A365D"),
        spaceAfter=5
    )
    
    section_h_style = ParagraphStyle(
        'SectionH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#2C5282"),
        spaceBefore=6,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=3
    )
    
    bullet_style = ParagraphStyle(
        'BulletText',
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#1A202C")
    )
    
    viva_q_style = ParagraphStyle(
        'VivaQ',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#9B2C2C"),
        spaceBefore=4
    )
    
    viva_a_style = ParagraphStyle(
        'VivaA',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#22543D"),
        leftIndent=10,
        spaceAfter=3
    )

    story = []
    
    # ================= PAGE 1: COVER & INDEX =================
    story.append(Spacer(1, 20))
    story.append(Paragraph("M.Sc. Informatics — Python Minor Projects", title_style))
    story.append(Paragraph("Viva Voce Presentation Cheat Sheet & Quick Reference Handbook", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#2B6CB0"), spaceAfter=15))
    
    intro_p = Paragraph(
        "This concise handbook is designed for practical presentation and viva voce examination. "
        "It summarizes all 10 minor Python projects, highlighting the core problem statement, working logic, "
        "step-by-step presentation script (what to explain to the teacher), and the most frequent viva questions with direct model answers.",
        body_style
    )
    story.append(intro_p)
    story.append(Spacer(1, 10))
    
    index_data = [
        [Paragraph("<b>#</b>", body_style), Paragraph("<b>Project Title</b>", body_style), Paragraph("<b>Type</b>", body_style), Paragraph("<b>Key Concepts</b>", body_style), Paragraph("<b>Page</b>", body_style)],
        [Paragraph("1", body_style), Paragraph("Country Information Finder", body_style), Paragraph("API-Based", body_style), Paragraph("requests.get, JSON parsing, dictionary lookup", body_style), Paragraph("2", body_style)],
        [Paragraph("2", body_style), Paragraph("Random Joke Generator", body_style), Paragraph("API-Based", body_style), Paragraph("requests.get, JSON decoding, status code check", body_style), Paragraph("3", body_style)],
        [Paragraph("3", body_style), Paragraph("Student Grade Calculator", body_style), Paragraph("Basic Python", body_style), Paragraph("float(), if-elif-else, percentage formula", body_style), Paragraph("4", body_style)],
        [Paragraph("4", body_style), Paragraph("Simple Expense Calculator", body_style), Paragraph("Basic Python", body_style), Paragraph("Lists, append(), sum(), max()", body_style), Paragraph("5", body_style)],
        [Paragraph("5", body_style), Paragraph("Electricity Bill Calculator", body_style), Paragraph("Basic Python", body_style), Paragraph("Progressive slab tariffs, cumulative calculation", body_style), Paragraph("6", body_style)],
        [Paragraph("6", body_style), Paragraph("Password Strength Checker", body_style), Paragraph("Basic Python", body_style), Paragraph("for loop, boolean flags, .isdigit(), .isupper()", body_style), Paragraph("7", body_style)],
        [Paragraph("7", body_style), Paragraph("Student Attendance Calculator", body_style), Paragraph("Basic Python", body_style), Paragraph("int(), zero-division check, >= 75% rule", body_style), Paragraph("8", body_style)],
        [Paragraph("8", body_style), Paragraph("Simple Quiz Application", body_style), Paragraph("Basic Python", body_style), Paragraph("List of dicts, .strip().lower(), accumulator", body_style), Paragraph("9", body_style)],
        [Paragraph("9", body_style), Paragraph("Temperature Converter", body_style), Paragraph("Basic Python", body_style), Paragraph("Menu choices, Celsius & Fahrenheit formulas", body_style), Paragraph("10", body_style)],
        [Paragraph("10", body_style), Paragraph("To-Do List Manager", body_style), Paragraph("Basic Python", body_style), Paragraph("while True loop, break, list append, indexing", body_style), Paragraph("11", body_style)],
    ]
    t_idx = Table(index_data, colWidths=[20, 160, 75, 230, 35])
    t_idx.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#FFFFFF"), colors.HexColor("#F7FAFC")]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (-1,0), (-1,-1), 'CENTER'),
    ]))
    story.append(t_idx)
    story.append(Spacer(1, 15))
    
    env_note = Paragraph(
        "<b>Demonstration Environment:</b> All 10 scripts are standalone, zero-dependency (offline except Projects 1 & 2), "
        "and fully executable directly within <b>VS Code</b> or the Windows Command Prompt.",
        body_style
    )
    story.append(env_note)
    story.append(PageBreak())

    # ================= PROJECTS DEFINITIONS (PAGES 2-11) =================
    projects = [
        {
            "num": 1,
            "title": "Country Information Finder (API-Based)",
            "file": "project_01_country_info.py",
            "aim": "Fetches live geographic details (Capital, ISO code) for any user-specified country using the free, keyless CountriesNow public REST API.",
            "concepts": "HTTP GET requests (requests.get), JSON parsing (.json()), dictionary iteration, case-insensitive string matching (.lower()), status code error handling.",
            "code": (
                "import requests\n"
                "country = input('Enter country name: ')\n"
                "url = 'https://countriesnow.space/api/v0.1/countries/capital'\n"
                "response = requests.get(url)\n"
                "if response.status_code == 200:\n"
                "    countries = response.json()['data']\n"
                "    found = False\n"
                "    for item in countries:\n"
                "        if item['name'].lower() == country.lower():\n"
                "            print('Name:', item['name'], '| Capital:', item['capital'], '| ISO:', item['iso2'])\n"
                "            found = True; break\n"
                "    if not found: print('Country not found. Please check spelling.')\n"
                "else: print('API is currently unavailable.')"
            ),
            "say": [
                "<b>Introduce:</b> 'Sir/Ma'am, this project demonstrates consuming a third-party REST API over the internet using Python's requests library.'",
                "<b>Explain Request:</b> 'The program prompts the user for a country name and sends an HTTP GET request to the CountriesNow web endpoint.'",
                "<b>Explain Response & Parsing:</b> 'We verify status code 200 (OK). The JSON text is parsed into Python dictionaries using response.json().'",
                "<b>Explain Traversal:</b> 'We iterate through the country list with a for loop, matching the input case-insensitively using .lower(), and display the capital and ISO code.'",
                "<b>Explain Error Handling:</b> 'If the country name is invalid or the internet is unreachable, the program gracefully prints an error message instead of crashing.'"
            ],
            "viva": [
                ("What is an API and why is it used here?", "An API (Application Programming Interface) connects two software programs. Here, it allows Python to fetch live country data without needing a large local database."),
                ("What does HTTP status code 200 mean?", "Status code 200 is the standard web response code for 'OK', confirming that the request was processed successfully."),
                ("What is JSON and how does Python decode it?", "JSON is a universal text format for data exchange. Python decodes it using .json(), which converts it into native Python dictionaries and lists.")
            ]
        },
        {
            "num": 2,
            "title": "Random Joke Generator (API-Based)",
            "file": "project_02_joke_generator.py",
            "aim": "Connects to the Official Joke API to fetch and display a random two-part joke (setup and punchline) on demand without authentication keys.",
            "concepts": "HTTP GET request, JSON deserialization, dictionary key extraction, HTTP status checking.",
            "code": (
                "import requests\n"
                "url = 'https://official-joke-api.appspot.com/random_joke'\n"
                "response = requests.get(url)\n"
                "if response.status_code == 200:\n"
                "    joke = response.json()\n"
                "    print('\\n--- Here is a Joke for You! ---')\n"
                "    print('Setup:', joke['setup'])\n"
                "    print('Punchline:', joke['punchline'])\n"
                "else:\n"
                "    print('Failed to fetch a joke. Please check your internet connection.')"
            ),
            "say": [
                "<b>Introduce:</b> 'This project demonstrates retrieving dynamic content where each call returns fresh random data without user parameters.'",
                "<b>Explain Flow:</b> 'We issue a GET request to the Official Joke API endpoint using requests.get(url).'",
                "<b>Explain Extraction:</b> 'Upon receiving status code 200, response.json() parses the payload into a dictionary named joke.'",
                "<b>Explain Output:</b> 'We access the specific fields joke[\"setup\"] and joke[\"punchline\"] and print them cleanly to the terminal.'"
            ],
            "viva": [
                ("Why does this API not require an API key?", "It is an open-source, public community API provided free for developers and learners without authentication barriers."),
                ("What is the difference between GET and POST?", "GET retrieves existing data from a server without side effects; POST sends new data to a server to create or update resources."),
                ("How does the program handle network failures?", "If the connection fails or status code is not 200, the else block catches the failure and informs the user.")
            ]
        },
        {
            "num": 3,
            "title": "Student Grade Calculator",
            "file": "project_03_grade_calculator.py",
            "aim": "Accepts marks for three subjects, calculates total score and percentage, and assigns an academic letter grade (A+, A, B, C, F).",
            "concepts": "input(), float() type casting, arithmetic operators (+, /), multi-branch conditional statements (if-elif-else), formatted strings (:.2f).",
            "code": (
                "# Take marks for 3 subjects\n"
                "sub1 = float(input('Enter marks for Subject 1: '))\n"
                "sub2 = float(input('Enter marks for Subject 2: '))\n"
                "sub3 = float(input('Enter marks for Subject 3: '))\n"
                "total = sub1 + sub2 + sub3\n"
                "percentage = total / 3\n"
                "print(f'\\nTotal Marks: {total}/300 | Percentage: {percentage:.2f}%')\n"
                "if percentage >= 90: print('Grade: A+')\n"
                "elif percentage >= 75: print('Grade: A')\n"
                "elif percentage >= 60: print('Grade: B')\n"
                "elif percentage >= 40: print('Grade: C')\n"
                "else: print('Grade: F (Fail)')"
            ),
            "say": [
                "<b>Introduce:</b> 'This project automates academic performance evaluation using sequential conditional branching.'",
                "<b>Explain Input:</b> 'We read three subject marks and cast them using float() so decimal scores like 78.5 can be evaluated accurately.'",
                "<b>Explain Calculation:</b> 'We sum the three variables and divide by 3 to compute percentage.'",
                "<b>Explain Ladder:</b> 'An if-elif-else ladder checks grading thresholds from top to bottom (>=90 is A+, >=75 is A, etc.). As soon as a condition matches, it stops.'"
            ],
            "viva": [
                ("Why use float() instead of int()?", "float() allows fractional/decimal numbers, which are common in exam scoring."),
                ("How does the if-elif-else structure work?", "Conditions are checked sequentially from top to bottom. The first True condition executes, and all subsequent elif/else blocks are bypassed."),
                ("What does :.2f mean in the print statement?", "It is an f-string format specifier that rounds and formats a floating-point number to exactly 2 decimal places.")
            ]
        },
        {
            "num": 4,
            "title": "Simple Expense Calculator",
            "file": "project_04_expense_calculator.py",
            "aim": "Gathers personal expenditures across 5 distinct categories, stores them in a list, and computes total spend and peak expense.",
            "concepts": "List data structure ([]), for loop iteration, append() method, built-in sum() and max() functions, f-strings.",
            "code": (
                "expenses = []\n"
                "categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other']\n"
                "print('--- Simple Expense Calculator ---')\n"
                "for category in categories:\n"
                "    amount = float(input(f'Enter amount spent on {category}: Rs. '))\n"
                "    expenses.append(amount)\n"
                "total_spent = sum(expenses)\n"
                "highest = max(expenses)\n"
                "print(f'\\nTotal Expenditure: Rs. {total_spent:.2f}')\n"
                "print(f'Highest Single Expense: Rs. {highest:.2f}')"
            ),
            "say": [
                "<b>Introduce:</b> 'This project is a personal budgeting tool demonstrating Python lists and aggregate functions.'",
                "<b>Explain Loop:</b> 'We iterate through the categories list using a for loop, prompting the user for expenditure on each category.'",
                "<b>Explain List Method:</b> 'Each entered decimal amount is appended to the expenses list using expenses.append(amount).'",
                "<b>Explain Aggregation:</b> 'Instead of manual accumulators, we leverage Python built-ins: sum(expenses) for the grand total and max(expenses) to pinpoint the largest spend.'"
            ],
            "viva": [
                ("What is the function of append()?", "append() adds a new item to the end of an existing list dynamically."),
                ("How do sum() and max() work on a list?", "sum() computes the arithmetic addition of all items in an iterable; max() scans and returns the highest numerical value."),
                ("Can the user add more categories?", "Yes, simply inserting another string inside the categories list will automatically incorporate it without rewriting logic.")
            ]
        },
        {
            "num": 5,
            "title": "Electricity Bill Calculator",
            "file": "project_05_electricity_bill.py",
            "aim": "Calculates domestic monthly power bills using realistic progressive slab tariffs and fixed meter maintenance charges.",
            "concepts": "Progressive tiered conditionals (if-elif-else), cumulative slab arithmetic, fixed service fee addition, currency formatting.",
            "code": (
                "units = float(input('Enter electricity units consumed: '))\n"
                "bill = 0.0\n"
                "if units <= 100:\n"
                "    bill = units * 1.50\n"
                "elif units <= 200:\n"
                "    bill = (100 * 1.50) + (units - 100) * 2.50\n"
                "elif units <= 300:\n"
                "    bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00\n"
                "else:\n"
                "    bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (units - 300) * 6.00\n"
                "total_bill = bill + 50.0\n"
                "print(f'Electricity Bill: Rs. {bill:.2f} | Total with Meter Fee: Rs. {total_bill:.2f}')"
            ),
            "say": [
                "<b>Introduce:</b> 'This project models real-world electrical utility billing using progressive tiered tariffs.'",
                "<b>Explain Slab Logic:</b> 'Units are charged in progressive blocks: the first 100 at Rs. 1.50, units 101-200 at Rs. 2.50, and so on. Higher tiers do not retroactively penalize initial subsidized units.'",
                "<b>Explain Cumulative Arithmetic:</b> 'For 150 units: 100 * 1.50 = 150; + (50 * 2.50) = 125, giving Rs. 275.'",
                "<b>Explain Fixed Surcharge:</b> 'A fixed meter maintenance fee of Rs. 50 is added to arrive at the final payable invoice.'"
            ],
            "viva": [
                ("What is a progressive slab tariff?", "A tariff structure where consumption is segmented into tiers, and higher rates apply only to consumption exceeding lower threshold limits."),
                ("What is the total bill if units consumed is 0?", "The energy charge is Rs. 0.00, and total bill is Rs. 50.00 (the base meter maintenance charge)."),
                ("Why is this more realistic than flat multiplication?", "Real-world utility boards charge tiered rates to provide lifeline subsidies to low consumers and deter excessive waste.")
            ]
        },
        {
            "num": 6,
            "title": "Password Strength Checker",
            "file": "project_06_password_checker.py",
            "aim": "Evaluates candidate password security based on length, presence of numeric digits, and uppercase characters, rating it Strong, Medium, or Weak.",
            "concepts": "String iteration with for loop, boolean state flags, .isdigit(), .isupper(), len(), combined logical and.",
            "code": (
                "password = input('Enter password: ')\n"
                "has_digit = False; has_upper = False\n"
                "for char in password:\n"
                "    if char.isdigit(): has_digit = True\n"
                "    elif char.isupper(): has_upper = True\n"
                "print('\\n--- Password Evaluation ---')\n"
                "if len(password) >= 8 and has_digit and has_upper:\n"
                "    print('Password Strength: Strong')\n"
                "elif len(password) >= 6:\n"
                "    print('Password Strength: Medium (Consider adding numbers and uppercase letters)')\n"
                "else:\n"
                "    print('Password Strength: Weak (Too short)')"
            ),
            "say": [
                "<b>Introduce:</b> 'This project promotes basic cybersecurity awareness by inspecting string composition.'",
                "<b>Explain Flags:</b> 'We initialize two boolean flags, has_digit and has_upper, to False.'",
                "<b>Explain Traversal:</b> 'A for loop traverses each character. Built-in methods char.isdigit() and char.isupper() toggle their respective flags to True upon detection.'",
                "<b>Explain Decision:</b> 'A password with >= 8 characters and both flags True is Strong; >= 6 characters is Medium; anything less is Weak.'"
            ],
            "viva": [
                ("What do .isdigit() and .isupper() do?", ".isdigit() returns True if a character is a number (0-9); .isupper() returns True if a character is an uppercase letter (A-Z)."),
                ("What is a boolean flag?", "A boolean variable (True/False) that acts as a signal indicating whether a condition has been met during iteration."),
                ("How could we add special character detection?", "By checking if char in '!@#$%^&*' and toggling a has_special flag.")
            ]
        },
        {
            "num": 7,
            "title": "Student Attendance Calculator",
            "file": "project_07_attendance_calculator.py",
            "aim": "Computes attendance percentage from total classes held vs attended, validating inputs and verifying eligibility for university examinations (>= 75%).",
            "concepts": "int() input casting, input validation (preventing zero division or impossible numbers), arithmetic percentage formula, threshold condition.",
            "code": (
                "total_classes = int(input('Enter total number of classes held: '))\n"
                "attended_classes = int(input('Enter number of classes attended: '))\n"
                "if total_classes <= 0 or attended_classes > total_classes:\n"
                "    print('Invalid attendance numbers entered.')\n"
                "else:\n"
                "    percentage = (attended_classes / total_classes) * 100\n"
                "    print(f'\\nAttendance Percentage: {percentage:.2f}%')\n"
                "    if percentage >= 75:\n"
                "        print('Status: Eligible for examinations.')\n"
                "    else:\n"
                "        print('Status: Shortage of attendance! Minimum 75% required.')"
            ),
            "say": [
                "<b>Introduce:</b> 'This project automates academic eligibility tracking according to university attendance rules.'",
                "<b>Emphasize Validation:</b> 'Before calculating, we check total_classes <= 0 or attended_classes > total_classes. This prevents division-by-zero crashes and eliminates illogical inputs.'",
                "<b>Explain Formula:</b> 'Percentage is computed via (attended / total) * 100.'",
                "<b>Explain Result:</b> 'If percentage >= 75%, it grants examination eligibility; otherwise, it warns of attendance shortage.'"
            ],
            "viva": [
                ("Why is input validation essential here?", "If a user inputs 0 for total classes, Python throws a fatal ZeroDivisionError. Validation guards against program termination."),
                ("Why use int() rather than float()?", "Class sessions and attendances are discrete whole numbers, making int() the correct data type."),
                ("What does the or operator do?", "The logical or operator returns True if either condition is satisfied.")
            ]
        },
        {
            "num": 8,
            "title": "Simple Quiz Application",
            "file": "project_08_quiz_app.py",
            "aim": "Runs an interactive multiple-question quiz stored in a list of dictionaries, tracks user score, and normalizes input text.",
            "concepts": "List of dictionaries, for loop, string normalization (.strip(), .lower()), accumulator variable, dynamic len().",
            "code": (
                "questions = [\n"
                "    {'q': 'What is the extension of Python files?', 'a': '.py'},\n"
                "    {'q': 'Which keyword is used to define a function in Python?', 'a': 'def'},\n"
                "    {'q': 'Which function is used to take input from the user?', 'a': 'input'}\n"
                "]\n"
                "score = 0\n"
                "print('--- Simple Python Quiz ---')\n"
                "for item in questions:\n"
                "    ans = input(item['q'] + ' : ')\n"
                "    if ans.strip().lower() == item['a'].lower():\n"
                "        print('Correct!\\n'); score = score + 1\n"
                "    else:\n"
                "        print(f'Wrong! Correct answer: {item[\"a\"]}\\n')\n"
                "print(f'Quiz Completed! Your Score: {score}/{len(questions)}')"
            ),
            "say": [
                "<b>Introduce:</b> 'This program provides an educational assessment quiz using structured in-memory data.'",
                "<b>Explain Data Structure:</b> 'Questions and answers are stored as key-value pairs within a list of dictionaries.'",
                "<b>Explain Traversal & Normalization:</b> 'A for loop asks each question. We apply .strip().lower() so answers like \".PY\" or \".py \" are recognized correctly regardless of case or spaces.'",
                "<b>Explain Score Tracking:</b> 'A score accumulator increments for every correct answer, and the final score is printed out of len(questions).'"
            ],
            "viva": [
                ("Why use .strip().lower()?", ".strip() eliminates whitespace, and .lower() ensures case-insensitivity so capitalization does not cause false negatives."),
                ("What is the benefit of using a list of dictionaries?", "It organizes related data (question and answer) cleanly and allows adding new questions without modifying program logic."),
                ("How does len(questions) help?", "It dynamically computes the total number of questions, keeping scoring accurate automatically.")
            ]
        },
        {
            "num": 9,
            "title": "Temperature Converter",
            "file": "project_09_temperature_converter.py",
            "aim": "A menu-driven scientific utility that converts temperatures between Celsius and Fahrenheit in both directions.",
            "concepts": "Menu-driven branching (if-elif-else), user choice validation, float arithmetic formulas, string formatting.",
            "code": (
                "print('1. Celsius to Fahrenheit\\n2. Fahrenheit to Celsius')\n"
                "choice = input('Enter your choice (1 or 2): ')\n"
                "if choice == '1':\n"
                "    c = float(input('Enter temperature in Celsius: '))\n"
                "    f = (c * 9/5) + 32\n"
                "    print(f'{c}°C is equal to {f:.2f}°F')\n"
                "elif choice == '2':\n"
                "    f = float(input('Enter temperature in Fahrenheit: '))\n"
                "    c = (f - 32) * 5/9\n"
                "    print(f'{f}°F is equal to {c:.2f}°C')\n"
                "else:\n"
                "    print('Invalid choice! Please select 1 or 2.')"
            ),
            "say": [
                "<b>Introduce:</b> 'This project implements an interactive menu-driven temperature conversion utility.'",
                "<b>Explain Menu:</b> 'The user chooses option 1 or 2. We keep choice as a string to avoid crashes if someone accidentally types a letter.'",
                "<b>Explain Conversion Formulas:</b> 'Option 1 calculates F = (C * 9/5) + 32. Option 2 calculates C = (F - 32) * 5/9.'",
                "<b>Explain Formatting:</b> 'Results are formatted cleanly with degree symbols and rounded to two decimal places.'"
            ],
            "viva": [
                ("State the temperature conversion formulas.", "Celsius to Fahrenheit: F = (C * 9/5) + 32; Fahrenheit to Celsius: C = (F - 32) * 5/9."),
                ("Why keep choice as a string instead of int(choice)?", "If a user enters text or presses enter accidentally, int() throws a ValueError. Keeping it a string allows safe validation via else."),
                ("At what temperature are Celsius and Fahrenheit equal?", "At -40 degrees (-40°C = -40°F).")
            ]
        },
        {
            "num": 10,
            "title": "To-Do List Manager",
            "file": "project_10_todo_manager.py",
            "aim": "A continuous terminal-based task organizer allowing users to view numbered tasks, append new tasks, and exit cleanly.",
            "concepts": "Infinite loop (while True), menu branching, list append(), dynamic human-friendly 1-based indexing (i + 1), break statement.",
            "code": (
                "tasks = []\n"
                "while True:\n"
                "    print('\\n1. View Tasks  2. Add Task  3. Exit')\n"
                "    choice = input('Choose an option: ')\n"
                "    if choice == '1':\n"
                "        if len(tasks) == 0: print('Your task list is empty.')\n"
                "        else:\n"
                "            print('\\nYour Tasks:')\n"
                "            for i in range(len(tasks)): print(f'{i + 1}. {tasks[i]}')\n"
                "    elif choice == '2':\n"
                "        new_task = input('Enter task description: ')\n"
                "        tasks.append(new_task); print(f'Task \\'{new_task}\\' added!')\n"
                "    elif choice == '3':\n"
                "        print('Goodbye!'); break\n"
                "    else: print('Invalid choice. Try again.')"
            ),
            "say": [
                "<b>Introduce:</b> 'This project demonstrates an interactive continuous application loop using Python.'",
                "<b>Explain Event Loop:</b> 'A while True loop keeps the application running until option 3 executes the break statement.'",
                "<b>Explain Viewing & Indexing:</b> 'Option 1 checks if the list is empty with len(tasks) == 0. If tasks exist, a for loop prints each task prefixed with i + 1 for natural numbering.'",
                "<b>Explain Task Insertion:</b> 'Option 2 takes user input and appends it dynamically to the tasks list.'"
            ],
            "viva": [
                ("How does the program safely exit the infinite while True loop?", "When choice == '3', the break keyword is executed, which terminates the loop immediately and exits the script."),
                ("Why do we print i + 1 instead of i?", "Python lists are zero-indexed (starting at 0), but humans naturally count from 1. i + 1 provides natural numbered lists."),
                ("Where are tasks saved during execution?", "Tasks are stored in-memory in the tasks list for the duration of the script execution.")
            ]
        }
    ]

    for p in projects:
        card = []
        
        # Header bar
        header_text = f"<b>Project {p['num']}: {p['title']}</b>"
        card.append(Paragraph(header_text, proj_title_style))
        card.append(Paragraph(f"<b>Script File:</b> <font color='#2B6CB0'>{p['file']}</font>", body_style))
        card.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2B6CB0"), spaceAfter=6))
        
        # Aim & Concepts
        card.append(Paragraph(f"<b>Aim:</b> {p['aim']}", body_style))
        card.append(Paragraph(f"<b>Key Python Concepts:</b> {p['concepts']}", body_style))
        card.append(Spacer(1, 4))
        
        # Code Box
        card.append(Paragraph("<b>Source Code Summary:</b>", section_h_style))
        code_p = Paragraph(p['code'].replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)
        t_code = Table([[code_p]], colWidths=[522])
        t_code.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
            ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#CBD5E0")),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ]))
        card.append(t_code)
        card.append(Spacer(1, 5))
        
        # What to Say to Teacher
        card.append(Paragraph("<b>Presentation Script (What to say when explaining to your teacher):</b>", section_h_style))
        for point in p['say']:
            card.append(Paragraph(f"• {point}", bullet_style))
        card.append(Spacer(1, 4))
        
        # Viva Q&A
        card.append(Paragraph("<b>Top Viva Questions & Direct Model Answers:</b>", section_h_style))
        for q, a in p['viva']:
            card.append(Paragraph(f"<b>Q: {q}</b>", viva_q_style))
            card.append(Paragraph(f"<b>A:</b> {a}", viva_a_style))
            
        story.extend(card)
        story.append(PageBreak())

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Dedicated 11-page handbook built successfully:", filename)

if __name__ == "__main__":
    out_path = r"E:\MSC informatics\10 Minor Python Projects with 1 API\MSc_Python_Minor_Projects_Short_Notes.pdf"
    build_pdf(out_path)
