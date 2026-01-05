import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def imagens_para_pdf():
    arquivos = filedialog.askopenfilenames(
        title="Selecione as imagens",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.webp")]
    )

    if not arquivos:
        return

    imagens = []
    for arquivo in arquivos:
        img = Image.open(arquivo).convert("RGB")
        imagens.append(img)

    salvar_em = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF", "*.pdf")],
        title="Salvar PDF"
    )

    if not salvar_em:
        return

    imagens[0].save(
        salvar_em,
        save_all=True,
        append_images=imagens[1:]
    )

    messagebox.showinfo(
        "Sucesso",
        f"PDF criado com {len(imagens)} páginas!"
    )

# --- Interface ---
root = tk.Tk()
root.title("Unir imagens em PDF")
root.geometry("300x150")

btn = tk.Button(
    root,
    text="Selecionar imagens e gerar PDF",
    command=imagens_para_pdf
)
btn.pack(expand=True)

root.mainloop()
