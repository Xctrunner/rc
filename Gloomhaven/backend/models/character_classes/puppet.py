from backend.models import action_model as actions
from backend.utils import attack_shapes as shapes
from backend.models import obstacle

cards = [
    actions.ActionCard(
        attack_name="Critical Meltdown",
        actions=[
            actions.ModifySelfHealth(-5),
            actions.AreaAttack(
                shape=shapes.circle(2),
                strength=6
            )
        ],
        movement=3,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Chain Reaction",
        actions=[
            actions.ModifySelfHealth(-2),
            actions.SingleTargetAttack(3,2),
            actions.SingleTargetAttack(3,2),
        ],
        movement=4,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Power Surge",
        actions=[
            actions.ChargeNextAttack(4),
        ],
        movement=0,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Containment Breach",
        actions=[
            actions.Pull(3, 3),
            actions.ModifySelfHealth(-4),
            actions.AreaAttack(
                shape=shapes.circle(1),
                strength=5
            )
        ],
        movement=2,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Destabilize",
        actions=[
            actions.ShieldSelf(4, 1),
            actions.WeakenAllEnemies(3, 2)
        ],
        movement=2,
        jump=False
    ),
    actions.ActionCard(
        attack_name="Execute Command",
        actions=[
            actions.SingleTargetAttack(3, 2)
        ],
        movement=2,
        jump=False
    )
]

health = 4