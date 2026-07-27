import pandas as pd
from schemas.duplicata_schema import DuplicataRequest

class DuplicataService:

    @staticmethod
    def valida(pk, dados):
        df = pd.DataFrame(dados)

        count_duplicata = df.duplicated(subset=[pk]).sum()

        return count_duplicata