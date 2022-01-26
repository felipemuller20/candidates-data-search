# ✌️ Boas vindas ao repositório do projeto Candidates Data Search!

O projeto **Candidates Data Search** consiste em uma aplicação desenvolvida em **Python** que captura uma lista fictícia de pessoas listadas como aprovadas em um vestibular e salva as informações num banco de dados **MySQL**.

É realizada a higienização dos dados, de forma que o banco de dados não salve caracteres especiais, acentos ou espaços a mais. Também é realizada a validação CPFs, de forma que os dados da pessoa sejam salvos apenas se o CPF for válido numericamente.

Existe também uma verificação por CPF para descobrir se os dados de uma pessoa já foram salvos no banco de dados, impedindo que uma mesma pessoa tenha mais de um registro.

A lista fictícia utilizada neste projeto pode ser acessada através [deste link](https://sample-university-site.herokuapp.com/).

Para padronização do código, foi utilizado o Linter Flake8.

---

# ⚛️ Tecnologias utilizadas

- Python
- MySQL

---

# 👀 Acessando o projeto

## Configurações iniciais

Este projeto utiliza o banco de dados MySQL, portanto, antes de iniciar, é importante verificar se o MySQL está ativo. No terminal Unix, utilize os comandos:

- Para verificar o status do banco:
```bash
systemctl status mysql
```
- Caso esteja desativado, ative o banco:
```bash
systemctl start mysql
```

Agora que o MySQL está ativo, clone o projeto:

```bash
git clone git@github.com:felipemuller20/candidates-data-search.git
```
```bash
cd candidates-data-search/
```

## Configurando variáveis de ambiente

O projeto utiliza algumas variáveis de ambiente que precisam ser configuradas. Para isso:

- **Renomeie o arquivo `.env.dev` para `.env`**. Este arquivo possui as informações utilizadas para realizar a conexão com o seu banco de dados MySQL;
- Se necessário, **altere o valor das variáveis `DB_HOST`, `DB_USER`, `DB_PASSWORD` e `PORT` para os valores correspondentes à sua conexão**.

Por padrão, o nome do banco criado será `university_dev_felipe`, porém você pode alterar para o nome que desejar, basta trocar o valor da variável `DB_NAME` no seu arquivo `.env`.

Não altere o valor da variável `BASE_URL`, pois é a URL utilizada para coletar as informações neste projeto.

## Executando o projeto

Agora, é necessário criar o ambiente virtual do Python, bem como instalar as dependencias do projeto. Para isso, **certifique-se de estar na raíz do projeto** e utilize os seguintes comandos no seu terminal:

- Crie o ambiente virtual:
```bash
python3 -m venv .venv
```
- Ative o ambiente virtual:
```bash
source .venv/bin/activate
```
- Instale as dependências do projeto:
```bash
python3 -m pip install -r dev-requirements.txt
```

Agora que tudo está configurado, precisamos executar o projeto para buscar as informações do site e salvar os dados no banco de dados. No terminal, digital o comando:

```bash
python3 main.py
```

Pronto! O projeto será executado. Toda captura de informação irá aparecer diretamente no seu terminal e o programa irá encerrar assim que adicionar o ultimo dado do site ao banco de dados!

---

# 👥 Autor
- [Felipe Muller](https://github.com/felipemuller20)
