class Solution:
    def helloworld(self, string):
        if string == "Hello World!":
            return "Hello World!"
        else:
            pass

def main():
    tc1 = Solution()
    string1= input()
    ans = tc1.helloworld(string1)
    print(ans)

if __name__ == "__main__":
    main()