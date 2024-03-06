import sys
from typing import Callable
from .base_module import BaseModule

from .modules import \
    DownloadDocumentsWithDB, \
    FilterOnlyNewDocumentWithDB, \
    WebDriver, \
    DownloadDocumentsWithParserMethods, \
    DownloadDocumentsThroughSeleniumTemp, \
    WebInstallerDriver, \
    ExtractTextFromFile, \
    UploadDocumentToDB, \
    TimezoneSafeControl, \
    CutJunkCharactersFromDocumentText, \
    SaveDocumentToDB

__all__ = [
    "BaseModule",
    "get_module_by_name",
    "DownloadDocumentsWithDB",
    "FilterOnlyNewDocumentWithDB",
    "WebDriver",
    "DownloadDocumentsWithParserMethods",
    "DownloadDocumentsThroughSeleniumTemp",
    "WebInstallerDriver",
    "ExtractTextFromFile",
    "UploadDocumentToDB",
    "TimezoneSafeControl",
    "CutJunkCharactersFromDocumentText",
    "SaveDocumentToDB",
]


def get_module_by_name(modulename: str) -> Callable:
    """

    :rtype: object
    """
    # Добавить обработку исключений
    if modulename in __all__:
        return getattr(sys.modules[__name__], modulename)
    raise NotImplemented
