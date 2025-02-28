import polars as pl
from pathlib import Path


def get_cols(csv_file, *cols) -> pl.DataFrame:
    """Pega colunas de um arquivo csv e filtra os nulos"""
    df = pl.read_csv(csv_file)
    new_df = df.select(*cols).drop_nulls()

    return new_df


def test_validate_csv(tmpdir: Path):
    # Arrage (file.csv, populado, com N colunas)
    f = tmpdir / 'temp.csv'

    data = (
        "nome,email,telefone\n"
        "eduardo,duno@ssauro,929292827\n"
        "fasuto,fasuto@ssauro,92928237\n"
        "kirb,,92928237\n"
        "dejair,deja@ir.net,\n"
    )

    f.write_text(data,encoding='utf-8')

    # act
    get_cols(str(f), 'nome', 'email')
