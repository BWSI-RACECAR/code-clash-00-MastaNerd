class HelloWorld:
    def helloWorlder(self, input):
        if input == "Hello World!":
            return "Hello World!"
        else:
            pass

def main():
    tc1 = HelloWorld()
    string1= input()
    ans = tc1.helloWorlder(string1)
    print(ans)

if __name__ == "__main__":
    main()