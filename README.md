# Ames Brewers League Website 🍻

http://www.amesbrewersleague.org

## About

This repository includes code for the Ames Brewers League website. The website's purpose is to inform potential new members about the group as well as provide a medium for meeting minutes and competition results to be shared.

Meetings take place monthly and the website is updated when those meeting minutes are available.

## Getting Started

Clone this repository

```shell
git clone https://github.com/ames-brewers-league/ames-brewers-league.github.io.git
```

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

Navigate to the root directory of the repository in your shell.

Copy `config.example.json` as `config.json` at the root of the repository. Update the paths, as needed.

## Data Files

Ensure that the data files and directory referenced in the `config.json` file line up to their location in your file system.

### competitions.json

This file contains all monthly competitions and the associated beer entries.

```json
{
    "date": "2026-10-13",
    "style": "Festbier, marzen, Oktoberfest beer",
    "category": null,
    "bjcp_year": 2021,
    "entries": [
        {
            "brewer": "John Doe",
            "beer": "Munich Dunkel",
            "points": 3.0
        }
    ]
}
```

### Minutes directory

Store PDF files of recorded meeting minutes in this directory. The file structure should mirror the one below. Naming convention is YYYY-MM.pdf.

```
└── minutes
    ├── 2016-01.pdf
    └── 2016-02.pdf
```

### raffle_sponsors.json

This file contains an array of raffle sponsors. An example is shown below.

```json
[
    {
        "name": "Super Awesome Brewing Supply Co.",
        "url": "http://.../",
        "logo_url": "https://.../logo.jpg"
    }
]
```

## Monthly Update

1. Create a PDF of the meeting minutes as YYYY-MM.pdf in the configured minutes directory.
2. Add to or update the `competitions.json` dataset.
3. Generate the HTML updates from the data files: `uv run generate.py`.
4. Commit and push the changes.
5. GitHub Actions will deploy the static site content.
6. Visit http://www.amesbrewersleague.org to confirm the changes.
