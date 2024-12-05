from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    chars = ["1", "2", "3", "4", "d", "c",
            "5", "6", "7"," 8", "+", "-",
            "9", "0", ".", "*", "/", "="  ]
    self.btn = {}
    gp = GridPanel()
    for i in chars:
      self.btn[i] = Button(text=i)
      gp.add_component(self.btn[i], 
                      row = 'A', 
                      col_xs=3,
                      width_xs=1)
    self.add_component(gp)