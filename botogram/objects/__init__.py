"""
    botogram.objects
    Representation of the different upstream API objects

    Copyright (c) 2015 Pietro Albini <pietro@pietroalbini.io>
    Released under the MIT license
"""

from .base import BaseObject, multiple, one_of, _itself
from . import mixins


class EmptyObject(BaseObject):
    """Just an empty object"""
    pass


class User(BaseObject, mixins.ChatMixin):
    """Telegram API representation of an user

    https://core.telegram.org/bots/api#user
    """

    required = {
        "id": int,
        "first_name": str,
    }
    optional = {
        "last_name": str,
        "username": str,
    }


class Chat(BaseObject, mixins.ChatMixin):
    """Telegram API representation of a chat

    https://core.telegram.org/bots/api#chat
    """

    required = {
        "id": int,
        "type": str,
    }
    optional = {
        "title": str,
        "username": str,
        "first_name": str,
        "last_name": str,
    }


class PhotoSize(BaseObject):
    """Telegram API representation of a photo size

    https://core.telegram.org/bots/api#photosize
    """

    required = {
        "file_id": str,
        "width": int,
        "height": int,
    }
    optional = {
        "file_size": int,
    }


class Audio(BaseObject):
    """Telegram API representation of an audio track

    https://core.telegram.org/bots/api#audio
    """

    required = {
        "file_id": str,
        "duration": int,
    }
    optional = {
        "performer": str,
        "title": str,
        "mime_type": str,
        "file_size": int,
    }


class Voice(BaseObject):
    """Telegram API representation of a voice message

    https://core.telegram.org/bots/api#voice
    """

    required = {
        "file_id": str,
        "duration": int,
    }
    optional = {
        "mime_type": str,
        "file_size": int,
    }


class Document(BaseObject):
    """Telegram API representation of a document

    https://core.telegram.org/bots/api#document
    """

    required = {
        "file_id": str,
    }
    optional = {
        "thumb": one_of(PhotoSize, EmptyObject),
        "file_name": str,
        "mime_type": str,
        "file_size": str,
    }


class Sticker(BaseObject):
    """Telegram API representation of a sticker

    https://core.telegram.org/bots/api#sticker
    """

    required = {
        "file_id": str,
        "width": int,
        "height": int,
    }
    optional = {
        "thumb": one_of(PhotoSize, EmptyObject),
        "file_size": int,
    }


class Video(BaseObject):
    """Telegram API representation of a video

    https://core.telegram.org/bots/api#video
    """

    required = {
        "file_id": str,
        "width": int,
        "height": int,
        "duration": int,
    }
    optional = {
        "thumb": one_of(PhotoSize, EmptyObject),
        "mime_type": str,
        "file_size": int,
    }


class Contact(BaseObject):
    """Telegram API representation of a contact

    https://core.telegram.org/bots/api#contact
    """

    required = {
        "phone_number": str,
        "first_name": str,
    }
    optional = {
        "last_name": str,
        "user_id": int,
    }


class Location(BaseObject):
    """Telegram API representation of a location mark

    https://core.telegram.org/bots/api#location
    """

    required = {
        "longitude": float,
        "latitude": float,
    }


class UserProfilePhotos(BaseObject):
    """Telegram API representation of an user's profile photos

    https://core.telegram.org/bots/api#userprofilephotos
    """

    required = {
        "total_count": int,
        "photos": multiple(multiple(one_of(PhotoSize, EmptyObject))),
    }


class Message(BaseObject, mixins.MessageMixin):
    """Telegram API representation of a message

    https://core.telegram.org/bots/api#message
    """

    required = {
        "message_id": int,
        "from": User,
        "date": int,
        "chat": Chat,
    }
    optional = {
        "forward_from": User,
        "forward_date": int,
        "reply_to_message": _itself,
        "text": str,
        "audio": Audio,
        "voice": Voice,
        "document": Document,
        "photo": multiple(PhotoSize),
        "sticker": Sticker,
        "video": Video,
        "caption": str,
        "contact": Contact,
        "location": Location,
        "new_chat_participant": User,
        "left_chat_participant": User,
        "new_chat_title": str,
        "new_chat_photo": multiple(PhotoSize),
        "delete_chat_photo": bool,
        "group_chat_crated": bool,
    }
    replace_keys = {
        "from": "from_",
    }


class ReplyKeyboardMarkup(BaseObject):
    """Telegram API representation of a custom keyboard

    https://core.telegram.org/bots/api#replykeyboardmarkup
    """

    required = {
        "keyboard": multiple(multiple(str)),
    }
    optional = {
        "resize_keyboard": bool,
        "one_time_keyboard": bool,
        "selective": bool,
    }


class ReplyKeyboardHide(BaseObject):
    """Telegram API special object which hides a custom keyboard

    https://core.telegram.org/bots/api#replykeyboardhide
    """

    required = {
        "hide_keyboard": bool,
    }
    optional = {
        "selective": bool,
    }


class ForceReply(BaseObject):
    """Telegram API special object which forces the user to reply to a message

    https://core.telegram.org/bots/api#forcereply
    """

    required = {
        "force_reply": bool,
    }
    optional = {
        "selective": bool,
    }


class Update(BaseObject):
    """Telegram API representation of an update

    https://core.telegram.org/bots/api#update
    """

    required = {
        "update_id": int,
    }
    optional = {
        "message": Message
    }


# Shortcut for the Updates type
Updates = multiple(Update)
