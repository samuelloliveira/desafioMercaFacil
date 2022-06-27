# Teste Mercafacil

Você recebe diariamente dois arquivos no formato CSV com algumas dados de vendas, esses dados devem passar por uma *pipeline* que realizará varias transformações para por fim disponibilizar essas informações ao varejista. Em uma das etapas dessa *pipeline* são realizadas um conjunto de validações e transformações, entre elas as seguintes:

## vendas_itens.csv

- codigo_venda:
-- Não nulo
-- Tipo texto
- valor_unitario:
-- Não nulo
-- Tipo float
- quantidade_produto:
-- Não nulo, usa como padrão o valor 0
-- Tipo float
- valor_total *(campo derivado)*:
-- *valor_unitario * quantidade_produto*
-- Não nulo, usa como padrão o valor 0
-- Tipo float
- codigo_produto:
-- Não nulo
-- Tipo inteiro
- codigo_cliente:
-- Tipo inteiro

## clientes.csv

- nome:
-- Não nulo
-- 3 <= tamanho < 20
-- Tipo texto
- telefone:
-- Tamanho >= 8
-- Tipo texto
- codigo_cliente:
-- Tipo Inteiro
-- Não nulo
-- Único
- data_cadastro:
-- Caso nulo, usar a data atual
-- Formato: DD/MM/AAAA
- tipo_cliente 
-- F = Pessoa Física (padrão)
-- J = Pessoa Jurídica

> Observe que alguns campos não serão fornecidos através do arquivo csv, porém podem ser criados com base nos dados fornecidos.

## Resultado esperado

Esperamos que o candidato possa aplicar os filtros citados e apresente os dados filtrados/corrigidos.

## Como será feita a avaliação

Alguns pontos que serão considerados, mas não se limitam a eles, serão os seguintes:

- Funcionamento do código;
- Código de fácil compreensão;
- Estrutura limpa;
- Escalabilidade;
- Facilidade em escrever testes;

## Ferramentas sugeridas

- pandas