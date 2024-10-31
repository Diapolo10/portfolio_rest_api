"""Global config options of the package."""

import os
from importlib import resources as pkg_resources
from pathlib import Path

from dotenv import load_dotenv

import portfolio_rest_api

load_dotenv()

PACKAGE_NAME = "portfolio_rest_api"

with pkg_resources.as_file(pkg_resources.files(portfolio_rest_api)) as package_dir:
    DEFAULT_CONFIG_FILE_PATH = package_dir / 'logger_config.toml'

LOGGER_CONFIG_FILE = Path(os.environ.get(
    "PORTFOLIO_REST_API_LOGGER_CONFIG_FILE",
    DEFAULT_CONFIG_FILE_PATH,
))
