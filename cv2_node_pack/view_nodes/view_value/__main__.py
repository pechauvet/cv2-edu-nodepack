def view_value(
    value: int,
    placeholder_text: str = "value = ",
) -> [
    {'name': 'value', 'type': int},
    {'name': 'preview_text', 'type': dict, 'viz': 'side'},
    {'name': 'full_text', 'type': dict, 'viz': 'loop'},
]:
    """
    Show an integer value. This a simplified version of the standard node view_text.
    :param value: the value to show in the node.
    :param placeholder_text: the text to show with the value.
    :return:
    """
    text = placeholder_text + str(value)
    return {
        'value': value,
        'preview_text': {'hint': 'monospaced_text', 'data': text},
        'full_text': {'hint': 'monospaced_text', 'data': text}
    }

### functions used must always be aliased as 'main'
main_callable = view_value



