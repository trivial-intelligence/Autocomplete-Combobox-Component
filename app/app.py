import reflex as rx
from app.states.autocomplete_state import (
    AutocompleteState,
    AutocompleteItem,
)
from app.states.demo_state import FRAMEWORKS


class FrameworkAutocomplete(AutocompleteState):
    autocomplete_items: list[AutocompleteItem] = FRAMEWORKS
    pass

framework_autocomplete = FrameworkAutocomplete.create(placeholder="Type to search frameworks (e.g., 'web', 'python')...")



def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            class_name="fixed inset-0 -z-10 h-full w-full bg-white bg-[linear-gradient(to_right,#f0f0f0_1px,transparent_1px),linear_gradient(to_bottom,#f0f0f0_1px,transparent_1px)] bg-[size:6rem_4rem]"
        ),
        rx.el.div(
            class_name="absolute bottom-0 left-0 right-0 top-0 bg-[radial-gradient(circle_800px_at_100%_200px,#d5c5ff,transparent)] -z-10 opacity-40"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Reflex Autocomplete",
                    class_name="text-4xl md:text-5xl font-extrabold tracking-tight text-gray-900 mb-4",
                ),
                rx.el.p(
                    "A robust, reusable combobox component built with rx.ComponentState.",
                    class_name="text-lg text-gray-600 max-w-2xl mx-auto leading-relaxed",
                ),
                class_name="text-center mb-16 pt-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Try it out",
                        class_name="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-4 ml-1",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Select Technologies",
                            class_name="block text-sm font-medium text-gray-700 mb-2",
                        ),
                        framework_autocomplete,
                        class_name="bg-white p-6 rounded-2xl shadow-xl border border-gray-100 ring-1 ring-gray-100",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                "Live State",
                                class_name="text-sm font-semibold text-gray-900 mb-3",
                            ),
                            rx.el.div(
                                rx.el.span("Selected: ", class_name="text-gray-500"),
                                rx.el.code(
                                    framework_autocomplete.State.selected_items.length(),
                                    class_name="font-mono font-bold text-indigo-600",
                                ),
                                class_name="mb-2 text-sm",
                            ),
                            rx.el.div(
                                rx.el.span("Values: ", class_name="text-gray-500"),
                                rx.el.div(
                                    rx.foreach(
                                        framework_autocomplete.State.selected_items,
                                        lambda item: rx.el.span(
                                            item["value"],
                                            class_name="inline-block bg-gray-100 px-2 py-0.5 rounded text-xs text-gray-600 mr-2 font-mono",
                                        ),
                                    ),
                                    class_name="mt-1 flex flex-wrap gap-1",
                                ),
                                class_name="text-sm",
                            ),
                            class_name="bg-gray-50 rounded-xl p-4 border border-gray-200",
                        ),
                        class_name="mt-8",
                    ),
                    class_name="max-w-xl mx-auto w-full",
                ),
                class_name="px-4",
            ),
            rx.el.div(
                rx.el.div(
                    FeatureCard(
                        icon="search",
                        title="Fuzzy Filtering",
                        desc="Filters items by name and keywords instantly as you type.",
                    ),
                    FeatureCard(
                        icon="keyboard",
                        title="Keyboard Nav",
                        desc="Use Arrow keys to navigate, Enter to select, Backspace to remove.",
                    ),
                    FeatureCard(
                        icon="mouse-pointer-2",
                        title="Multi-select",
                        desc="Select multiple items with tag-style badges and easy removal.",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto mt-24 px-4",
                )
            ),
            class_name="min-h-screen pb-20 font-['Inter']",
        ),
    )


def FeatureCard(icon: str, title: str, desc: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="w-6 h-6 text-indigo-600"),
            class_name="w-12 h-12 rounded-xl bg-indigo-50 flex items-center justify-center mb-4",
        ),
        rx.el.h3(title, class_name="text-lg font-bold text-gray-900 mb-2"),
        rx.el.p(desc, class_name="text-gray-600 leading-relaxed"),
        class_name="bg-white/50 backdrop-blur-sm p-6 rounded-2xl border border-gray-100 hover:border-indigo-100 transition-colors",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        )
    ],
)
app.add_page(index, route="/")