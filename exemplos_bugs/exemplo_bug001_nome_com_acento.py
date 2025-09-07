# TICKET: #2847
# Prioridade: Média
# Descrição: Usuários não conseguem se cadastrar quando o nome tem acentos
# Reprodução: Tentar cadastrar com nome "José da Silva" - sistema rejeita
# Framework: Flask/Django (API endpoint)

# ============= CÓDIGO ATUAL COM BUGS =============

import re
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

class ValidadorCadastro:
    def __init__(self):
        pass
    
    def validar_nome(self, nome):
        # Bug #1: Regex não aceita acentos nem caracteres especiais
        if not re.match(r'^[a-zA-Z\s]+$', nome):
            return False, "Nome deve conter apenas letras"
        
        # Bug #2: Não verifica tamanho mínimo/máximo
        return True, ""
    
    def validar_email(self, email):
        # Bug #3: Validação muito simples
        if '@' not in email:
            return False, "Email inválido"
        
        # Bug #4: Não verifica formato adequado
        return True, ""
    
    def validar_senha(self, senha, confirmar_senha):
        # Bug #5: Senha muito simples - só verifica tamanho
        if len(senha) < 6:
            return False, "Senha deve ter pelo menos 6 caracteres"
        
        # Bug #6: Não verifica complexidade (maiúscula, número, etc.)
        
        if senha != confirmar_senha:
            return False, "Senhas não coincidem"
        
        return True, ""

class CadastroService:
    def __init__(self):
        self.validador = ValidadorCadastro()
    
    def processar_cadastro(self, dados):
        nome = dados.get('nome', '').strip()
        email = dados.get('email', '').strip()
        senha = dados.get('senha', '')
        confirmar_senha = dados.get('confirmar_senha', '')
        
        # Validações
        nome_valido, erro_nome = self.validador.validar_nome(nome)
        if not nome_valido:
            return {"sucesso": False, "erro": erro_nome}
        
        email_valido, erro_email = self.validador.validar_email(email)
        if not email_valido:
            return {"sucesso": False, "erro": erro_email}
        
        senha_valida, erro_senha = self.validador.validar_senha(senha, confirmar_senha)
        if not senha_valida:
            return {"sucesso": False, "erro": erro_senha}
        
        # Bug #7: Não verifica se email já existe
        
        # Bug #8: Chama API externa sem tratamento de erro
        resultado = self.salvar_usuario(nome, email, senha)
        
        # Bug #9: Não verifica se salvou corretamente
        return {"sucesso": True, "mensagem": "Usuário cadastrado!"}
    
    def salvar_usuario(self, nome, email, senha):
        try:
            # Bug #10: Senha salva em texto plano (sem hash)
            usuario_data = {
                "nome": nome,
                "email": email,
                "senha": senha,  # CRÍTICO: senha sem hash!
                "ativo": True
            }
            
            # Bug #11: Timeout muito alto e sem retry
            response = requests.post(
                'http://api-interna.empresa.com/usuarios',
                json=usuario_data,
                timeout=30
            )
            
            # Bug #12: Não verifica status HTTP
            return response.json()
            
        except Exception as e:
            # Bug #13: Log de erro expõe dados sensíveis
            print(f"Erro ao salvar usuário: {nome}, {email}, {senha}")
            return None

# Endpoint da API
@app.route('/api/cadastro', methods=['POST'])
def cadastrar_usuario():
    try:
        dados = request.get_json()
        
        # Bug #14: Não valida se dados foram enviados
        service = CadastroService()
        resultado = service.processar_cadastro(dados)
        
        return jsonify(resultado)
        
    except Exception as e:
        # Bug #15: Retorna erro genérico sem log adequado
        return jsonify({"erro": "Erro interno"}), 500

# Bug #16: Código de exemplo/teste em produção
if __name__ == '__main__':
    # Testando com dados problemáticos
    dados_teste = {
        "nome": "José da Silva",  # Vai falhar pela regex
        "email": "jose@email.com",
        "senha": "123456",
        "confirmar_senha": "123456"
    }
    
    service = CadastroService()
    resultado = service.processar_cadastro(dados_teste)
    print(resultado)  # Vai mostrar erro de nome inválido
    
    app.run(debug=True)  # Debug True em produção é perigoso

# ============= BUGS IDENTIFICADOS =============

"""
PROBLEMAS PRINCIPAIS:

1. Regex não aceita acentos (á, ã, ç, ñ, etc.)
   - Solução: r'^[a-zA-ZÀ-ÿ\u00f1\u00d1\s]+$'

2. Validação de email muito básica
   - Solução: Usar regex mais robusta ou biblioteca

3. Senha sem verificação de complexidade
   - Solução: Verificar maiúscula, minúscula, número

4. Não verifica tamanho do nome (muito curto/longo)
   - Solução: Adicionar validação de length

5. Senha salva sem hash (CRÍTICO!)
   - Solução: Usar bcrypt ou similar

6. Não trata erros de rede/API
   - Solução: try/except adequado

7. Não verifica se email já existe
   - Solução: Consulta ao banco antes de cadastrar

8. Logs expõem dados sensíveis
   - Solução: Never log passwords!

9. Debug True em produção
   - Solução: Usar variáveis de ambiente

10. Não valida entrada JSON
    - Solução: Verificar se dados existem

TAREFAS PARA O DEV JÚNIOR:
1. Corrigir regex do nome para aceitar acentos
2. Implementar hash de senha com bcrypt
3. Melhorar validação de email
4. Adicionar tratamento de exceções adequado
5. Escrever testes unitários
6. Remover logs que expõem senhas

NÍVEL DE PRIORIDADE:
- CRÍTICO: Hash de senha, logs com dados sensíveis
- ALTO: Validação de nome (bug reportado)
- MÉDIO: Validações de email, tratamento de erros
- BAIXO: Melhorias gerais de código
"""