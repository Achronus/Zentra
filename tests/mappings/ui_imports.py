VALID_IMPORTS = {
    # CONTROL COMPONENTS
    "button": {
        "simple": 'import { Button } from "@/components/ui/button"',
        "icon": 'import { Button } from "@/components/ui/button"\nimport { Loader } from "lucide-react"',
        "icon_url": [
            'import { Button } from "@/components/ui/button"',
            'import Link from "next/link"',
            'import { Loader } from "lucide-react"',
        ],
    },
    "calendar": '"use client"\nimport { useState } from "react"\nimport { Calendar } from "@/components/ui/calendar"',
    "checkbox": '"use client"\nimport { Checkbox } from "@/components/ui/checkbox"',
    "collapsible": '"use client"\nimport { useState } from "react"\nimport { Collapsible, CollapsibleTrigger, CollapsibleContent } from "@/components/ui/collapsible"\nimport { Button } from "@/components/ui/button"\nimport { ChevronsUpDown } from "lucide-react"',
    "input": 'import { Input } from "@/components/ui/input"',
    "input_otp": {
        "standard": 'import { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator } from "@/components/ui/input-otp"',
        "pattern": 'import { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator } from "@/components/ui/input-otp"\nimport { REGEXP_ONLY_DIGITS_AND_CHARS } from "input-otp"',
        "custom_pattern": 'import { InputOTP, InputOTPGroup, InputOTPSlot, InputOTPSeparator } from "@/components/ui/input-otp"',
    },
    "label": 'import { Label } from "@/components/ui/label"',
    "pagination": 'import { useState } from "react"\nimport { Pagination, PaginationContent, PaginationEllipsis, PaginationItem, PaginationLink, PaginationNext, PaginationPrevious } from "@/components/ui/pagination"',
    "radio_group": 'import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"\nimport { Label } from "@/components/ui/label"',
    "scroll_area": {
        "simple": 'import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"',
        "vertical": 'import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"\nimport { Separator } from "@/components/ui/separator"',
        "horizontal": [
            'import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"',
            "import Image from 'next/image'",
        ],
    },
    "select": 'import { Select, SelectContent, SelectGroup, SelectItem, SelectLabel, SelectTrigger, SelectValue } from "@/components/ui/select"',
    "slider": 'import { Slider } from "@/components/ui/slider"\nimport { cn } from "@/lib/utils"',
    "switch": 'import { Switch } from "@/components/ui/switch"',
    "textarea": 'import { Textarea } from "@/components/ui/textarea"',
    "toggle": {
        "simple": 'import { Toggle } from "@/components/ui/toggle"',
        "icon": 'import { Toggle } from "@/components/ui/toggle"\nimport { Italic } from "lucide-react"',
    },
    "toggle_group": 'import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"\nimport { Bold, Italic, Underline } from "lucide-react"',
    # NOTIFICATION COMPONENTS
    "alert": {
        "simple": 'import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert"',
        "icon": 'import { Alert, AlertTitle, AlertDescription } from "@/components/ui/alert"\nimport { Terminal } from "lucide-react"',
    },
    "alert_dialog": {
        "simple": 'import { AlertDialog, AlertDialogPortal, AlertDialogOverlay, AlertDialogTrigger, AlertDialogContent, AlertDialogHeader, AlertDialogFooter, AlertDialogTitle, AlertDialogDescription, AlertDialogAction, AlertDialogCancel } from "@/components/ui/alert-dialog"'
    },
    "tooltip": {
        "button": 'import { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider } from "@/components/ui/tooltip"\nimport { Button } from "@/components/ui/button"',
        "string": 'import { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider } from "@/components/ui/tooltip"',
        "icon": 'import { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider } from "@/components/ui/tooltip"\nimport { Loader } from "lucide-react"',
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
