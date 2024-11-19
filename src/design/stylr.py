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
    
    
    
  def maketable(self,**kwargs):
    table = kwargs.get('table')
    self.console.print(table)
    
    


  def makepanel(self,**kwargs):
    panel = Panel(kwargs['text'], title=kwargs['title'], style=kwargs['style'], border_style=kwargs['border_style'],title_align="center")
    self.console.print(panel, justify="center",style=kwargs['style'])
    
    
    
  def maketree(self,**kwargs):
    
    tree = Tree(kwargs['text'])
    self.console.print(tree)
    
  def makelayout(self,**kwargs):
    layout = Layout()
    layout.split(
        Layout(name="header"),
        Layout(name="main", ratio=1),
        Layout(name="footer"),
    )
    self.console.print(layout)
    
  def makeprompt(self,**kwargs):
    prompt = Prompt.ask(kwargs['text'],style=kwargs['style'])
    return prompt
  
  
  def makelive(self,**kwargs):
    live = Live()
    self.console.print(live)
    
  def makeprint(self,**kwargs):
    print(kwargs['text'])
    




