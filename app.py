import eel


def main():
    eel.init("web")
    eel.start("hello.html", size=(1024, 768), port=8080)


if __name__ == "__main__":
    main()