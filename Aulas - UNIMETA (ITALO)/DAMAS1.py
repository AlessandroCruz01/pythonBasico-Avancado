import tkinter
from tkinter import *


class Peca():
    idVal = 0
    row = 0
    column = 0
    color = ""
    king = False
    neNeighbor = []
    nwNeighbor = []
    seNeighhbor = []
    swNeighbor = []

    def __init__(self, row_, column_, color_, king_, idVal_):
        self.row = row_
        self.column = column_
        self.king = king_
        self.color = color_
        self.idVal = idVal_
        self.assignNeighbors()

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def getColor(self):
        return self.color

    def isKing(self):
        return self.king

    def getIDVal(self):
        return self.idVal

    def setToKing(self):
        self.king = True

    def getNEneighbor(self):
        return self.neNeighbor

    def getNWneighbor(self):
        return self.nwNeighbor

    def getSEneighbor(self):
        return self.seNeighhbor

    def getSWneighbor(self):
        return self.swNeighbor


    def assignNeighbors(self):

        northRow = 100
        southRow = 100
        eastCol = 100
        westCol = 100


        if (self.row - 1) >= 0:
            northRow = self.row - 1
        if (self.row + 1) <= 7:
            southRow = self.row + 1
        if (self.column - 1) >= 0:
            westCol = self.column - 1
        if (self.column + 1) <= 7:
            eastCol = self.column + 1


        self.neNeighbor = (northRow, eastCol)
        self.nwNeighbor = (northRow, westCol)
        self.seNeighhbor = (southRow, eastCol)
        self.swNeighbor = (southRow, westCol)


    def updateLocation(self, row_, column_):
        self.row = row_
        self.column = column_
        self.assignNeighbors()
        if row_ == 0 and self.color == "white":
            if not self.isKing():
                self.setToKing()
        if row_ == 7 and self.color == "grey":
            if not self.isKing():
                self.setToKing()

    def printLocation(self):
        print
        "Location: (%s, %s)" % (self.column, self.row)

    def printInfo(self):
        print
        "Location: (%s, %s)" % (self.column, self.row),
        print("King: %s" % self.king)



