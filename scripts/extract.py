from pathlib import Path

from frictionless import Package
import requests
import logging
import shutil
import html2text
from rich import print as rprint
from rich.panel import Panel
from rich.text import Text

logger = logging.getLogger(__name__)


def extract_resource(resource_name: str, descriptor: str = 'datapackage.yaml'):
    package = Package(descriptor)
    resource = package.get_resource(resource_name)

    logger.info(f"Extracting resource {resource_name}")

    url_params = {
        "month": package.custom["month"],
        "year": package.custom["year"],
        "ppag": package.custom["ppag"]
    }

    res = requests.get(resource.custom['api_url'].format(**url_params))  # Resource is stripping url property
    res.raise_for_status()
    h = html2text.HTML2Text()
    rprint(Panel(Text(h.handle(res.text), style="green")))
    if 'gerado com sucesso!' not in res.text:
        logger.error('Erro na geração do arquivo texto')
        raise Exception

    res = requests.get(resource.custom['download_url'], stream=True)
    res.raise_for_status()
    res.raw.decode_content = True

    Path(resource.path).parent.mkdir(parents=True, exist_ok=True)
    with open(resource.path, 'wb') as file:
        shutil.copyfileobj(res.raw, file)


