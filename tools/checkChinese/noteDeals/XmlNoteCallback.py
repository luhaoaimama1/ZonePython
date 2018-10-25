from tools.checkChinese.noteDeals.NoteCallback import *


class XmlNoteCallback(NoteCallback):
    isNote = False
    note = ["<!--", "-->"]  # 可以包含 // 所以先检查 note1

    def dealFile(self, line):
        return self.checkNote(line)

    def checkNote(self, lineContent):
        if self.isNote:
            return self.checkNoteEnd(lineContent)
        else:
            return self.checkNoteStart(lineContent)

    def checkNoteEnd(self, lineContent):
        if lineContent.find(self.note[1]) != -1:
            self.isNote = False
        return ""

    def checkNoteStart(self, lineContent):
        findLoction = lineContent.find(self.note[0])
        if findLoction != -1:
            if (lineContent.find(self.note[1]) > findLoction):
                self.isNote = False
                return ""
            self.isNote = True
            return ""
        else:
            return lineContent
