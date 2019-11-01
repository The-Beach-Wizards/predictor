import navigator


def test_getPythonHomepage():
    assert navigator.getPythonHomepage()


def test_getPythonGetsCorrectSite():
    assert "The official home of the Python Programming Language" in navigator.getPythonHomepage()
