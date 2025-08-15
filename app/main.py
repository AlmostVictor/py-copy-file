def copy_file(command : str) -> None:
    if "/" in command or "\\" in command:
        return

    parts = command.split()
    if len(parts) == 3:
        cmd, source_file_name, destination_file_name = parts
    else:
        return

    if cmd != "cp" or source_file_name == destination_file_name:
        return

    try:
        with open(parts[1], "r") as source, open(parts[2], "w") as destination:
            destination.write(source.read())
    except FileNotFoundError:
        return
