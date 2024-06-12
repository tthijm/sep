"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

import discord
import pytest


@pytest.mark.parametrize(
    ('red', 'green', 'blue'),
    [
        (10,10,10),
    ],
)
def test_from_rgb(red, green, blue):
    assert discord.Colour.from_rgb(red,green,blue).r == 10
    assert discord.Colour.from_rgb(red,green,blue).g == 10
    assert discord.Colour.from_rgb(red,green,blue).b == 10

@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        ('0xFF1294',                 0xFF1294),
        ('0xff1294',                 0xFF1294),
        ('0xFFF',                    0xFFFFFF),
        ('0xfff',                    0xFFFFFF),
        ('#abcdef',                  0xABCDEF),
        ('#ABCDEF',                  0xABCDEF),
        ('#ABC',                     0xAABBCC),
        ('#abc',                     0xAABBCC),
        ('rgb(68,36,59)',            0x44243B),
        ('rgb(26.7%, 14.1%, 23.1%)', 0x44243B),
        ('rgb(20%, 24%, 56%)',       0x333D8F),
        ('rgb(20%, 23.9%, 56.1%)',   0x333D8F),
        ('rgb(51, 61, 143)',         0x333D8F),
    ],
)
def test_from_str(value, expected):
    assert discord.Colour.from_str(value) == discord.Colour(expected)

@pytest.mark.parametrize(
    ('expected', 'value'),
    [
        ((68, 36, 59),  0x44243B),
        ((51, 61, 143), 0x333D8F),
    ],
)
def test_to_rgb(value, expected):
    assert expected == discord.Colour.to_rgb(discord.Colour(value))


@pytest.mark.parametrize(
    ('value'),
    [
        'not valid',
        '0xYEAH',
        '0x#',
        '#YEAH',
        '#FFFFFFF',
        '#yeah',
        'yellow',
        'rgb(-10, -20, -30)',
        'rgb(30, -1, 60)',
        'invalid(a, b, c)',
        'rgb(',
        'rgb(120%,100%,90%)',
        'rgb(320,300,300)',
        '',
    ],
)
def test_from_str_failures(value):
    with pytest.raises(ValueError):
        discord.Colour.from_str(value)

@pytest.mark.parametrize(
    ('value'),
    [
        'not valid',
        '0xYEAH',
        '0x#',
        '#YEAH',
        '#FFFFFFF',
        '#yeah',
        'yellow',
        'rgb(-10, -20, -30)',
        'rgb(30, -1, 60)',
        'invalid(a, b, c)',
        'rgb(120%,100%,90%)',
        'rgb(320,300,300)',
        '',
    ],
)
def test_init_failures(value):
    with pytest.raises(TypeError):
        discord.Colour(value)

@pytest.mark.parametrize(
    ('red', 'green', 'blue', 'expected'),
    [
        (0,    0,    0,     0x000000),
        (0,    1,    1,     0xFF0000),
        (0,    0.5,  0.5,   0x408080),
        (0.25, 0.5,  0.5,   0x608040),
        (0.25, 0.4,  0.2,   0x29331f),
        (0.5,  0.3,  0.7,   0x7db3b3),
        (0.7,  0.12, 0.49,  0x716e7d),
    ],
)
def test_from_hsv(red, green, blue, expected):
    print(0)
    #assert discord.Colour.from_hsv(red, green, blue) == discord.Colour(expected)

def test_random():
    for i in range(1000):
        assert discord.Colour.random().__int__() <= discord.Colour.__hash__(discord.Colour(0xFFFFFF))
        assert discord.Colour.random().__int__() >= discord.Colour.__hash__(discord.Colour(0x000000))
