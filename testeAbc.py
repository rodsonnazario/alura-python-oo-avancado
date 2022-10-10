from collections.abc import MutableSequence


class MinhaListinhaMutavel(MutableSequence):
    pass


objetoValidado = MinhaListinhaMutavel()
# deve mostrar o erro TypeError: Can't instantiate abstract class MinhaListinhaMutavel with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert
print(objetoValidado)
