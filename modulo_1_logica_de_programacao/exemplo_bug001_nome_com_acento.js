// TICKET: #BUG-2847
// Prioridade: Média
// Descrição: Usuários não conseguem se cadastrar quando o nome tem acentos
// Reprodução: Tentar cadastrar com nome "José da Silva" - formulário não envia

// ============= CÓDIGO ATUAL COM BUGS =============

function validarFormularioCadastro() {
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    const confirmarSenha = document.getElementById('confirmar-senha').value;
    
    // Bug #1: Validação de nome não aceita acentos
    if (!nome.match(/^[a-zA-Z\s]+$/)) {
        alert('Nome deve conter apenas letras');
        return false;
    }
    
    // Bug #2: Validação de email muito simples
    if (!email.includes('@')) {
        alert('Email inválido');
        return false;
    }
    
    // Bug #3: Não verifica se a senha tem requisitos mínimos
    if (senha.length < 6) {
        alert('Senha deve ter pelo menos 6 caracteres');
        return false;
    }
    
    // Bug #4: Comparação case-sensitive desnecessária
    if (senha !== confirmarSenha) {
        alert('Senhas não coincidem');
        return false;
    }
    
    // Bug #5: Não trata erro de envio
    enviarCadastro(nome, email, senha);
    return true;
}

function enviarCadastro(nome, email, senha) {
    // Bug #6: Fetch sem tratamento de erro
    fetch('/api/cadastro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome: nome,
            email: email,
            senha: senha
        })
    })
    .then(response => response.json())
    .then(data => {
        alert('Cadastro realizado com sucesso!');
        // Bug #7: Não limpa o formulário após sucesso
    });
}

// Bug #8: Event listener pode ser adicionado múltiplas vezes
document.getElementById('form-cadastro').addEventListener('submit', function(e) {
    e.preventDefault();
    validarFormularioCadastro();
});

// ============= SUGESTÕES PARA CORREÇÃO =============

/*
BUGS IDENTIFICADOS:

1. Regex não aceita acentos (á, ã, ç, etc.)
   - Solução: Usar /^[a-zA-ZÀ-ÿ\s]+$/ ou similar

2. Validação de email muito básica
   - Solução: Usar regex mais robusta para email

3. Senha sem validação de complexidade
   - Solução: Verificar maiúscula, minúscula, número

4. Comparação de senhas OK (este não é bug real)

5. Não trata erros de rede/servidor
   - Solução: Adicionar .catch() no fetch

6. Fetch sem tratamento de erro HTTP
   - Solução: Verificar response.ok

7. Formulário não é limpo após sucesso
   - Solução: Adicionar form.reset()

8. Event listener pode duplicar
   - Solução: Verificar se já existe ou usar once: true

TAREFAS PARA O DEV JÚNIOR:
- Corrigir a validação de nome para aceitar acentos
- Melhorar validação de email
- Adicionar tratamento de erro no fetch
- Limpar formulário após cadastro bem-sucedido
- Escrever testes unitários para as validações
*/