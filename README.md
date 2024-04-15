# sigplan-monitoramento-dados

[![Updated](https://github.com/splor-mg/sigplan-monitoramento-dados/actions/workflows/all.yaml/badge.svg)](https://github.com/splor-mg/sigplan-monitoramento-dados/actions/)

## Pré-requisitos

Para execução local é necessário a a criação do ambiente virtual do projeto e instalação das dependências do python:

```bash
python -m venv venv
cd pasta/do/projeto
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Uso

Para executar a pipeline de dados:

```bash
make all
```

Cada uma das etapas da pipeline pode ser executadas separadamente, caso necessário, com os comandos make `extract`, `describe`, `validate`, `transform`, `build`, `check`.

Se o processo ocorrer sem erros e as validações e checagens não apresentarem problemas, para realizar o upload atualizando o datapackage no github utilize: 

```
make publish
```

Obs.: As bases do monitoramento do sigplan estão em formato [wide](https://en.wikipedia.org/wiki/Wide_and_narrow_data) e novas colunas são adicionadas a cada mês. Por isso, os [schemas](https://specs.frictionlessdata.io//table-schema/) dos recursos de dados devem ser atualizados de maneira correspondente. O target `describe` presente no `makefile` realiza essa atualização dinâmica por meio do pacote [Jinja2](https://palletsprojects.com/p/jinja/).


_Gerado a partir de [cookiecutter-datapackage@a50ad4d](https://github.com/splor-mg/cookiecutter-datapackage/commit/a50ad4d30928e5e1066d0e20ef697e110a888a64)_
