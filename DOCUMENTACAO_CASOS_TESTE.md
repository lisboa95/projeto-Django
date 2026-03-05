# CASOS DE TESTE - SISTEMA DE GESTÃO DE CURSOS

## CT01 - TESTE DE CRIAÇÃO DE CURSO
**Pré-condições:** Sistema iniciado, banco de dados vazio
**Passos:**
1. Acessar /admin/cursos/curso/add/
2. Preencher nome: "Python Básico"
3. Preencher descrição: "Curso introdutório"
4. Preencher carga horária: 40
5. Preencher datas
6. Clicar em "Salvar"
**Resultado esperado:** Curso criado no banco de dados
**Resultado obtido:** ✅ Sucesso

## CT02 - TESTE DE LISTAGEM DE CURSOS
**Pré-condições:** Pelo menos 1 curso cadastrado
**Passos:**
1. Acessar http://127.0.0.1:8000/cursos/
2. Verificar se cursos são listados
3. Verificar se há botão "Ver Detalhes"
**Resultado esperado:** Lista de cursos exibida corretamente
**Resultado obtido:** ✅ Sucesso

## CT03 - TESTE DE DETALHES DO CURSO
**Pré-condições:** CT02 executado com sucesso
**Passos:**
1. Clicar em "Ver Detalhes" em um curso
2. Verificar se informações do curso são exibidas
3. Verificar se botões funcionam
**Resultado esperado:** Página de detalhes carregada
**Resultado obtido:** ✅ Sucesso

## CT04 - TESTE DE LOGIN
**Pré-condições:** Usuário "admin" criado
**Passos:**
1. Acessar http://127.0.0.1:8000/login/
2. Inserir usuário: "admin"
3. Inserir senha: "123"
4. Clicar em "Entrar"
**Resultado esperado:** Redirecionamento para dashboard
**Resultado obtido:** ✅ Sucesso

## CT05 - TESTE DE DASHBOARD
**Pré-condições:** CT04 executado com sucesso
**Passos:**
1. Após login, acessar dashboard
2. Verificar se estatísticas são exibidas
3. Verificar se menu funciona
**Resultado esperado:** Dashboard carregado com dados
**Resultado obtido:** ✅ Sucesso

## CT06 - TESTE DE PERFIL
**Pré-condições:** CT04 executado com sucesso
**Passos:**
1. Clicar em "Perfil" no menu
2. Verificar se informações do usuário são exibidas
**Resultado esperado:** Página de perfil carregada
**Resultado obtido:** ✅ Sucesso

## CT07 - TESTE DE LOGOUT
**Pré-condições:** Usuário logado
**Passos:**
1. Clicar em "Sair" no dashboard
2. Tentar acessar dashboard novamente
**Resultado esperado:** Redirecionamento para login
**Resultado obtido:** ✅ Sucesso

## CT08 - TESTE DE RESPONSIVIDADE
**Pré-condições:** Sistema em execução
**Passos:**
1. Acessar sistema em diferentes dispositivos/tamanhos de tela
2. Verificar se layout se adapta
**Resultado esperado:** Interface responsiva
**Resultado obtido:** ✅ Sucesso

## CT09 - TESTE DE PERFORMANCE
**Pré-condições:** Sistema com dados de teste
**Passos:**
1. Medir tempo de carregamento da home
2. Medir tempo de carregamento da lista de cursos
**Resultado esperado:** < 3 segundos por página
**Resultado obtido:** ✅ Sucesso (média: 0.5s)

## CT10 - TESTE DE SEGURANÇA
**Pré-condições:** Sistema em execução
**Passos:**
1. Tentar acessar /dashboard/ sem login
2. Tentar acessar /admin/ sem credenciais
**Resultado esperado:** Redirecionamento para login
**Resultado obtido:** ✅ Sucesso