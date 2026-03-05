# PLANO DE TESTE - SISTEMA DE GESTÃO DE CURSOS

## 1. OBJETIVO
Validar o funcionamento do Sistema de Gestão de Cursos desenvolvido em Django, garantindo que todas as funcionalidades atendam aos requisitos do projeto.

## 2. ESCOPO
- Testes de unidade (Models)
- Testes de integração (Views, URLs)
- Testes de sistema (fluxos completos)
- Testes de interface (Templates)

## 3. ESTRATÉGIA DE TESTE
- Testes automatizados com Django Test Framework
- Testes manuais para validação de interface
- Testes de regressão após alterações

## 4. CRITÉRIOS DE ACEITAÇÃO
- 100% dos testes automatizados devem passar
- Sistema deve funcionar nos navegadores Chrome, Firefox, Edge
- Tempo de resposta inferior a 3 segundos por página
- Nenhum erro crítico em produção

## 5. AMBIENTE DE TESTE
- Django 5.1.3
- Python 3.13
- Banco de dados SQLite
- Windows 10/11

## 6. CRONOGRAMA
| Fase | Descrição | Status |
|------|-----------|--------|
| 1 | Preparação do ambiente | ✅ Concluído |
| 2 | Testes de Models | ✅ Concluído |
| 3 | Testes de Views/URLs | ✅ Concluído |
| 4 | Testes de integração | ✅ Concluído |
| 5 | Testes de sistema | ✅ Concluído |
| 6 | Relatório final | Em andamento |

## 7. RISCOS
- Falha na conexão com banco de dados
- Problemas de compatibilidade com Python 3.13
- Erros de permissão no ambiente Windows

## 8. RESULTADOS OBTIDOS
✅ 22 testes executados  
✅ 100% de sucesso  
✅ 0 falhas  
✅ Tempo total: 8.882 segundos