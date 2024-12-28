from odd_collector_clickhouse.logger import logger


def get_version() -> str:
    try:
        from odd_collector_clickhouse.__version__ import VERSION

        return VERSION
    except Exception as e:
        logger.warning(f"Can't get version from odd_collector.__version__. {e}")
        return "-"
