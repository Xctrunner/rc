from backend.models import action_model as actions
from backend.utils import attack_shapes as shapes
from backend.models import obstacle

cards = [
    actions.ActionCard(
        attack_name="Mutation Surge",
        actions=[
            actions.AreaAttack(
                shape=shapes.arc(3),
                strength=4
            )
        ],
        movement=3,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Flesh Whips",
        actions=[
            actions.Pull(2, 2),
            actions.SingleTargetAttack(
                strength=2,
                att_range=2
            ),
            actions.SingleTargetAttack(
                strength=2,
                att_range=2
            ),
        ],
        movement=2,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Writhing Mass",
        actions=[
            actions.AreaAttack(
                shape=shapes.circle(2),
                strength=2
            ),
            actions.CurseAllEnemies(2)
        ],
        movement=3,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Twisted Growth",
        actions=[
            actions.ChargeNextAttack(3),
            actions.ModifySelfHealth(-1)
        ],
        movement=4,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Flesh Eruption",
        actions=[
            actions.AreaAttack(
                shape=shapes.cone(3),
                strength=3
            ),
            actions.WeakenAllEnemies(1, 2)
        ],
        movement=2,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Consume Self",
        actions=[
            actions.ModifySelfHealth(-3),
            actions.AreaAttack(
                shape=shapes.circle(1),
                strength=5
            )
        ],
        movement=1,
        jump=False
    )
]

health = 4