class CheckerBoard(Canvas):
    gb = tkinter.Tk()
    greyPieces = []
    redPieces = []
    board = []
    highlightedTiles = []
    currentlySelectedCheckerObject = Peca(0, 0, "grey", False, 0)
    currentlySelectedCheckerID = 0
    tileWidth = 31
    tileHeight = 31
    rows = 8
    columns = 8
    GREY_CHECKER = 1
    RED_CHECKER = 2
    tileBorder = .75
    checkerBorder = 4
    currentPlayer = "red"
    mustDoubleJump = False
    redCount = 12
    greyCount = 12
    redScoreBoard = Label(gb, text="Branco: %i" % redCount)
    greyScoreBoard = Label(gb, text="Preto: %i" % greyCount)


    def startNewGame(self):

        for i in self.greyPieces:
            self.delete(i[0])
        for i in self.redPieces:
            self.delete(i[0])


        for i in range(0, len(self.greyPieces)):
            self.greyPieces.pop()

        for i in range(0, len(self.redPieces)):
            self.redPieces.pop()

        for i in range(0, len(self.highlightedTiles)):
            self.highlightedTiles.pop()



        self.greyPieces = []
        self.redPieces = []
        self.highlightedTiles = []
        self.currentlySelectedCheckerObject = Peca(0, 0, "grey", False, 0)
        self.currentlySelectedCheckerID = 0
        self.currentPlayer = "red"
        self.mustDoubleJump = False
        self.redCount = 12
        self.greyCount = 12
        self.redScoreBoard.config(text="Red: %i" % self.redCount)
        self.greyScoreBoard.config(text="Grey: %i" % self.greyCount)


        self.createCheckers()



    def __init__(self):
        self.gb.minsize(250, 350)
        Canvas.__init__(self, self.gb, bg="grey", height=250, width=250)
        newGameButton = Button(self.gb, text="Novo Jogo", command=self.startNewGame)
        self.redScoreBoard.pack()
        self.greyScoreBoard.pack()
        self.pack()
        newGameButton.pack()
        self.criar_tabuleiro()
        self.createCheckers()
        self.gb.mainloop()



    def criar_tabuleiro(self):
        width = self.tileWidth
        height = self.tileHeight
        for i in range(0, self.columns):
            x1 = (i * width) + self.tileBorder
            x2 = ((i + 1) * width) - self.tileBorder
            for j in range(0, self.rows):
                y1 = (j * height) + self.tileBorder
                y2 = ((j + 1) * height) - self.tileBorder
                idVal = 0
                if ((i + j) % 2 == 0):
                    idVal = self.create_rectangle(x1, y1, x2, y2, fill="white")
                else:
                    idVal = self.create_rectangle(x1, y1, x2, y2, fill="black")
                if idVal != 0:
                    self.board.append((idVal, j, i, x1, x2, y1, y2))


    def createCheckers(self):
        checkerWidth = self.tileWidth
        checkerHeight = self.tileWidth

        for i in range(0, self.rows):

            if i == 3 or i == 4:
                continue

            y1 = (i * checkerWidth) + self.checkerBorder
            y2 = ((i + 1) * checkerWidth) - self.checkerBorder

            if i < 3:
                checkerColor = "grey"

            elif i > 4:
                checkerColor = "red"

            for j in range(0, self.columns):

                if ((i + j) % 2 == 1):

                    x1 = (j * checkerHeight) + self.checkerBorder
                    x2 = ((j + 1) * checkerHeight) - self.checkerBorder

                    idTag = self.create_oval(x1, y1, x2, y2, fill=checkerColor)
                    self.tag_bind(idTag, "<ButtonPress-1>", self.processCheckerClick)

                    newChecker = Peca(i, j, checkerColor, False, idTag)

                    if checkerColor == "grey":
                        self.greyPieces.append((idTag, newChecker))
                    elif checkerColor == "red":
                        self.redPieces.append((idTag, newChecker))


    def processCheckerClick(self, event):
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        idValue = self.find_closest(x, y)[0]
        selectedChecker = self.getCheckerObject(idValue)

        if selectedChecker == 0:
            return

        if (self.currentPlayer == selectedChecker.getColor()) and (self.mustDoubleJump == False):

            self.currentlySelectedCheckerObject = selectedChecker
            self.currentlySelectedCheckerID = idValue

            self.resetHighlightedTiles()

            self.showAllAvailableRegularMoves(selectedChecker)

            self.showAllAvailableJumpMoves(selectedChecker)



    def processHighlightedTileClicked(self, event):
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        idValue = self.find_closest(x, y)[0]

        newRow = 100
        newCol = 100
        jumpedCheckerID = 0
        for i in self.board:
            if i[0] == idValue:
                newRow = i[1]
                newCol = i[2]
                jumpedCheckerID = self.getJumpedCheckerID(newRow, newCol)
                break

        if newRow == 100:
            return


        self.moveCurrentlySelectedChecker(newRow, newCol)

        self.resetHighlightedTiles()

        if jumpedCheckerID != 0:
            self.removeChecker(jumpedCheckerID)
            self.showAllAvailableJumpMoves(self.currentlySelectedCheckerObject)

            if len(self.highlightedTiles) > 0:
                self.mustDoubleJump = True

            else:
                self.switchCurrentPlayer()
                self.mustDoubleJump = False

        else:
            self.switchCurrentPlayer()


    def switchCurrentPlayer(self):
        if self.currentPlayer == "red":
            self.currentPlayer = "grey"
        elif self.currentPlayer == "grey":
            self.currentPlayer = "red"


    def removeChecker(self, checkerID):
        if checkerID != 0:
            self.delete(checkerID)
            for i in self.redPieces:
                if i[0] == checkerID:
                    self.redPieces.remove(i)
                    self.redCount = self.redCount - 1
                    self.redScoreBoard.config(text="Red: %i" % self.redCount)
                    break
            for i in self.greyPieces:
                if i[0] == checkerID:
                    self.greyPieces.remove(i)
                    self.greyCount = self.greyCount - 1
                    self.greyScoreBoard.config(text="Grey: %i" % self.greyCount)
                    break
            self.checkForWin()


    def checkForWin(self):
        if self.redCount <= 0:
            greyWinnerLabel = Label(self.gb, text="Grey Wins!")
            greyWinnerLabel.pack()
            self.stopTheGame()
        elif self.greyCount <= 0:
            redWinnerLabel = Label(self.gb, text="Red Wins!")
            redWinnerLabel.pack()
            self.stopTheGame()


    def stopTheGame(self):
        for i in self.redPieces:
            checkerIDVal = i[0]
            if checkerIDVal != 0:
                self.tag_unbind(checkerIDVal, "<ButtonPress-1>")
        for i in self.greyPieces:
            checkerIDVal = i[0]
            if checkerIDVal != 0:
                self.tag_unbind(checkerIDVal, "<ButtonPress-1>")
        self.resetHighlightedTiles()



    def getJumpedCheckerID(self, row_, col_):
        for i in self.highlightedTiles:
            if row_ == i[0] and col_ == i[1]:
                return i[2]
        return 0


    def moveCurrentlySelectedChecker(self, newRow_, newCol_):
        y1 = (newRow_ * self.tileWidth) + self.checkerBorder
        y2 = ((newRow_ + 1) * self.tileWidth) - self.checkerBorder
        x1 = (newCol_ * self.tileWidth) + self.checkerBorder
        x2 = ((newCol_ + 1) * self.tileWidth) - self.checkerBorder

        self.coords(self.currentlySelectedCheckerID, (x1, y1, x2, y2))

        self.currentlySelectedCheckerObject.updateLocation(newRow_, newCol_)
        if self.currentlySelectedCheckerObject.isKing():
            self.itemconfig(self.currentlySelectedCheckerID, outline="cyan")



    def resetHighlightedTiles(self):

        for i in self.highlightedTiles:
            tileIDVal = self.getTileID(i[0], i[1])
            if tileIDVal != 0:
                self.itemconfig(tileIDVal, outline="black")
                self.tag_unbind(tileIDVal, "<ButtonPress-1>")


        for i in range(0, len(self.highlightedTiles)):
            self.highlightedTiles.pop()



    def showAllAvailableRegularMoves(self, _selectedChecker):
        selectedChecker = _selectedChecker
        selectedCheckerIsKing = selectedChecker.isKing()
        selectedCheckerColor = selectedChecker.getColor()
        openSpaces = []

        if selectedCheckerIsKing:

            rowValue = selectedChecker.getNWneighbor()[0]
            colValue = selectedChecker.getNWneighbor()[1]
            if (not self.isTileOccupied(rowValue, colValue)[0]):
                openSpaces.append(selectedChecker.getNWneighbor())


            rowValue = selectedChecker.getNEneighbor()[0]
            colValue = selectedChecker.getNEneighbor()[1]
            if (not self.isTileOccupied(rowValue, colValue)[0]):
                openSpaces.append(selectedChecker.getNEneighbor())


            rowValue = selectedChecker.getSWneighbor()[0]
            colValue = selectedChecker.getSWneighbor()[1]
            if (not self.isTileOccupied(rowValue, colValue)[0]):
                openSpaces.append(selectedChecker.getSWneighbor())


            rowValue = selectedChecker.getSEneighbor()[0]
            colValue = selectedChecker.getSEneighbor()[1]
            if (not self.isTileOccupied(rowValue, colValue)[0]):
                openSpaces.append(selectedChecker.getSEneighbor())

        elif selectedCheckerColor == "red":

            rowValue = selectedChecker.getNWneighbor()[0]
            colValue = selectedChecker.getNWneighbor()[1]
            if (not self.isTileOccupied(rowValue, colValue)[0]):
                openSpaces.append(selectedChecker.getNWneighbor())


            rowValue = selectedChecker.getNEneighbor()[0]
            colValue = selectedChecker.getNEneighbor()[1]
            if (not self.isTileOccupied(rowValue, colValue)[0]):
                openSpaces.append(selectedChecker.getNEneighbor())

        elif selectedCheckerColor == "grey":

            rowValue = selectedChecker.getSWneighbor()[0]
            colValue = selectedChecker.getSWneighbor()[1]
            if (not self.isTileOccupied(rowValue, colValue)[0]):
                openSpaces.append(selectedChecker.getSWneighbor())


            rowValue = selectedChecker.getSEneighbor()[0]
            colValue = selectedChecker.getSEneighbor()[1]
            if (not self.isTileOccupied(rowValue, colValue)[0]):
                openSpaces.append(selectedChecker.getSEneighbor())


        for i in range(0, len(openSpaces)):
            highlightRow = openSpaces[i][0]
            highlightCol = openSpaces[i][1]
            if highlightRow == 100 or highlightCol == 100:
                continue
            tileIDVal = self.getTileID(highlightRow, highlightCol)
            if tileIDVal != 0:
                self.itemconfig(tileIDVal, outline="yellow")
                self.tag_bind(tileIDVal, "<ButtonPress-1>", self.processHighlightedTileClicked)
                self.highlightedTiles.append((highlightRow, highlightCol, 0))
            else:
                print ("Invalid tile")


    def showAllAvailableJumpMoves(self, selectedChecker_):
        selectedChecker = selectedChecker_
        selectedCheckerIsKing = selectedChecker.isKing()
        selectedCheckerColor = selectedChecker.getColor()

        if selectedCheckerIsKing:

            rowValue = selectedChecker.getNWneighbor()[0]
            colValue = selectedChecker.getNWneighbor()[1]
            isTileOccupiedReturnArray = self.isTileOccupied(rowValue, colValue)
            isTileOccupied = isTileOccupiedReturnArray[0]
            tileColor = isTileOccupiedReturnArray[1]
            jumpCheckerID = isTileOccupiedReturnArray[2]
            if isTileOccupied:
                if selectedCheckerColor != tileColor:
                    jumpRow = selectedChecker.getNWneighbor()[0]
                    jumpCol = selectedChecker.getNWneighbor()[1]
                    self.checkForJump(jumpRow - 1, jumpCol - 1, jumpCheckerID)


            rowValue = selectedChecker.getNEneighbor()[0]
            colValue = selectedChecker.getNEneighbor()[1]
            isTileOccupiedReturnArray = self.isTileOccupied(rowValue, colValue)
            isTileOccupied = isTileOccupiedReturnArray[0]
            tileColor = isTileOccupiedReturnArray[1]
            jumpCheckerID = isTileOccupiedReturnArray[2]
            if isTileOccupied:
                if selectedCheckerColor != tileColor:
                    jumpRow = selectedChecker.getNEneighbor()[0]
                    jumpCol = selectedChecker.getNEneighbor()[1]
                    self.checkForJump(jumpRow - 1, jumpCol + 1, jumpCheckerID)


            rowValue = selectedChecker.getSWneighbor()[0]
            colValue = selectedChecker.getSWneighbor()[1]
            isTileOccupiedReturnArray = self.isTileOccupied(rowValue, colValue)
            isTileOccupied = isTileOccupiedReturnArray[0]
            tileColor = isTileOccupiedReturnArray[1]
            jumpCheckerID = isTileOccupiedReturnArray[2]
            if isTileOccupied:
                if selectedCheckerColor != tileColor:
                    jumpRow = selectedChecker.getSWneighbor()[0]
                    jumpCol = selectedChecker.getSWneighbor()[1]
                    self.checkForJump(jumpRow + 1, jumpCol - 1, jumpCheckerID)


            rowValue = selectedChecker.getSEneighbor()[0]
            colValue = selectedChecker.getSEneighbor()[1]
            isTileOccupiedReturnArray = self.isTileOccupied(rowValue, colValue)
            isTileOccupied = isTileOccupiedReturnArray[0]
            tileColor = isTileOccupiedReturnArray[1]
            jumpCheckerID = isTileOccupiedReturnArray[2]
            if isTileOccupied:
                if selectedCheckerColor != tileColor:
                    jumpRow = selectedChecker.getSEneighbor()[0]
                    jumpCol = selectedChecker.getSEneighbor()[1]
                    self.checkForJump(jumpRow + 1, jumpCol + 1, jumpCheckerID)


        elif selectedCheckerColor == "red":

            rowValue = selectedChecker.getNWneighbor()[0]
            colValue = selectedChecker.getNWneighbor()[1]
            isTileOccupiedReturnArray = self.isTileOccupied(rowValue, colValue)
            isTileOccupied = isTileOccupiedReturnArray[0]
            tileColor = isTileOccupiedReturnArray[1]
            jumpCheckerID = isTileOccupiedReturnArray[2]
            if isTileOccupied:
                if selectedCheckerColor != tileColor:
                    jumpRow = selectedChecker.getNWneighbor()[0]
                    jumpCol = selectedChecker.getNWneighbor()[1]
                    self.checkForJump(jumpRow - 1, jumpCol - 1, jumpCheckerID)


            rowValue = selectedChecker.getNEneighbor()[0]
            colValue = selectedChecker.getNEneighbor()[1]
            isTileOccupiedReturnArray = self.isTileOccupied(rowValue, colValue)
            isTileOccupied = isTileOccupiedReturnArray[0]
            tileColor = isTileOccupiedReturnArray[1]
            jumpCheckerID = isTileOccupiedReturnArray[2]
            if isTileOccupied:
                if selectedCheckerColor != tileColor:
                    jumpRow = selectedChecker.getNEneighbor()[0]
                    jumpCol = selectedChecker.getNEneighbor()[1]
                    self.checkForJump(jumpRow - 1, jumpCol + 1, jumpCheckerID)

        elif selectedCheckerColor == "grey":

            rowValue = selectedChecker.getSWneighbor()[0]
            colValue = selectedChecker.getSWneighbor()[1]
            isTileOccupiedReturnArray = self.isTileOccupied(rowValue, colValue)
            isTileOccupied = isTileOccupiedReturnArray[0]
            tileColor = isTileOccupiedReturnArray[1]
            jumpCheckerID = isTileOccupiedReturnArray[2]
            if isTileOccupied:
                if selectedCheckerColor != tileColor:
                    jumpRow = selectedChecker.getSWneighbor()[0]
                    jumpCol = selectedChecker.getSWneighbor()[1]
                    self.checkForJump(jumpRow + 1, jumpCol - 1, jumpCheckerID)


            rowValue = selectedChecker.getSEneighbor()[0]
            colValue = selectedChecker.getSEneighbor()[1]
            isTileOccupiedReturnArray = self.isTileOccupied(rowValue, colValue)
            isTileOccupied = isTileOccupiedReturnArray[0]
            tileColor = isTileOccupiedReturnArray[1]
            jumpCheckerID = isTileOccupiedReturnArray[2]
            if isTileOccupied:
                if selectedCheckerColor != tileColor:
                    jumpRow = selectedChecker.getSEneighbor()[0]
                    jumpCol = selectedChecker.getSEneighbor()[1]
                    self.checkForJump(jumpRow + 1, jumpCol + 1, jumpCheckerID)


    def checkForJump(self, row_, col_, jumpedCheckerID_):

        if not self.isValidPosition(row_, col_):
            return 0

        if not self.isTileOccupied(row_, col_)[0]:
            tileIDVal = self.getTileID(row_, col_)
            if tileIDVal != 0:
                self.itemconfig(tileIDVal, outline="yellow")
                self.tag_bind(tileIDVal, "<ButtonPress-1>", self.processHighlightedTileClicked)
                self.highlightedTiles.append((row_, col_, jumpedCheckerID_))



    def isTileOccupied(self, rowVal, colVal):
        row = rowVal
        col = colVal

        if (not self.isValidPosition(row, col)):
            return (False, "NA", 0)


        for i in range(0, len(self.greyPieces)):
            currentChecker = self.greyPieces[i][1]
            if (row == currentChecker.getRow()) and (col == currentChecker.getColumn()):
                return (True, "grey", self.greyPieces[i][0])


        for i in range(0, len(self.redPieces)):
            currentChecker = self.redPieces[i][1]
            if (row == currentChecker.getRow()) and (col == currentChecker.getColumn()):
                return (True, "red", self.redPieces[i][0])


        return (False, "NA", 0)



    def getCheckerObject(self, idValue):

        for i in range(0, len(self.greyPieces)):
            if self.greyPieces[i][0] == idValue:
                return self.greyPieces[i][1]


        for i in range(0, len(self.redPieces)):
            if self.redPieces[i][0] == idValue:
                return self.redPieces[i][1]


        return 0


    def getTileID(self, row_, col_):
        row = row_
        col = col_
        for i in range(0, len(self.board)):
            if row == self.board[i][1] and col == self.board[i][2]:
                return self.board[i][0]
        return 0


    def isValidPosition(self, row_, col_):
        return self.isValidRow(row_) and self.isValidColumn(col_)


    def isValidRow(self, row_):
        if (row_ >= 0 and row_ <= 7):
            return True
        else:
            return False


    def isValidColumn(self, col_):
        if (col_ >= 0 and col_ <= 7):
            return True
        else:
            return False
if __name__ == '__main__':
    CheckerBoard()