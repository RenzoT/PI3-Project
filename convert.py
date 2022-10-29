import  jpype     
import  asposecells

jpype.startJVM() 
from asposecells.api import Workbook

workbook = Workbook("images/prueba.jpg")
workbook.Save("Output.xlsx")
jpype.shutdownJVM()