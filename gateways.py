class UsuarioGateway:
    def salvar(self, username, senha):
        with open("usuarios.txt", "a") as f:
            f.write(f"{username};{senha}\n")

    def buscar_por_username(self, username):
        try:
            with open("usuarios.txt", "r") as f:
                for linha in f:
                    dados = linha.strip().split(';')
                    if len(dados) >= 2 and dados[0] == username:
                        return {
                            "username": dados[0],
                            "senha": dados[1]
                        }
        except FileNotFoundError:
            return None
        return None

class LivroGateway:
    def _gerar_id(self):
        try:
            with open("livros.txt", "r") as f:
                return sum(1 for _ in f) + 1
        except FileNotFoundError:
            return 1

    def salvar(self, livro):
        livro_id = self._gerar_id()
        with open("livros.txt", "a") as f:
            f.write(f"{livro_id};{livro['titulo']};{livro['autor']};{livro['ano']};{livro['dono']};{livro['disponivel']};{livro['alugado_por']}\n")
        return livro_id
    
    def listar_todos(self):
        livros = []
        try:
            with open("livros.txt", "r") as f:
                for linha in f:
                    dados = linha.strip().split(';')
                    if len(dados) < 7: continue
                    livros.append({
                        "id": dados[0],
                        "titulo": dados[1],
                        "autor": dados[2],
                        "ano": dados[3],
                        "dono": dados[4],
                        "disponivel": dados[5],
                        "alugado_por": dados[6]
                    })
        except FileNotFoundError:
            pass
        return livros
    
    def buscar_por_id(self, livro_id):
        try:
            with open("livros.txt", "r") as f:
                for linha in f:
                    dados = linha.strip().split(';')
                    if dados[0] == str(livro_id):
                        return {
                            "id": dados[0],
                            "titulo": dados[1],
                            "autor": dados[2],
                            "ano": dados[3],
                            "dono": dados[4],
                            "disponivel": dados[5],
                            "alugado_por": dados[6]
                        }
        except FileNotFoundError:
            return None
        return None
    
    def atualizar(self, livro_atualizado):
        linhas = []
        atualizado = False
        
        try:
            with open("livros.txt", "r") as f:
                for linha in f:
                    dados = linha.strip().split(';')
                    # Verificar se é o livro a ser atualizado
                    if len(dados) > 0 and dados[0] == livro_atualizado['id']:
                        # Construir nova linha atualizada
                        nova_linha = f"{livro_atualizado['id']};{livro_atualizado['titulo']};"
                        nova_linha += f"{livro_atualizado['autor']};{livro_atualizado['ano']};"
                        nova_linha += f"{livro_atualizado['dono']};{livro_atualizado['disponivel']};"
                        nova_linha += f"{livro_atualizado['alugado_por']}\n"
                        linhas.append(nova_linha)
                        atualizado = True
                    else:
                        linhas.append(linha)
        except FileNotFoundError:
            return False
        
        if atualizado:
            with open("livros.txt", "w") as f:
                f.writelines(linhas)
            return True
        return False
    
    def excluir(self, livro_id):
        livros = []
        encontrado = False
        
        try:
            with open("livros.txt", "r") as f:
                for linha in f:
                    dados = linha.strip().split(';')
                    if dados[0] == str(livro_id):
                        encontrado = True
                    else:
                        livros.append(linha)
        except FileNotFoundError:
            return False
        
        if encontrado:
            with open("livros.txt", "w") as f:
                f.writelines(livros)
            return True
        return False
    
    