from keywords import keywords

class Mail:
    '''
    subj - subject mail,
    body - body mail,
    tags - tags mail.
    '''
    def __select_tags(self, body:str) -> list:
        result = []
        
        for key in keywords.keys():
            for tag in keywords.get(key):
                if len(tag)>3 and body.lower().find(tag) > -1:
                    result.append(key)
                    break
        return result

        pass


    def __init__(self,index: int = 0, body: str = '', subj:str = '') -> None:
        self.index = index
        self.subj = subj
        self.tags = self.__select_tags(body)
        self.body = body

        pass

    def set_tag(self, tag):
        self.tags.append(tag)

    def __str__(self) -> str:
        tags = [f'#{t}' for t in self.tags]
        return f'{self.index}: {self.subj}\n{self.body}\n'+", ".join(tags)
        pass

    def __repr__(self) -> str:
        tags = [f'#{t}' for t in self.tags]
        return f'{self.index}: {self.subj}\n{self.body}\n'+", ".join(tags)
        pass