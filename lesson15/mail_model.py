
class Mail:

    def __init__(self,index: int = 0, subj: str = '', body:str = '') -> None:
        self.index = index
        self.subj = subj
        self.tags = []
        self.body = body

        pass

    def set_tag(self, tag):
        self.tags.append(tag)