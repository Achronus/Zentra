from functools import reduce
from itertools import product
from operator import mul

import pytest
from pydantic import ValidationError

from tests.mappings.helper import builder
from tests.mappings.ui_attributes import BTN_VALID_ATTRS, ICON_BTN_VALID_ATTRS
from tests.mappings.ui_content import ICON_BTN_VALID_CONTENT
from zentra.core import Icon
from zentra.core.enums.ui import (
    ButtonIconPosition,
    ButtonSize,
    ButtonVariant,
    IconButtonSize,
)
from zentra.ui.control import Button, IconButton


@pytest.fixture
def example_btn_values() -> dict:
    return {
        "text": "test",
        "url": "https://example.com/",
        "variants": [variant.value for variant in ButtonVariant],
        "sizes": [size.value for size in ButtonSize],
        "disables": [True, False],
    }


def calc_valid_total(*iterables) -> int:
    return reduce(mul, (len(iterable) for iterable in iterables))


class TestButton:
    @staticmethod
    def test_attr_str_valid(example_btn_values):
        variants = example_btn_values["variants"]
        sizes = example_btn_values["sizes"]
        disables = example_btn_values["disables"]

        valid_total = 0
        desired_total = calc_valid_total(variants, sizes, disables)

        for idx, (variant, size, disabled) in enumerate(
            product(variants, sizes, disables)
        ):
            btn = Button(
                text=example_btn_values["text"],
                url=example_btn_values["url"],
                variant=variant,
                size=size,
                disabled=disabled,
            )
            attr_str = btn.attr_str()
            result = builder(btn).attr_str

            if (attr_str == BTN_VALID_ATTRS[idx]) and (attr_str == result):
                valid_total += 1

        assert valid_total == desired_total, f"{valid_total}/{desired_total}"

    @staticmethod
    def test_content_str_valid():
        btn = Button(text="test")

        content_str = btn.content_str()
        result = builder(btn).content_str

        assert content_str == result, (result, content_str)

    @staticmethod
    def test_text_empty_str():
        with pytest.raises(ValidationError):
            Button(text="")

    @staticmethod
    def test_invalid_variant():
        with pytest.raises(ValidationError):
            Button(text="test", variant="test")

    @staticmethod
    def test_invalid_size():
        with pytest.raises(ValidationError):
            Button(text="test", size="test")

    @staticmethod
    def test_invalid_url():
        with pytest.raises(ValidationError):
            Button(text="test", url="not a url")


class TestIconButton:
    @pytest.fixture
    def example_values(self, example_btn_values) -> dict:
        values = {
            "icon": Icon(name="test"),
            "icon_positions": [pos.value for pos in ButtonIconPosition],
            **example_btn_values,
        }
        values["size"] = [size.value for size in IconButtonSize]
        return values

    @staticmethod
    def test_attr_str_valid(example_values):
        icon_positions = example_values["icon_positions"]
        variants = example_values["variants"]
        sizes = example_values["sizes"]
        disables = example_values["disables"]

        valid_total = 0
        desired_total = calc_valid_total(icon_positions, variants, sizes, disables)

        for idx, (position, variant, size, disabled) in enumerate(
            product(icon_positions, variants, sizes, disables)
        ):
            btn = IconButton(
                icon=example_values["icon"],
                icon_position=position,
                text=example_values["text"],
                url=example_values["url"],
                variant=variant,
                size=size,
                disabled=disabled,
            )
            attr_str = btn.attr_str()
            result = builder(btn).attr_str

            if (attr_str == ICON_BTN_VALID_ATTRS[idx]) and (attr_str == result):
                valid_total += 1

        assert valid_total == desired_total, f"{valid_total}/{desired_total}"

    @staticmethod
    def test_content_str_valid(example_values):
        positions = example_values["icon_positions"]

        valid_total = 0
        desired_total = len(positions)

        for idx, position in enumerate(positions):
            btn = IconButton(
                icon=example_values["icon"],
                icon_position=position,
                text=example_values["text"],
            )
            content_str = btn.content_str()
            result = builder(btn).content_str

            if (content_str == ICON_BTN_VALID_CONTENT[idx]) and (content_str == result):
                valid_total += 1

        assert valid_total == desired_total, f"{valid_total}/{desired_total}"

    @staticmethod
    def test_icon_empty():
        with pytest.raises(ValidationError):
            IconButton(icon="")

    @staticmethod
    def test_invalid_variant():
        with pytest.raises(ValidationError):
            IconButton(icon=Icon(name="test"), variant="test")

    @staticmethod
    def test_invalid_size():
        with pytest.raises(ValidationError):
            IconButton(icon=Icon(name="test"), size="test")

    @staticmethod
    def test_invalid_url():
        with pytest.raises(ValidationError):
            IconButton(icon=Icon(name="test"), url="not a url")
