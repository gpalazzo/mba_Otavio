# -*- coding: utf-8 -*-
"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from itaete_buy_prop.pipelines import (
    analise_fin_pipeline,
    fx_pipeline,
    logreg_pipeline,
    master_table_pipeline,
    origem_receita_frota_pipeline,
    quali_clientes_crm_pipeline,
    spine_pipeline,
    yfinance_pipeline,
)


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {"__default__": pipeline([spine_pipeline() +
                                     quali_clientes_crm_pipeline() +
                                     origem_receita_frota_pipeline() +
                                     analise_fin_pipeline() +
                                     fx_pipeline() +
                                     yfinance_pipeline() +
                                     master_table_pipeline() +
                                     logreg_pipeline()])}
