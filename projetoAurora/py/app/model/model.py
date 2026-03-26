class SistemaDecolagemModel:
    def __init__(self):
        self.limites = {
            "temp_int": (18, 27),
            "temp_ext": (9.5, 35),
            "pressao": (350, 400),
            #Deixei a sugestão em kPa, equivalente a 51 a 57 psia.
            "energia_min": 85,
            "integridade_ok": 1
        }

    def validar_decolagem(self, dados):
        erros = []

        if not (self.limites["temp_int"][0] <= dados['temp_int'] <= self.limites["temp_int"][1]):
            erros.append(f"Temperatura Interna diferente do intervalo seguro ({dados['temp_int']}ºC)")

        if not (self.limites["temp_ext"][0] <= dados['temp_ext'] <= self.limites["temp_ext"][1]):
            erros.append(f"Temperatura Externa diferente do intervalo seguro ({dados['temp_ext']}ºC)")

        if not (self.limites["pressao"][0] <= dados['pressao_tanque'] <= self.limites["pressao"][1]):
            erros.append(f"Pressão dos Tanques fora do limite ({dados['pressao_tanque']})")

        if dados['nivel_energia'] < self.limites["energia_min"]:
            erros.append(f"Energia insuficiente para decolagem ({dados['nivel_energia']}%)")

        if dados['integridade'] != self.limites["integridade_ok"]:
            erros.append("Revise a integridade da estrutura")

        if not dados['modulos_ok']:
            erros.append("Falha grave nos módulos críticos")

        return erros