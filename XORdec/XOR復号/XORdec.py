import tkinter as tk
from tkinter import messagebox

def xor_decrypt():
    ciphertext = entry_cipher.get()
    key = entry_key.get()

    if not ciphertext or not key:
        messagebox.showwarning("入力エラー", "暗号文とキーを入力してください")
        return
    
    try:
        cipher_bytes = bytes.fromhex(ciphertext)
    except ValueError:
        messagebox.showerror("形式エラー", "暗号文は16進数(hex)形式で入力してください")
        return
    
    key_bytes = key.encode()
    decrypted = bytes([b^key_bytes[i%len(key_bytes)]for i, b in enumerate(cipher_bytes)])

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted.decode(errors='replace'))

#GUI
root = tk.Tk()
root.title("XOR暗号デコーダ")
    
tk.Label(root, text="暗号文()hex :").pack()
entry_cipher = tk.Entry(root, width=50)
entry_cipher.pack()

tk.Label(root, text="キー:").pack()
entry_key = tk.Entry(root, width=50)
entry_key.pack()

tk.Button(root, text="復号する", command=xor_decrypt).pack(pady=5)

tk.Label(root, text="復号結果:").pack()
output_text=tk.Text(root, height=5, width=50)
output_text.pack()

root.mainloop()