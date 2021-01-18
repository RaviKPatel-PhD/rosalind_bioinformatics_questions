def FIB(n: int, k: int) -> int:
   dp = [None]*(n)
   dp[0], dp[1] = 1,1
   months = 2
   while months < n:
      dp[months] = dp[months-1] + dp[months-2]*k
      months +=1
   return dp[-1]

if __name__ == "__main__":
   with open("rosalind_fib.txt") as text_file:
      example = text_file.read().strip()
   ex = [int(i) for i in example.split(" ")]
   print(FIB(ex[0],ex[1]))