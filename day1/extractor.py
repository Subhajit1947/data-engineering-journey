from abc import ABC,abstractmethod
import pandas as pd
from dataclasses import dataclass
import logging
from typing import Callable,Any
import time
from functools import wraps
logger = logging.getLogger(__name__)


class DataSourceError(Exception): ...
class ExtractionError(DataSourceError): ...
class ValidationError(DataSourceError): ...



def retry(max_retries:int=3,delay:float=1,backoff=2):
    """Retry decorator with exponential backoff"""
    def decorator(func:Callable)->Callable:
        @wraps(func)
        def wrapper(*args:Any,**kwargs:Any)->Any:
            last_exception=None
            for attempt in range(1,max_retries+1):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    last_exception=e
                    logger.warning(
                        "Attempt %d/%d failed: %s. Retrying in %.1fs...",
                        attempt,max_retries,e,delay*(backoff**(attempt-1))
                    )
                    time.sleep(delay*(backoff**(attempt-1)))
            raise last_exception
        return wrapper
    return decorator
            

@dataclass
class SourceConfig:
    filepath: str
    encoding: str="utf-8"


class DataSource(ABC):
    def __init__(self,config: SourceConfig):
        self.config=config
    @abstractmethod
    def extract(self)->pd.DataFrame:
        pass
    def validate(self,data:pd.DataFrame)->None:
        """Default validation: check for empty DataFrame."""
        if data.empty:
            raise ValidationError("Extracted DataFrame is empty.")
        logger.info("Validation passed: %d rows, %d columns.", len(data), len(data.columns))

class CSVSource(DataSource):
    @retry(max_retries=3,delay=1,backoff=3)
    def extract(self)->pd.DataFrame:
        try:
            df=pd.read_csv(self.config.filepath,encoding=self.config.encoding)
            logger.info("successfully extracted CSV: %s",self.config.filepath)
            return df
        except FileNotFoundError as e:
            raise ExtractionError(f"CSV file not found: {self.config.filepath}") from e
        except pd.errors.EmptyDataError as e:
            raise ExtractionError("CSV file is empty.") from e
        except Exception as e:
            raise ExtractionError(f"Failed to read CSV: {e}") from e
        
class JSONSource(DataSource):
    @retry(max_retries=3, delay=1, backoff=2)
    def extract(self) -> pd.DataFrame:
        try:
            df = pd.read_json(self.config.filepath, encoding=self.config.encoding)
            logger.info("Successfully extracted JSON: %s", self.config.filepath)
            return df
        except ValueError as e:
            raise ExtractionError(f"Invalid JSON format: {e}") from e
        except FileNotFoundError as e:
            raise ExtractionError(f"JSON file not found: {self.config.filepath}") from e
        except Exception as e:
            raise ExtractionError(f"Failed to read JSON: {e}") from e




