# sigplan-monitoramento-dados

[![Updated](https://github.com/splor-mg/sigplan-monitoramento-dados/actions/workflows/all.yaml/badge.svg)](https://github.com/splor-mg/sigplan-monitoramento-dados/actions/)

## Pré-requisitos

Esse projeto utiliza Docker para gerenciamento das dependências. Para fazer _build_  da imagem execute:

```bash
docker build --tag sigplan-monitoramento-dados .
```

## Uso

Para executar o container

```bash
docker run -it --rm --mount type=bind,source=$(PWD),target=/project sigplan-monitoramento-dados bash
```

Uma vez dentro do container execute os comandos do make

```bash
make all
```

_Gerado a partir de [cookiecutter-datapackage@a50ad4d](https://github.com/splor-mg/cookiecutter-datapackage/commit/a50ad4d30928e5e1066d0e20ef697e110a888a64)_
