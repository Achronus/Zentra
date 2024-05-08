from cli.templates.ui.attributes import alt_attribute, src_attribute

from zentra.core import Component
from zentra.core.base import JSIterable
from zentra.core.html import Div
from zentra.core.react import LucideIcon
from zentra.ui.control import (
    Checkbox,
    Collapsible,
    InputOTP,
    RadioButton,
    RadioGroup,
    ScrollArea,
    Select,
    SelectGroup,
)
from zentra.ui.notification import Alert, TextAlertDialog, Tooltip
from zentra.ui.presentation import Avatar


def param_reformat_helper(text: str) -> list[str]:
    """A helper function to reformat a string of text with parameter values. Returns the new version as a list of strings."""
    new_text = []
    for word in text.split(" "):
        if word:
            if word.startswith("$"):
                new_text.append(f"{{{word[1:]}}}")
            else:
                new_text.append(word)

    return [" ".join(new_text)]


def div_content(div: Div) -> Component | JSIterable | list:
    """Returns the required format for Div content based on the components attributes. For example, if `div.items` is a string, it converts it to a list and reformats its `parameter` values if required. If no formatting is required, will return the `Component` model, `JSIterable` model, or `list` of items provided."""
    if isinstance(div.items, str):
        return param_reformat_helper(div.items)

    return div.items


def checkbox_content(cb: Checkbox) -> list[str]:
    """Returns a list of strings for the Checkbox content based on the components attributes."""
    content = [
        '<div className="grid gap-1.5 leading-none">',
        f'<label htmlFor="{cb.id}" className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">',
        f"{cb.label}",
        "</label>",
    ]

    if cb.more_info:
        content.extend(
            ['<p className="text-sm text-muted-foreground">', cb.more_info, "</p>"]
        )

    content.append("</div>")
    return content


def collapsible_content(comp: Collapsible) -> list[str]:
    """Returns a list of strings for the Collapsible content based on the components attributes."""
    content = [
        '<div className="flex items-center justify-between space-x-4 px-4">',
        '<h4 className="text-sm font-semibold">',
        comp.title,
        "</h4>",
        "<CollapsibleTrigger asChild>",
        '<Button variant="ghost" size="sm" className="w-9 p-0">',
        '<ChevronsUpDown className="h-4 w-4" />',
        '<span className="sr-only">',
        "Toggle",
        "</span>",
        "</Button>",
        "</CollapsibleTrigger>",
        "</div>",
        '<div className="rounded-md border px-4 py-3 font-mono text-sm">',
        comp.items[0],
        "</div>",
        '<CollapsibleContent className="space-y-2">',
    ]

    if len(comp.items) > 1:
        for item in comp.items[1:]:
            content.extend(
                [
                    '<div className="rounded-md border px-4 py-3 font-mono text-sm">',
                    item,
                    "</div>",
                ]
            )

    content.append("</CollapsibleContent>")
    return content


def radio_button_content(rb: RadioButton) -> list[str]:
    """Returns a list of strings for the RadioButton content based on the components attributes."""
    return [
        '<div className="flex items-center space-x-2">',
        f'<RadioGroupItem value="{rb.value}" id="{rb.id}" />',
        f'<Label htmlFor="{rb.id}">',
        rb.text,
        "</Label>",
        "</div>",
    ]


def radio_group_content(rg: RadioGroup) -> list[str]:
    """Returns a list of strings for the RadioGroup content based on the components attributes."""
    content = []
    for rb in rg.items:
        content.extend(radio_button_content(rb))

    return content


def scroll_area_content(sa: ScrollArea) -> list[str]:
    """Returns a list of strings for the ScrollArea content based on the components attributes."""
    return [f'<ScrollBar orientation="{sa.orientation}" />']


def select_content(select: Select) -> list[str]:
    """Returns a list of strings for the Select content based on the components attributes."""
    content = [
        f'<SelectTrigger className="w-[{select.box_width}px]">',
        f'<SelectValue placeholder="{select.display_text}" />',
        "</SelectTrigger>",
    ]

    if isinstance(select.groups, SelectGroup):
        select.groups = [select.groups]

    group_content = []
    for group in select.groups:
        group_content.extend(
            ["<SelectGroup>", f"<SelectLabel>{group.label}</SelectLabel>"]
        )
        for item in group.items:
            group_content.append(
                f'<SelectItem value="{item[0]}">{item[1]}</SelectItem>'
            )
        group_content.append("</SelectGroup>")

    if len(select.groups) == 1 and not select.show_label:
        group_content.pop()
        group_content.pop(0)
        group_content.pop(0)

    content.extend(group_content)
    return content


def alert_content(alert: Alert) -> list[str]:
    """Returns a list of strings for the Alert content based on the components attributes."""
    content = [
        "<AlertTitle>",
        alert.title,
        "</AlertTitle>",
        "<AlertDescription>",
        alert.description,
        "</AlertDescription>",
    ]

    if alert.icon:
        content.insert(0, LucideIcon(name=alert.icon).content_str)

    return content


def text_alert_dialog_content(ad: TextAlertDialog) -> list[str]:
    """Returns a list of strings for the TextAlertDialog content based on the components attributes."""
    return [
        "<AlertDialogTrigger asChild>",
        '<Button variant="outline">',
        ad.trigger_text,
        "</Button>",
        "</AlertDialogTrigger>",
        "<AlertDialogContent>",
        "<AlertDialogHeader>",
        "<AlertDialogTitle>",
        ad.title,
        "</AlertDialogTitle>",
        "<AlertDialogDescription>",
        ad.description,
        "</AlertDialogDescription>",
        "</AlertDialogHeader>",
        "<AlertDialogFooter>",
        "<AlertDialogCancel>",
        ad.cancel_btn_text,
        "</AlertDialogCancel>",
        "<AlertDialogAction>",
        ad.action_btn_text,
        "</AlertDialogAction>",
        "</AlertDialogFooter>",
        "</AlertDialogContent>",
    ]


def tooltip_content(tt: Tooltip) -> list[str]:
    """Returns a list of strings for the Tooltip content based on the components attributes."""
    return [
        "<TooltipTrigger asChild>",
        "</TooltipTrigger>",
        "<TooltipContent>",
        f"<p>{tt.text}</p>",
        "</TooltipContent>",
    ]


def avatar_content(avatar: Avatar) -> list[str]:
    """Returns a list of strings for the Avatar content based on the components attributes."""
    src = src_attribute(avatar.src)
    alt = alt_attribute(avatar.alt)

    return [
        f"<AvatarImage {src} {alt} />",
        f"<AvatarFallback>{avatar.fallback_text}</AvatarFallback>",
    ]


def input_otp_content(otp: InputOTP) -> list[str]:
    """Returns a list of strings for the Avatar content based on the components attributes."""
    content = []

    slot_group_size = otp.num_inputs // otp.num_groups
    slot_idx = 0

    group_tag = "InputOTPGroup>"

    for group_idx in range(otp.num_groups):
        content.append(f"<{group_tag}")
        for _ in range(slot_group_size):
            content.append(f"<InputOTPSlot index={{{slot_idx}}} />")
            slot_idx += 1
        content.append(f"</{group_tag}")

        if otp.num_groups > 1 and group_idx + 1 != otp.num_groups:
            content.append("<InputOTPSeparator />")

    return content


def text_content(text: str | list[str]) -> list[str]:
    """Returns a list of strings of text content with variable preprocessing
    (if required) or a HTMLContent model."""
    if isinstance(text, str):
        return param_reformat_helper(text)

    return text
