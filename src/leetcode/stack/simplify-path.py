"""
turn into split array spliting on '/'

initialize reuslt path = ""

i.e. ['', '...', 'a', '..', 'b', 'c', '..', 'd', '.', '']
pop ['', '...', 'a', '..', 'b', 'c', '..', 'd', '.'] empty string do nothing
pop ['', '...', 'a', '..', 'b', 'c', '..', 'd', '.'] '.' curr dir do nothing
pop ['', '...', 'a', '..', 'b', 'c', '..', 'd'] d add to result path, also its our first so don't include trailing slash
pop ['', '...', 'a', '..', 'b', 'c', '..'] found '..' so pop again to remove the c
pop ['', '...', 'a', '..', 'b'] found 'b' so add to result array
etc...

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        result = ""
        split_path = path.split('/')
        back_count = 0
        while split_path:
            elem = split_path.pop()
            if len(split_path) == 0:
                split_path = None
                break
            elif elem == '.' or elem == '':
                continue
            elif elem == '..' and len(split_path) > 0:
                back_count += 1
                continue
            else:
                if back_count:
                    back_count -= 1
                    continue
                else:
                    result = f"/{elem}{result}"
        return result if result != "" else "/"
