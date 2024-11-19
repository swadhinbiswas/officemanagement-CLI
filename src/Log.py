import logging
from rich.logging import RichHandler
import click

from rich.panel import Panel
from rich.console import Console


x=Panel("Hello World",title="Welcome",style="bold red")
console = Console()





logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])]
)

logger = logging.getLogger("rich")
