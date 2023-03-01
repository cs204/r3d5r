def main():
    s = input()
    print(convert(s))
def convert(s):
    s = s.replace(':)', '\U0001f642')
    s = s.replace(':(', '\U0001f641')
    return s
main()