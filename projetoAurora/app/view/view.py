class TerminalView:
    @staticmethod
    def coletar_dados():
        print("\n" + "="*30)
        print("  SISTEMA DE VERIFICAÇÃO - DECOLAGEM")
        print("="*30)
        try:
            return {
                'temp_int': float(input("Temperatura Interna (ºC): ")),
                'temp_ext': float(input("Temperatura Externa (ºC): ")),
                'pressao_tanque': float(input("Pressão dos Tanques (kPa): ")),
                'nivel_energia': float(input("Nível de Energia (%): ")),
                'integridade': int(input("Integridade (1=OK / 0=FALHA): ")),
                'modulos_ok': input("Módulos Críticos OK? (s/n): ").lower().startswith('s')
            }
        except ValueError:
            return None

    @staticmethod
    def exibir_resultado(sucesso, falhas=None):
        if sucesso:
            print("\n" + "#"*25)
            print("  PRONTO PARA DECOLAR")
            print("#"*25)
        else:
            print("\n" + "!"*25)
            print("  DECOLAGEM ABORTADA")
            print("!"*25)
            if falhas:
                print("\nMOTIVOS DO CANCELAMENTO:")
                for erro in falhas:
                    print(f" -> {erro}")