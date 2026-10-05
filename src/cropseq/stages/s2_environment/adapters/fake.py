"""Working fake adapters for S2: payloads come from the stage fixture."""

from cropseq.contracts import Location

from ..fixture import load_fixture


class FakeSoilProvider:
    """Serves the soil payload stored in s2_output.json."""

    def fetch(self, location: Location) -> dict:
        # TODO: replace with a real SoilGrids call.
        return load_fixture()["soil_raw"]


class FakeWeatherProvider:
    """Serves the weather payload stored in s2_output.json."""

    def fetch(self, location: Location) -> dict:
        # TODO: replace with a real Open-Meteo call.
        return load_fixture()["weather_raw"]
