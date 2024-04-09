from frictionless import Package
import typer
from scripts.extract import extract_resource
from scripts.transform import transform_resource
from scripts.build import build_package
from scripts.render_template import render_schema_monitoramento

app = typer.Typer(pretty_exceptions_show_locals=False)

@app.callback()
def callback():
    """
    ETL scripts.
    """

@app.command()
def resources(descriptor: str = 'datapackage.yaml'):
    """
    Data package resource names
    """
    package = Package(descriptor)
    output = ' '.join(package.resource_names)
    print(output)
    return 0


app.command(name="extract")(extract_resource)
app.command(name="transform")(transform_resource)
app.command(name="build")(build_package)
app.command(name="describe")(render_schema_monitoramento)

if __name__ == "__main__":
    app()
