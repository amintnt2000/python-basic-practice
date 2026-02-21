def tup_make(item) -> tuple:
            if isinstance( item , tuple):
                return item
            elif isinstance(item , list):
                return tuple(item)
            elif isinstance(item , (int , float)):
                return (item,)
            elif isinstance(item , str):
                return tuple(item)
            else:
                return "unsupported"
print(tup_make(2.2))