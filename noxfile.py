import pathlib

import nox


dependencies = pathlib.Path("requirements.txt").read_text().splitlines()


@nox.session(python=["3.11"])
def buildoc(session):
    session.install(*dependencies)
    session.run(
        "make",
        "html",
    )
