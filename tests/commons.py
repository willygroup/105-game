import os
import shutil
import tempfile


def get_dirname() -> str:
    dirname = os.path.realpath(__file__)
    dirname = os.path.split(dirname)[0]
    return dirname


def prepare_env(suffix):
    return tempfile.mkdtemp("tmp_", suffix)


def restore_env(directory):
    shutil.rmtree(directory, ignore_errors=True)
