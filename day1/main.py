# -----------------------Task--------------
# Build a Python class-based ETL pipeline simulator

# --------------------Requirements----------------------------
# Create an abstract base class 'DataSource' with methods extract() and validate(). 
# Implement concrete classes CSVSource, JSONSource.
# Add error handling, logging, and type hints. Use dataclasses for configuration.

#----------------------Final Result----------------------------------
# A working Python module with 3+ classes, 
# decorators for retry logic, and a main.py that demonstrates polymorphism.
# Write unit tests with pytest.


# "E:\D_Drive\download\MW-NIFTY-50-28-May-2026.csv"
from extractor import CSVSource,JSONSource,SourceConfig,DataSourceError
import argparse
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger=logging.getLogger(__name__)
SUPPORTED_EXTENSIONS = {
    "csv": CSVSource,
    "json": JSONSource,
}

def main():
    parser=argparse.ArgumentParser(description="ETL Pipeline Simulator")
    parser.add_argument("--filepath",required=True,help="Path to the data file")
    parser.add_argument("--encoding", default="utf-8", help="File encoding")
    args=parser.parse_args()

    ext=args.filepath.rsplit(".",1)[-1].lower()
    if ext not in SUPPORTED_EXTENSIONS:
        logger.error("Unsupported file extension: .%s", ext)
        return
    source_class=SUPPORTED_EXTENSIONS[ext]
    config=SourceConfig(
        filepath=args.filepath,
        encoding=args.encoding
    )
    source=source_class(config)
    try:
        df=source.extract()
        source.validate(df)
        logger.info("Pipeline completed successfully.")
        print(df.head())
    except DataSourceError as e:
        logger.error("Pipeline failed: %s", e)
    except Exception as e:
        logger.exception("Unexpected error: %s", e)
    
if __name__=='__main__':
    main()

