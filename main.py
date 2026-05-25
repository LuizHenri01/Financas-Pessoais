"""
Sistema de Finanças Pessoal Com funções para:
Cadastra receitas e despesas
Vê um dashboard com gráficos do seu saldo
Filtra por mês e categoria
Exporta relatório
"""
from telas.dashboard import Dashboard

app = Dashboard()
app.mainloop()