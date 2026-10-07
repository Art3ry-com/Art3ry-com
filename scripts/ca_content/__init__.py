from .cities1 import CITIES1
from .cities2 import CITIES2
from .industries import INDUSTRIES
from .combos import COMBOS
from .hub import HUB

ORDER = ["los-angeles", "san-diego", "san-jose", "san-francisco", "sacramento", "fresno",
         "bakersfield", "oakland", "long-beach", "inland-empire", "orange-county"]
CITIES = sorted(CITIES1 + CITIES2, key=lambda c: ORDER.index(c["slug"]))

from .more import MORE
from .more2 import MORE2
from .more3 import FAQ3
for _p in CITIES + INDUSTRIES + COMBOS:
    _p["secs"] = list(_p["secs"]) + list(MORE.get(_p["slug"], [])) + list(MORE2.get(_p["slug"], []))
    if _p["slug"] in FAQ3:
        _p["faq"] = list(_p["faq"]) + [FAQ3[_p["slug"]]]
