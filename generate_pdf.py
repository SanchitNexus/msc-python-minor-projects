from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
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
        if self._pageNumber > 1:
            self.drawString(45, 755, "M.Sc. Informatics - 10 Minor Python Projects (Viva & Presentation Notes)")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.6)
            self.line(45, 748, 567, 748)
        self.setFont("Helvetica", 8)
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(567, 28, footer_text)
        self.drawString(45, 28, "Academic Presentation Notes - Master of Science (Informatics)")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.6)
        self.line(45, 38, 567, 38)
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=45, rightMargin=45, topMargin=50, bottomMargin=48)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('CoverTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=colors.HexColor("#1A365D"), alignment=1, spaceAfter=8)
    subtitle_style = ParagraphStyle('CoverSubtitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=colors.HexColor("#2B6CB0"), alignment=1, spaceAfter=15)
    proj_title_style = ParagraphStyle('ProjTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14, leading=17, textColor=colors.HexColor("#1A365D"), spaceAfter=5)
    section_h_style = ParagraphStyle('SectionH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=colors.HexColor("#2C5282"), spaceBefore=6, spaceAfter=3)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor("#2D3748"), spaceAfter=3)
    bullet_style = ParagraphStyle('BulletText', parent=body_style, leftIndent=12, firstLineIndent=-8, spaceAfter=3)
    code_style = ParagraphStyle('CodeStyle', parent=styles['Normal'], fontName='Courier', fontSize=8, leading=10.5, textColor=colors.HexColor("#1A202C"))
    viva_q_style = ParagraphStyle('VivaQ', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11.5, textColor=colors.HexColor("#9B2C2C"), spaceBefore=4)
    viva_a_style = ParagraphStyle('VivaA', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=colors.HexColor("#22543D"), leftIndent=10, spaceAfter=3)

    story = []

    # Page 1: Cover & Index
    story.append(Spacer(1, 20))
    story.append(Paragraph("M.Sc. Informatics - Python Minor Projects", title_style))
    story.append(Paragraph("Viva Voce Presentation Cheat Sheet & Quick Reference Handbook", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#2B6CB0"), spaceAfter=15))
    story.append(Paragraph("This concise handbook summarizes all 10 minor Python projects, detailing their core objective, key concepts, speaking points for viva demonstration, and expected viva questions with concise answers.", body_style))
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
    story.append(PageBreak())

    projects = [
        {
            "num": 1, "title": "Country Information Finder (API-Based)", "file": "project_01_country_info.py",
            "aim": "Fetches live geographic details (Capital, ISO code) for any user-specified country using the free CountriesNow public REST API.",
            "concepts": "HTTP GET requests (requests.get), JSON parsing (.json()), dictionary iteration, case-insensitive string matching (.lower()), status code error handling.",
            "code": "import requests\ncountry = input('Enter country name: ')\nurl = 'https://countriesnow.space/api/v0.1/countries/capital'\nresponse = requests.get(url)\nif response.status_code == 200:\n    countries = response.json()['data']\n    found = False\n    for item in countries:\n        if item['name'].lower() == country.lower():\n            print('Name:', item['name'], '| Capital:', item['capital'], '| ISO:', item['iso2'])\n            found = True; break\n    if not found: print('Country not found.')\nelse: print('API unavailable.')",
            "say": ["1. Introduce: Explain that this project consumes a public REST API over the internet using requests.", "2. Flow: Python sends a GET request to CountriesNow API and receives JSON data.", "3. Parsing: Convert JSON into Python dictionaries and search using case-insensitive comparison.", "4. Error Handling: Handles typos and network issues gracefully."],
            "viva": [("What is an API?", "An Application Programming Interface enables different software systems to communicate and exchange data."), ("What does status code 200 mean?", "It is the standard HTTP response indicating success ('OK').")]
        },
        {
            "num": 2, "title": "Random Joke Generator (API-Based)", "file": "project_02_joke_generator.py",
            "aim": "Fetches and displays a fresh random joke (setup and punchline) on demand using the Official Joke API.",
            "concepts": "HTTP GET requests, JSON deserialization, dictionary key indexing, status code validation.",
            "code": "import requests\nurl = 'https://official-joke-api.appspot.com/random_joke'\nresponse = requests.get(url)\nif response.status_code == 200:\n    joke = response.json()\n    print('Setup:', joke['setup'])\n    print('Punchline:', joke['punchline'])\nelse:\n    print('Failed to fetch joke.')",
            "say": ["1. Introduce: Demonstrates fetching dynamic random data without requiring user query parameters.", "2. Flow: Sends a GET request to the public joke endpoint.", "3. Data Extraction: Accesses setup and punchline via dictionary keys."],
            "viva": [("Why does this API require no key?", "It is an open educational endpoint provided freely without authentication."), ("What does response.json() do?", "It converts the JSON text string into native Python dictionaries/lists.")]
        },
        {
            "num": 3, "title": "Student Grade Calculator", "file": "project_03_grade_calculator.py",
            "aim": "Calculates total marks, percentage, and assigns an academic letter grade across three subjects.",
            "concepts": "input(), float() casting, arithmetic operations, if-elif-else conditional ladder, f-string formatting.",
            "code": "sub1 = float(input('Marks 1: '))\nsub2 = float(input('Marks 2: '))\nsub3 = float(input('Marks 3: '))\ntotal = sub1 + sub2 + sub3\npercentage = total / 3\nprint(f'Total: {total}/300 | Percentage: {percentage:.2f}%')\nif percentage >= 90: print('Grade: A+')\nelif percentage >= 75: print('Grade: A')\nelif percentage >= 60: print('Grade: B')\nelif percentage >= 40: print('Grade: C')\nelse: print('Grade: F (Fail)')",
            "say": ["1. Introduce: Automates student grading using structured decision-making.", "2. Type Casting: Uses float() to accommodate decimal exam marks.", "3. Evaluation: Checks thresholds sequentially using an if-elif-else ladder."],
            "viva": [("Why use float() over int()?", "To permit decimal numbers like 82.5 in mark entry."), ("What does :.2f specify?", "It formats floating-point values to exactly 2 decimal places.")]
        },
        {
            "num": 4, "title": "Simple Expense Calculator", "file": "project_04_expense_calculator.py",
            "aim": "Tracks expenditures across 5 categories, computing total spending and identifying the highest single expense.",
            "concepts": "Lists ([]), for loops, append() method, built-in sum() and max() functions.",
            "code": "expenses = []\ncategories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other']\nfor cat in categories:\n    amt = float(input(f'Spent on {cat}: Rs. '))\n    expenses.append(amt)\nprint(f'Total: Rs. {sum(expenses):.2f} | Highest: Rs. {max(expenses):.2f}')",
            "say": ["1. Introduce: A personal budgeting utility illustrating list data structures.", "2. Loops & Appending: Gathers user inputs and dynamically appends them to a list.", "3. Built-ins: Uses sum() for total addition and max() to find peak spend."],
            "viva": [("What does append() do?", "It inserts a new element at the end of an existing list."), ("How does sum() work?", "It iterates through a list of numbers and returns their total sum.")]
        },
        {
            "num": 5, "title": "Electricity Bill Calculator", "file": "project_05_electricity_bill.py",
            "aim": "Computes monthly domestic electricity bills using realistic tiered slab tariffs and fixed meter fees.",
            "concepts": "Tiered conditionals (if-elif-else), cumulative calculation logic, fixed maintenance surcharges.",
            "code": "units = float(input('Units consumed: '))\nif units <= 100: bill = units * 1.50\nelif units <= 200: bill = (100 * 1.50) + (units - 100) * 2.50\nelif units <= 300: bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00\nelse: bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (units - 300) * 6.00\ntotal = bill + 50.0\nprint(f'Energy: Rs. {bill:.2f} | Total with Meter Fee: Rs. {total:.2f}')",
            "say": ["1. Introduce: Models actual utility billing using progressive tiered tariffs.", "2. Slab Logic: Units are charged progressively so low-usage brackets remain subsidized.", "3. Surcharge: Adds a standard Rs. 50 meter fee to the total."],
            "viva": [("What is a tiered tariff?", "A billing method where successive consumption brackets are charged at increasing unit rates."), ("What if units consumed is 0?", "The bill equals the fixed meter fee of Rs. 50.00.")]
        },
        {
            "num": 6, "title": "Password Strength Checker", "file": "project_06_password_checker.py",
            "aim": "Assesses password security by verifying length, numeric digits, and uppercase characters.",
            "concepts": "for loop string traversal, boolean flags, .isdigit(), .isupper(), len(), logical and.",
            "code": "pwd = input('Enter password: ')\nhas_num = False; has_up = False\nfor ch in pwd:\n    if ch.isdigit(): has_num = True\n    elif ch.isupper(): has_up = True\nif len(pwd) >= 8 and has_num and has_up: print('Strength: Strong')\nelif len(pwd) >= 6: print('Strength: Medium')\nelse: print('Strength: Weak')",
            "say": ["1. Introduce: Demonstrates string validation and cybersecurity hygiene.", "2. Inspection: Checks each character with .isdigit() and .isupper(), updating boolean flags.", "3. Decision: Rates as Strong if length >= 8 with both digits and uppercase letters."],
            "viva": [("What do .isdigit() and .isupper() do?", ".isdigit() detects numbers 0-9; .isupper() detects capital letters A-Z."), ("What is a boolean flag?", "A variable holding True or False to track whether an event occurred during iteration.")]
        },
        {
            "num": 7, "title": "Student Attendance Calculator", "file": "project_07_attendance_calculator.py",
            "aim": "Calculates attendance percentage and verifies student eligibility for semester examinations (>= 75%).",
            "concepts": "int() casting, zero-division input validation, percentage calculation, comparison logic.",
            "code": "total = int(input('Total classes held: '))\natt = int(input('Classes attended: '))\nif total <= 0 or att > total: print('Invalid numbers entered.')\nelse:\n    pct = (att / total) * 100\n    print(f'Attendance: {pct:.2f}%')\n    if pct >= 75: print('Status: Eligible for exams.')\n    else: print('Status: Shortage of attendance! Minimum 75% required.')",
            "say": ["1. Introduce: Automates attendance monitoring against academic regulations.", "2. Input Validation: Prevents division by zero when total classes <= 0.", "3. Verification: Checks against university 75% threshold."],
            "viva": [("Why validate input before calculation?", "To prevent fatal ZeroDivisionError crashes when zero or invalid values are entered."), ("Why use int()?", "Class counts are discrete integers.")]
        },
        {
            "num": 8, "title": "Simple Quiz Application", "file": "project_08_quiz_app.py",
            "aim": "Runs a multi-question interactive quiz stored in dictionaries, tracks scoring, and normalizes user answers.",
            "concepts": "List of dictionaries, for loops, .strip().lower() string normalization, score accumulator.",
            "code": "quiz = [\n    {'q': 'Python file extension?', 'a': '.py'},\n    {'q': 'Keyword to define a function?', 'a': 'def'},\n    {'q': 'Function for user input?', 'a': 'input'}\n]\nscore = 0\nfor item in quiz:\n    ans = input(item['q'] + ' : ')\n    if ans.strip().lower() == item['a'].lower():\n        score += 1; print('Correct!')\n    else: print(f'Wrong! Answer: {item[\"a\"]}')\nprint(f'Final Score: {score}/{len(quiz)}')",
            "say": ["1. Introduce: An educational assessment tool using structured in-memory data.", "2. Structure: Pairs questions and answers using dictionaries.", "3. Normalization: Uses .strip().lower() for case-insensitive matching."],
            "viva": [("Why use .strip().lower()?", "To remove accidental whitespace and ignore letter capitalization differences."), ("What is the advantage of len(quiz)?", "It dynamically tracks total question count without hardcoding.")]
        },
        {
            "num": 9, "title": "Temperature Converter", "file": "project_09_temperature_converter.py",
            "aim": "Menu-driven tool for converting temperatures between Celsius and Fahrenheit in both directions.",
            "concepts": "Menu-driven if-elif-else branching, choice validation, float arithmetic formulas.",
            "code": "print('1. Celsius to Fahrenheit\\n2. Fahrenheit to Celsius')\nch = input('Choice (1 or 2): ')\nif ch == '1':\n    c = float(input('Enter Celsius: '))\n    print(f'{c} C = {(c * 9/5) + 32:.2f} F')\nelif ch == '2':\n    f = float(input('Enter Fahrenheit: '))\n    print(f'{f} F = {(f - 32) * 5/9:.2f} C')\nelse: print('Invalid choice!')",
            "say": ["1. Introduce: Interactive scientific temperature conversion utility.", "2. Formulas: Implements standard thermodynamic formulas for Celsius and Fahrenheit.", "3. Safe Choice: Keeps menu choice as string to avoid type error crashes."],
            "viva": [("What are the conversion formulas?", "F = (C * 9/5) + 32 and C = (F - 32) * 5/9."), ("At what temperature are C and F equal?", "At -40 degrees (-40 C = -40 F).")]
        },
        {
            "num": 10, "title": "To-Do List Manager", "file": "project_10_todo_manager.py",
            "aim": "Interactive terminal task manager allowing users to view, add, and organize tasks within a continuous loop.",
            "concepts": "while True loop, break keyword, list append(), 1-based indexing (i + 1).",
            "code": "tasks = []\nwhile True:\n    print('\\n1. View Tasks  2. Add Task  3. Exit')\n    ch = input('Option: ')\n    if ch == '1':\n        if len(tasks) == 0: print('List is empty.')\n        else:\n            for i in range(len(tasks)): print(f'{i + 1}. {tasks[i]}')\n    elif ch == '2':\n        tasks.append(input('Task: '))\n    elif ch == '3': break\n    else: print('Invalid choice.')",
            "say": ["1. Introduce: A task management console tool demonstrating infinite event loops.", "2. Loop & Exit: Runs continuously using while True until option 3 triggers break.", "3. Indexing: Displays tasks using i + 1 for natural human-readable numbering."],
            "viva": [("How does the program stop?", "The break keyword terminates the while True loop when option 3 is selected."), ("Why display i + 1 instead of i?", "Python lists start at 0, while users naturally count starting from 1.")]
        }
    ]

    for p in projects:
        card = []
        card.append(Paragraph(f"<b>Project {p['num']}: {p['title']}</b>", proj_title_style))
        card.append(Paragraph(f"<b>Script File:</b> <font color='#2B6CB0'>{p['file']}</font>", body_style))
        card.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2B6CB0"), spaceAfter=6))
        card.append(Paragraph(f"<b>Aim:</b> {p['aim']}", body_style))
        card.append(Paragraph(f"<b>Key Python Concepts:</b> {p['concepts']}", body_style))
        card.append(Spacer(1, 4))
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
        card.append(Paragraph("<b>Presentation Script (What to say when explaining to your teacher):</b>", section_h_style))
        for point in p['say']:
            card.append(Paragraph(f"* {point}", bullet_style))
        card.append(Spacer(1, 4))
        card.append(Paragraph("<b>Top Viva Questions & Direct Model Answers:</b>", section_h_style))
        for q, a in p['viva']:
            card.append(Paragraph(f"<b>Q: {q}</b>", viva_q_style))
            card.append(Paragraph(f"<b>A:</b> {a}", viva_a_style))
        story.extend(card)
        story.append(PageBreak())

    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF generated successfully:", filename)

if __name__ == "__main__":
    out_path = r"E:\MSC informatics\10 Minor Python Projects with 1 API\MSc_Python_Minor_Projects_Short_Notes.pdf"
    build_pdf(out_path)
