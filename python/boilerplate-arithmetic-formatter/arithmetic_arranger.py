def arithmetic_arranger(problems, giveSolution=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    valid_ops = ['+', '-']
    digits = "0123456789"
    unvalid_ops = ['*', '/']

    first_problem = True

    first_line = ""
    second_line = ""
    third_line = ""
    if giveSolution:
        fourth_line = ""

    for problem in problems:
        if any(x in problem for x in unvalid_ops):
            return "Error: Operator must be '+' or '-'."

        for op in valid_ops:
            if op in problem:
              pos = problem.find(op)
              first = problem[:pos].strip()
              second = problem[pos + 1:].strip()

              if not all(x in digits for x in first + second):
                  return "Error: Numbers must only contain digits."

              if len(first) > 4 or len(second) > 4:
                  return "Error: Numbers cannot be more than four digits."

              maxLength = len(first) if len(first) > len(second) else len(second)
              maxLength += 2
              if giveSolution:
                  if op == "+":
                      fourth = str(int(first) + int(second))
                  elif op == "-":
                      fourth = str(int(first) - int(second))
                  maxLength = maxLength if maxLength > len(fourth) else len(fourth)

              while len(first) < maxLength:
                  first = " " + first
              while len(second) < maxLength - 1:
                  second = " " + second
              second = op + second
              third = ""
              while len(third) < maxLength:
                  third += "-"


              if not first_problem:
                  first_line += "    "
                  second_line += "    "
                  third_line += "    "
                  if giveSolution:
                      fourth_line += "    "

              first_line += first
              second_line += second
              third_line += third
              if giveSolution:
                  while len(fourth) < maxLength:
                    fourth = " " + fourth
                  fourth_line += fourth

        first_problem = False

    arranged_problems = first_line + "\n" + second_line + "\n" + third_line
    if giveSolution:
        arranged_problems += "\n" + fourth_line

    return arranged_problems
