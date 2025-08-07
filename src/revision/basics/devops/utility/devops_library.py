import os
import logging

# Configure logging to write to a file and also print to console
def setup_safe_logging(log_filename, primary_dir="/var/log"):
    """
    Sets up logging to a safe location. Tries to use the primary directory,
    falls back to the current working directory if permission is denied.

    Args:
        log_filename (str): Name of the log file (e.g., "my_script.log").
        primary_dir (str): Preferred directory for logging (default: "/var/log").

    Returns:
        str: Path to the active log file being used.
    """
    primary_path = os.path.join(primary_dir, log_filename)
    fallback_path = os.path.join(os.getcwd(), log_filename)

    try:
        with open(primary_path, "a"):
            pass
        active_path = primary_path
    except PermissionError:
        active_path = fallback_path
        # Delay logging until after handlers are configured

    # Clear existing handlers to prevent duplicate logs
    root_logger = logging.getLogger()
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # Configure file logging
    logging.basicConfig(
        filename=active_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Add console logging
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console.setFormatter(formatter)
    root_logger.addHandler(console)

    # Now it's safe to log fallback message
    if active_path == fallback_path:
        logging.warning(f"Permission denied for {primary_path}. Falling back to {fallback_path}")

    return active_path
