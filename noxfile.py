import pathlib

import nox


dependencies = pathlib.Path("requirements.txt").read_text().splitlines()


@nox.session(python=["3.9"])
def buildoc(session):
    py_version = session.python.replace(".", "")
    session.install(*dependencies)
    session.run(
        "make",
        "html",
    )


