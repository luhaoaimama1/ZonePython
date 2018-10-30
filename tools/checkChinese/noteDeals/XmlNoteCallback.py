from tools.checkChinese.noteDeals.NoteCallback import *
import re

class XmlNoteCallback(NoteCallback):
    isNote = False
    note = ["<!--", "-->"]  # 可以包含 // 所以先检查 note1
    note2 = [ '''tools:text="''','''"''']  # 可以包含 // 所以先检查 note1
    # notCheckFilePathRules = [
    #     # ".*tools:text=".*",
    #     '''tools:text="''','''"'''
    # ]

    def dealFile(self, lineContent):
        content=self.checkNote(lineContent,self.note)
        content2=self.checkNote(content,self.note2)
        return content2

    def checkNote(self, lineContent,noteRule):
        if self.isNote:
            return self.checkNoteEnd(lineContent,noteRule)
        else:
            return self.checkNoteStart(lineContent,noteRule)

    def checkNoteEnd(self, lineContent,noteRule):
        if lineContent.find(noteRule[1]) != -1:
            self.isNote = False
        return ""

    def checkNoteStart(self, lineContent,noteRule):
        findLoction = lineContent.find(noteRule[0])
        if findLoction != -1:
            if (lineContent.find(noteRule[1]) > findLoction+len(noteRule[0])-1):
                self.isNote = False
                return ""
            self.isNote = True
            return ""
        else:
            return lineContent
