from frictionless import Package
from jinja2 import Environment, FileSystemLoader
import logging

logger = logging.getLogger(__name__)

def render_schema(resource_name: str, descriptor: str = 'datapackage.yaml'):
    """
    Render table schema of monitoramento datasets

    >>> render_schema("resource_name", 'datapackage.yaml' )
    """
    package = Package(descriptor)

    month = int(package.custom["month"])
    year = int(package.custom["year"])
    months = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

    logger.info(f"Rendering schema {resource_name}.yaml for {months[0]}/{year}-{months[month-1]}/{year}")

    env = Environment(loader=FileSystemLoader("templates"),
                      trim_blocks=True,
                      lstrip_blocks=True,
                      keep_trailing_newline=True)
    template = env.get_template(f"{resource_name}.yaml.j2")
    result = template.render(period=year, months=months[:month])

    with open(f"schemas/{resource_name}.yaml", 'w', encoding='utf-8') as fs:
        fs.write(result)


