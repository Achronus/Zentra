from cli.conf.storage import ComponentDetails
from cli.templates.builders import add_to_storage
from cli.templates.storage import JSXComponentContentStorage, JSXComponentExtras

from cli.templates.ui.mappings.storage import JSIterableMappings
from cli.templates.utils import str_to_list
from zentra.core import Component
from zentra.core.base import HTMLTag, JSIterable
from zentra.nextjs import NextJs


class JSIterableBuilder:
    """A builder for creating Zentra `JSIterable` model content as JSX."""

    def __init__(
        self,
        model: JSIterable,
        mappings: JSIterableMappings,
        details_dict: dict[str, ComponentDetails],
    ) -> None:
        self.model = model
        self.maps = mappings
        self.details_dict = details_dict

        self.comp_storage = JSXComponentExtras()

    def build_component(
        self, component: Component, full_shell: bool = False
    ) -> tuple[list[str], JSXComponentContentStorage]:
        """Creates the JSX for a `Component` model and returns its details as a tuple in the form of `(content, comp_storage)`."""
        from cli.templates.builders.component import ComponentBuilder

        builder = ComponentBuilder(
            component=component,
            mappings=self.maps.component,
            details=self.details_dict[component.classname],
        )
        builder.build(full_shell=full_shell)
        return str_to_list(builder.storage.content), builder.storage

    def build_nextjs_component(
        self, component: Component
    ) -> tuple[list[str], JSXComponentContentStorage]:
        """Creates the JSX for a `NextJS` model and returns its details as a tuple in the form of `(content, comp_storage)`."""
        from cli.templates.builders.nextjs import NextJSComponentBuilder

        nextjs = NextJSComponentBuilder(
            component=component,
            mappings=self.maps.component,
        )
        nextjs.build()
        return str_to_list(nextjs.storage.content), nextjs.storage

    def build_html_tag(self, model: HTMLTag) -> tuple[list[str], JSXComponentExtras]:
        """Creates the JSX for a `HTMLTag` model and returns its details as a tuple in the form of `(content, multi_comp_storage)`."""
        from cli.templates.builders.html import HTMLBuildController

        builder = HTMLBuildController(
            model=model,
            mappings=self.maps.html,
            details_dict=self.details_dict,
        )
        content, storage = builder.build()
        return content, storage

    def build(self) -> list[str]:
        """Builds the content for the JSX iterable and returns it as a list of strings. If the the content inside is a component, also stores its information in `self.storage`."""
        start, end = self.get_container()
        inner_model: HTMLTag | Component = self.model.content

        if isinstance(inner_model, HTMLTag):
            content, storage = self.build_html_tag(inner_model)
            self.comp_storage = add_to_storage(self.comp_storage, storage, extend=True)

        elif isinstance(inner_model, NextJs):
            content, storage = self.build_nextjs_component(inner_model)
            self.comp_storage = add_to_storage(self.comp_storage, storage)

        else:
            try:
                content, storage = self.build_component(inner_model)
                self.comp_storage = add_to_storage(self.comp_storage, storage)
            except AttributeError:
                raise AttributeError(
                    f"'JSIterableContentBuilder.build(details=None)'. Missing 'ComponentDetails' for provided '{inner_model.classname}' Component",
                )

        return [start, *content, end]

    def get_container(self) -> tuple[str, str]:
        """Creates the outer shell of the iterable and returns it in the form of `(start, end)`."""
        start = (
            "{"
            + f"{self.model.obj_name}.{self.model.classname}(({self.model.param_name}) => ("
        )
        end = "))}"
        return start, end
