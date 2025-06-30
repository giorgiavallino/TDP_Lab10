from xml.dom.xmlbuilder import Options
import flet as ft
from model.country import Country


class Controller:

    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # Altro
        self._statoSelezionato = None

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
        self._view._btnStatiRaggiungibili.disabled = False
        self._view._txtStato.disabled = False
        self._view.update_page()

    def handleRaggiungibili(self, e):
        self._view._txt_result.controls.clear()
        if self._statoSelezionato is None:
            self._view.create_alert("Selezionare uno stato!")
            self._view.update_page()
            return
        if not self._model.controlNode(self._statoSelezionato):
            self._view.create_alert("Lo stato selezionato non rappresenta un vertice del grafo creato!")
            self._view.update_page()
            return
        self._view._txt_result.controls.append(ft.Text(f"Gli stati raggiungibili, a partire da {self._statoSelezionato}, sono:"))
        nodi = self._model.getNodesRaggiungibili(self._statoSelezionato)
        for nodo in nodi:
            self._view._txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()

    def addOptionsTxtAnno(self):
        for i in range(1816, 2017):
            self._view._txtAnno.options.append(ft.dropdown.Option(str(i)))

    def addOptionsTxtStato(self):
        stati = self._model._stati
        for stato in stati:
            self._view._txtStato.options.append(ft.dropdown.Option(key=stato.CCode,
                                                                    text=stato.StateNme,
                                                                    data=stato,
                                                                    on_click=self.readStato))

    def readStato(self, e):
        self._statoSelezionato = e.control.data