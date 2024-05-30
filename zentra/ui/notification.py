from typing import Optional
from zentra.core import Component
from zentra.core.enums.ui import AlertVariant
from zentra.core.html import Div, HTMLContent
from zentra.core.react import LucideIcon, LucideIconWithText
from zentra.ui import ShadcnUi
from zentra.ui.control import Button

from pydantic import Field, PrivateAttr, field_validator

from zentra.validation import check_kebab_case


class Alert(Component, ShadcnUi):
    """
    A Zentra model for the [Shadcn/ui Alert](https://ui.shadcn.com/docs/components/alert) component.

    Parameters:
    - `title` (`string`) - the text for the `AlertTitle`
    - `description` (`string`) - the text for the `AlertDescription`
    - `icon` (`string, optional`) - the name of the [Lucide React Icon](https://lucide.dev/icons). Must be in kebab-case format. E.g., `circle-arrow-down` or `loader`. When provided, adds the icon to the start of the `Alert`. `None` by default
    - `variant` (`string, optional`) - the style of the alert. Valid options: `['default', 'destructive']`. `default` by default
    """

    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    icon: Optional[str] = None
    variant: AlertVariant = "default"

    @property
    def child_names(self) -> list[str]:
        return ["AlertTitle", "AlertDescription"]

    @field_validator("icon")
    def validate_icon(cls, icon: str) -> str:
        return check_kebab_case(icon)


class TextAlertDialog(Component, ShadcnUi):
    """
    A Zentra model for the [Shadcn/ui AlertDialog](https://ui.shadcn.com/docs/components/alert-dialog) component focusing on a text based implementation.

    Looking for something more customizable? Try the `zentra.ui.notification.AlertDialog` model.

    Parameters:
    - `title` (`string`) - the text for the `AlertDialogTitle`
    - `description` (`string`) - the text for the `AlertDialogDescription`
    - `trigger_text` (`string`) - the text to display on the `AlertDialogTrigger` button
    - `cancel_btn_text` (`string, optional`) - the text for the `AlertDialogCancel` button in the `AlertDialogFooter`. `Cancel` by default
    - `cancel_btn_text` (`string, optional`) - the text for the `AlertDialogAction` button in the `AlertDialogFooter`. `Continue` by default

    Example Usage:
    1. A delete account dialog.
    ```python
    from zentra.ui.notification import TextAlertDialog

    TextAlertDialog(
        title="Are you absolutely sure?",
        description="This action cannot be undone. This will permanently delete your account and remove your data from our servers.",
        trigger_text="Delete Account",
    )
    ```
    JSX equivalent ->
    ```jsx
    import { AlertDialog, AlertDialogPortal, AlertDialogOverlay, AlertDialogTrigger, AlertDialogContent, AlertDialogHeader, AlertDialogFooter, AlertDialogTitle, AlertDialogDescription, AlertDialogAction, AlertDialogCancel } from "@/components/ui/text-alert-dialog"

    <AlertDialog>
      <AlertDialogTrigger asChild>
        <Button variant="outline">Delete Account</Button>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
          <AlertDialogDescription>
            This action cannot be undone. This will permanently delete your
            account and remove your data from our servers.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancel</AlertDialogCancel>
          <AlertDialogAction>Continue</AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
    ```
    """

    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    trigger_text: str = Field(min_length=1)
    cancel_btn_text: str = "Cancel"
    action_btn_text: str = "Continue"

    _container_name = PrivateAttr(default="AlertDialog")


class AlertDialog(Component, ShadcnUi):
    """
    A Zentra model for the [Shadcn/ui AlertDialog](https://ui.shadcn.com/docs/components/alert-dialog) component that allows more advanced functionality, such as including inner components.

    Looking for something simple? Try the `zentra.ui.notification.TextAlertDialog` model.

    Parameters:
    - `content` (`list[zentra.core.Component | zentra.core.html.Div | zentra.core.html.HTMLContent]`) - content to add to the `AlertDialogDescription`. Can be a list of a single or combined set of the following:
        1. Any Zentra `Component` model
        2. Zentra `Div` models
        3. Zentra `HTMLContent` models
    - `title` (`string, optional`) - the text for the `AlertDialogTitle`. `None` by default
    - `trigger` (`zentra.ui.control.Button | string, optional`) - the text or `Button` model to display in the `AlertDialogTrigger`. `None` by default
    - `footer` (`list[zentra.core.Component | zentra.core.html.Div | zentra.core.html.HTMLContent]`) - the content to add to the `AlertDialogFooter`. Acts the same as the `content` attribute, but in a different wrapper. `None` by default
    """

    # TODO: add as 'ParentComponent' and use 'demo/agency_details.py' as example

    content: list[Component | Div | HTMLContent]
    title: str = None
    trigger: Button | str = None
    footer: list[Component | Div | HTMLContent] = None

    @property
    def child_names(self) -> list[str]:
        return [
            "AlertDialogPortal",
            "AlertDialogOverlay",
            "AlertDialogTrigger",
            "AlertDialogContent",
            "AlertDialogHeader",
            "AlertDialogFooter",
            "AlertDialogTitle",
            "AlertDialogDescription",
            "AlertDialogAction",
            "AlertDialogCancel",
        ]


class Sonner(Component, ShadcnUi):
    """
    A Zentra model for the [Shadcn/ui Sonner](https://ui.shadcn.com/docs/components/sonner) component.

    Parameters:
    - `name` (`str`) - the name of the component
    """


class Toast(Component, ShadcnUi):
    """
    A Zentra model for the [Shadcn/ui Toast](https://ui.shadcn.com/docs/components/toast) component.

    Parameters:
    - `name` (`str`) - the name of the component
    """


class Tooltip(Component, ShadcnUi):
    """
    A Zentra model for the [Shadcn/ui Tooltip](https://ui.shadcn.com/docs/components/tooltip) component.

    Parameters:
    - `text` (`str`) - the text to display inside the tooltip
    - `trigger` (`zentra.ui.control.Button | zentra.core.react.LucideIcon | zentra.core.react.LucideIconWithText | string`) - An item to apply the tooltip to. Can be either:
      1. A Zentra `Button` model
      2. A Zentra `LucideIcon` model
      3. A Zentra `LucideIconWithText` model
      4. A string of text
    """

    text: str
    trigger: Button | LucideIcon | LucideIconWithText | str

    _container_name = PrivateAttr(default="TooltipProvider")

    @property
    def custom_common_content(self) -> list[str]:
        return ["text"]

    @property
    def child_names(self) -> list[str]:
        return ["TooltipTrigger", "TooltipContent", "TooltipProvider"]
