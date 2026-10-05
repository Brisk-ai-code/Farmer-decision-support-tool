"""S2 environment: fetch raw soil + weather (fixture-backed via adapters)."""

from cropseq.config import config
from cropseq.contracts import Location, RawEnvironment

from .adapters.fake import FakeSoilProvider, FakeWeatherProvider
from .fixture import load_fixture
from .ports import SoilProvider, WeatherProvider


def _soil_provider() -> SoilProvider:
    name = config.adapters["soil"]
    if name == "fake":
        return FakeSoilProvider()
    raise NotImplementedError(
        f"Soil adapter '{name}' is not implemented yet. Create "
        f"'src/cropseq/stages/s2_environment/adapters/{name}.py' and register "
        "it in _soil_provider() in src/cropseq/stages/s2_environment/service.py."
    )


def _weather_provider() -> WeatherProvider:
    name = config.adapters["weather"]
    if name == "fake":
        return FakeWeatherProvider()
    raise NotImplementedError(
        f"Weather adapter '{name}' is not implemented yet. Create "
        f"'src/cropseq/stages/s2_environment/adapters/{name}.py' and register "
        "it in _weather_provider() in src/cropseq/stages/s2_environment/service.py."
    )


def run(location: Location) -> RawEnvironment:
    """Fetch raw soil + weather payloads for the farm location.

    Metadata (fetched_at, warnings, source) comes from the fixture so the
    stub output equals s2_output.json exactly.
    """
    data = load_fixture()
    return RawEnvironment(
        soil_raw=_soil_provider().fetch(location),
        weather_raw=_weather_provider().fetch(location),
        fetched_at=data["fetched_at"],
        warnings=data["warnings"],
        source=data["source"],
    )
