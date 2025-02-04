"""Generate the static ABL website using file-based data sources."""

import datetime as dt
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from src import competition, config, leaderboard, minutes, sponsor

PUBLISH_DIR = Path("publish")
TEMPLATE_DIR = Path("templates")
CONFIG_FILE = Path("config.json")


def render(env: Environment, filename: str, **kwargs):
    """Render an HTML template and save it in the publish directory."""
    template = env.get_template(filename)
    html = template.render(**kwargs)
    (PUBLISH_DIR / filename).write_text(html)


def ignore_non_pdf_files(_: str, names: list[str]) -> list[str]:
    return [name for name in names if not name.endswith(".pdf")]


def main():
    conf = config.load(CONFIG_FILE)

    # Clear out existing content from the publish directory.
    shutil.rmtree(PUBLISH_DIR)
    PUBLISH_DIR.mkdir()

    # Copy static resources to the publish one.
    shutil.copytree(TEMPLATE_DIR / "static", PUBLISH_DIR / "static")

    # Copy meeting minutes to the publish directory.
    shutil.copytree(conf.minutes, PUBLISH_DIR / "minutes", ignore=ignore_non_pdf_files)

    # Render HTML files with data.
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    comps = competition.load(conf.competitions, conf.entries)
    history, upcoming = competition.split_competition_list(comps, dt.date.today())
    lboards = leaderboard.create_leaderboards(comps)
    mins = sorted(minutes.load(conf.minutes), key=lambda m: m.date, reverse=True)
    sponsors = sponsor.load(conf.sponsors)
    sponsor_rows = sponsor.batch(sponsors, 3)
    render(env, "index.html")
    render(env, "minutes.html", minutes=mins)
    render(env, "leaderboard.html", leaderboards=lboards)
    render(env, "results.html", competitions=history)
    render(env, "upcoming.html", competitions=upcoming)
    render(env, "raffle.html", sponsor_rows=sponsor_rows)


if __name__ == "__main__":
    main()
