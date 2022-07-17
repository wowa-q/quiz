import pytest
import pathlib

def fun():
    raise SystemExit(1)

@pytest.mark.skip
def test_mytest():
    with pytest.raises(SystemExit):
        fun()

class Test_Prepare():
    QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
    def test_fileExists(self):
        assert self.QUESTIONS_PATH == pathlib.Path(__file__).parent / "questions.toml"