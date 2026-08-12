
from typing import List,Optional
def nameReadFun(fileName:str)->Optional[List[str]]:
    with open(fileName,"r") as f:
        lines=f.readlines()
        if not lines:
            raise Exception("file is empty")
        names=[]
        for line in lines[1::]:
            parts=line.split()
            if len(parts)>=2:
                name=parts[1]
                if name not in names:
                    names.append(name)
        return names




if __name__=="__main__":
    try:
        print(nameReadFun("ass01.txt"))
    except Exception as e:
        print(e)

