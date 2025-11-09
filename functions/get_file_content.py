import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(abs_work, file_path))
    if not (abs_target == abs_work or abs_target.startswith(abs_work + os.sep)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_target, "r") as f:
            content = f.read(MAX_CHARS)
            extra = f.read(1)
            return content + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]' if extra else content
    except Exception as e:
        return f'Error: {e}'