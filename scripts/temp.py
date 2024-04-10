from frictionless.resources import TableResource


resource = TableResource("data-raw/Programa_monitoramento.txt", dialect="dialect.yaml", format='csv')
resource.infer()
print(resource.schema.to_yaml("schemas/programa_monitoramento.yaml"))