import reflex as rx
from typing import TypedDict, ClassVar, Any


class AutocompleteItem(TypedDict):
    name: str
    value: str
    keywords: list[str]


class AutocompleteState(rx.ComponentState):
    """
    A reusable component state for an autocomplete combobox.
    Inherit from this class and override on_autocomplete_query if you need backend data fetching.
    """

    autocomplete_items: list[AutocompleteItem] = []
    selected_items: list[AutocompleteItem] = []
    input_value: str = ""
    highlighted_index: int = 0
    is_open: bool = False
    loading: bool = False
    initial_items: ClassVar[list[AutocompleteItem]] = []

    @rx.event
    def on_autocomplete_query(self, query: str):
        """
        Abstract method to be overridden by subclasses.
        Use this to fetch data from an API or filter a large dataset on the backend.
        """
        pass

    @rx.var
    def filtered_items(self) -> list[AutocompleteItem]:
        """
        Computes the filtered list of items based on the input query.
        This runs on the backend to ensure consistent state for keyboard navigation.
        """
        query = self.input_value.lower().strip()
        items = self.autocomplete_items
        if not query:
            return items
        return [
            item
            for item in items
            if query in item["name"].lower()
            or any((query in k.lower() for k in item.get("keywords", [])))
        ]

    @rx.event
    def set_input_value(self, value: str):
        self.input_value = value
        self.is_open = True
        self.highlighted_index = 0
        self.on_autocomplete_query(value)

    @rx.event
    def focus_input(self):
        self.is_open = True

    @rx.event
    def blur_input(self):
        pass

    @rx.event
    def close_dropdown(self):
        self.is_open = False

    @rx.event
    def select_item(self, item: AutocompleteItem):
        current_values = [i["value"] for i in self.selected_items]
        if item["value"] not in current_values:
            self.selected_items.append(item)
        self.input_value = ""
        self.highlighted_index = 0

    @rx.event
    def remove_item(self, item: AutocompleteItem):
        self.selected_items.remove(item)

    @rx.event
    def handle_key(self, key: str):
        if key == "ArrowDown":
            count = len(self.filtered_items)
            if count > 0:
                self.highlighted_index = (self.highlighted_index + 1) % count
        elif key == "ArrowUp":
            count = len(self.filtered_items)
            if count > 0:
                self.highlighted_index = (self.highlighted_index - 1 + count) % count
        elif key == "Enter":
            items = self.filtered_items
            if items and len(items) > self.highlighted_index:
                self.select_item(items[self.highlighted_index])
        elif key == "Escape":
            self.is_open = False
            self.input_value = ""
        elif key == "Backspace":
            if self.input_value == "" and len(self.selected_items) > 0:
                self.selected_items = self.selected_items[:-1]

    @classmethod
    def get_component(
        cls, placeholder: str, **props
    ) -> rx.Component:
        return rx.el.div(
            rx.el.div(
                rx.foreach(
                    cls.selected_items,
                    lambda item: rx.el.span(
                        item["name"].to(str),
                        rx.icon(
                            "x",
                            size=14,
                            class_name="ml-1.5 cursor-pointer hover:text-red-500 transition-colors",
                            on_click=cls.remove_item(item),
                            on_mouse_down=rx.prevent_default,
                        ),
                        class_name="inline-flex items-center px-2.5 py-1 rounded-md text-sm font-medium bg-indigo-50 text-indigo-700 border border-indigo-100 animate-fade-in",
                    ),
                ),
                rx.el.input(
                    placeholder=rx.cond(cls.selected_items.length() > 0, "", placeholder),
                    on_change=cls.set_input_value,
                    on_key_down=cls.handle_key,
                    on_focus=cls.focus_input,
                    class_name="flex-1 min-w-[120px] bg-transparent outline-none text-gray-800 placeholder-gray-400 py-1",
                    default_value=cls.input_value,
                ),
                class_name=f"flex flex-wrap gap-2 p-2 min-h-[46px] w-full bg-white border border-gray-200 rounded-xl focus-within:ring-2 focus-within:ring-indigo-500/20 focus-within:border-indigo-500 transition-all duration-200 shadow-sm {props.get('class_name', '')}",
            ),
            rx.cond(
                cls.is_open & (cls.filtered_items.length() > 0),
                rx.el.div(
                    rx.foreach(
                        cls.filtered_items,
                        lambda item, index: rx.el.div(
                            rx.el.div(
                                rx.el.span(
                                    item["name"].to(str),
                                    class_name="font-medium text-gray-900",
                                ),
                                rx.cond(
                                    item["keywords"].length() > 0,
                                    rx.el.span(
                                        item["keywords"].join(", "),
                                        class_name="text-xs text-gray-400 ml-2 truncate max-w-[150px]",
                                    ),
                                ),
                                class_name="flex items-center justify-between w-full",
                            ),
                            class_name=rx.cond(
                                index == cls.highlighted_index,
                                "px-4 py-2.5 bg-indigo-50 text-indigo-700 cursor-pointer border-l-4 border-indigo-500",
                                "px-4 py-2.5 text-gray-700 hover:bg-gray-50 cursor-pointer border-l-4 border-transparent",
                            ),
                            on_click=cls.select_item(item),
                            on_mouse_down=rx.prevent_default,
                        ),
                    ),
                    class_name="absolute z-50 w-full mt-2 bg-white rounded-xl shadow-xl border border-gray-100 overflow-hidden max-h-64 overflow-y-auto animate-in fade-in slide-in-from-top-2 duration-200",
                ),
            ),
            class_name="relative w-full font-['Inter']",
        )