def arithmetic_arranger(problems, optional = False):
  firstList = list() # list for first number
  secondList = list() # list for the operator
  dashList = list() # list for the dash line
  fourthList = list() # list for the answers

  # problems shouldn't have more than 5 elements
  if len(problems) > 5:
    return('Error: Too many problems.')
  
  # for loop to split the list contents
  for problem in problems:
    parts = problem.split()
    
    # for loop to determine which of the two numbers has more characters to create the proper spacing
    for i in parts:
      try:
        if int(parts[0]) > int(parts[2]):
          length = len(parts[0]) + 2 # add 2 to accomodate for the operator and the required space
        else:
          length = len(parts[2]) + 2
      except:
        return('Error: Numbers must only contain digits.')

      # if statement for the first number passed
      if parts.index(i) == 0:
        first = i
        if len(first) <= 4: # string can't be longer than four characters
          if first.isdecimal(): # string can only contain numbers
            firstList.append(str(' ' * (length - len(first)) + first)) # create spacing based on the length
          else:
            return('Error: Numbers must only contain digits.')
        else:
          return('Error: Numbers cannot be more than four digits.')

      # elif to determine if the operator is '+' or '-'
      elif parts.index(i) == 1:
        second = i
        if second == '+' or second == '-':
          continue
        else:
          return("Error: Operator must be '+' or '-'.")

      # else statement for the second number passed
      elif parts.index(i) == 2:
        third = i
        if len(third) <= 4: # string can't be longer than four characters
          if third.isdecimal(): # string can only contain numbers
            secondList.append(str(second + ' ' * (length - len(third) - 2) + ' ' + third)) # create spacing based on the length
          else:
            return('Error: Numbers must only contain digits.')
        else:
          return('Error: Numbers cannot be more than four digits.')
        dashList.append(str('-' * length)) # dash line creation

        # if optional is true then create answers based on the arithmetic sign
        if optional == True:
          if second == '+':
            answer = int(first) + int(third)
            fourthList.append(str(' ' * (length - len(str(answer))) + str(answer))) # create spacing based on the length
          else:
            answer = int(first) - int(third)
            fourthList.append(str(' ' * (length - len(str(answer))) + str(answer))) # create spacing based on the length
            
  # if else to determine which arranged_problems will be returned based on the optional argument
  if optional == True:
    # create proper spacing between each problem
    arranged_problems = '    '.join(firstList) + '\n' + '    '.join(secondList) + '\n' + '    '.join(dashList) + '\n' + '    '.join(fourthList)
    return arranged_problems
  else:
    # create proper spacing between each problem
    arranged_problems = '    '.join(firstList) + '\n' + '    '.join(secondList) + '\n' + '    '.join(dashList)
    return arranged_problems