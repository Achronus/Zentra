VALID_IMPORTS = {
    # CONTROL COMPONENTS
    "button": {
        "simple": 'import { Button } from "@/components/ui/button"',
        "icon": 'import { Button } from "@/components/ui/button"\nimport { Loader } from "lucide-react"',
        "icon_url": '''import Link from 'next/link'\nimport { Button } from "@/components/ui/button"\nimport { Loader } from "lucide-react"''',
    },
    "calendar": 'import { Calendar } from "@/components/ui/calendar"\nimport { useState } from "react"',
    "checkbox": 'import { Checkbox } from "@/components/ui/checkbox"',
    "collapsible": 'import { Collapsible, CollapsibleTrigger, CollapsibleContent } from "@/components/ui/collapsible"\nimport { useState } from "react"\nimport { Button } from "@/components/ui/button"\nimport { ChevronsUpDown } from "lucide-react"',
    "input": 'import { Input } from "@/components/ui/input"',
    "input_otp": {
        "standard": 'import { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator } from "@/components/ui/input-otp"',
        "pattern": 'import { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator } from "@/components/ui/input-otp"\nimport { REGEXP_ONLY_DIGITS_AND_CHARS } from "input-otp"',
        "custom_pattern": 'import { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator } from "@/components/ui/input-otp"',
    },
    "label": 'import { Label } from "@/components/ui/label"',
    "radio_group": 'import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"\nimport { Label } from "@/components/ui/label"',
    "scroll_area": {
        "simple": 'import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"',
        "vertical": 'import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"\nimport { Separator } from "@/components/ui/separator"',
        "horizontal": '''import Image from 'next/image'\nimport { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"''',
    },
    "select": 'import { Select, SelectContent, SelectGroup, SelectItem, SelectLabel, SelectTrigger, SelectValue } from "@/components/ui/select"',
    "slider": 'import { Slider } from "@/components/ui/slider"\nimport { cn } from "@/lib/utils"',
    "switch": 'import { Switch } from "@/components/ui/switch"',
    "textarea": 'import { Textarea } from "@/components/ui/textarea"',
    "toggle": {
        "simple": 'import { Toggle } from "@/components/ui/toggle"',
        "icon": 'import { Italic } from "lucide-react"\nimport { Toggle } from "@/components/ui/toggle"',
    },
    "toggle_group": 'import { Bold, Italic, Underline } from "lucide-react"\nimport { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"',
    # NOTIFICATION COMPONENTS
    "alert": {
        "simple": 'import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert"',
        "icon": 'import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert"\nimport { Terminal } from "lucide-react"',
    },
    "alert_dialog": {
        "simple": 'import { AlertDialog, AlertDialogPortal, AlertDialogOverlay, AlertDialogTrigger, AlertDialogContent, AlertDialogHeader, AlertDialogFooter, AlertDialogTitle, AlertDialogDescription, AlertDialogAction, AlertDialogCancel } from "@/components/ui/alert-dialog"'
    },
    "tooltip": {
        "button": 'import { Button } from "@/components/ui/button"\nimport { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip"',
        "label": 'import { Label } from "@/components/ui/label"\nimport { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider } from "@/components/ui/tooltip"',
        "image": [
            "import Image from 'next/image'",
            'import { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider } from "@/components/ui/tooltip"',
        ],
    },
    # PRESENTATION COMPONENTS
    "separator": 'import { Separator } from "@/components/ui/separator"',
    "avatar": {
        "path_n_url": 'import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar"',
        "static_img": [
            'import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar"',
            "import profilePic from './me.png'",
        ],
    },
    "badge": 'import { Badge } from "@/components/ui/badge"',
}


NEXTJS_VALID_IMPORTS = {
    "image": {
        "standard": "import Image from 'next/image'",
        "static_src": "import Image from 'next/image'\nimport profilePic from './me.png'",
    },
    "link": "import Link from 'next/link'",
}

REACT_VALID_IMPORTS = {
    "lucide_icon": {
        "italic": 'import { Italic } from "lucide-react"',
        "loader": 'import { Loader } from "lucide-react"',
    }
}
