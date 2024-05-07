from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class GCP_Config:
    gcp_project_id: str = "576452154103"
    gcp_secret_id: str = "MANCITY_token"
    gcp_version_id: str = MISSING


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="GCP_schema", node=GCP_Config, group="infrastucture")
