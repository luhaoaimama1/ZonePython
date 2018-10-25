from tools.checkChinese.noteDeals.NoteCallback import *


class JavaKtNoteCallback(NoteCallback):
    isNote1 = False
    note1 = ["/*", "*/"]  # 可以包含 // 所以先检查 note1
    note2 = "//"  # 不可以包含note1

    def dealFile(self, line):
        validContent = self.checkNote1(line)
        if self.isNote1 == False:
            validContent = self.checkNote2(validContent)
        return validContent

    def checkNote2(self, lineContent):
        if lineContent.find(self.note2) != -1:
            return lineContent.split(self.note2)[0]
        else:
            return lineContent

    def checkNote1(self, lineContent):
        if self.isNote1:
            return self.checkNote1End(lineContent)
        else:
            return self.checkNote1Start(lineContent)

    def checkNote1End(self, lineContent):
        if lineContent.find(self.note1[1]) != -1:
            self.isNote1 = False
        return ""

    def checkNote1Start(self, lineContent):
        findLoction = lineContent.find(self.note1[0])
        if findLoction != -1:
            if (lineContent.find(self.note1[1]) > findLoction):
                self.isNote1 = False
                return ""
            self.isNote1 = True
            return ""
        else:
            return lineContent
