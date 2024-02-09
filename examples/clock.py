import tkinter as tk
import time

# 建立主視窗
root = tk.Tk()

# 設定主視窗標題
root.title("數字型時鐘")

# 設定主視窗大小
root.geometry("200x100")

# 建立一個標籤用來顯示時間
label = tk.Label(root, font=("Arial", 20))
label.pack()

# 定義一個函數來更新時間顯示
def update_time():
    # 取得目前時間
    time = tk.time()

    # 將時間轉換成字串
    time_str = tk.strftime("%H:%M:%S", time)

    # 更新標籤的文字
    label.config(text=time_str)

    # 每隔1秒更新一次時間顯示
    root.after(1000, update_time)

# 呼叫update_time函數來初始化時間顯示
update_time()

# 顯示主視窗
root.mainloop()
