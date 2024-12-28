from typing import Literal, Optional

from odd_collector_sdk.domain.plugin import Plugin as BasePlugin
from odd_collector_sdk.types import PluginFactory
from pydantic import SecretStr

from odd_collector_clickhouse.domain.predefined_data_source import PredefinedDatasourceParams


class WithPredefinedDataSource:
    predefined_datasource: PredefinedDatasourceParams


class WithHost(BasePlugin):
    host: str


class WithPort(BasePlugin):
    port: str


class DatabasePlugin(WithHost, WithPort):
    database: Optional[str]
    user: str
    password: str


class ClickhousePlugin(DatabasePlugin):
    type: Literal["clickhouse"]
    port: Optional[int]
    password: SecretStr
    secure: bool = False
    verify: bool = True
    server_hostname: Optional[str] = None
    query_limit: Optional[int] = 0


PLUGIN_FACTORY: PluginFactory = {
    "clickhouse": ClickhousePlugin,
}