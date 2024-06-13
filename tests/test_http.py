import pytest
from discord import http


class CustomResponse:
    def __init__(self, text_data, content_type):
        self._text = text_data
        self.headers = {'content-type': content_type}

    async def text(self, encoding='utf-8'):
        return self._text


@pytest.mark.asyncio
async def test_json_or_text():
    # Testing with json data
    response = CustomResponse('{"key": "value"}', 'application/json')
    result = await http.json_or_text(response)
    assert isinstance(result, dict)
    assert result == {"key": "value"}

    # Testing with plain text data
    response = CustomResponse('Hello world!', 'text/plain')
    result = await http.json_or_text(response)
    assert isinstance(result, str)
    assert result == 'Hello world!'
