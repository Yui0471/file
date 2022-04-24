#Python環境の用意
#OBSでウインドウキャプチャ→フィルタからクロマキーで背景を抜いて色補正をかける

import winsound #windows環境前提
import time
import random
import tkinter as tk
import threading
import os

pathlist = [
            #再生したいBGMをパスで複数指定(同ディレクトリならパス無くてもOK)　※wav形式のみ
        ]

class Window:
    back = -1
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("BGM")
        self.label = tk.Label(self.root)
        self.label["font"] = ("MS P ゴシック", 50) #フォントとフォントサイズを指定(インストール済みフォントもOK,プロポーショナル推奨)
        self.label["bg"] = "#00ff00" #背景色の指定(#00ff00でグリーンバック)
        self.label["fg"] = "#2b2b2b" #文字色の指定
        self.label.grid(column=0, row=0)

    def playingWave(self):
        while True:
            index = random.randrange(len(pathlist))

            while self.back != -1 and self.back == index:
                index = random.randrange(len(pathlist))

            path = pathlist[index]

            self.back = index
            title = os.path.basename(path)
            self.label["text"] = title[:title.rfind(".")]
            
            winsound.PlaySound(path, winsound.SND_FILENAME)
            time.sleep(1)

if __name__ == "__main__":
    window = Window()
    thread = threading.Thread(target=window.playingWave)
    thread.start()
    window.root.mainloop()