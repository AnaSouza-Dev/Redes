"""Modelos de dados Pydantic para retorno da API"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Representa a saúde do endpoint payload."""

    ok: bool
    now: int


class SummaryBin(BaseModel):
    """Volume de tráfego agregado por cliente em um bin de tempo"""

    ts: int
    client_ip: str
    in_bytes: int
    out_bytes: int


class SummaryResponse(BaseModel):
    """Modelo de resposta para o endpoint de resumo de tráfego"""

    bins: List[SummaryBin]


class DrilldownItem(BaseModel):
    """Detalhes de agregação em nível de protocolo
    """

    protocol: str
    in_bytes: int
    out_bytes: int


class DrilldownResponse(BaseModel):
    """Modelo de Resposta para informação drill-down."""

    ts: int
    client_ip: str
    items: List[DrilldownItem]


class JsonDataRequest(BaseModel):
    """Modelo de requisição para dados JSON recebidos via FTP"""
    
    client_id: str
    timestamp: int
    data_type: str
    payload: Dict[str, Any]
    file_size: int


class JsonDataResponse(BaseModel):
    """Modelo de resposta para o processamento de dados JSON"""
    
    received: bool
    processed_at: int
    client_id: str
    file_size: int
    message: str


