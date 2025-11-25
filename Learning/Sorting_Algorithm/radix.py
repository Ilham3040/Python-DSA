import math

def radix_sort(arr):
  max_value= max(arr)
  total_digits = math.floor(math.log10(max_value)) + 1
  for exp in range(total_digits):
    digits_arr = [0] * 10
    output = [0] * len(arr)
    for num in arr:
      digit = (num // 10**exp) % 10
      digits_arr[digit] += 1
    for i in range(1,10):
      digits_arr[i] += digits_arr[i-1]
    for num in reversed(arr):
      digit = (num // 10**exp) % 10
      digits_arr[digit] -= 1
      output[digits_arr[digit]] = num
    arr = output
    
  return arr
    



if __name__ == "__main__":
  my_arr = [666,578,979,101,70,30,65]

  my_arr = radix_sort(my_arr)
  print(my_arr)
