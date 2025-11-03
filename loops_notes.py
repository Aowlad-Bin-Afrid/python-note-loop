# ---------------------------------------------------------
# 🟩  Loops (For Loop & While Loop Notes)
# ---------------------------------------------------------
# Created by: chatGPT
# Description:
#   Detailed explanation of "for loop" and "while loop" in Python
# ---------------------------------------------------------

# =========================================================
# 🔶 1️⃣ What is a Loop?
# =========================================================
# A loop is a programming structure that repeats a block of code
# multiple times until a certain condition becomes False.
# Loops help avoid writing the same code repeatedly.

# In Python, there are two main types of loops:
#   1. for loop
#   2. while loop
# ---------------------------------------------------------


# =========================================================
# 🟦 2️⃣ FOR LOOP
# =========================================================
# 👉 Definition:
# A "for loop" is used when you know in advance how many times
# the loop should run.

# 👉 Structure:
# for variable in range(start, stop, step):
#     # code block
# ---------------------------------------------------------


# ✅ Example 1: Print numbers 1 to 5
for i in range(1, 6):
    print("Number:", i)

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
# ---------------------------------------------------------


# ✅ Example 2: Sum of 1 to 5
total = 0
for i in range(1, 6):
    total += i
print("Total =", total)
# Output: Total = 15
# ---------------------------------------------------------


# 🧠 How it works:
# range(1, 6) means it starts from 1 and stops before 6.
# In each iteration, the variable 'i' increases by 1 automatically.


# =========================================================
# 🟩 3️⃣ WHILE LOOP
# =========================================================
# 👉 Definition:
# A "while loop" is used when you don’t know how many times the loop
# will run — it continues as long as a given condition is True.

# 👉 Structure:
# while condition:
#     # code block
# ---------------------------------------------------------


# ✅ Example 1: Print numbers 1 to 5
i = 1
while i <= 5:
    print("Number:", i)
    i += 1

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
# ---------------------------------------------------------


# 🧠 How it works:
# Starts with i = 1
# The loop keeps running while (i <= 5) is True.
# Each time, i increases by 1.
# When i becomes 6, the condition is False and the loop stops.


# =========================================================
# 🟨 4️⃣ Key Difference Between FOR and WHILE Loop
# =========================================================
# Feature             | For Loop                  | While Loop
# -------------------------------------------------------------
# When used           | Loop count known           | Loop count unknown
# Condition control   | range() or iterable        | logical condition
# Initialization      | inside range()             | before the loop
# Increment/Decrement | automatic inside range()   | manually inside loop
# Typical use case    | Print 1–10 numbers         | Wait for user input
# -------------------------------------------------------------


# =========================================================
# 🟧 5️⃣ While Loop Example (User Input)
# =========================================================
# Example: Keep asking for password until the correct one is entered

# Uncomment to test:
# password = ""
# while password != "python":
#     password = input("Enter password: ")
# print("Access Granted!")
# ---------------------------------------------------------


# =========================================================
# 🟪 6️⃣ Extra Tips (break, continue, else)
# =========================================================
# break    → Stops the loop immediately
# continue → Skips the current iteration and goes to the next one
# else     → Executes once after the loop finishes (if not broken)
# ---------------------------------------------------------


# ✅ Example: Skip number 3
for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    print(i)
else:
    print("Loop Finished!")

# Output:
# 1
# 2
# 4
# 5
# Loop Finished!
# ---------------------------------------------------------


# =========================================================
# 🟫 7️⃣ Summary
# =========================================================
# 🔹 for loop  → used when the number of repetitions is known
# 🔹 while loop → used when repetition depends on a condition
# ---------------------------------------------------------

# ✅ Quick Comparison Table:
# Concept        | for loop            | while loop
# -------------------------------------------------
# Repeat count   | Fixed               | Unknown
# Condition type | range()             | Boolean condition
# Example        | for i in range(5)   | while x < 5
# -------------------------------------------------

# 🎯 Final Note:
#   🔥 Use "for loop" → when you know how many times to repeat
#   🔥 Use "while loop" → when repetition depends on a condition
# ---------------------------------------------------------
