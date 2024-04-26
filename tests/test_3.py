# search for '## 3' in packages and solve issues

import packages.openai.chat as chat
from unittest.mock import patch

def save_args(self, **kwargs):
    self.kwargs = kwargs

def test_connect():
    args = {"OPENAI_API_KEY": "dummy", "OPENAI_API_HOST": "dummy"}
    with patch("openai.AzureOpenAI.__init__", side_effect=save_args):
        ai = chat.connect(args)
        print(ai)
        assert True

def test_request():
    assert True