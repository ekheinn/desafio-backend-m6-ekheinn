# **_Desafio para vaga Back-end - JUNIOR_**

<div style="display: inline_block"><br/>
    <img align="center" alt="git" src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white"/>
    <img align="center" alt="github" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
    <img align="center" alt="python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img align="center" alt="django" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
    <img align="center" alt="sqlite" src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
    <img align="center" alt="vscode" src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"/>
</div>

<br/>

A aplicação consiste em parsear arquivo de texto(CNAB) e salvar suas informações(transações financeiras) em um banco de dados. Feita com o intuito de simular um teste técnico no curso de desenvolvimento FullStack na Kenze Academy Brasil.

---

<br/>

## Instalação e execução em ambientes de desenvolvimento

### Crie o ambiente virtual

```
python -m venv venv
```

### Ative o venv

```bash
# linux
source venv/bin/activate

# windows
.\venv\Scripts\activate

```

### Instale as dependências

```
pip install -r requirements.txt
```

### Execute as migrações

```
./manage.py migrate
```

---

<br/>

Arquivo para fazer testes: **[Arquivo CNAB](https://github.com/Kenzie-Academy-Brasil-Developers/desafio-backend-m6/blob/main/CNAB.txt)**

## Base URL

> http://127.0.0.1:8000/api/

## Documentação

> http://127.0.0.1:8000/api/docs/

## Rotas

- Rota de upload do arquivo [POST], e listagem de todas as transações financeiras [GET]

  > http://127.0.0.1:8000/api/cnab/

- Rota para ver o saldo de todas as lojas [GET]
  > http://127.0.0.1:8000/api/balance/
