"""Ports (Protocol interfaces) for S2. Adapters implement these."""

from typing import Protocol

from cropseq.contracts import Location


class SoilProvider(Protocol):
    """Returns the raw soil payload exactly as the upstream API sent it."""

    def fetch(self, location: Location) -> dict: ...


class WeatherProvider(Protocol):
    """Returns the raw weather payload exactly as the upstream API sent it."""

    def fetch(self, location: Location) -> dict: ...
