from PyQt5.QtWidgets import (QFrame, QPushButton, QWidget, QTabWidget,
                             QApplication, QHBoxLayout, QVBoxLayout, QCalendarWidget, QSplitter, QFormLayout,
                             QLabel, QLineEdit, QComboBox, QMessageBox)
from PyQt5.QtCore import Qt


import sqlite3

import sys
import Tabela as tab


class Inicio(QWidget):
    def __init__(self):
        super().__init__()

        self.hbox = QHBoxLayout()
        self.hbox.setSpacing(0)
        self.hbox.setContentsMargins(0, 0, 0, 0)

        frameE = QFrame()
        frameE.setFrameShape(QFrame.StyledPanel)

        frameE.setStyleSheet("""background-image: url(teste.png);
                                background-repeat: no-repeat;""")

        frameD = QFrame()
        frameD.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(frameE)
        splitter1.addWidget(frameD)

        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(1, 1, 1, 1)

        cal = QCalendarWidget()
        cal.setGridVisible(True)

        down = QFrame()
        down.setFrameShape(QFrame.StyledPanel)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(cal)
        splitter2.addWidget(down)

        self.vbox.addWidget(splitter2)

        frameD.setLayout(self.vbox)

        self.hbox.addWidget(splitter1)

        self.setLayout(self.hbox)


