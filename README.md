📋 TodoApp — SPEC-Driven Development com Google Antigravity
> Aplicação web de lista de tarefas construída **sem escrever código manualmente**.
> Todo o código foi gerado por agentes autônomos do Google Antigravity a partir de especificações em Markdown.
---
🧠 Como Funciona
Este projeto segue o paradigma SPEC-Driven Development (SDD): a especificação é o produto principal, e o código é apenas seu subproduto gerado automaticamente pelos agentes.
O ciclo funciona em 4 fases:
```
/startcycle "descrição da ideia"
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│  Phase 1 — SPEC                                         │
│  Agente PM lê a ideia e gera spec.md com histórias     │
│  de usuário no formato Given/When/Then                  │
│               ↓ [você aprova]                           │
│  Phase 2 — PLAN                                         │
│  Agente Full-Stack gera plan.md: estrutura de           │
│  arquivos, dependências + Constitutional Check ✅       │
│               ↓ [você aprova]                           │
│  Phase 3 — IMPLEMENT                                    │
│  Agentes geram todo o código do projeto                 │
│               ↓                                         │
│  Phase 4 — VERIFY                                       │
│  Agente QA executa pytest e audita constitution.md     │
└─────────────────────────────────────────────────────────┘
        │
        ▼
  flask run → http://localhost:5000 ✅
```
O desenvolvedor não escreve código — apenas revisa e aprova cada fase.
---
🗂️ Estrutura do Projeto
```
todoapp/
├── .agents/
│   └── rules/
│       └── constitution.md     ← lei suprema arquitetural
├── .env                        ← variáveis de ambiente (não commitar)
├── .env.example                ← modelo de variáveis
├── AGENTS.md                   ← regras globais para os agentes
├── GEMINI.md                   ← regras específicas do Antigravity
├── requirements.txt            ← dependências Python
├── spec.md                     ← especificação funcional (gerada pelo Agente PM)
├── plan.md                     ← plano técnico (gerado pelo Agente Dev)
├── run.py                      ← entrypoint da aplicação
└── app/
    ├── __init__.py             ← factory pattern do Flask
    ├── auth/
    │   ├── __init__.py         ← Blueprint de autenticação
    │   ├── routes.py           ← /login, /register, /logout
    │   └── forms.py            ← LoginForm, RegisterForm
    ├── tasks/
    │   ├── __init__.py         ← Blueprint de tarefas
    │   ├── routes.py           ← CRUD /tasks/*
    │   └── forms.py            ← TaskForm
    ├── models/
    │   ├── user.py             ← User(db.Model)
    │   └── task.py             ← Task(db.Model)
    └── templates/
        ├── base.html
        ├── auth/
        │   ├── login.html
        │   └── register.html
        └── tasks/
            ├── index.html
            └── form.html
```
---
⚙️ Artefatos de Spec
`AGENTS.md` — Regras Globais dos Agentes
Define o stack tecnológico e os guardrails que todos os agentes devem respeitar:
Stack: Python 3.12, Flask Blueprints (MVC), SQLite + SQLAlchemy ORM, Flask-Login
Regras de código: max 300 linhas por arquivo, docstrings obrigatórias, sem credenciais hardcoded
Guardrails de segurança: nunca escrever no banco sem confirmação, validar todo input
Git: commits convencionais (`feat:`, `fix:`, `test:`, `refactor:`)
`constitution.md` — Lei Suprema Arquitetural
O Antigravity executa um Constitutional Check contra este arquivo antes de cada geração de código:
Padrão MVC com Flask Blueprints é obrigatório
SQL raw é proibido (somente SQLAlchemy ORM)
Lógica de negócio proibida nas rotas (vai nos `services/`)
Todo endpoint autenticado deve retornar 401 se não logado
Tarefas pertencem ao usuário — acesso cruzado resulta em 403
Proteção CSRF em todos os formulários
Cobertura de testes mínima: 80%
---
🚀 Pré-requisitos
Python 3.12+
Conta Gmail (gratuita)
Google Antigravity instalado
---
📥 Instalação do Google Antigravity
Acesse `antigravity.google/download`
Baixe o instalador para seu sistema:
Windows: arquivo `.exe` (~150 MB)
macOS: arquivo `.dmg`
Linux: arquivo `.deb` / `.rpm` / AppImage
Instale normalmente
Na primeira abertura, configure:
Setup flow → Fresh Start
Agent behavior → Terminal Policy: `Auto`
Sign in → autentique com Google
Model → Gemini 3.1 Pro (cota gratuita)
---
🛠️ Rodando o Projeto
1. Clone ou abra a pasta no Antigravity
```bash
# Abra o Antigravity e use: File > Open Folder
# Selecione a pasta todoapp/
```
2. Crie o ambiente virtual
```bash
python -m venv venv
```
3. Ative o ambiente virtual
```bash
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```
4. Instale as dependências
```bash
pip install -r requirements.txt
```
5. Configure as variáveis de ambiente
```bash
cp .env.example .env
```
Edite o arquivo `.env`:
```env
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///todoapp.db
FLASK_ENV=development
FLASK_DEBUG=1
```
6. Inicie o servidor
```bash
flask run
```
7. Acesse no navegador
```
http://localhost:5000
```
---
🔄 Gerando o Projeto do Zero com o Antigravity
Se quiser ver o pipeline SDD completo em ação a partir do zero:
Passo 1 — Abra o Agent Manager
Use o atalho `Ctrl+Shift+A` (Windows/Linux) ou `Cmd+Shift+A` (macOS)
Passo 2 — Dispare o ciclo
```
/startcycle "Crie um app web de lista de tarefas onde o usuário
pode se registrar, fazer login, criar/editar/deletar tarefas
e filtrar por status: pendente, em progresso ou concluído"
```
Passo 3 — Acompanhe e aprove cada fase
Fase	O que acontece	Sua ação
Spec	Agente PM gera `spec.md` com histórias de usuário	Revisar e clicar Approve
Plan	Agente Dev gera `plan.md` + Constitutional Check	Revisar e clicar Approve
Implement	Agentes geram todos os arquivos de código	Aguardar (~8 min)
Verify	Agente QA executa pytest e audita a constitution	Aguardar resultado
Passo 4 — Rode localmente
Após a fase Verify ser concluída, siga os passos de instalação acima.
---
🧪 Executando os Testes
```bash
# Rodar todos os testes
pytest

# Com relatório de cobertura
pytest --cov=app --cov-report=term-missing

# Gerar relatório HTML de cobertura
pytest --cov=app --cov-report=html
# Abra htmlcov/index.html no navegador
```
A cobertura mínima exigida pela `constitution.md` é de 80%.
---
🔐 Funcionalidades da Aplicação
✅ Cadastro de usuário com validação de email único
✅ Login e logout com sessão segura (Flask-Login)
✅ Criar tarefa com título e status inicial
✅ Editar tarefa (apenas o próprio usuário)
✅ Deletar tarefa (apenas o próprio usuário)
✅ Filtrar tarefas por status: `pendente`, `em_progresso`, `concluído`
✅ Proteção CSRF em todos os formulários
✅ Isolamento de dados entre usuários (403 em acesso cruzado)
---
🛡️ Segurança
Mecanismo	Implementação
Senhas	Hash com Werkzeug (bcrypt)
Sessões	Flask-Login com `SECRET_KEY`
CSRF	Flask-WTF em todos os formulários
Isolamento	`task.user_id == current_user.id` antes de qualquer operação
SQL Injection	SQLAlchemy ORM (sem SQL raw)
Input validation	WTForms + validação server-side
---
📦 Dependências
```
Flask==3.1.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Flask-WTF==1.2.1
Werkzeug==3.1.1
python-dotenv==1.0.1
pytest==8.3.2
pytest-flask==1.3.0
pytest-cov==5.0.0
```
---
📊 Resultado do Pipeline SDD
Fase	Agente	Duração	Código humano
Spec	PM Agent	~2 min	0 linhas
Plan	Full-Stack Agent	~3 min	0 linhas
Implement	Full-Stack Agent	~8 min	0 linhas
Verify	QA Agent	~4 min	0 linhas
Revisão humana	Você	~10 min	Apenas aprovações
---
📚 Referências
Google Antigravity — Documentação Oficial
Getting Started with Google Antigravity — Google Codelabs
Build Autonomous Developer Pipelines — Google Codelabs
Spec-Driven Development — Wikipedia
AGENTS.md Guide — Antigravity Rules
---
> **Projeto acadêmico** — Trabalho de Pesquisa: SPEC-Driven Development no Google Antigravity
> Disciplina: Desenvolvimento Web
