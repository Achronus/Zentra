from zentra_models.core import Page
from zentra_models.ui import Form, FormField
from zentra_models.ui.control import Input, Switch
from zentra_models.ui.notification import AlertDialog
from zentra_models.ui.presentation import Card
from zentra_models.uploadthing import FileUpload


form_fields = [
    FormField(
        name="agencyLogo",
        label="Agency Logo",
        content=FileUpload(),
    ),
    [
        FormField(
            name="name",
            label="Agency Name",
            content=Input(id="agencyName", type="text", placeholder="Your Agency Name"),
        ),
        FormField(
            name="companyEmail",
            label="Agency Email",
            content=Input(id="email", type="email", placeholder="Email"),
        ),
    ],
    FormField(
        name="companyPhone",
        label="Agency Phone Number",
        content=Input(id="phone", type="tel", placeholder="Phone"),
    ),
    FormField(
        name="whiteLabel",
        label="White Label Mode",
        description="Turning on White label mode will show your agency logo to all sub accounts by default. You can override this behaviour through sub account settings.",
        content=Switch(),
        message=False,
    ),
    FormField(
        name="address",
        label="Address",
        content=Input(id="address", type="text", placeholder="123 st..."),
    ),
    [
        FormField(
            name="city",
            label="City",
            content=Input(id="city", type="text", placeholder="City"),
        ),
        FormField(
            name="state",
            label="State",
            content=Input(id="state", type="text", placeholder="State"),
        ),
        FormField(
            name="zipCode",
            label="Zipcode",
            content=Input(id="zipcode", type="text", placeholder="Zipcode"),
        ),
    ],
]

agency_details = Page(
    name="AgencyDetails",
    components=[
        AlertDialog(
            name="agencyAlertDialog",
            content=[
                Card(
                    name="agencyInfo",
                    title="Agency Information",
                    description="Let's create an agency for your business. You can edit agency settings later from the agency settings tab.",
                    content=[
                        Form(
                            name="agencyForm",
                            fields=form_fields,
                            btn_text="Save Agency Information",
                        ),
                    ],
                ),
            ],
        ),
    ],
)