class Cadastro(QWidget):
    def __init__(self, what):
        super().__init__()

        self.conexao = sqlite3.connect('database.db')

        if what == 'alunos':

            form = QFormLayout()

            self.nome = QLineEdit()

            self.cpf = QLineEdit()
            self.cpf.setInputMask('000.000.000-00')


            self.rg = QLineEdit()

            self.dtn = QLineEdit()
            self.dtn.setInputMask('00/00/0000')

            self.sex = QComboBox()
            self.sex.addItem('Masculino')
            self.sex.addItem('Feminino')

            self.situ = QComboBox()
            self.situ.addItem('Cursando')
            self.situ.addItem('Aprovado')
            self.situ.addItem('Reprovado')


            self.escolari = QComboBox()
            self.escolari.addItem('Nenhum')
            self.escolari.addItem('1° Série')
            self.escolari.addItem('2° Série')
            self.escolari.addItem('3° Série')
            self.escolari.addItem('4° Série')

            self.responsavel = QLineEdit()
            self.telResponsavel = QLineEdit()
            self.telResponsavel.setInputMask('(00) 00000-0000')

            form.addRow(QLabel('Nome:'), self.nome)
            form.addRow(QLabel('CPF:'), self.cpf)
            form.addRow(QLabel('RG:'), self.rg)
            form.addRow(QLabel('Data de Nascimento:'), self.dtn)
            form.addRow(QLabel('Sexo:'), self.sex)
            form.addRow(QLabel('Situação:'), self.situ)
            form.addRow(QLabel('Escolaridade:'), self.escolari)
            form.addRow(QLabel('Nome Responsável:'), self.responsavel)
            form.addRow(QLabel('Tel. Responsável:'), self.telResponsavel)

            form.setSpacing(10)

            down = QFrame()
            down.setFixedHeight(80)

            center = QFrame()
            center.setFixedWidth(500)

            salvar = QPushButton('Salvar')
            salvar.setFixedWidth(80)
            salvar.clicked.connect(self.salvarAluno)
            limpar = QPushButton('Limpar')
            limpar.setFixedWidth(90)

            hbox = QHBoxLayout()
            hbox2 = QHBoxLayout()

            form.addWidget(down)

            hbox2.addWidget(salvar)
            hbox2.addWidget(limpar)
            down.setLayout(hbox2)

            center.setLayout(form)

            hbox.addWidget(center)

            self.setLayout(hbox)
        elif what == 'funcionarios':

            form = QFormLayout()

            self.nome = QLineEdit()

            self.cpf = QLineEdit()
            self.cpf.setInputMask('000.000.000-00')

            self.rg = QLineEdit()

            self.dtn = QLineEdit()
            self.dtn.setInputMask('00/00/0000')

            self.sexo = QComboBox()
            self.sexo.addItem('Masculino')
            self.sexo.addItem('Feminino')

            self.tel = QLineEdit()
            self.tel.setInputMask('(00) 00000-0000')

            self.cargo = QLineEdit()

            form.addRow(QLabel('Nome:'), self.nome)
            form.addRow(QLabel('CPF:'), self.cpf)
            form.addRow(QLabel('RG:'), self.rg)
            form.addRow(QLabel('Data de Nascimento:'), self.dtn)
            form.addRow(QLabel('Sexo:'), self.sexo)
            form.addRow(QLabel('Telefone:'), self.tel)
            form.addRow(QLabel('Cargo:'), self.cargo)

            form.setSpacing(10)

            down = QFrame()
            down.setFixedHeight(80)

            center = QFrame()
            center.setFixedWidth(500)

            salvar = QPushButton('Salvar')
            salvar.setFixedWidth(80)
            salvar.clicked.connect(self.salvarFuncionarios)
            limpar = QPushButton('Limpar')
            limpar.setFixedWidth(90)

            hbox = QHBoxLayout()
            hbox2 = QHBoxLayout()

            form.addWidget(down)

            hbox2.addWidget(salvar)
            hbox2.addWidget(limpar)
            down.setLayout(hbox2)

            center.setLayout(form)

            hbox.addWidget(center)

            self.setLayout(hbox)
        elif what == 'cargos':
            form = QFormLayout()

            self.nomeCargo = QLineEdit()
            self.setor = QLineEdit()

            form.addRow(QLabel('Nome Cargo:'), self.nomeCargo)
            form.addRow(QLabel('Setor:'), self.setor)
            form.setSpacing(10)

            down = QFrame()
            down.setFixedHeight(80)

            center = QFrame()
            center.setFixedWidth(500)

            salvar = QPushButton('Salvar')
            salvar.setFixedWidth(80)
            salvar.clicked.connect(self.salvarCargo)
            limpar = QPushButton('Limpar')
            limpar.setFixedWidth(90)

            hbox = QHBoxLayout()
            hbox2 = QHBoxLayout()

            form.addWidget(down)

            hbox2.addWidget(salvar)
            hbox2.addWidget(limpar)
            down.setLayout(hbox2)

            center.setLayout(form)

            hbox.addWidget(center)

            self.setLayout(hbox)

        elif what == 'disciplinas':
            form = QFormLayout()

            self.nomeDisciplina = QLineEdit()
            self.cargaH = QLineEdit()

            self.professor = QComboBox()
            self.professor.addItem('Selecione')

            form.addRow(QLabel('Nome da Disciplina:'), self.nomeDisciplina)
            form.addRow(QLabel('Carga Horária:'), self.cargaH)
            form.addRow(QLabel('Professor Ministrante:'), self.professor)

            form.setSpacing(10)

            down = QFrame()
            down.setFixedHeight(80)

            center = QFrame()
            center.setFixedWidth(500)

            salvar = QPushButton('Salvar')
            salvar.setFixedWidth(80)
            salvar.clicked.connect(self.salvarFuncionarios)
            limpar = QPushButton('Limpar')
            limpar.setFixedWidth(90)

            hbox = QHBoxLayout()
            hbox2 = QHBoxLayout()

            form.addWidget(down)

            hbox2.addWidget(salvar)
            hbox2.addWidget(limpar)
            down.setLayout(hbox2)

            center.setLayout(form)

            hbox.addWidget(center)

            self.setLayout(hbox)
        else:
            if what == 'notas':
                form = QFormLayout()

                self.nota = QLineEdit()
                self.modulo = QLineEdit()

                self.aluno = QComboBox()
                self.aluno.addItem('Selecione')

                self.disciplina = QComboBox()
                self.disciplina.addItem('Selecione')

                form.addRow(QLabel('Nota:'), self.nota)
                form.addRow(QLabel('Módulo:'), self.modulo)
                form.addRow(QLabel('Aluno:'), self.aluno)
                form.addRow(QLabel('Disciplina:'), self.disciplina)

                form.setSpacing(10)

                down = QFrame()
                down.setFixedHeight(80)

                center = QFrame()
                center.setFixedWidth(500)

                salvar = QPushButton('Salvar')
                salvar.setFixedWidth(80)
                salvar.clicked.connect(self.salvarNotas)
                limpar = QPushButton('Limpar')
                limpar.setFixedWidth(90)

                hbox = QHBoxLayout()
                hbox2 = QHBoxLayout()

                form.addWidget(down)

                hbox2.addWidget(salvar)
                hbox2.addWidget(limpar)
                down.setLayout(hbox2)

                center.setLayout(form)

                hbox.addWidget(center)

                self.setLayout(hbox)

    def salvarAluno(self):
        if self.nome.text() != '' and self.cpf.text() != '..-' and len(self.cpf.text()) != 14 and\
                        self.rg.text() != '' and self.dtn.text() != '//' and len(self.dtn.text()) != 10 and\
                        self.responsavel.text() != '' and self.telResponsavel != '() -' and len(self.telResponsavel.text()) != 15:
            cursor = self.conexao.cursor()
            cursor.execute("""SELECT nome FROM alunos WHERE cpf = '%s'""" % self.cpf.text())

            if cursor.fetchone() == None:

                aviso = QMessageBox.question(self, 'Salvar', 'Você tem certeza que deseja cadastrar %s como aluno?' % self.nome.text(), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if aviso == QMessageBox.Yes:
                    cursor.execute("""
                                INSERT INTO alunos(nome, cpf, rg, data_nascimento, sexo, situacao, escolaridade, responsavel, tel_responsavel)
                                VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"""
                                   % (self.nome.text(), self.cpf.text(), self.rg.text(), self.dtn.text(),
                                      self.sex.currentText(),
                                      self.situ.currentText(), self.escolari.currentText(), self.responsavel.text(),
                                      self.telResponsavel.text()))
                    self.conexao.commit()
                    apagar = [self.nome, self.cpf, self.rg, self.dtn, self.responsavel, self.telResponsavel]
                    for i in apagar:
                        i.clear()
                    self.situ.setCurrentIndex(0)
                    self.escolari.setCurrentIndex(0)
                else:
                    pass
            else:
                QMessageBox.information(self, 'Atenção', 'Aluno já cadastrado', QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Erro', 'Todos os Campos são obrigatórios.', QMessageBox.Ok)

    def salvarFuncionarios(self):
        print('funcionarios')
    def salvarDisciplinas(self):
        print('disciplinas')
    def salvarNotas(self):
        print('notas')
    def salvarCargo(self):
        if self.nomeCargo.text() != '' and self.setor.text() != '':
            cursor = self.conexao.cursor()
            cursor.execute("""SELECT nome_cargo FROM cargos WHERE nome_cargo = '%s'""" % self.nomeCargo.text())

            if cursor.fetchone() == None:
                aviso = QMessageBox.question(self, 'Salvar', 'Você têm certeza que deseja cadastrar %s como cargo?' % self.nomeCargo.text(), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if aviso == QMessageBox.Yes:
                    cursor.execute("""INSERT INTO cargos(nome_cargo, setor) VALUES('%s', '%s');""" % (self.nomeCargo.text(), self.setor.text()))
                    self.conexao.commit()
                    self.nomeCargo.clear()
                    self.setor.clear()
                else:
                    pass
            else:
                QMessageBox.information(self, 'Atenção', 'Cargo já Cadastrado', QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Erro', 'Todos os campos são obrigatórios', QMessageBox.Ok)

    def __del__(self):
        self.conexao.close()

class Principal(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 100, 1000, 500)
        self.initUI()

    def initUI(self):
        self.tabs = QTabWidget()
        self.tabs.setMovable(True)
        self.tabs.setDocumentMode(True)
        self.tabs.setUsesScrollButtons(True)

        self.tabs.addTab(Inicio(), 'Início')
        self.tabs.addTab(Cadastro('alunos'), 'Cad. Alunos')
        self.tabs.addTab(Cadastro('funcionarios'), 'Cad. Funcionários')
        self.tabs.addTab(Cadastro('cargos'), 'Cargos')
        self.tabs.addTab(Cadastro('disciplinas'), 'Cad. Disciplinas')
        self.tabs.addTab(Cadastro('notas'), 'Notas')
        self.tabs.addTab(tab.TableWidget(), 'Listar')

        hbox = QHBoxLayout()
        hbox.addWidget(self.tabs)

        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet("""       

QTabWidget::tab-bar:top {
    top: 1px;
}

QTabWidget::tab-bar:bottom {
    bottom: 1px;
}

QTabWidget::tab-bar:left {
    right: 1px;
}

QTabWidget::tab-bar:right {
    left: 1px;
}

QTabBar::tab {
    border: 1px solid black;
}

QTabBar::tab:selected {
    background: white;
}

QTabBar::tab:!selected {
    background: silver;
}

QTabBar::tab:!selected:hover {
    background: #999;
}

QTabBar::tab:top:!selected {
    margin-top: 3px;
}

QTabBar::tab:bottom:!selected {
    margin-bottom: 3px;
}

QTabBar::tab:top, QTabBar::tab:bottom {
    min-width: 10px;
    margin-right: -1px;
    padding: 7px 10px 6px 10px;
}

QTabBar::tab:top:selected {
    border-bottom-color: none;
}

QTabBar::tab:left:!selected {
    margin-right: 3px;
}

QTabBar::tab:right:!selected {
    margin-left: 3px;
}

QTabBar::tab:left, QTabBar::tab:right {
    min-height: 8ex;
    margin-bottom: -1px;
    padding: 10px 5px 10px 5px;
}
""")

    teste = Principal()
    teste.show()
    sys.exit(app.exec_())
