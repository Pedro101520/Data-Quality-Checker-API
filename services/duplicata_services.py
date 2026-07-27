import pandas as pd

class DuplicataService:

    @staticmethod
    def valida(pk, dados):
        df = pd.DataFrame(dados)

        if pk in df.columns:
            count_duplicata = df.duplicated(subset=[pk]).sum()
            return count_duplicata
        else:
            raise ValueError("Pk não encontrada nos dados disponibilizados")