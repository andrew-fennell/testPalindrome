import argparse

def isPalindrome(s: str):
    l, r = 0, len(s) - 1
    mistakes = 0

    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else: # mistakes
            mistakes += 1
            if mistakes > 1:
                return False
            
            # case 1: increment left
            l += 1
            if s[l] == s[r]:
                continue
            l -= 1
            # case 2: decrement right
            r -= 1
            if s[l] == s[r]:
                continue
            return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Check if a string is a palindrome")
    parser.add_argument("string", type=str)

    args = parser.parse_args()
    # Adding comment
    if isPalindrome(args.string):
        print(f"{args.string} is a palindrome!")
    else:
        print(f"{args.string} is not a palindrome...")

    

if __name__ == "__main__":
    """
    sample = "racecar"
    sample2 = "race car"

    print(isPalindrome(sample))
    """