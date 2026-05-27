import json
import os
from datetime import datetime

ARQUIVO = "tarefas.json"

# ─── Cores no terminal ───────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
VERDE  = "\033[92m"
AMARELO= "\033[93m"
VERMELHO="\033[91m"
CIANO  = "\033[96m"
ROXO   = "\033[95m"

# ─── Carregar / Salvar ───────────────────────────────────────────
def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

# ─── Utilitários de exibição ─────────────────────────────────────
def cor_prioridade(prioridade):
    return {
        "Alta":   VERMELHO,
        "Média":  AMARELO,
        "Baixa":  VERDE,
    }.get(prioridade, RESET)

def exibir_tarefa(i, t):
    status   = f"{VERDE}✔ Concluída{RESET}" if t["concluida"] else f"{AMARELO}⏳ Pendente{RESET}"
    cor_prio = cor_prioridade(t["prioridade"])
    print(f"  {BOLD}[{i+1}]{RESET} {t['titulo']}")
    print(f"       Prioridade : {cor_prio}{t['prioridade']}{RESET}  |  Status: {status}")
    print(f"       Criada em  : {t['criada_em']}")
    if t.get("descricao"):
        print(f"       Descrição  : {t['descricao']}")
    print()

def cabecalho(texto):
    print(f"\n{CIANO}{BOLD}{'─'*45}")
    print(f"  {texto}")
    print(f"{'─'*45}{RESET}\n")

# ─── Funcionalidades ─────────────────────────────────────────────
def listar_tarefas(tarefas, filtro=None):
    cabecalho("📋  LISTA DE TAREFAS")

    lista = tarefas
    if filtro == "pendentes":
        lista = [t for t in tarefas if not t["concluida"]]
    elif filtro == "concluidas":
        lista = [t for t in tarefas if t["concluida"]]

    if not lista:
        print("  Nenhuma tarefa encontrada.\n")
        return

    for i, t in enumerate(lista):
        exibir_tarefa(i, t)

def adicionar_tarefa(tarefas):
    cabecalho("➕  NOVA TAREFA")
    titulo = input("  Título da tarefa : ").strip()
    if not titulo:
        print(f"  {VERMELHO}Título não pode ser vazio.{RESET}\n")
        return

    descricao = input("  Descrição (opcional): ").strip()

    print("  Prioridade: 1-Alta  2-Média  3-Baixa")
    opcao = input("  Escolha [1/2/3]: ").strip()
    prioridade = {"1": "Alta", "2": "Média", "3": "Baixa"}.get(opcao, "Média")

    tarefa = {
        "titulo":    titulo,
        "descricao": descricao,
        "prioridade":prioridade,
        "concluida": False,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f"\n  {VERDE}✔ Tarefa '{titulo}' adicionada!{RESET}\n")

def concluir_tarefa(tarefas):
    cabecalho("✅  CONCLUIR TAREFA")
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        num = int(input("  Número da tarefa a concluir: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas[num]["concluida"] = True
            salvar_tarefas(tarefas)
            print(f"\n  {VERDE}✔ Tarefa marcada como concluída!{RESET}\n")
        else:
            print(f"  {VERMELHO}Número inválido.{RESET}\n")
    except ValueError:
        print(f"  {VERMELHO}Digite apenas números.{RESET}\n")

def remover_tarefa(tarefas):
    cabecalho("🗑️  REMOVER TAREFA")
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        num = int(input("  Número da tarefa a remover: ")) - 1
        if 0 <= num < len(tarefas):
            removida = tarefas.pop(num)
            salvar_tarefas(tarefas)
            print(f"\n  {VERDE}✔ Tarefa '{removida['titulo']}' removida!{RESET}\n")
        else:
            print(f"  {VERMELHO}Número inválido.{RESET}\n")
    except ValueError:
        print(f"  {VERMELHO}Digite apenas números.{RESET}\n")

def resumo(tarefas):
    cabecalho("📊  RESUMO")
    total     = len(tarefas)
    concluidas= sum(1 for t in tarefas if t["concluida"])
    pendentes = total - concluidas
    print(f"  Total     : {BOLD}{total}{RESET}")
    print(f"  Pendentes : {AMARELO}{pendentes}{RESET}")
    print(f"  Concluídas: {VERDE}{concluidas}{RESET}\n")

# ─── Menu principal ──────────────────────────────────────────────
def menu():
    print(f"\n{ROXO}{BOLD}{'═'*45}")
    print("   ✅  GERENCIADOR DE TAREFAS")
    print(f"{'═'*45}{RESET}")
    print("  1. Ver todas as tarefas")
    print("  2. Ver apenas pendentes")
    print("  3. Ver apenas concluídas")
    print("  4. Adicionar nova tarefa")
    print("  5. Marcar tarefa como concluída")
    print("  6. Remover tarefa")
    print("  7. Resumo")
    print("  0. Sair")
    print(f"{ROXO}{'─'*45}{RESET}")
    return input("  Escolha uma opção: ").strip()

def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()
        if   opcao == "1": listar_tarefas(tarefas)
        elif opcao == "2": listar_tarefas(tarefas, filtro="pendentes")
        elif opcao == "3": listar_tarefas(tarefas, filtro="concluidas")
        elif opcao == "4": adicionar_tarefa(tarefas)
        elif opcao == "5": concluir_tarefa(tarefas)
        elif opcao == "6": remover_tarefa(tarefas)
        elif opcao == "7": resumo(tarefas)
        elif opcao == "0":
            print(f"\n  {VERDE}Até logo! 👋{RESET}\n")
            break
        else:
            print(f"  {VERMELHO}Opção inválida.{RESET}\n")

if __name__ == "__main__":
    main()
