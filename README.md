## OpenDataDiscovery collector for ClickHouse

This collector is designed to collect metadata from ClickHouse databases. Based on the [OpenDataDiscovery SDK](https://github.com/opendatadiscovery/odd-collectors/tree/main/odd-collector-sdk).

## Usage

Modify example config from `config_example/collector_config.yaml` and run the collector:

```bash
docker run -v $(pwd)/collector_config.yaml:/app/collector_config.yaml ghcr.io/akurdyukov/odd-collector-clickhouse:latest
```
