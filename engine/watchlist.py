"""Parser watchlist.txt + konvensi nama file data."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


@dataclass(frozen=True)
class Item:
    market: str
    symbol: str
    timeframe: str
    strategy: str = "auto"

    @property
    def key(self) -> str:
        return f"{self.market}__{self.symbol.replace('/', '-').replace(':', '_')}__{self.timeframe}"

    @property
    def csv_path(self) -> Path:
        return DATA_DIR / f"{self.key}.csv"


def read_watchlist(path: Path | str = ROOT / "watchlist.txt") -> list[Item]:
    items, errors = [], []
    for ln, line in enumerate(Path(path).read_text().splitlines(), 1):
        s = line.split("#", 1)[0].strip()
        if not s:
            continue
        parts = s.split()
        if len(parts) < 3:
            errors.append(f"baris {ln}: butuh 'market simbol timeframe' -> '{line}'")
            continue
        market, symbol, tf = parts[0].lower(), parts[1].upper(), parts[2].lower()
        strat = parts[3].lower() if len(parts) > 3 else "auto"
        if market not in ("crypto_spot", "crypto_perp", "idx"):
            errors.append(f"baris {ln}: market '{market}' tidak dikenal")
            continue
        if market == "idx" and tf != "1d":
            errors.append(f"baris {ln}: idx hanya mendukung 1d")
            continue
        if market != "idx" and tf not in ("4h", "1d"):
            errors.append(f"baris {ln}: crypto mendukung 4h atau 1d")
            continue
        items.append(Item(market, symbol, tf, strat))
    if errors:
        print("PERINGATAN watchlist:\n  " + "\n  ".join(errors))
    return items
