import dataclasses

from typing import List, TypedDict


class ImageData(TypedDict):
    title: str
    url: str
    attribution: str


@dataclasses.dataclass
class PeriodicEntry:
    name: str
    appearance: str
    atomic_mass: float
    boil: float
    category: str
    density: float
    discovered_by: str
    melt: float
    molar_heat: float
    named_by: str
    number: int
    period: int
    group: int
    phase: str
    source: str
    bohr_model_image: str
    bohr_model_3d: str
    spectral_img: str
    summary: str
    symbol: str
    xpos: int
    ypos: int
    wxpos: int
    wypos: int
    shells: List[int]
    electron_configuration: str
    electron_configuration_semantic: str
    electron_affinity: float
    electronegativity_pauling: float
    ionization_energies: List[float]
    cpk_hex: str
    image: ImageData
    block: str

    @staticmethod
    def from_dict(d: dict):
        return PeriodicEntry(
            name=d["name"],
            appearance=d["appearance"],
            atomic_mass=d["atomic_mass"],
            boil=d["boil"],
            category=d["category"],
            density=d["density"],
            discovered_by=d["discovered_by"],
            melt=d["melt"],
            molar_heat=d["molar_heat"],
            named_by=d["named_by"],
            number=d["number"],
            period=d["period"],
            group=d["group"],
            phase=d["phase"],
            source=d["source"],
            bohr_model_image=d["bohr_model_image"],
            bohr_model_3d=d["bohr_model_3d"],
            spectral_img=d["spectral_img"],
            summary=d["summary"],
            symbol=d["symbol"],
            xpos=d["xpos"],
            ypos=d["ypos"],
            wxpos=d["wxpos"],
            wypos=d["wypos"],
            shells=d["shells"],
            electron_configuration=d["electron_configuration"],
            electron_configuration_semantic=d["electron_configuration_semantic"],
            electron_affinity=d["electron_affinity"],
            electronegativity_pauling=d["electronegativity_pauling"],
            ionization_energies=d["ionization_energies"],
            cpk_hex=d["cpk-hex"],
            image=d["image"],
            block=d["block"]
        )
