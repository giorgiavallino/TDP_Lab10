from xml.dom.xmlbuilder import Options
import flet as ft

class Controller:

    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        if anno is None:
            self._view.create_alert("Selezionare un anno!")
            self._view.update_page()
            return
        self._model.buildGraph(anno)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato correttamente!"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getCompConnesse()} componenti connesse."))
        self._view._txt_result.controls.append(ft.Text(f"Di seguito i dettagli sui nodi:"))
        infoNodi = self._model.getNodesDegree()
        for info in infoNodi:
            self._view._txt_result.controls.append(ft.Text(f"{info[0]} - {info[1]} vicini."))
        self._view.update_page()

    def addOptionsTxtAnno(self):
        for i in range(1816, 2017):
            self._view._txtAnno.options.append(ft.dropdown.Option(str(i)))