import wordz

def test_compte_mots():
    counts = wordz.compte_mots(
        ["'Cause I'm a real tough kid, I can handle my shit"]
    )
    assert counts["kid"] == 1
    assert counts["I"] == 1
    assert counts["be"] == 0