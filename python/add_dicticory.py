from PyPDF2 import PdfReader, PdfWriter

# 输入和输出文件
input_pdf_path = "data/SuttonBartoIPRLBook2ndEd.pdf"
output_pdf_path = "outputs/SuttonBartoIPRLBook2ndEd.pdf"

# 读取 PDF
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# 复制所有页面
for page in reader.pages:
    writer.add_page(page)

# 目录及子目录（全部强制用三元组表示，避免解包错误）
toc = [
    ("Preface", -6, []),
    ("Series Forward", -2, []),
    ("Summary of Notation", -1, []),
    (
        "1 The Reinforcement Learning Problem",
        1,
        [
            ("1.1 Reinforcement Learning", 2, []),
            ("1.2 Examples", 5, []),
            ("1.3 Elements of Reinforcement Learning", 7, []),
            ("1.4 Limitations and Scope", 9, []),
            ("1.5 An Extended Example: Tic-Tac-Toe", 10, []),
            ("1.6 Summary", 15, []),
            ("1.7 History of Reinforcement Learning", 16, []),
            ("1.8 Bibliographical Remarks", 25, []),
        ],
    ),
    (
        "2 Multi-arm Bandits",
        31,
        [
            ("2.1 An n-Armed Bandit Problem", 32, []),
            ("2.2 Action-Value Methods", 33, []),
            ("2.3 Incremental Implementation", 36, []),
            ("2.4 Tracking a Nonstationary Problem", 38, []),
            ("2.5 Optimistic Initial Values", 39, []),
            ("2.6 Upper-Confidence-Bound Action Selection", 41, []),
            ("2.7 Gradient Bandits", 42, []),
            ("2.8 Associative Search (Contextual Bandits)", 46, []),
            ("2.9 Summary", 47, []),
        ],
    ),
    (
        "3 Finite Markov Decision Processes",
        53,
        [
            ("3.1 The Agent–Environment Interface", 53, []),
            ("3.2 Goals and Rewards", 57, []),
            ("3.3 Returns", 59, []),
            ("3.4 Unified Notation for Episodic and Continuing Tasks", 61, []),
            ("3.5 The Markov Property", 62, []),
            ("3.6 Markov Decision Processes", 67, []),
            ("3.7 Value Functions", 70, []),
            ("3.8 Optimal Value Functions", 75, []),
            ("3.9 Optimality and Approximation", 79, []),
            ("3.10 Summary", 80, []),
        ],
    ),
    (
        "4 Dynamic Programming",
        89,
        [
            ("4.1 Policy Evaluation", 90, []),
            ("4.2 Policy Improvement", 94, []),
            ("4.3 Policy Iteration", 96, []),
            ("4.4 Value Iteration", 98, []),
            ("4.5 Asynchronous Dynamic Programming", 101, []),
            ("4.6 Generalized Policy Iteration", 104, []),
            ("4.7 Efficiency of Dynamic Programming", 106, []),
            ("4.8 Summary", 107, []),
        ],
    ),
    (
        "5 Monte Carlo Methods",
        113,
        [
            ("5.1 Monte Carlo Prediction", 114, []),
            ("5.2 Monte Carlo Estimation of Action Values", 119, []),
            ("5.3 Monte Carlo Control", 120, []),
            ("5.4 Monte Carlo Control without Exploring Starts", 124, []),
            ("5.5 Off-policy Prediction via Importance Sampling", 127, []),
            ("5.6 Incremental Implementation", 133, []),
            ("5.7 Off-Policy Monte Carlo Control", 135, []),
            ("5.8 Importance Sampling on Truncated Returns", 136, []),
            ("5.9 Summary", 138, []),
        ],
    ),
    (
        "6 Temporal-Difference Learning",
        143,
        [
            ("6.1 TD Prediction", 143, []),
            ("6.2 Advantages of TD Prediction Methods", 148, []),
            ("6.3 Optimality of TD(0)", 151, []),
            ("6.4 Sarsa: On-Policy TD Control", 154, []),
            ("6.5 Q-Learning: Off-Policy TD Control", 157, []),
            ("6.6 Games, Afterstates, and Other Special Cases", 160, []),
            ("6.7 Summary", 161, []),
        ],
    ),
    (
        "7 Eligibility Traces",
        167,
        [
            ("7.1 n-Step TD Prediction", 168, []),
            ("7.2 The Forward View of TD(λ)", 172, []),
            ("7.3 The Backward View of TD(λ)", 177, []),
            ("7.4 Equivalences of Forward and Backward Views", 181, []),
            ("7.5 Sarsa(λ)", 183, []),
            ("7.6 Watkins’s Q(λ)", 186, []),
            ("7.7 Off-policy Eligibility Traces using Importance Sampling", 188, []),
            ("7.8 Implementation Issues", 189, []),
            ("7.9 Variable λ", 190, []),
            ("7.10 Conclusions", 190, []),
        ],
    ),
    (
        "8 Planning and Learning with Tabular Methods",
        195,
        [
            ("8.1 Models and Planning", 195, []),
            ("8.2 Integrating Planning, Acting, and Learning", 198, []),
            ("8.3 When the Model Is Wrong", 203, []),
            ("8.4 Prioritized Sweeping", 206, []),
            ("8.5 Full vs. Sample Backups", 210, []),
            ("8.6 Trajectory Sampling", 213, []),
            ("8.7 Heuristic Search", 217, []),
            ("8.8 Monte Carlo Tree Search", 220, []),
            ("8.9 Summary", 220, []),
        ],
    ),
    (
        "9 On-policy Approximation of Action Values",
        225,
        [
            ("9.1 Value Prediction with Function Approximation", 226, []),
            ("9.2 Gradient-Descent Methods", 229, []),
            ("9.3 Linear Methods", 232, []),
            ("9.4 Control with Function Approximation", 241, []),
            ("9.5 Should We Bootstrap?", 247, []),
            ("9.6 Summary", 249, []),
        ],
    ),
    ("10 Off-policy Approximation of Action Values", 255, []),
    (
        "11 Policy Approximation",
        257,
        [
            ("11.1 Actor–Critic Methods", 257, []),
            ("11.2 Eligibility Traces for Actor–Critic Methods", 259, []),
            ("11.3 R-Learning and the Average-Reward Setting", 260, []),
        ],
    ),
    ("12 Psychology", 269, []),
    ("13 Neuroscience", 271, []),
    (
        "14 Applications and Case Studies",
        273,
        [
            ("14.1 TD-Gammon", 273, []),
            ("14.2 Samuel’s Checkers Player", 279, []),
            ("14.3 The Acrobot", 282, []),
            ("14.4 Elevator Dispatching", 286, []),
            ("14.5 Dynamic Channel Allocation", 291, []),
            ("14.6 Job-Shop Scheduling", 295, []),
        ],
    ),
    (
        "15 Prospects",
        303,
        [
            ("15.1 The Unified View", 303, []),
            ("15.2 State Estimation", 306, []),
            ("15.3 Temporal Abstraction", 306, []),
            ("15.4 Predictive Representations", 306, []),
            ("15.5 Other Frontier Dimensions", 306, []),
        ],
    ),
    ("References", 311, []),
    ("Index", 338, []),
]

# PDF 文件实际页码和书籍页码的偏移
pdf_preface_page = 8
book_preface_page = 8
offset = pdf_preface_page - book_preface_page
# offset = 8


# 递归函数：添加目录和子目录
def add_toc_items(writer, parent, items, offset):
    for title, book_page, children in items:
        pdf_page = book_page + offset - 1
        # if 0 <= pdf_page < len(reader.pages):
        if parent is None:
            item = writer.add_outline_item(title, pdf_page + 14)
        else:
            item = writer.add_outline_item(title, pdf_page, parent=parent)
        if children:
            add_toc_items(writer, item, children, 14)


# 添加目录及子目录
add_toc_items(writer, None, toc, offset)

# 保存带子目录的新 PDF
with open(output_pdf_path, "wb") as f:
    writer.write(f)

output_pdf_path
