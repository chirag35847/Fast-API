def seralizeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def seralizeList(entity) -> list:
    print(entity)
    return [seralizeDict(a) for a in entity]