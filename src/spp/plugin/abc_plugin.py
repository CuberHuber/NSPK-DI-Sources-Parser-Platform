from __future__ import annotations

import zipfile
from abc import ABCMeta, abstractmethod
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from spp.plugin.config import Config
    from src.spp.types import ABC_Plugin_Parser, SPP_plugin


class ABC_Plugin(metaclass=ABCMeta):
    """
    Класс, представляющий плагин.
    """
    metadata: SPP_plugin

    parser: ABC_Plugin_Parser | Callable = None
    config: Config

    BASE_PLUGIN_ARCHIVE_DIR_PATH: str  # Абсолютный путь до архива плагинов
    PLUGIN_CATALOG_NAME: str  # Имя каталога плагина. Нужен для проверки на уже существующее имя.
    PARSER_FILENAME: str | None
    PARSER_REPO_FILENAME: str | None  # Имя файла парсера в репозитории
    SPPFILE_REPO_FILENAME: str  # Имя файла конфигурации в репозитории
    zip_repository: zipfile.ZipFile

    @abstractmethod
    def load(self):
        """
        Загружает файлы плагина и извлекает парсер.
        После этого можно
        :return:
        :rtype:
        """
        ...

    @abstractmethod
    def __del__(self):
        """
        Метод вызывается при уничтожении объекта.

        Его задача удалить временный каталог с файлами плагина
        """
        # Требуется удалить каталог этого плагина
        ...

    ...