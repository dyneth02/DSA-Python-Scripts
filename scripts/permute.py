def permutations(string, remain = ""):
    if len(string) == 0:
        print(remain)
    else:
        for i in range(len(string)):
          letter = string[i]
          front = string[:i]
          back = string[i+1:]
          together = front + back
          print("looped")
          permutations(together, remain + letter)


permutations("ABC")
