"""Define schema for competition data. Load competitions from file."""

import datetime as dt
from dataclasses import dataclass


@dataclass(frozen=True)
class Entry:
    """A single brewer's beer submission to a competition."""

    brewer: str
    beer: str | None
    points: float


@dataclass(frozen=True)
class Competition:
    """A monthly brewing competition."""

    date: dt.date
    style: str
    category: str | None
    bjcp_year: int
    entries: list[Entry]


def load(data: list[dict]) -> list[Competition]:
    """Load and compile competition data to create Competition objects"""
    out = []
    for competition in data:
        # Sort entries from most points to least points
        sorted_entries = sorted(
            competition["entries"], key=lambda e: e["points"], reverse=True
        )
        competition = Competition(
            date=dt.date.fromisoformat(competition["date"]),
            style=competition["style"],
            category=competition["category"],
            bjcp_year=competition["bjcp_year"],
            entries=[Entry(**e) for e in sorted_entries],
        )
        out.append(competition)
    return out


def split_competition_list(
    competitions: list[Competition], date: dt.date
) -> tuple[list[Competition], list[Competition]]:
    """Split a list of competitions on a given date.

    Returns:
        tuple[list[Competition], list[Competition]]: Competitions before the
            date (sorted descending) and competitions on or after the date
            (sorted ascending).
    """
    before = []
    after = []
    for comp in competitions:
        if comp.date >= date:
            after.append(comp)
        else:
            before.append(comp)

    before = list(sorted(before, key=lambda c: c.date, reverse=True))
    after = list(sorted(after, key=lambda c: c.date))
    return before, after
