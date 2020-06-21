# This file is part of whatsthis. See LICENSE file for license information.
"""Test __init__.py."""

from whatsthis import __features__, __version__


def test_features():
    """Verify features is a valid JSON string."""
    assert __features__
    assert isinstance(__features__, dict)
    assert "subcommands" in __features__
    assert "probes" in __features__


def test_version():
    """Verify version returns and in correct format."""
    assert __version__
    assert isinstance(__version__, str)
    assert "." in __version__