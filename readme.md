# Tema 4: Universidade

## Descrição da Aplicação

Uma aplicação para uma Universidade precisa armazenar informações sobre os seus professores, disciplinas e sobre as disciplinas ministradas por cada professor. Os dados a serem armazenados sobre cada uma dessas entidades são apresentados a seguir:

### Entidades

- **Professor**
  - Registro Funcional (chave)
  - Nome
  - Data de Nascimento
  - Sexo
  - Área de Pesquisa
  - Titulação
  - Graduação
  - E-mails
  - Telefones

- **Disciplina**
  - Sigla (chave)
  - Nome
  - Ementa
  - Bibliografia
  - Número de Créditos
  - Carga Horária

- **Prof_Disc**
  - Registro Funcional do Professor (chave)
  - Sigla da Disciplina (chave)
  - Ano
  - Semestre
  - Dias da Semana
  - Horários de Início
  - Curso

## Funcionalidades da Aplicação

Utilizando os conhecimentos aprendidos nas aulas, desenvolva um programa em Python que apresente o seguinte menu de opções para o usuário e implemente cada operação usando função. Escolha a estrutura de dados mais apropriada para armazenar os dados de cada entidade descrita anteriormente.

### Menu de Opções

1. **Submenu de Professores**
2. **Submenu de Disciplinas**
3. **Submenu de Professores-Disciplinas**
4. **Submenu Relatórios**
5. **Sair**

### Submenus

Cada Submenu deverá oferecer as opções:

- Listar todos
- Listar um elemento específico do conjunto
- Incluir (sem repetição)
- Alterar
- Excluir (após confirmação dos dados) um elemento do conjunto

**Observação:** Os atributos que estão no plural indicam que deverá ser possível incluir vários itens daquele mesmo atributo. Por exemplo, o atributo Telefones indica que uma pessoa pode ter vários telefones (a quantidade é indefinida). Portanto, deve-se utilizar uma estrutura que seja adequada para armazenar todos os telefones que a entidade possuir.

### Submenu Relatórios

O Submenu Relatórios deverá ter uma opção para cada um dos relatórios solicitados a seguir:

#### Relatórios

a) Mostrar todos os dados de todos os professores que têm determinada titulação fornecida pelo usuário (mestrado ou doutorado);

b) Mostrar todos os dados de todas as disciplinas que possuem mais do que X créditos;

c) Mostrar o Registro Funcional do Professor, o nome do professor, a Sigla da disciplina, o nome da disciplina e todos os demais atributos de Prof_Disc para aquelas disciplinas que serão ministradas às terças e às quintas feiras de cada semana.

## Implementação

**Observação:** Não utilize variáveis globais. Use parâmetros para fazer a transferência de valores entre as funções. Dê nomes significativos para variáveis e funções.

### Persistência de Dados

O programa deverá utilizar Arquivos para a persistência dos dados manipulados pela aplicação. Em outras palavras, cada registro de Professor, Disciplina e Prof_Disc deverá ser armazenado em um arquivo texto específico, que conterá apenas registros daquele mesmo tipo de entidade. O submenu Relatórios também deverá usar arquivos textos para a persistência dos relatórios gerados.
