import aircontrol

def main():
    print("Something went wrong." if aircontrol.get_state() == aircontrol.UAVState.UNKNOWN else "???")

if __name__ == "__main__":
    main()