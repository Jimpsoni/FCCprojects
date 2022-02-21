def arithmetic_arranger(counts, answers=False):
    if len(counts) > 5:
        return "Error: Too many problems."

    # Build the return value piece by piece
    first_line, second_line, dashed_line, answer_line = "", "", "", ""

    for problem in counts:
        n1, oper, n2 = problem.split(" ")
        length_n1, length_n2 = len(n1), len(n2)

        if oper not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if length_n1 > 4 or length_n2 > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            int(n1), int(n2)
        except ValueError:
            return "Error: Numbers must only contain digits."

        answer = str(eval(problem))
        length_answer = len(answer)

        longer = length_n1 if length_n1 > length_n2 else length_n2

        first_line += " " * (longer - length_n1 + 2) + n1
        second_line += oper + " " * (longer - length_n2 + 1) + n2
        dashed_line += "-" * (longer + 2)
        answer_line += " " * (longer - length_answer + 2) + answer

        first_line += "    "
        second_line += "    "
        dashed_line += "    "
        answer_line += "    "

    whole_string = first_line[:-4] + "\n" + second_line[:-4] + "\n" + dashed_line[:-4]

    if answers:
        whole_string += "\n" + answer_line[:-4]

    return whole_string
