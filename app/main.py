# This line imports the "calculator" function from another file.
# Think of "calculator" as a tool or function that we previously created elsewhere,
# and now we are telling the program, "Find that calculator tool for us."
# The "app" is like a folder, and inside it, there's a file called "calculator.py",
# which contains the "calculator" function that we need.
from app.calculator import calculator

# This part is crucial! It checks if this file is being run directly.
# Here's how it works: in Python, we sometimes run files directly, and other times we use them as part of other programs.
# The variable "__name__" is special in Python and helps determine how a file is being run.
# If "__name__" equals "__main__", it means we are running the file directly.

# In simple terms, this line says: "If this program is being run directly, start the calculator."
if __name__ == "__main__":
    # Here, we use the calculator function we imported earlier. This will launch the calculator, 
    # which will keep running and performing math operations based on user input.
    calculator()
