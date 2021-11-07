"""Useful functions for multiple views across Cam Hudson's personal website."""

def create_index_card(name: str, text: str, a_href:str,
                      img_href: str, img_alt: str) -> dict:
    """Return HTML/CSS card created with the information provided."""
    return {
        'name': name,
        'text': text,
        'a_href': a_href,
        'img_href': img_href,
        'img_alt': img_alt
    }

def create_contact_info_card(name: str, text: str, href: str, svg: str) -> dict:
    """Return HTML/CSS card created with the information provided."""
    return {
        'name': name,
        'text': text,
        'href': href,
        'svg': svg
    }
