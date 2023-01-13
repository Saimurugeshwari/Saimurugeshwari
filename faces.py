def main():
    #Get user input
        get=input()
    #Call convert function
        result = convert(get)
    #print the result
        print(result)
def convert(get):
    #replace :) for happy emoji
    get1 = get.replace(":)", '🙂')
     #replace :( for sad emoji
    get2 = get1.replace(":(", '🙁')
    #return string
    return get2

main()