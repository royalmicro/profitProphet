def convert_path_to_module(path: str):
    path = path.replace("/", ".").replace(".py", "")
    cleaned_path = path.lstrip(".")
    return cleaned_path


def split_and_capitalize(input_string, split_by: str = "_"):
    substrings = input_string.split(split_by)
    capitalized_substrings = [substring.capitalize() for substring in substrings]
    return "".join(capitalized_substrings)
