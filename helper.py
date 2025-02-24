from flask import render_template


def alert(message: str, error_code: int):
    """Renders customizable Error page"""
    return render_template("alert.html", error_code=error_code, message=message)
