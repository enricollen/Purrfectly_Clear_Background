from cat.mad_hatter.decorators import hook, tool, plugin
from cat.log import log
from .image_parser import ImageParser

@hook
def rabbithole_instantiates_parsers(file_handlers: dict, cat) -> dict:
    new_file_handlers = file_handlers

    new_file_handlers["image/png"] = ImageParser()
    new_file_handlers["image/jpeg"] = ImageParser()
    new_file_handlers["image/webp"] = ImageParser()

    return new_file_handlers

@hook
def before_rabbithole_splits_text(text: list, cat):
    is_image = text[0].metadata["source"] == "Purrfectly_Clear_Background"

    if is_image:
            log.warning("Removing background...")
            cat.send_ws_message(content='Removing background...', msg_type='chat_token')
            content = text[0].page_content
            name = text[0].metadata["name"]
            cat.send_ws_message(
                f"<p>Here is your image <b>{name}</b> with background removed: \n</p>{content}",
                "chat"
            )

    return text