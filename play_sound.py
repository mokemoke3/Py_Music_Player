import pygame

def playmusic(mp3):
    pygame.mixer.init(frequency = 44100, channels=2)    # 初期設定
    pygame.mixer.music.load(mp3)     # 音楽ファイルの読み込み
    pygame.mixer.music.play(1)              # 音楽の再生回数(1回)
    while(1):   #これ以降を後で書き換える
        a = input("Finish? --->")
        if(a == 'y'): break
    pygame.mixer.music.fadeout(1)              # 再生の終了(フェードアウト付き)
    return 0
    
if __name__ == "__main__":
    playmusic("n74.mp3")