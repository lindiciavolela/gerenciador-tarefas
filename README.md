# Gerenciador de Tarefas — Python

Projeto em Python para gerenciar tarefas pelo terminal, com cores, prioridades e salvamento automático em arquivo JSON.

## Funcionalidades

- Adicionar tarefas com título, descrição e prioridade (Alta / Média / Baixa)
- Listar todas as tarefas com status visual
- Filtrar por **pendentes** ou **concluídas**
- Marcar tarefas como concluídas
- Remover tarefas
- Resumo com contagens
- Dados salvos automaticamente em `tarefas.json`

## Como executar

Você precisa ter o **Python 3** instalado.

```bash
python tarefas.py
```

## Estrutura do projeto

```
gerenciador_tarefas/
├── tarefas.py       # Código principal
├── tarefas.json     # Criado automaticamente ao adicionar tarefas
└── README.md        # Este arquivo
```

## Conceitos utilizados

- Funções e modularização
- Leitura e escrita de arquivos JSON
- Manipulação de listas e dicionários
- Formatação de strings com cores ANSI
- Tratamento de erros com `try/except`
- Módulos da biblioteca padrão: `json`, `os`, `datetime`
