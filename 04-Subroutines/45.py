def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return None
