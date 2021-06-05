
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QMenu,
                             QActionGroup, QAction, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout,
                             QComboBox, QFrame)
import sqlite3


# ======================= CLASE tableWidget ========================

class TableWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):

        self.con = sqlite3.connect('database.db')

        self.horizontal = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.vertical = QVBoxLayout()

        self.frameBotoes = QFrame()

        self.vertical.addWidget(self.frameBotoes)

        # ================== WIDGET  QTableWidget ==================

        self.tabela = QTableWidget(self)

        # Desabilitar edição da tabela
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Desabilitar arrastar e soltar
        self.tabela.setDragDropOverwriteMode(False)

        # Especifica onde devem aparecer os pontos "..."
        # textos que não encaixam
        self.tabela.setTextElideMode(Qt.ElideRight)  # Qt.ElideNone

        # Estabelecer o ajuste de palavras do texto
        self.tabela.setWordWrap(False)

        # Estabelecer o número de linhas
        self.tabela.setRowCount(0)

        # Alinhamento do texto do cabeçálho
        self.tabela.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                           Qt.AlignCenter)

        # Desabilitar negrito do texto do cabeçálho ao selecionar uma linha
        self.tabela.horizontalHeader().setHighlightSections(True)

        # Fazer com que a última coluna visível do cabeçálho ocupe tôdo o espaço disponível
        self.tabela.horizontalHeader().setStretchLastSection(True)

        # Ocultar cabeçálho vertical
        self.tabela.verticalHeader().setVisible(False)

        # Deixar o fundo com cores alternadas
        self.tabela.setAlternatingRowColors(True)

        # Estabelecer altura das linhas
        self.tabela.verticalHeader().setDefaultSectionSize(20)

        # Menú contextual
        self.tabela.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabela.customContextMenuRequested.connect(self.menuContextual)

        self.vertical.addWidget(self.tabela)

        # =================== WIDGETS QPUSHBUTTON ==================

        self.frameE = QFrame()
        self.frameD = QFrame()



        self.botaoMostrarDados = QComboBox(self)
        self.botaoMostrarDados.addItem('Selecione')
        self.botaoMostrarDados.addItem('Alunos')
        self.botaoMostrarDados.addItem('Funcionários')
        self.botaoMostrarDados.addItem('Cargos')
        self.botaoMostrarDados.addItem('Disciplinas')
        self.botaoMostrarDados.addItem('Notas')
        self.botaoMostrarDados.setFixedWidth(140)
        self.hbox2.addWidget(self.botaoMostrarDados)

        self.botaoMostrarOcultar = QPushButton("Motrar/ocultar colunas", self)
        self.botaoMostrarOcultar.setFixedWidth(180)

        self.hbox2.addWidget(self.botaoMostrarOcultar)

        self.botaoSalvar = QPushButton("Salvar Dados", self)
        self.botaoSalvar.setFixedWidth(100)
        self.botaoSalvar.clicked.connect(self.salvarGeral)
        self.hbox3.addWidget(self.botaoSalvar)

        botaoLimpar = QPushButton("Limpar", self)
        botaoLimpar.setFixedWidth(80)
        self.hbox3.addWidget(botaoLimpar)

        self.frameE.setLayout(self.hbox2)
        self.frameD.setLayout(self.hbox3)

        self.hbox1.addWidget(self.frameE)
        self.hbox1.addWidget(self.frameD)

        self.frameBotoes.setLayout(self.hbox1)

        self.horizontal.addLayout(self.vertical)
        self.setLayout(self.horizontal)

        # ======================== EVENTOS =========================

        self.botaoMostrarDados.activated.connect(self.dadosTabela)
        botaoLimpar.clicked.connect(self.limparTabela)

        self.tabela.itemDoubleClicked.connect(self.editar)

    # ======================= FUNCÕES ============================

    def editar(self, text):
        self.tabela.editItem(text)

    def salvarGeral(self):
        if self.botaoMostrarDados.currentText() == 'Alunos':
            self.salvarAluno()
        elif self.botaoMostrarDados.currentText() == 'Funcionários':
            self.salvarFuncionário()
        elif self.botaoMostrarDados.currentText() == 'Disciplinas':
            self.salvarDisciplina()
        elif self.botaoMostrarDados.currentText() == 'Cargos':
            self.salvarCargo()



    def dadosTabela(self):
        cursor = self.con.cursor()
        if self.botaoMostrarDados.currentText() == 'Selecione':
            self.tabela.clearContents()

        elif self.botaoMostrarDados.currentText() == 'Alunos':

            # Estabelecer o número de colunas
            self.tabela.setColumnCount(10)

            self.nomeColunas = (
            "Id", "Nome", "CPF", "RG", "Data de Nascimento", "Sexo", "Situação", "Escolaridade", "Responsável",
            "Tel. Responsável")

            # Estabelecer os títulos do cabeçálho:
            self.tabela.setHorizontalHeaderLabels(self.nomeColunas)

            # Estabelecer largura das colunas
            for indice, largura in enumerate((80, 120, 120, 110, 150, 100, 100, 130, 130, 150), start=0):
                self.tabela.setColumnWidth(indice, largura)

            menu = QMenu()
            for indice, coluna in enumerate(self.nomeColunas, start=0):
                acao = QAction(coluna, menu)
                acao.setCheckable(True)
                acao.setChecked(True)
                acao.setData(indice)

                menu.addAction(acao)

            self.botaoMostrarOcultar.setMenu(menu)
            menu.triggered.connect(self.mostrarOcultar)

            cursor.execute("""SELECT * FROM alunos;""")
            dados = cursor.fetchall()

            self.tabela.clearContents()

            row = 0
            for ind in dados:
                self.tabela.setRowCount(row+1)

                self.tabela.setItem(row, 0, QTableWidgetItem(str(ind[0])))
                self.tabela.setItem(row, 1, QTableWidgetItem(ind[1]))
                self.tabela.setItem(row, 2, QTableWidgetItem(ind[2]))
                self.tabela.setItem(row, 3, QTableWidgetItem(ind[3]))
                self.tabela.setItem(row, 4, QTableWidgetItem(ind[4]))
                self.tabela.setItem(row, 5, QTableWidgetItem(ind[5]))
                self.tabela.setItem(row, 6, QTableWidgetItem(ind[6]))
                self.tabela.setItem(row, 7, QTableWidgetItem(ind[7]))
                self.tabela.setItem(row, 8, QTableWidgetItem(ind[8]))
                self.tabela.setItem(row, 9, QTableWidgetItem(ind[9]))

                row += 1

        elif self.botaoMostrarDados.currentText() == 'Funcionários':
            pass
        elif self.botaoMostrarDados.currentText() == 'Cargos':


            self.tabela.setColumnCount(3)

            self.headersCargos = ('Id', 'Nome do Cargo', 'Setor')
            self.tabela.setHorizontalHeaderLabels(self.headersCargos)

            for indice, largura in enumerate((80, 150, 150), start=0):
                self.tabela.setColumnWidth(indice, largura)

            menuCargo = QMenu()
            for indice, coluna in enumerate(self.headersCargos, start=0):
                acao = QAction(coluna, menuCargo)
                acao.setCheckable(True)
                acao.setChecked(True)
                acao.setData(indice)
                menuCargo.addAction(acao)

            self.botaoMostrarOcultar.setMenu(menuCargo)
            menuCargo.triggered.connect(self.mostrarOcultar)

            cursor.execute("""SELECT * FROM cargos;""")
            dados = cursor.fetchall()

            self.tabela.clearContents()

            row = 0
            for ind in dados:
                self.tabela.setRowCount(row+1)

                self.tabela.setItem(row, 0, QTableWidgetItem(str(ind[0])))
                self.tabela.setItem(row, 1, QTableWidgetItem(ind[1]))
                self.tabela.setItem(row, 2, QTableWidgetItem(ind[2]))
                row += 1


        elif self.botaoMostrarDados.currentText() == 'Disciplinas':
            pass
        else:
            pass



    def mostrarOcultar(self, accion):
        columna = accion.data()

        if accion.isChecked():
            self.tabela.setColumnHidden(columna, False)
        else:
            self.tabela.setColumnHidden(columna, True)

    def salvarAluno(self):
        c = self.con.cursor()

        x = range(len(self.tabela.verticalHeader()))
        a = []
        for i in x:
            self.tabela.selectRow(i)
            y = self.tabela.selectedItems()
            z = [dado.text() for dado in y]
            a.append(z)

        for linha in a:
            c.execute("""UPDATE alunos SET nome = '%s' WHERE id_aluno = '%s'""" % (linha[1], linha[0]))
            c.execute("""UPDATE alunos SET cpf = '%s' WHERE id_aluno = '%s'""" % (linha[2], linha[0]))
            c.execute("""UPDATE alunos SET rg = '%s' WHERE id_aluno = '%s'""" % (linha[3], linha[0]))
            c.execute("""UPDATE alunos SET data_nascimento = '%s' WHERE id_aluno = '%s'""" % (linha[4], linha[0]))
            c.execute("""UPDATE alunos SET sexo = '%s' WHERE id_aluno = '%s'""" % (linha[5], linha[0]))
            c.execute("""UPDATE alunos SET situacao = '%s' WHERE id_aluno = '%s'""" % (linha[6], linha[0]))
            c.execute("""UPDATE alunos SET escolaridade = '%s' WHERE id_aluno = '%s'""" % (linha[7], linha[0]))
            c.execute("""UPDATE alunos SET responsavel = '%s' WHERE id_aluno = '%s'""" % (linha[8], linha[0]))
            c.execute("""UPDATE alunos SET tel_responsavel = '%s' WHERE id_aluno = '%s'""" % (linha[9], linha[0]))
        teste = QMessageBox.question(self, 'Alteração', 'Tem certeza que deseja salvar?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if teste == QMessageBox.Yes:
            self.con.commit()
        else:
            self.con.rollback()
    def salvarFuncionário(self):
        pass
    def salvarDisciplina(self):
        pass
    def salvarCargo(self):
        pass

    def limparTabela(self):
        self.tabela.clearContents()
        self.tabela.setRowCount(0)

    def menuContextual(self, posicion):
        indices = self.tabela.selectedIndexes()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)

            menu.addAction(QAction("Copiar", itemsGrupo))

            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)

            menu.exec_(self.tabela.viewport().mapToGlobal(posicion))

    def copiarTableWidgetItem(self, accion):
        itemSelecionado = [dado.text() for dado in self.tabela.selectedItems()]
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)

        if accion.text() == "Copiar":
            x = '\n'.join(itemSelecionado)
            cb.setText(x, mode=cb.Clipboard)

        return


# ===============================================================

# if __name__ == "__main__":
#     import sys
#
#     aplicacion = QApplication(sys.argv)
#
    # fonte = QFont()
    # fonte.setPointSize(10)
    # aplicacion.setFont(fonte)
#
#     janela = tableWidget()
#     janela.show()
#
#     sys.exit(aplicacion.exec_())
