import os

def get_files_info(working_directory, directory="."):
    wd_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, directory))

    if not (target_abs == wd_abs or target_abs.startswith(wd_abs + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_abs):
        return f'Error: "{directory}" is not a directory'

    try:
        lines = []
        for name in os.listdir(target_abs):
                if name.startswith("__"):
                    continue
                full = os.path.join(target_abs, name)
                is_dir = os.path.isdir(full)
                size = os.path.getsize(full)
                lines.append(f' - {name}: file_size={size} bytes, is_dir={is_dir}')
        return "\n".join(lines)
    except Exception as e:
        return f'Error: {e}'