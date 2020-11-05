from aiogram import types

from .. import bot
from ..models import GroupModel, TimusUserModel
from .parser.submission import Submission
from .message_formers import form_leaderboard_message, form_submission_message


async def update_group_leaderboard(group: GroupModel) -> None:
    if group.leaderboard_message_id is not None:
        await bot.send_message(
            group.telegram_id,
            await form_leaderboard_message(group),
            parse_mode=types.ParseMode.MARKDOWN_V2
        )


async def notify_about_submission_verdict(submission: Submission, author_model: TimusUserModel) -> None:
    await author_model.fetch_related('tracked_in')
    for group in author_model.tracked_in:
        await bot.send_message(
            group.telegram_id,
            form_submission_message(submission),
            parse_mode=types.ParseMode.MARKDOWN_V2
        )
