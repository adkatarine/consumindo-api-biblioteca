def helper_convert(obras: list) -> list:
    if obras:
        for obra in obras:
            obra["authors"] = ", ".join(obra["authors"])
        return obras
    return obras
