from rich import print
from rich.console import Console
from rich.live import Live
from rich.tree import Tree
from rich.table import Table
from rich.prompt import Prompt
from rich.layout import Layout
from rich.panel import Panel

class Style:
  def __init__(self):
    self.console = Console()
    
  
  def makeheading(self,*args,**kwargs):
    panel = Panel(kwargs['text'], title=kwargs['title'], style=kwargs['style'], border_style=kwargs['border_style'],title_align="center")
    self.console.print(panel, justify="center",style=kwargs['style'])
  def layout(self,**kwargs):
    layout = Layout()
    layout.split(
        Layout(name=kwargs['name'], size=3),
        Layout(name=kwargs['name1'], size=12, ratio=2),
        Layout(name=kwargs['name2'], size=3),
    )
    self.console.print(layout)

    
    
  def maketable(self,**kwargs):
    table = kwargs.get('table')
    self.console.print(table)
    
    


  def makepanel(self,**kwargs):
    panel = Panel(kwargs['text'], title=kwargs['title'], style=kwargs['style'], border_style=kwargs['border_style'],title_align="center")
    self.console.print(panel, justify="center",style=kwargs['style'])
    
    
    
  def maketree(self,**kwargs):
    
    tree = Tree(kwargs['text'],guide_style="bold green")
    self.console.print(tree,style="bold green")
    

    
  def warn(self, text):
    self.console.print(text, style="bold red")
  
  
  def makelive(self,**kwargs):
    live = Live()
    self.console.print(live)
    
  def makeprint(self,**kwargs):
    print(kwargs['text'])
    




