def palindrome():
    s="madam"
    left=0
    right=len(s)-1
    while(left<right):
        if s[left]!=s[right]:
            print("not a palindrome")
            return
            left+=1
            right-=1
    print("not a palindrome")
palindrome()

