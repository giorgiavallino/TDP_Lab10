from xml.dom.xmlbuilder import Options

import flet as ft

class Controller:

    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._model.buildGraph(1816)
        self._view._txt_result.controls.append(ft.Text(f"{self._model.getNumNodes()}"))
        self._view.update_page()

    def addOptionsTxtAnno(self):
        for i in range(1816, 2017):
            self._view._txtAnno.options.append(ft.dropdown.Option(str(i)))

if __name__=="__main__":
    pass