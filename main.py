import logging
# Set up basic logging
logging.basicConfig(level=logging.INFO)


def main():
    # Logging examples
    logging.debug("This is a debug message")   # Low-level details
    logging.info("This is an info message")    # General info
    logging.warning("This is a warning")       # Something unexpected
    logging.error("This is an error")          # Serious problem
    logging.critical("This is critical!")      # Very serious error

if __name__ == "__main__":
    main()
