def main():
    time=input("what time is it? ")
    time= convert(time)

    if time  >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")
    else:
        pass
def convert(time):
    hours, minutes = time.split(":")
    minutes=float(minutes)/60
    hours=float(hours)
    time=minutes+hours
    return time

if __name__ == "__main__":
        main()