# Labric Python SDK

The official Python library for the [Labric](https://labric.co) API.
Full documentation is available at [docs.labric.co](https://docs.labric.co).

## Installation

```bash
pip install labric
```

## Usage

```python
from labric import Labric

client = Labric()  # reads LABRIC_API_KEY from the environment
# or pass the API key explicitly: Labric(api_key="lbk_...")

client.tools.write(
    target_name="samples",
    target_type="table",
    data=[{"sample_id": "S-001", "status": "received"}],
    mode="create",
)
```

An async client is also available:

```python
from labric import AsyncLabric
```

See the [API reference](https://docs.labric.co/api-reference) for the full list of
methods and types.

## Support

- [Documentation](https://docs.labric.co)
- [Issues](https://github.com/Labric-Platforms/py-sdk/issues)

## Contributing

This SDK is largely generated code. See
[CONTRIBUTING.md](https://github.com/Labric-Platforms/py-sdk/blob/main/CONTRIBUTING.md)
for how it is generated and released.
