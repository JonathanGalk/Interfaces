from BlocoGUI import *
from PySide2.QtWidgets import QMessageBox
from dialogoGUI import *
def main():        
    #Funções
    def openWindow():
        global window
        window = QtWidgets.QWidget()
        u = Ui_Form()
        u.setupUi(window)
        window.show()
        
        def img():
            global file
            global image
            file = QtWidgets.QFileDialog.getOpenFileName(None, 'Inserir imagem',".","Images (*.png *.xpm *.jpg *.bmp *.gif)")[0]
            image = QtGui.QImage(file)
            u.altura.setValue(image.width())
            u.largura.setValue(image.height())
            
        def insert():
            altura = u.altura.value()
            largura = u.largura.value()
            img = image.scaled(largura, altura, QtCore.Qt.IgnoreAspectRatio)
            cursor = ui.textEdit.textCursor()
            cursor.insertImage(img, file)
            window.destroy()
            
        u.pushButton.clicked.connect(insert)
        u.btnOpen.clicked.connect(img)
        sys.exit(window.exec_())
        
    def lista():
        cursor = ui.textEdit.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numLista():
        cursor = ui.textEdit.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)
        
    def corFonte():
        color = QtWidgets.QColorDialog.getColor()
        ui.textEdit.setTextColor(color)
        
    def novo():
        ui.textEdit.clear()
        esquerda()
        ui.textEdit.setFontWeight(QtGui.QFont.Normal)
        ui.textEdit.setFontItalic(False)
        ui.textEdit.setFontUnderline(False)
        ui.textEdit.setTextColor('#000')
        ui.textEdit.setFontPointSize(8)
        
    def esquerda():
        ui.textEdit.setAlignment(QtCore.Qt.AlignLeft)

    def centralizar():
        ui.textEdit.setAlignment(QtCore.Qt.AlignCenter)
        
    def direita():
        ui.textEdit.setAlignment(QtCore.Qt.AlignRight)
   
    def negrito():
        if ui.textEdit.fontWeight() == QtGui.QFont.Bold:
            ui.textEdit.setFontWeight(QtGui.QFont.Normal)
        else:
            ui.textEdit.setFontWeight(QtGui.QFont.Bold)

    def italico():
        status = ui.textEdit.fontItalic()
        ui.textEdit.setFontItalic(not status)

    def sublinhado():
        status = ui.textEdit.fontUnderline()
        ui.textEdit.setFontUnderline(not status)
   
    def salvar():
        fileName = QtWidgets.QFileDialog.getSaveFileName(None, 'Salvar',
                                                         '','Arquivos de Texto (*.writer *.txt)')[0]
        with open(fileName, 'w', encoding='utf8') as f:
            texto = ui.textEdit.toHtml()
            f.write(texto)
        QMessageBox.about(None, 'Salvar Arquivo', 'Arquivo salvo com sucesso!')
        
    def abrir():
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, 'Abrir','.','(*.writer *.txt)')[0]
        if fileName:
            with open(fileName, 'r', encoding='utf8') as f:
                ui.textEdit.setText(f.read())
            
    #-----------------------------------------------
    #Tamanho das fontes
    fontSize = ui.spinBox
    fontSize.valueChanged.connect(lambda size: ui.textEdit.setFontPointSize(size))
    #Tipo de fonte
    tipo = ui.QfontComboBox
    tipo.currentFontChanged.connect(lambda font: ui.textEdit.setCurrentFont(font))
    
    #Botões
    ui.actionAbrir.triggered.connect(abrir)
    ui.actionSalvar.triggered.connect(salvar)
    ui.actionNegrito.triggered.connect(negrito)
    ui.actionItalico.triggered.connect(italico)
    ui.actionSublinhado.triggered.connect(sublinhado)
    ui.actionAlinhar_Esquerda.triggered.connect(esquerda)
    ui.actionCentralizar.triggered.connect(centralizar)
    ui.actionAlinhar_Direita.triggered.connect(direita)
    ui.actionNovo.triggered.connect(novo)
    ui.actionCor_Fonte.triggered.connect(corFonte)
    ui.actionLista.triggered.connect(lista)
    ui.actionLista_Numerada.triggered.connect(numLista)
    ui.actionInserir_Imagem.triggered.connect(openWindow)
    
    

  


   



    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main()
    sys.exit(app.exec_())
