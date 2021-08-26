import numpy as np
import pandas as pd
from sqlalchemy import create_engine, exc
from sqlalchemy.types import String
from django.core.exceptions import ValidationError
from .. import models

def excelFileHandler(file, user):
    try:
        df = pd.read_excel(file, sheet_name="Sheet1")
    except ValueError:
        return []
    # Removes empty rows and columns
    df = df.dropna(axis=1, how="all")
    df = df.dropna(how="all")
    if len(df.columns) != 7:
        return []
    df.columns=["date", "best_of", "deck_title", "nb_wins", "nb_losses", "colors", "expansion_id"]
    draft_results = []
    exp_codes = []
    for expansion in models.Expansion.objects.all():
        exp_codes.append(expansion.code)
    for i in range(len(df.index)):
        row = df.iloc[i]
        if row["expansion_id"] in exp_codes:
            expansion_id = models.Expansion.objects.get(code=row["expansion_id"]).id
        else:
            return []
        new_result = models.DraftResult(
            date=row["date"],
            best_of=row["best_of"],
            deck_title=row["deck_title"],
            nb_wins=row["nb_wins"],
            nb_losses=row["nb_losses"],
            colors=row["colors"],
            expansion_id=expansion_id,
            user_id=user.id
            )
        try:
            new_result.full_clean()
            draft_results.append(new_result)
        except ValidationError as e:
            draft_results = []
            break
    return draft_results