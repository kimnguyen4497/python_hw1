def multiply_list(numberlist):

	# Multiply elements one by one
    result = 1
    for i in numberlist:
          try:
               int(i)
          except:
               return False

    for i in numberlist:
         result = result * i
         
    return result

