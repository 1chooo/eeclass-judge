import os
import subprocess

def get_code(txt):
    with open("tmp.py", "w") as file:
        file.write(txt)

    try:
        output = subprocess.check_output(
            ["python", "tmp.py"], 
            stderr=subprocess.STDOUT, 
            universal_newlines=True,
        )
        print("Script output:")
        print(output)

        result = judge_question_1(output)
        return result
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)
        return e.output
    finally:
        os.remove("tmp.py")

def judge_question_1(output):
    if output == "Hello World\n":
        return "AC"
    elif output == "Hello World":
        return "AC"
    else:
        return "WA"
