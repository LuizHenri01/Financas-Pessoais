import customtkinter as ctk

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__() # aqui estou rodando o __init__ do CTk primeiro

        self.title("fincanças Pessoais")
        self.geometry("900x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.criar_layout()

    def criar_layout(self):
    # sidebar esquerda
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

    # área principal direita
        self.area_principal = ctk.CTkFrame(self)
        self.area_principal.pack(side="right", fill="both", expand=True)

        self.criar_sidebar()

    def criar_sidebar(self):
    # título do app
        titulo = ctk.CTkLabel(
        self.sidebar,
        text="💰 Finanças",
        font=ctk.CTkFont(size=20, weight="bold")
    )
        titulo.pack(pady=30)

    # botões do menu
        ctk.CTkButton(
        self.sidebar,
        text="Dashboard",
        command=lambda: print("dashboard")
    ).pack(pady=10, padx=20)

        ctk.CTkButton(
        self.sidebar,
        text="Adicionar",
        command=lambda: print("adicionar")
    ).pack(pady=10, padx=20)

        ctk.CTkButton(
        self.sidebar,
        text="Histórico",
        command=lambda: print("histórico")
    ).pack(pady=10, padx=20)