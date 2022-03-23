from dis_snek import InteractionContext, MessageContext
from typeguard import check_type
from dis_taipan import protocols


def test_sendable_context() -> None:
    check_type('message_context', MessageContext, protocols.SendableContext)
    check_type('interaction_context', InteractionContext, protocols.SendableContext)
