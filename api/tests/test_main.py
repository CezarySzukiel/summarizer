import random

from src.main import add


def test_main(monkeypatch):
    def fake_randint(a, b):
        return 39
    monkeypatch.setattr(random, "randint", fake_randint)

    assert add(1, 2) == 42