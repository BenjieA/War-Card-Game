import pytest
import app

def test_house():
        assert len(app.housegen())==5
