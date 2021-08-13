from click import command, option
from tgforwarderclient.app import make_app


@command(
    context_settings=dict(
        auto_envvar_prefix="bot",
        show_default=True,
    ),
)
@option(
    "--api_id",
    help="Client's api_id",
    required=True,
    type=int,
    allow_from_autoenv=True,

)
@option(
    "--api_hash",
    help="Client's api_hash",
    required=True,
    allow_from_autoenv=True,
)
@option(
    "--session_key",
    "--session",
    help="Session key",
    required=True,
    allow_from_autoenv=True,
)
@option(
    "--channels",
    "--channel",
    help="One or more channels for listening",
    required=True,
    allow_from_autoenv=True,
    multiple=True,
)
@option(
    "--chats",
    "--chat",
    help="One or more chats for message forwarding",
    required=True,
    allow_from_autoenv=True,
    type=int,
    multiple=True,
)
def main(
    api_id: int,
    api_hash: str,
    session_key: str,
    channels: list[str],
    chats: list[int],
) -> None:
    app = make_app(
        api_id=api_id,
        api_hash=api_hash,
        session_key=session_key,
        channels=channels,
        chats=chats,
    )
    app.run()
