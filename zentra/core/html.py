from zentra.core import Component
from zentra.core.base import HTMLTag, JSIterable
from zentra.core.enums.html import HTMLContentTagType
from zentra.nextjs import Image

from pydantic import ConfigDict, field_validator
from pydantic_core import PydanticCustomError


class HTMLContent(HTMLTag):
    """
    A model dedicated to HTML content tags, including `headings`, `paragraphs`, and `span`.

    Parameters:
    - `text` (`string`) - the text inside the tag. Can also include parameters, signified by a `$` at the start of the parameter name. This is useful when using the `Image` inside an `iterable` function like `map`
    - `tag` (`string`) - the type of tag to wrap around the `text` attribute. Valid options: `['h1', 'h2', 'h3', 'h4', 'h5', h6', 'p', 'span']`
    - `styles` (`string, optional`) - the CSS styles to apply to the tag. `None` by default
    """

    text: str
    tag: HTMLContentTagType

    model_config = ConfigDict(use_enum_values=True)

    @property
    def classname(self) -> str:
        return self.tag


class Div(HTMLTag):
    """
    A model dedicated to the `<div>` HTML tag.

    Parameters:
    - `items` (`string | zentra.core.Component | zentra.core.js.JSIterable | list[string | zentra.core.html.HTMLTag | zentra.core.Component | zentra.core.js.JSIterable]`) - Can be either:
      1. A `string` of text. Can include parameter variables (indicated by starting the variable name with a `$`) or be one specifically
      2. Any `zentra.core.Component` model, such as `zentra.ui.control.Label`
      3. Any `zentra.core.js.JSIterable` model, such as `zentra.core.js.Map`
      4. A `list` of a combination of `strings` of text, `zentra.core.html.HTMLTag` models, `zentra.core.js.JSIterable` models, or `zentra.core.Component` models
    - `shell` (`boolean, optional`) - A flag to indicate whether the div should be an empty tag wrapper (`<>`, `</>`). Often used in JSX when a single parent container is needed. `False` by default
    - `key` (`string, optional`) - A unique identifier added to the container. Needed when using JS iterables like `map`. When provided, must be a parameter (start with a `$`). `None` by default
    - `styles` (`string, optional`) - the CSS styles to apply to the tag. `None` by default
    """

    items: str | Component | JSIterable | list[str | HTMLTag | Component | JSIterable]
    shell: bool = False
    key: str = None

    @field_validator("key")
    def validate_key(cls, key: str) -> str:
        if key and not key.startswith("$"):
            raise PydanticCustomError(
                "key_must_be_a_parameter",
                f"'{key}' != '${key}'! Must start with a '$' to set as a parameter\n",
                dict(wrong_value=key),
            )
        return key


class FigCaption(HTMLTag):
    """
    A model dedicated to the `<figcaption>` HTML tag used within the `<figure>` tag.

    Parameters:
    - `text` (`string | zentra.core.html.HTMLContent | list[string | zentra.core.html.HTMLContent]`) - the text to put into the caption. Can either be:
      1. A single or multi-line `string` of text without any tags wrapped around it
      2. A `zentra.core.html.HTMLContent` object for wrapping the text in a `heading`, `paragraph`, or `span` tag
      3. A `list` of combined `string` and `zentra.core.html.HTMLContent` objects for more advanced captions
    - `styles` (`string, optional`) - the CSS styles to apply to the tag. `None` by default

    Example Usage:
    1. Advanced captioning.
    ```python
    from zentra.core.html import FigCaption, HTMLContent

    FigCaption(
        text=[
            'Photo by{" "}',
            HTMLContent(
                tag="span",
                text="{artwork.artist}",
                styles="font-semibold text-foreground",
            ),
        ],
        styles="pt-2 text-xs text-muted-foreground",
    )
    ```
    JSX equivalent ->
    ```jsx
    <figcaption className="pt-2 text-xs text-muted-foreground">
        Photo by{" "}
        <span className="font-semibold text-foreground">
            {artwork.artist}
        </span>
    </figcaption>
    ```
    """

    text: str | HTMLContent | list[str | HTMLContent]


class Figure(HTMLTag):
    """
    A model dedicated to the `<figure>` HTML tag.

    Parameters:
    - `img` (`zentra.nextjs.Image`) - a NextJS `Image` component defining the image to display in the figure
    - `caption` (`zentra.core.html.FigCaption`) - a `FigCaption` component representing the caption of the Image
    - `styles` (`string, optional`) - the CSS styles to apply to the tag. `None` by default
    - `key` (`string, optional`) -A unique identifier added to the figure. Needed if using a JS iterable like `map`. When provided, must be a parameter (start with a `$`). `None` by default
    - `img_container_styles` (`string, optional`) - a string of CSS styles to apply to a `div` tag around the image. When provided, a `div` tag is automatically wrapped around the image with the styles supplied to its `className` attribute. `None` by default

    Example usage:
    1. A detailed figure with variables.
    ```python
    from zentra.core.html import Figure, FigCaption, HTMLContent
    from zentra.nextjs import Image

    Figure(
        img=Image(
            src="$artwork.art",
            alt="Photo by $artwork.artist",
            width=300,
            height=400,
            styles="aspect-[3/4] h-fit w-fit object-cover",
        ),
        caption=FigCaption(
            text=[
                'Photo by{" "}',
                HTMLContent(
                    tag="span",
                    text="$artwork.artist",
                    styles="font-semibold text-foreground",
                )
            ],
            styles="pt-2 text-xs text-muted-foreground",
        ),
        key="$artwork.art",
        img_container_styles="overflow-hidden rounded-md",
    )
    ```
    JSX equivalent ->
    ```jsx
    <figure key={artwork.artist} className="shrink-0">
        <div className="overflow-hidden rounded-md">
            <Image
            src={artwork.art}
            alt={`Photo by ${artwork.artist}`}
            className="aspect-[3/4] h-fit w-fit object-cover"
            width={300}
            height={400}
            />
        </div>
        <figcaption className="pt-2 text-xs text-muted-foreground">
            Photo by{" "}
            <span className="font-semibold text-foreground">
            {artwork.artist}
            </span>
        </figcaption>
    </figure>
    ```
    """

    img: Image
    caption: FigCaption
    key: str = None
    img_container_styles: str = None

    @field_validator("key")
    def validate_key(cls, key: str) -> str:
        if key and not key.startswith("$"):
            raise PydanticCustomError(
                "key_must_be_a_parameter",
                f"'{key}' != '${key}'! Must start with a '$' to set as a parameter\n",
                dict(wrong_value=key),
            )
        return key
