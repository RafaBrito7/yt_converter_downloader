from pytube import YouTube


def main():
    link = "https://www.youtube.com/watch?v=9v200un_STc&ab_channel=CNNBrasil"
    yt = YouTube(link)

    print(f"Título: {yt.title}")
    print(f"Duração: {yt.length} seg")

if __name__ == "__main__":
    main()