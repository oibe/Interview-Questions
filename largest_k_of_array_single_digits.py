def largest_k(array, k):
      counts = [0] * 10
      for number in array:
          counts[number] += 1

      sum = 0
      index = 9
      while k > 0:
          if k - counts[index] >= 0:
              sum += index * counts[index]
          else:
              sum += index * k

          k -= counts[index]
          index -= 1
      return sum

if __name__ == "__main__":
    # answer = 21
    print largest_k([1, 2, 3, 4, 5, 6], k=6)

    # answer = 20
    print largest_k([1, 2, 3, 4, 5, 6], k=5)

    # answer = 26
    print largest_k([9, 9, 8, 3, 5, 2, 6, 6], k=3)
