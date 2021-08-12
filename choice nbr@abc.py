import itertools


def brute_force(charset, length):
  return (''.join(candidate)
   for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
   for i in range (1, length + 1)))

def main():
  for attempt in brute_force('0123456789', 8):
    print(attempt)
    
    
if __name__ == '__main__':
  main()