from frictionless import Package
from jinja2 import Environment, FileSystemLoader

# todo logging messages

def render_schema_monitoramento(resource_name: str, descriptor: str = 'datapackage.yaml'):
    """
    Render table schema of monitoramento datasets

    >>> render_schema_monitoramento("monitoramento", 'datapackage.yaml' )
    """
    package = Package(descriptor)
    resource = package.get_resource(resource_name)

    month = int(package.custom["month"])
    year = int(package.custom["year"])
    months = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]


    env = Environment(loader=FileSystemLoader("templates"),
                      trim_blocks=True,
                      lstrip_blocks=True,
                      keep_trailing_newline=True)
    template = env.get_template(f"{resource_name}.yaml.j2")
    result = template.render(period = year, months = months[:month])
    with open(f"schemas/{resource_name}.yaml", 'w', encoding='utf-8') as fs:
        fs.write(result)


