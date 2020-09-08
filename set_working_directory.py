"""sets as working directory the parent of data/

Assumes this file is distributed inside TIB_ROOT/doc directory"""
import os
import pathlib

project = "Topics in Bioinformatics"
copyright = "2020, Gavin Huttley"
author = "Gavin Huttley"

release = "2020"


def get_parent_data_dir():
    """returns path to doc data directory parent"""
    current = pathlib.Path(__file__).absolute().parent
    data_paths = []
    for path in current.glob("**/*data*"):
        if any(part.startswith(".") for part in path.parts):
            continue
        if path.is_dir() and path.name == "data":
            data_paths.append(path)

    if len(data_paths) == 0:
        raise RuntimeError(f"could not find data dir from {current}")

    if len(data_paths) > 1:
        raise RuntimeError(f"too many data dirs {data_paths}")

    return data_paths[0].parent


data_dir = get_parent_data_dir()
os.chdir(data_dir)
