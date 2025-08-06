# 📚 Sistema de Compartilhamento de Livros

Este sistema permite que usuários cadastrem, aluguem e devolvam livros, com histórico de ações e notificações automáticas para o dono do livro alugado.  
O projeto foi desenvolvido utilizando **padrões de projeto** para garantir código mais organizado, escalável e fácil de manter.

---

## ✨ Funcionalidades
- Cadastro e login de usuários (**Strategy** para autenticação via nome de usuário ou e-mail).
- Cadastro de livros (**Factory** para criação de objetos).
- Aluguel e devolução de livros (**Command** para encapsular operações).
- Registro de histórico de ações (**Memento**).
- Notificação ao dono quando o livro é alugado (**Observer**).
- Organização de funcionalidades em uma única interface (**Facade**).
- Geração de QR Code para cada operação de aluguel/devolução.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **qrcode** → Geração de QR Codes.
- Estrutura modular com **arquitetura de pacotes** (`patterns`, `services`, `gateways`).

---

## 📂 Estrutura do Projeto
```plaintext
BibliotecaAutonoma/
│── main.py               # Menu principal
│── patterns/
│   ├── facade.py         # Implementação do Facade
│   ├── observer.py       # Implementação do Observer
│   ├── command.py        # Implementação do Command
│   ├── factory.py        # Implementação do Factory
│   ├── memento.py        # Implementação do Memento
│   ├── strategy.py       # Implementação do Strategy
│── services/             # Regras de negócio
│── gateways/             # Acesso a dados
│── README.md             # Este arquivo
```


🚀 Como Executar

1. **Clonar o repositório**:
git clone https://github.com/Rodolfilho/BibliotecaAutonama
cd BibliotecaAutonoma


2. Executar Projeto:
    python main.py


📌 Exemplos de Uso

📍 Menu inicial:
    --- Sistema de Compartilhamento de Livros ---
    1. Cadastrar
    2. Login
    3. Ver Catálogo
    4. Sair

📍 Exemplo de notificação via Observer:
    [NOTIFICAÇÃO para rodolfo] Livro 'Maus' alugado por ana

📍 Histórico de alterações via Memento:
    [03/08/2025 14:21] Livro adicionado por rodolfo
    [03/08/2025 14:25] Livro alugado por ana


🏗️ Padrões de Projeto Implementados
| Padrão       | Função no Projeto                                          |
| ------------ | ---------------------------------------------------------- |
| **Strategy** | Escolha do método de autenticação (usuário ou e-mail).     |
| **Factory**  | Criação de objetos de livro com dados padronizados.        |
| **Command**  | Encapsulamento de operações como aluguel e devolução.      |
| **Memento**  | Registro e consulta de histórico de alterações nos livros. |
| **Observer** | Notificação automática ao dono quando seu livro é alugado. |
| **Facade**   | Interface única para centralizar as funcionalidades.       |
