import moeda
import dados

p = dados.validarD()
a = dados.validarAu()
d = dados.validarDe()

print(moeda.resumo(p, a, d))
