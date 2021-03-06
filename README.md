# Consumindo API do [sistema de gerenciamento de uma biblioteca](https://github.com/adkatarine/biblioteca-backend).

### π PrΓ©-requisitos

Primeiro, clone este projeto em sua mΓ‘quina, crie um ambiente virtual e ative. Feito isso, execute o seguinte comando para instalar todas as suas dependΓͺncias:

```
pip install -r requirements.txt
```

Caso queira fazer melhorias ou alteraΓ§Γ΅es no projeto, execute este comando:
```
pre-commit install
```

ApΓ³s isso, crie um arquivo .env e insira esta variΓ‘vel com sua respectiva informaΓ§Γ£o:
```
export API_LIBRARY_WORK_URL = 
```

Por fim, siga os passos para executar a [API](https://github.com/adkatarine/biblioteca-backend/blob/master/README.md).


E agora vocΓͺ jΓ‘ pode executar este ultimo comando para iniciar e testar a aplicaΓ§Γ£o:
```
python app.py runserver
```

## π¨οΈ PΓ‘gina inicial do projeto

![](src/blueprints/library/static/library.png)


## π οΈ Estrutura do projeto
```
biblioteca-backend
βββ src/
β   βββ __init__.py
β   βββ blueprints/
β   β   βββ __init__.py
β   β   βββ library/
β   β       βββ __init__.py
β   β       βββ library.py
β   β       βββ static/
β   β       |   βββ library.png
β   β       βββ templates/
β   β           βββ base.html
β   β           βββ index.html
β   βββ config/
β   β   βββ __init__.py
β   β   βββ library_api.py
β   βββ consume_api/
β   β   βββ __init__.py
β   β   βββ consume_api_library.py
β   βββ helper/
β       βββ __init__.py
β       βββ helper.py
β       βββ verify_status_code.py
βββ venv/
βββ .env
βββ .flake8
βββ .gitignore
βββ .pre-commit-config.yaml
βββ .pylintrc
βββ .app.py
βββ README.md
βββ requirements.txt
```

## π§ ConstruΓ­do com

Ferramentas utilizadas para o desenvolvimento deste projeto:

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Framework
* [Requests](https://docs.python-requests.org/en/latest/) - Biblioteca HTTP Python
* [Pylint](https://pypi.org/project/pylint/) - Ferramenta de anΓ‘lise de cΓ³digo estΓ‘tico do Python
* [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/) - Framework