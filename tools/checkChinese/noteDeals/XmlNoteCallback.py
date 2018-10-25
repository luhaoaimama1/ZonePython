from tools.checkChinese.noteDeals.NoteCallback import *

class XmlNoteCallback(NoteCallback):
    isNote1 = False
    note = ["<!--", "-->"]  # 可以包含 // 所以先检查 note1

    def dealFile(self, line):
        return self.checkNote(line)

    def checkNote(self, lineContent):
        if self.isNote1:
            return self.checkNoteEnd(lineContent)
        else:
            return self.checkNoteStart(lineContent)

    def checkNoteEnd(self, lineContent):
        if lineContent.find(self.note[1]) != -1:
            self.isNote1 = False
        return ""

    def checkNoteStart(self, lineContent):
        if lineContent.find(self.note[0]) != -1:
            self.isNote1 = True
            return ""
        else:
            return lineContent
